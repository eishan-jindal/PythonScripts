#Python3
#AutoScroll Script
#Author Eishan Jindal

import pyautogui,time, sys
import tkinter as tk
from tkinter import messagebox

def setter(string):
    global v
    v.set(string)
    l.update()

def startScrolling():
    
    setter('Running')

    s = timeinput.get()
    if(s == ''):
        setter("Stopped")
        return

    s = int(s)
    s = s/2
    s = int(s*10)

    if(s == 0):
        setter("Stopped")
        return

    setter('Timer Started')
    time.sleep(3)
    
    original = pyautogui.position()
    new = original
    
    while (new == original):
        setter('Scrolling')
        
        pyautogui.scroll(-1)
        for i in range(s):
            new = pyautogui.position()
            if(new!=original):
                break
            else:
                time.sleep(.200)
                

    setter("Stopped")    

def term():
    root.destroy()

def instruction():
    msg = '''1. The time defines how long(sec) the Scroller has to wait before scrolling down the window.\n
2. To start the scroller, enter a non-zero, non-negative time in the textbox. Then, Press the start button.\n
3. You have 3 seconds to move your cursor to the window you want to be scrolled automatically.\n
4. After 3 seconds, the scroller will start.\n
5. Moving your mouse from it's initial position, pauses the program.'''
    messagebox.showinfo("Instructions", msg)
        
root = tk.Tk()
root.title("AutoScroll - by EA")
#root.geometry("350x150")
root.resizable(width=False, height=False)
root.configure(background='white')

timelblframe = tk.Frame(root, bg='white')
timeframe = tk.Frame(root, bg='white')
btnframe = tk.Frame(root, bg = 'white')
utilframe = tk.Frame(root, bg = 'red')

root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

timelblframe.grid(row=0, sticky="ew", pady = 5)
timeframe.grid(row=1, sticky="ew")
btnframe.grid(row=2, column = 0 ,sticky="ew")
utilframe.grid(row=3, sticky="ew")


l = tk.Label(timeframe, text = "Enter time", bg='white')
timeinput = tk.Entry(timeframe)
B1 = tk.Button(timeframe, text = "?",bd = 0, activebackground = 'white',activeforeground = 'Royalblue', command = instruction, bg = 'gray97')


l.grid(row=0,column=0, padx = 5 ,pady = 5)
l.config(font=('', 10, ''))
timeinput.grid(row=0,column=1, padx = 10)
B1.grid(row = 0 , column = 2,pady = 1, padx = 5)
B1.config(font=('helvetica', 15, 'bold'))

start = tk.Button(btnframe, text='Start', bd = 0, bg = 'gray93', activebackground = 'white',activeforeground = 'green',command=startScrolling)
lb = tk.Label(btnframe, text = "   ", bg='white')
stop = tk.Button(btnframe, text="Exit",bd = 0, activeforeground = 'red', activebackground = 'white', command=term)

lb.grid(row = 0, column = 0,padx = 40, pady = 10)
start.grid(row = 0, column = 1,padx = 5, pady = 10)
start.config(font=('', 10, ''))
stop.config(font=('', 10, ''))
stop.grid(row = 0 , column = 2, padx = 0, pady = 0)


v = tk.StringVar()
l = tk.Label(utilframe, textvariable=v ,bg='red', fg = "white")
v.set("Ready")



l.grid(row = 0, column = 1 , padx = 0, pady = 5 , columnspan = 2)
l.config(font=('', 10, 'italic'))
root.mainloop()
