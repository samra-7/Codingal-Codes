# Make sure you upload image in your current Repl
# Import all the necessary libraries
# PIL (Python Imaging Library) provides image editing capabilities to the python interpreter 
from tkinter import *
from PIL import Image, ImageTk

# Create a window with a title bar and set its geometry as well
window = Tk()
window.title('image')
window.geometry('400x400')

# Now use Image.open to open and identify the given image file. 
limage = Image.open("img.png")

# Convert this Image to Tkinter compatible image
image_l = ImageTk.PhotoImage(limage)

# Add image to Tkinter Label
label = Label(window, image=image_l, height=200, width=300)
button = Button(text = "Click Here", bg="#BC544B")
textbox = Text()
textbox.insert(END, "This is how you do it!")

label.pack()
button.pack()
textbox.pack()