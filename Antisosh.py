from json import load
import tkinter as tk
from tkinter import END, messagebox
from typing import Text
from PIL import Image, ImageTk
import warnings
warnings.filterwarnings("ignore")
import numpy as np
import random
import string
import socket
import threading
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import ttk
from tkPDFViewer import tkPDFViewer as pdf
class FirstPage(tk.Frame):
def __init__(self, parent, controller):
tk.Frame.__init__(self, parent)
self.configure(bg=

'black')

border = tk.LabelFrame(self, text=

'ANTISHOSH'
,

bg=
'silver'
, bd = 10, font=("Arial"
, 30))

border.pack(fill=
"both"
, expand=
"yes"
, padx = 150,

pady=150)
L1 = tk.Label(border, text=

"Login"

, font=("Arial Bold"
,
8

20), bg=

'ivory')
L1.place(x=220, y=20)
L1 = tk.Label(border, text=

"Username"

, font=("Arial

Bold"
, 18), bg=

'ivory')

L1.place(x=50, y=100)
T1 = tk.Entry(border, width = 35, bd = 5)
T1.place(x=220, y=100)
L2 = tk.Label(border, text=

"Password"

, font=("Arial Bold"
,

18), bg=

'ivory')
L2.place(x=50, y=180)
T2 = tk.Entry(border, width = 35, show=
'*'
, bd = 5)

T2.place(x=220, y=180)
def verify():
try:
with open("credential.txt"
,
"r") as f:

info = f.readlines()
i = 0
for e in info:
u, p =e.split("
,
")

if u.strip() == T1.get() and p.strip() ==

T2.get():

i=1
controller.show_frame(SecondPage)
break
if i==0:
messagebox.showinfo(""
,
"Please provide

correct username !!")
except:
messagebox.showinfo("Error"
,
"Please provide

correct username !!")

9

B1 = tk.Button(border, text=

"Submit"

, font=("Arial"
,

20),bg=
"pink"
, command=verify)
B1.place(x=320, y=300)
def register():
window = tk.Tk()
window.resizable(0,0)
window.configure(bg=

"deep sky blue")

window.title("Register")
l1 = tk.Label(window, text=

"Username:"
,

font=("Arial"

,15), bg=

"deep sky blue")

l1.place(x=10, y=10)
t1 = tk.Entry(window, width=30, bd=5)
t1.place(x = 200, y=10)
l2 = tk.Label(window, text=

"Password:"
,

font=("Arial"

,15), bg=

"deep sky blue")

l2.place(x=10, y=60)
t2 = tk.Entry(window, width=30, show=
"*"
, bd=5)

t2.place(x = 200, y=60)
l3 = tk.Label(window, text=

"Confirm Password:"
,

font=("Arial"

,15), bg=

"deep sky blue")

l3.place(x=10, y=110)
t3 = tk.Entry(window, width=30, show=
"*"
, bd=5)

t3.place(x = 200, y=110)
def check():
if t1.get()!=

"" or t2.get()!=

"" or t3.get()!=
"":

if t2.get()==t3.get():
with open("credential.txt"
,
"a") as f:

f.write(t1.get()+"
,
"+t2.get()+"\n")
messagebox.showinfo("Welcome"
,
"You are

registered successfully!!")

else:
messagebox.showinfo("Error"
,
"Your password
10

didn't get match!!")
else:
messagebox.showinfo("Error"
,
"Please fill the

complete field!!")

b1 = tk.Button(window, text=

"Sign in"
,

font=("Arial"

,15), bg=

"#ffc22a"

, command=check)

b1.place(x=170, y=150)
window.geometry("470x220")
window.mainloop()
B2 = tk.Button(self, text=

"Register"
, bg =

"pink"
,

font=("Arial"

,15), command=register)

B2.place(x=650, y=20)

class SecondPage(tk.Frame):
def __init__(self, parent, controller):
tk.Frame.__init__(self, parent)
self.configure(bg=

'black')

border = tk.LabelFrame(self, text=

'ANTISHOSH'
,

bg=
'silver'
, bd = 10, font=("Arial"
, 30))

border.pack(fill=
"both"
, expand=
"yes"
, padx = 150,

pady=150)
my_text =
tk.Text(border,width=50,height=20,font=
"arial"
,bg=
"light

blue")
my_text.pack(pady=10)
my_text.config(state=

"normal")
my_text.insert(tk.INSERT,

"""WELCOME TO ANTISHOSH!

This app is made userfriendly for both
introverts and extroverts.
This app helps both to socialize with people.

11

If you are one who struggles to find people of your type
Dont worry your not alone,
this app will let you connect with people of your type.
Have a Great time !!""")
my_text.config(state=

"disabled")
Button = tk.Button(self, text=
"Next"
, font=("Arial"
,

15),bg=
"pink"

,command=lambda:
controller.show_frame(ThirdPage))
Button.place(x=600, y=600)
Button = tk.Button(self, text=

"Back"
, font=("Arial"
,

15),bg=
"pink"
, command=lambda:
controller.show_frame(FirstPage))
Button.place(x=150, y=600)

class ThirdPage(tk.Frame):
def __init__(self, parent, controller):
tk.Frame.__init__(self, parent)
self.configure(bg=

'black')
L1 = tk.Label(self, text=

"ANTISHOSH"

, font=("Arial Bold"
,

20), bg=

'ivory')
L1.place(x=300, y=20)
def chat():
def send():
send =

"You-> "+e.get()

txt.insert(END,

"\n"+send)

if(e.get()==

"Hi" or "hi" or "HI"):

txt.insert(END,

"\n"+"Bot-> Hi,How can I help

you? ")

if(e.get()==

"How are you"):

12

txt.insert(END,

"\n"+"Bot-> Iam fine and you? ")

if(e.get()==

"Tell me a joke"):

txt.insert(END,

"\n"+"Bot-> ")

if(e.get()==

"Tell me about introverts"):

txt.insert(END,

"\n"+"Bot-> ")

if(e.get()==

"Tell me about extroverts"):

txt.insert(END,

"\n"+"Bot-> ")

if(e.get()==

"How is this app hepfull"):

txt.insert(END,

"\n"+"Bot-> ")

if(e.get()==

"What are the features in the app?"):

txt.insert(END,

"\n"+"Bot-> ")

if(e.get()==

"How to Socialize with people"):

txt.insert(END,

"\n"+"Bot-> ")

if(e.get()==

"How to start a conversation"):

txt.insert(END,

"\n"+"Bot-> ")

if(e.get()==

"How to survive in a party as introvert"):

txt.insert(END,

"\n"+"Bot-> ")

window = tk.Tk()
window.resizable(0,0)
window.configure(bg=

"black")
window.title("CHAT BOT")
txt = tk.Text(window)
txt.grid(row=0,column=0,columnspan=2)
e = tk.Entry(window,width=100)
Button = tk.Button(window, text=

"Send"

, font=("Arial"
,

15),bg=

"ivory"

,command=send).grid(row=1,column=1)

e.grid(row=1,column=0)
my_text =

tk.Text(window,width=20,height=20,font=

"arial")

my_text.config(state=

"normal")
my_text.insert(tk.INSERT,
"""-hi

-How is this app hepfull
-Tell me a joke
-Tell me about introverts
-Tell me about extroverts

13

-What are the features
in the app?
-How to Socialize with
people?
-How to survive in a party
as introvert
-How to start a
conversation""")

my_text.grid(row=0,column=2)
window.mainloop()

Button = tk.Button(self, text=
"CHAT

BOT"
,height=2,width=45, font=("Arial"

, 15),bg=

"light blue"

,command=chat)
Button.place(x=150, y=100)
def textbox():
window = tk.Tk()
window.resizable(0,0)
window.configure(bg=

"deep sky blue")

window.title("NOTE PAD")
my_text =

tk.Text(window,width=60,height=20,font=

"arial")

my_text.pack(pady=30)
window.geometry("470x220")
window.mainloop()
B2 = tk.Button(self, text=

"NOTE PAD"
,

height=2,width=45,bg =

"pink"
, font=("Arial"
,15),

command=textbox)
B2.place(x=150, y=200)
Button = tk.Button(self, text=

"Home"

, font=("Arial"
,

15),bg=

"silver"

, command=lambda:
controller.show_frame(FirstPage))

14

Button.place(x=650, y=500)
Button = tk.Button(self, text=

"Back"
, font=("Arial"
,

15),bg=

"silver"

, command=lambda:
controller.show_frame(SecondPage))
Button.place(x=100, y=500)
def intro():
HOST =

'127.0.0.1'
PORT = 1235
FORMAT=

"utf-8"

cons=[]
DARK_GREY =

'#121212'

MEDIUM_GREY =

'#1F1B24'

OCEAN_BLUE =

'#464EB8'

WHITE =

"white"
FONT = ("Helvetica"
, 17)
BUTTON_FONT = ("Helvetica"
, 15)
SMALL_FONT = ("Helvetica"
, 13)
client = socket.socket(socket.AF_INET,

socket.SOCK_STREAM)

def add_message(message):
message_box.config(state=tk.NORMAL)
username = username_textbox.get()
message_box.insert(tk.END, message+"\n")
message_box.config(state=tk.DISABLED)
def connect():
client.connect((HOST, PORT))
print("Successfully connected to server")
add_message("[SERVER] successfully connected to

the server")

username = username_textbox.get()

15

if username !=
'':

client.sendall(username.encode())
client.send(username.encode())
else:
messagebox.showerror("Invalid username"
,

"Username cannot be empty")

threading.Thread(target=listen_for_messages_from_server,
args=(client, )).start()

username_textbox.config(state=tk.DISABLED)
username_button.config(state=tk.DISABLED)
def send_message():
message = message_textbox.get()
if message !=
'':

client.send(message.encode())
message_textbox.delete(0, len(message))
else:
messagebox.showerror("Empty message"
,

"Message cannot be empty")

def listen_for_messages_from_server(client):
while 1:
message = client.recv(2048).decode('utf-8')
if message !=
'':

username = message.split("
~
")[0]

content = message.split('
~
')[1]

add_message(f"[{username}] {content}")
else:
messagebox.showerror("Error"
,
"Message

recevied from client is empty")

16

w=tk.Tk()
w.geometry("650x650")
w.title("Messenger Client")
w.resizable(False, False)
w.grid_rowconfigure(0, weight=1)
w.grid_rowconfigure(1, weight=4)
w.grid_rowconfigure(2, weight=1)
top_frame = tk.Frame(w, width=600, height=100,

bg=DARK_GREY)

top_frame.grid(row=0, column=0, sticky=tk.NSEW)
middle_frame = tk.Frame(w, width=600, height=400,

bg=MEDIUM_GREY)

middle_frame.grid(row=1, column=0, sticky=tk.NSEW)
bottom_frame = tk.Frame(w, width=600, height=100,

bg=DARK_GREY)

bottom_frame.grid(row=2, column=0, sticky=tk.NSEW)
username_label = tk.Label(top_frame, text=
"Enter

username:"

, font=FONT, bg=DARK_GREY, fg=WHITE)
username_label.pack(side=tk.LEFT, padx=10)
username_textbox = tk.Entry(top_frame, font=FONT,

bg=MEDIUM_GREY, fg=WHITE, width=23)
username_textbox.pack(side=tk.LEFT)
username_button = tk.Button(top_frame, text=
"Join"
,

font=BUTTON_FONT, bg=OCEAN_BLUE, fg=WHITE,
command=connect)

username_button.pack(side=tk.LEFT, padx=15)
message_textbox = tk.Entry(bottom_frame,
font=FONT, bg=MEDIUM_GREY, fg=WHITE, width=38)

17

message_textbox.pack(side=tk.LEFT, padx=10)
message_button = tk.Button(bottom_frame,

text=
"Send"

, font=BUTTON_FONT, bg=OCEAN_BLUE,

fg=WHITE, command=send_message)

message_button.pack(side=tk.LEFT, padx=10)
message_box =

scrolledtext.ScrolledText(middle_frame, font=SMALL_FONT,
bg=MEDIUM_GREY, fg=WHITE, width=67, height=26.5)

message_box.config(state=tk.DISABLED)
message_box.pack(side=tk.TOP)

def main():
w.mainloop()
if __name__ ==

'__main__':

main()
Button = tk.Button(self,
text=
"INTROVERT"

,height=2,width=45, font=("Arial"
,

15),bg=

"light blue"

,command=intro)
Button.place(x=150, y=300)
def extro():
HOST =

'127.0.0.1'
PORT = 1234
FORMAT=

"utf-8"

cons=[]
DARK_GREY =

'#121212'

MEDIUM_GREY =

'#1F1B24'

OCEAN_BLUE =

'#464EB8'

WHITE =

"white"

18

FONT = ("Helvetica"
, 17)
BUTTON_FONT = ("Helvetica"
, 15)
SMALL_FONT = ("Helvetica"
, 13)
client = socket.socket(socket.AF_INET,

socket.SOCK_STREAM)

def add_message(message):
message_box.config(state=tk.NORMAL)
username = username_textbox.get()
message_box.insert(tk.END, message+"\n")
message_box.config(state=tk.DISABLED)
def connect():
client.connect((HOST, PORT))
print("Successfully connected to server")
add_message("[SERVER] successfully connected to

the server")

username = username_textbox.get()
if username !=
'':

client.sendall(username.encode())
client.send(username.encode())
else:
messagebox.showerror("Invalid username"
,

"Username cannot be empty")

threading.Thread(target=listen_for_messages_from_server,
args=(client, )).start()

username_textbox.config(state=tk.DISABLED)
username_button.config(state=tk.DISABLED)
def send_message():
message = message_textbox.get()
if message !=
'':

client.send(message.encode())

19

message_textbox.delete(0, len(message))
else:
messagebox.showerror("Empty message"
,

"Message cannot be empty")

def listen_for_messages_from_server(client):
while 1:
message = client.recv(2048).decode('utf-8')
if message !=
'':

username = message.split("
~
")[0]

content = message.split('
~
')[1]

add_message(f"[{username}] {content}")
else:
messagebox.showerror("Error"
,
"Message

recevied from client is empty")

w=tk.Tk()
w.geometry("650x650")
w.title("Messenger Client")
w.resizable(False, False)
w.grid_rowconfigure(0, weight=1)
w.grid_rowconfigure(1, weight=4)
w.grid_rowconfigure(2, weight=1)
top_frame = tk.Frame(w, width=600, height=100,

bg=DARK_GREY)

top_frame.grid(row=0, column=0, sticky=tk.NSEW)
middle_frame = tk.Frame(w, width=600, height=400,

bg=MEDIUM_GREY)

middle_frame.grid(row=1, column=0, sticky=tk.NSEW)

20

bottom_frame = tk.Frame(w, width=600, height=100,

bg=DARK_GREY)

bottom_frame.grid(row=2, column=0, sticky=tk.NSEW)
username_label = tk.Label(top_frame, text=
"Enter

username:"

, font=FONT, bg=DARK_GREY, fg=WHITE)
username_label.pack(side=tk.LEFT, padx=10)
username_textbox = tk.Entry(top_frame, font=FONT,

bg=MEDIUM_GREY, fg=WHITE, width=23)
username_textbox.pack(side=tk.LEFT)
username_button = tk.Button(top_frame, text=
"Join"
,

font=BUTTON_FONT, bg=OCEAN_BLUE, fg=WHITE,
command=connect)

username_button.pack(side=tk.LEFT, padx=15)
message_textbox = tk.Entry(bottom_frame,
font=FONT, bg=MEDIUM_GREY, fg=WHITE, width=38)
message_textbox.pack(side=tk.LEFT, padx=10)
message_button = tk.Button(bottom_frame,

text=
"Send"

, font=BUTTON_FONT, bg=OCEAN_BLUE,

fg=WHITE, command=send_message)

message_button.pack(side=tk.LEFT, padx=10)
message_box =

scrolledtext.ScrolledText(middle_frame, font=SMALL_FONT,
bg=MEDIUM_GREY, fg=WHITE, width=67, height=26.5)

message_box.config(state=tk.DISABLED)
message_box.pack(side=tk.TOP)

def main():
w.mainloop()

21

if __name__ ==

'__main__':

main()
Button = tk.Button(self,
text=
"EXTROVERT"

,height=2,width=45, font=("Arial"
,

15),bg=
"pink"

,command=extro)
Button.place(x=150, y=400)
class Application(tk.Tk):
def __init__(self,

*args,

**kwargs):

tk.Tk.__init__(self,

*args,

**kwargs)

window = tk.Frame(self)
window.pack()
window.grid_rowconfigure(0, minsize = 500)
window.grid_columnconfigure(0, minsize = 800)
self.frames = {}
for F in (FirstPage, SecondPage, ThirdPage):
frame = F(window, self)
self.frames[F] = frame
frame.grid(row = 0, column=0, sticky=

"nsew")

self.show_frame(FirstPage)
def show_frame(self, page):
frame = self.frames[page]
frame.tkraise()
self.title("Application")
app = Application()
app.maxsize(800,800)
app.mainloop()