from tkinter import *
root = Tk()
root.geometry("600x400")

#set variables
count = 0

#def click event
def click(count,amount):
       count += amount

myBox = Label(root,text=count)
myBox.update
myBox.pack()

myButton = Button(root, text="+1",height=5,width=10,bg="red",fg="black")
myButton.place(x= 630,y=500)
myButton.bind( Event, count.click(1))
root.update
root.mainloop()