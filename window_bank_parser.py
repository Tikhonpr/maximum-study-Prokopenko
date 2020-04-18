from tkinter import * 
import requests
from bs4 import BeautifulSoup
from datetime import datetime

window = Tk()
window.geometry("400x400")
window.title("Курс валют")

btn = Button (window, text = "Озвучить")
btn.place(x = 200, y = 100)

today = datetime.today()
today = today.strftime("%d/%m/%Y")
dictionary = {"date_req":today}


url = "http://www.cbr.ru/scripts/XML_daily.asp?"


response = requests.get(url, params=dictionary )

xml = BeautifulSoup(response.content, "lxml")

def getCourse(j):
    return xml.find("valute", {'id': j}).value.text


course_USD = Label(window, text = "$ " + getCourse("R01235"), font = "Arial 18")
course_USD.place(x = 90, y = 200)

course_EUR = Label(window, text = "€ " + getCourse("R01239"), font = "Arial 18")
course_EUR.place(x = 90, y = 150)

course_today = Label(window, text = "Курс на " + today.replace("/", "."), font = "Arial 18")
course_today.place (x = 90, y = 100)

img = PhotoImage(file = "ROSSIA.png")
pic = Label(window, image = img)
pic.place(x = 0, y = 0)


my_file = open('speach.txt', 'a')
my_file.read(course_EUR, course_USD)
my_file.close()

window.mainloop()