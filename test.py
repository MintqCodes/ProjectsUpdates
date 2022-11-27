#codegenerator
import random
random_list = []
for i in range(0,6):
    n = random.randint(0, 9)
    random_list.append(n)
    print(random_list)#counterapp
from tkinter import *
root = Tk()
myLabel1 = Label(root, text="Hello world!")
myLabel2 = Label(root, text="I'm Minty!")
myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1,column=0)
root.mainloop()
