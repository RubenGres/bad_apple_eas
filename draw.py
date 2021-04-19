from tkinter import *
import pickle
import sys
from PIL import Image, ImageTk

WIDTH = 416
HEIGHT = 300

offsetX = 90
offsetY = 80

X = WIDTH/2
Y = HEIGHT/2

drawing_speed = 1

def left(event):
    global X
    draw(X, Y, X-drawing_speed, Y)
    X-=drawing_speed
def right(event):
    global X
    draw(X, Y, X+drawing_speed, Y)
    X+=drawing_speed
def up(event):
    global Y
    draw(X, Y-drawing_speed, X, Y)
    Y-=drawing_speed
def down(event):
    global Y
    draw(X, Y+drawing_speed, X, Y)
    Y+=drawing_speed
    
def draw(X1, Y1, X2, Y2):
    w.create_line(offsetX + X1, offsetY + Y1, offsetX + X2, offsetY + Y2)

def drawEAS(eas):
    global Y
    global X

    X = eas[0][0]
    Y = eas[0][1]

    for l in eas:
        if l[0] == X or l[1] == Y:
            draw(X, Y, l[0], l[1])
            X = l[0]
            Y = l[1]
        else:
            print('Unaligned line : ' + str(l))

if len(sys.argv) < 2:
    print("Need a eas file")
    exit(0)

filename = sys.argv[1]
with open(filename, 'rb') as handle:
    eas = pickle.load(handle)

root = Tk()
root.title('Etch a Sketch')

image = Image.open("etch.png") 
photo = ImageTk.PhotoImage(image) 


w = Canvas(root, width = image.size[0], height = image.size[1]) 
w.create_image(0,0, anchor = NW, image=photo)
w.pack() 

root.bind('<Left>', left)
root.bind('<Right>', right)
root.bind('<Up>', up)
root.bind('<Down>', down)

drawEAS(eas)

root.mainloop()