# Project Calculator
# Author - Sandip Sadhukhan
# Copyright @2019 All Rights Reserved

#import modules
from tkinter import *

# String to result function
def stringToResult(myString):
    myString = myString.replace('x','*')
    try:
        result = eval(myString)
    except:
        result = "Undefined"
    return result

# one to seven Button function
def zeroFun():
    curr = currentResultVar.get()
    currentResultVar.set(curr+"0")
def oneFun():
    curr = currentResultVar.get()
    currentResultVar.set(curr+"1")
def twoFun():
    curr = currentResultVar.get()
    currentResultVar.set(curr+"2")
def threeFun():
    curr = currentResultVar.get()
    currentResultVar.set(curr+"3")
def fourFun():
    curr = currentResultVar.get()
    currentResultVar.set(curr+"4")
def fiveFun():
    curr = currentResultVar.get()
    currentResultVar.set(curr+"5")
def sixFun():
    curr = currentResultVar.get()
    currentResultVar.set(curr+"6")
def sevenFun():
    curr = currentResultVar.get()
    currentResultVar.set(curr+"7")
def eightFun():
    curr = currentResultVar.get()
    currentResultVar.set(curr+"8")
def nineFun():
    curr = currentResultVar.get()
    currentResultVar.set(curr+"9")
def dotFun():
    curr = currentResultVar.get()
    if '.' in curr:
        return
    currentResultVar.set(curr+".")

 
# delete and clear button
def deleteFun():
    curr = currentResultVar.get()
    if curr == "":
        return
    now = curr[:len(curr)-1]
    currentResultVar.set(now)
def clearFun():
    currentResultVar.set("")
    previousResultVar.set("")
# operator button funtion
def additionFun():
    curr = currentResultVar.get()
    currentResultVar.set(curr+"+")
def subtractionFun():
    curr = currentResultVar.get()
    currentResultVar.set(curr+"-")
def multipicationFun():
    curr = currentResultVar.get()
    currentResultVar.set(curr+"x")
def divisionFun():
    curr = currentResultVar.get()
    currentResultVar.set(curr+"/")
# equal fun
def equalFun():
    curr = currentResultVar.get()
    result = stringToResult(str(curr))
    previousResultVar.set(curr)
    currentResultVar.set(result)


# initlize the root
root = Tk()
root.title("Calculator")

# Create the Gui
# Default Window Size 
WIDTH = 320
HEIGHT = 520
# canvas
canvas = Canvas(root, width = WIDTH, height = HEIGHT)
canvas.pack()
# Frame
frame = Frame(canvas, bg="white")
frame.place(relwidth=1, relheight=1)
# previous result
previousResultVar = StringVar()
previousResult = Label(frame, textvariable=previousResultVar, bg="#fff", anchor="e", font=('verdana', 13), fg="tomato")
previousResult.place( rely=.01, relwidth=1, relheight=.08)
# Current result
currentResultVar = StringVar()
currentResult = Label(frame, textvariable=currentResultVar, bg="#c4c4c4", anchor="e", font=('verdana', 18), fg="#000")
currentResult.place(relwidth=1,relheight=.1, rely=.1)
# create the lower frame
lowerFrame = Frame(frame,bg="#fff")
lowerFrame.place(rely=.2, relwidth=1, relheight=1)
# clear button
clearButton = Button(lowerFrame, text = "C", bg="#fff", fg="#000", font=('verdana', 18), command=clearFun)
clearButton.place(relwidth=.5,rely=0, relheight=.12)
# delete button
deleteButton = Button(lowerFrame, text = "DEL", bg="#fff", fg="#000", font=('verdana', 18), command=deleteFun)
deleteButton.place(relwidth=.5,rely=0, relheight=.12, relx=.5)
# seven button
sevenButton = Button(lowerFrame, text = "7", bg="#fff", fg="#000", font=('verdana', 18), command=sevenFun)
sevenButton.place(relwidth=.25,rely=.12, relheight=.12, relx=.0)
# eight button
eightButton = Button(lowerFrame, text = "8", bg="#fff", fg="#000", font=('verdana', 18), command=eightFun)
eightButton.place(relwidth=.25,rely=.12, relheight=.12, relx=.25)
# nine button
nineButton = Button(lowerFrame, text = "9", bg="#fff", fg="#000", font=('verdana', 18), command=nineFun)
nineButton.place(relwidth=.25,rely=.12, relheight=.12, relx=.5)
# division button
divisionButton = Button(lowerFrame, text = "/", bg="#f4f4f4", fg="tomato", font=('verdana', 18), command=divisionFun)
divisionButton.place(relwidth=.25,rely=.12, relheight=.12, relx=.75)
# four button
fourButton = Button(lowerFrame, text = "4", bg="#fff", fg="#000", font=('verdana', 18), command=fourFun)
fourButton.place(relwidth=.25,rely=.24, relheight=.12, relx=.0)
# five button
fiveButton = Button(lowerFrame, text = "5", bg="#fff", fg="#000", font=('verdana', 18), command=fiveFun)
fiveButton.place(relwidth=.25,rely=.24, relheight=.12, relx=.25)
# six button
sixButton = Button(lowerFrame, text = "6", bg="#fff", fg="#000", font=('verdana', 18), command=sixFun)
sixButton.place(relwidth=.25,rely=.24, relheight=.12, relx=.5)
# multipication button
multipicationButton = Button(lowerFrame, text = "x", bg="#f4f4f4", fg="tomato", font=('verdana', 18), command=multipicationFun)
multipicationButton.place(relwidth=.25,rely=.24, relheight=.12, relx=.75)
# one button
oneButton = Button(lowerFrame, text = "1", bg="#fff", fg="#000", font=('verdana', 18), command=oneFun)
oneButton.place(relwidth=.25,rely=.36, relheight=.12, relx=.0)
# two button
twoButton = Button(lowerFrame, text = "2", bg="#fff", fg="#000", font=('verdana', 18), command=twoFun)
twoButton.place(relwidth=.25,rely=.36, relheight=.12, relx=.25)
# three button
threeButton = Button(lowerFrame, text = "3", bg="#fff", fg="#000", font=('verdana', 18), command=threeFun)
threeButton.place(relwidth=.25,rely=.36, relheight=.12, relx=.5)
# subtraction button
subtractionButton = Button(lowerFrame, text = "-", bg="#f4f4f4", fg="tomato", font=('verdana', 18), command=subtractionFun)
subtractionButton.place(relwidth=.25,rely=.36, relheight=.12, relx=.75)
# zero button
zeroButton = Button(lowerFrame, text = "0", bg="#fff", fg="#000", font=('verdana', 18), command=zeroFun)
zeroButton.place(relwidth=.25,rely=.48, relheight=.12, relx=.0)
# dot button
dotButton = Button(lowerFrame, text = ".", bg="#fff", fg="#000", font=('verdana', 18), command=dotFun)
dotButton.place(relwidth=.25,rely=.48, relheight=.12, relx=.25)
# equal button
equalButton = Button(lowerFrame, text = "=", bg="#f4f4f4", fg="tomato", font=('verdana', 18), command=equalFun)
equalButton.place(relwidth=.25,rely=.48, relheight=.12, relx=.50)
# addition button
additionButton = Button(lowerFrame, text = "+", bg="#f4f4f4", fg="tomato", font=('verdana', 18), command=additionFun)
additionButton.place(relwidth=.25,rely=.48, relheight=.12, relx=.75)
# copyright text
copyrightText = Label(lowerFrame, text = "Developed by Sandip Sadhukhan", fg="tomato", bg="white")
copyrightText.place(rely=.7, relwidth=1)

root.mainloop()
