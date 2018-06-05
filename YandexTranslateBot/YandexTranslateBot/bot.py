import config
import telebot
import telegram
import urllib.request
import requests
import json
from telebot import apihelper
#import urllib2
from pprint import pprint

apihelper.proxy = {'http', 'http://173.9.47.220:8080'}
bot = telebot.TeleBot(token=config.token) #, proxy=dict(https="https://177.44.229.246:20183")


print(config.token);

firstLang = 'tt'
secondLang = 'en'

yaKey = config.yaToken;
listLang = requests.get('https://translate.yandex.net/api/v1.5/tr.json/getLangs?ui=ru&key='+yaKey);
print(listLang)
listLang = json.loads(listLang.text)["langs"]
print(listLang);
#updates = bot.get_updates();


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "!Привет!")
    bot.reply_to(message, "Изначально установлен перевод с татарского на английский язык")
    bot.reply_to(message, "Для выбора языка, с которого надо переводить, наберите команду /set_from")

@bot.message_handler(commands=['set_from'])
def send_welcome(message):
    msg = bot.reply_to(message, "Введите язык")    
    bot.register_next_step_handler(msg,set_first)


@bot.message_handler(commands=['set_to'])
def send_welcome(message):
    msg = bot.reply_to(message, "Введите язык")    
    bot.register_next_step_handler(msg,set_second)

@bot.message_handler(func=lambda message: True)
def set_first_lang(message):
    global yaKey
    bot.reply_to(message, requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate?lang='+firstLang+'-'+secondLang+'&format=plain&text=' + message.text + '&key=' + yaKey).json().get("text"))
    bot.reply_to(message, "Введите текст")

def set_first(message):
    global firstLang
    global listLang;
    for i in listLang:
        if i == message.text:
            firstLang = message.text
            bot.reply_to(message, "Для выбора языка, на который надо переводить, наберите команду /set_to")
            break;
    


def set_second(message):
    global secondLang 
    global listLang
    for i in listLang:
        if i == message.text:
            secondLang = message.text
            bot.reply_to(message, "Введите любое слово для перевода")
            break

#@bot.message_handler(func=lambda message: True)
#def echo_all(message):
#	bot.reply_to(message, requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate?lang='+firstLang+'-'+secondLang+'&format=plain&text=' + str1 + '&key=trnsl.1.1.20180410T163309Z.ed66cbadb7962459.5ed7300ec4ce337bc7d4754a42b066d938c7db1b').json().get("text"))

if __name__ == '__main__':
    bot.polling(none_stop=True)
