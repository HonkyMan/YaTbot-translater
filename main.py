import urllib.request
import requests
import json
from pprint import pprint

str1='';
while(True):
    if(str1 == 'exit'):
        break;
    print('Выберите язык с какого переводить: ');
    firstLang = str(input());
    print('Выберите язык на какой переводить: ');
    secondLang = str(input());
    while(True):
        print('\nЧто переводить?');
        str1 = str(input());
        if(str1 == 'break' or str1 == 'exit'):
            break;
        response = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate?lang='+firstLang+'-'+secondLang+'&format=plain&text=' + str1 + '&key=trnsl.1.1.20180410T163309Z.ed66cbadb7962459.5ed7300ec4ce337bc7d4754a42b066d938c7db1b')
        pprint(response.json().get("text"))
print('Спасибо за использование')
