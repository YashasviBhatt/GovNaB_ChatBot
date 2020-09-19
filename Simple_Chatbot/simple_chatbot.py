# Simple ChatBot

# importing the classes
from nltk_chat_util_updated import Chat, reflections
from tkinter import Tk
from tkinter import Label
from tkinter import Frame
from tkinter import Canvas
from tkinter import Scrollbar
from tkinter import StringVar
from tkinter import Entry
from tkinter import Button
from tkinter.messagebox import showinfo
from tkinter import PhotoImage


#-------------------------------------------------Programming Logic-------------------------------------------------

y = 0

# creating function to process string
def string_processor(string):
    counter = 0
    updated_string = ''
    string_list = string.split(' ')
    for word in string_list:
        counter += 1
        if counter == 6:
            updated_string += '\n ' + word + ' '
            counter = 0
        else:
            updated_string += word + ' '
    return updated_string

# creating function to display the text on window
def screen_text(text_x, text_y, txt, color, ancr):
    global y
    txt = ' ' + txt + ' '
    t = canvas.create_text(text_x, text_y, text = txt, font = 'lucida 15', anchor = ancr)           # drawing text on canvas
    r = canvas.create_rectangle(canvas.bbox(t), fill = color)                                       # drawing box on canvas
    canvas.tag_lower(r, t)                                                                          # fitting text inside box
    rect_coord = canvas.bbox(r)                                                                     # fetching coordinates of retangle
    y += (rect_coord[3] - rect_coord[1]) + 5

# creating function to bind the Entry Field with Return
def send(event):
    chatbot()

# creating function to trigger the chatbot
def chatbot_preprocessing():
    # creating user input and it's respective response list
    pairs = [
        ['hello|hi|hey', [' Hello', ' Hey There']],
        ['my name is (.*)', [' Hi %1, how are you today']],
        ['what are you doing(.*)', [' I am solving your problems :)']],
        ['what is your name(.*)|who are you(.*)', [' I am GovNar :)']],
        ['how are you(.*)', [' I am fine, How about you ?']],
        ['fine(.*)|i am fine(.*)|(.*)great|doing great', [' Nice to hear :o']],
        ['age(.*)|your age(.*)|what is your age(.*)|how old are you(.*)',[' Asking someone\'s age is a rude step towards them :(']],
        ['sorry(.*)', [' It\'s Okay, never mind :)']],
        ['thanks(.*)', [' I am very much delighted :)']],
        ['who is your creator(.*)|who created you(.*)|who made you(.*)',[' Yashasvi Bhatt created me using NLTK Library of Python']],
        ['quit|bye', [' Bye! Take Care']]
    ]
    chat = Chat(pairs, reflections)                                             # binding the input and their respective response
    return chat

# creating function to print the values on screen
def chatbot():
    chat = chatbot_preprocessing()                                              # calling chatbot_preprocessing to process the patterns and o|p
    usr_inpt = input_query.get()
    input_query.set('')
    screen_text(20, y, usr_inpt, '#ffb85f', 'nw')                               # calling screen_text to display text on GUI Window
    if usr_inpt != None:
        usr_inpt.lower()
    bot_response = chat.converse(usr_inpt)                                      # taking input from user and getting it's respective response
    if bot_response == None:
        screen_text(430, y, 'Sorry! I didn\'t get that', '#ff7a5a', 'ne')       # calling screen_text to display text on GUI Window
    else:
        screen_text(430, y, string_processor(bot_response), '#ff7a5a', 'ne')    # calling screen_text to display text on GUI Window
    if usr_inpt.lower() == 'quit' or usr_inpt.lower() == 'bye':
        showinfo('Are you Leaving ? :(', 'Nice talking to you :)')
        root.destroy()
        quit()
    # moving the canvas scroll to the bottom
    canvas.configure(scrollregion = canvas.bbox('all'))
    canvas.yview_moveto(1)

# function to move screen up or scroll down
def move_down():
    canvas.configure(scrollregion = canvas.bbox('all'))                     # adding scroll functionality to canvas
    canvas.yview_scroll(1, 'unit')                                          # moving content up or scroll down

# function to move screen down or scroll up
def move_up():
    canvas.configure(scrollregion = canvas.bbox('all'))                     # adding scroll functionality to canvas
    canvas.yview_scroll(-1, 'unit')                                         # moving content down or scroll up

# giving mouse scroll functionality to canvas
def on_mousewheel(event):
    canvas.configure(scrollregion = canvas.bbox('all'))
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

#-------------------------------------------------Programming Logic-------------------------------------------------


#-------------------------------------------------GUI Logic-------------------------------------------------

# setting up the GUI Window
# opening the GUI Window
root = Tk()                                                                 # creating object of Tk Class
root.geometry('450x650')                                                    # setting the default size of GUI Window
root.minsize(450, 650)                                                      # setting the minimum size of GUI Window
root.maxsize(450, 650)                                                      # setting the maximum size of GUI Window
root.title('GovNar - A ChatBot made by Yashasvi Bhatt')                     # giving the title to GUI Window
root.wm_iconbitmap('images/simple_chatbot.ico')                             # giving icon to GUI Window
root.configure(bg = '#00aaa0')                                              # setting the background color of root window

# setting up the main layout of GUI Window

# header
Label(text = 'GovNar', font = 'lucida 25 bold', bg = '#462666', fg = '#fcf4d9', width = 450, height = 2).pack()

# body header
Label(text = 'Hey There! I am a ChatBot, I can help you', font = 'lucida 15 bold', fg = '#003366', bg = '#00aaa0').pack(pady = 10)

# creating a canvas for chat representation
canvas = Canvas(width = 450, height = 400, bg = '#00aaa0', highlightthickness = 0)
canvas.pack()
canvas.bind_all("<MouseWheel>", on_mousewheel)                      # binding the mousewheel with scroll functionality

# creating scroll-down button
photo_down = PhotoImage(file = 'images/down.png')
Button(image = photo_down, width = 20, height = 20, command = move_down).place(x = 150, y = 552)

# creating scroll-up button
photo_up = PhotoImage(file = 'images/up.png')
Button(image = photo_up, width = 20, height = 20, command = move_up).place(x = 280, y = 552)

# creating input field
input_query = StringVar()
input_field = Entry(textvariable = input_query, width = 22, font = 'comicsansms 20 italic', relief = 'sunken', borderwidth = 8)
input_field.place(x = 10, y = 593)
input_field.bind('<Return>', send)                                  # binding the enter button to send functionality


# creating send button
Button(text = 'Send', font = 'comicsansms 13 bold', height = 1, borderwidth = 10, command = chatbot).place(x = 370, y = 593)


# holding the GUI window open
root.mainloop()

#-------------------------------------------------GUI Logic-------------------------------------------------