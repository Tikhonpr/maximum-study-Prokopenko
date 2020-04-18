import requests
from bs4 import BeautifulSoup
from datetime import datetime

today = datetime.today()
today = today.strftime("%d/%m/%Y")
dictionary = {"date_req":today}


url = "http://www.cbr.ru/scripts/XML_daily.asp?"


response = requests.get(url, params=dictionary )

xml = BeautifulSoup(response.content, "lxml")


valute_from = "EUR"
valute_to = "USD"
amount = 800
def course (valute_from, valute_to, amount):
    a = xml.find("valute", {'id': valute_from }).value.text
    b = xml.find("valute", {'id': valute_to }).value.text
    rub = amount/a
    result = rub*b
    return result
peremenaya = xml.find(valute_from, valute_to, amount)
print(peremenaya)
#1. перевести valute_from в рубли, сохранить в  переменную a результат
#2. перевести valute_to в рубли, сохранить в  переменную b результат
#3. amount/a = rub, rub*b=result
#4. result вывести на экран 