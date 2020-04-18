from tkinter import *

window = Tk()
window.title("Моё первое оконное приложение")
window.geometry("700x500")

lab = Label(window, text = "1", bg = "yellow", fg = "#4287f5", font = "16")
lab.place(x = 100, y = 300)

def changeLabel():
    a = int(lab["text"])
    a = a + 1 
    lab["text"] = a 

btn = Button (window, text = "Просто здравствуй", command = changeLabel)
btn.place(x = 200, y = 100)

img = PhotoImage(file = "logo.png")
pic = Label(window, image = img)
pic.place(x = 0, y = 0)

window.mainloop()