#import library
from tkinter import *
from PIL import ImageTk,Image #PIL -> Pillow
import random

#initialize window
root = Tk()
root.geometry('400x400')
root.resizable(0,0)
root.title('Rock,Paper,Scissors-Game')
root.config(bg ='seashell3')

same=True
n= 0.9

# Adding a background image
background_image = Image.open("sps.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth * n)
if same:
    newImageSizeHeight = int(imageSizeHeight * n)
else:
    newImageSizeHeight = int(imageSizeHeight / n)

background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)
Canvas1 = Canvas(root)
Canvas1.create_image(200, 200, image=img)
Canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
Canvas1.pack(expand=True, fill=BOTH)


#heading
Label(root, text = 'Rock, Paper ,Scissors' , font='arial 20 bold', bg = 'white').pack()


##user choice
user_take = StringVar()

#functions runned by choice buttons
def Rock():
    user_take.set("rock")

def Scissor():
    user_take.set("scissors")

def Paper():
    user_take.set("paper")


Label(root, text = 'Choose any one: rock, paper, scissors' , font='arial 15 bold', bg = 'white').place(x = 20,y=70)
#Buttons to select option
Button(root, font = 'arial 13 bold', text = 'ROCK'  ,padx =5, bg ='Cornflowerblue' ,fg = 'white',command = Rock ).place(x=70,y=110)
Button(root, font = 'arial 13 bold', text = 'PAPER'  ,padx =5, bg ='Cornflowerblue',fg = 'white' ,command = Paper ).place(x=160,y=110)
Button(root, font = 'arial 13 bold', text = 'SCISSOR'  ,padx =5, bg ='Cornflowerblue', fg = 'white' ,command = Scissor ).place(x=255,y=110)

#user input box
Entry(root, font = 'arial 15', textvariable = user_take , bg = 'antiquewhite2').place(x=90 , y = 150)



#computer choice
comp_pick = random.randint(1,3)
if comp_pick == 1:
    comp_pick = 'rock'
elif comp_pick ==2:
    comp_pick = 'paper'
else:
    comp_pick = 'scissors'
    



##function to play
Result = StringVar()

def play():
    user_pick = user_take.get()
    if user_pick == comp_pick:
        Result.set('tie,you both select same')
    elif user_pick == 'rock' and comp_pick == 'paper':
        Result.set('you loose,computer select paper')
    elif user_pick == 'rock' and comp_pick == 'scissors':
        Result.set('you win,computer select scissors')
    elif user_pick == 'paper' and comp_pick == 'scissors':
        Result.set('you loose,computer select scissors')
    elif user_pick == 'paper' and comp_pick == 'rock':
        Result.set('you win,computer select rock')
    elif user_pick == 'scissors' and comp_pick == 'rock':
        Result.set('you loose,computer select rock')
    elif user_pick == 'scissors' and comp_pick == 'paper':
        Result.set('you win ,computer select paper')
    else:
        Result.set('invalid: choose any one -- rock, paper, scissors')
    
        
    
##fun to reset
def Reset():
    Result.set("") 
    user_take.set("")

##fun to exit
def Exit():
    root.destroy()


###### button
Entry(root, font='arial 10 bold', textvariable=Result, bg='lightgray', width=50).place(x=25, y=250)

Button(root, font='arial 13 bold', text='PLAY > ', padx=5, bg='cyan', command=play).place(x=150, y=190)

Button(root, font='arial 13 bold', text='RESET', padx=5, bg='lime', command=Reset).place(x=70, y=310)

Button(root, font='arial 13 bold', text='EXIT', padx=5, bg='red', fg='white', command=Exit).place(x=230, y=310)

root.mainloop()
