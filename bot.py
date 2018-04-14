import config
import telebot
import urllib.request
import requests
import json
from pprint import pprint

bot = telebot.TeleBot(config.token)
print(config.token);

firstLang = 'tt';
secondLang = 'en'

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
        bot.reply_to(message, "!Привет!")
        bot.reply_to(message, "Выберете язык с какого переводить")

@bot.message_handler(func=lambda message: True)
def set_first_lang(message):
        firstLang = str(message)
        bot.reply_to(message, "Выберете язык на какой переводить")
        secondLang = str(message)
        bot.reply_to(message, "Введите фразу:")
        bot.reply_to(message, requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate?lang='+firstLang+'-'+secondLang+'&format=plain&text=' + str(message) + '&key=trnsl.1.1.20180410T163309Z.ed66cbadb7962459.5ed7300ec4ce337bc7d4754a42b066d938c7db1b').json().get("text"))


#@bot.message_handler(func=lambda message: True)
#def echo_all(message):
#	bot.reply_to(message, requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate?lang='+firstLang+'-'+secondLang+'&format=plain&text=' + str1 + '&key=trnsl.1.1.20180410T163309Z.ed66cbadb7962459.5ed7300ec4ce337bc7d4754a42b066d938c7db1b').json().get("text"))

if __name__ == '__main__':
    bot.polling(none_stop=True)
