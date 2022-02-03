from tkinter import *
from tkinter import filedialog
from PIL import Image


# Function to open an image in the system
def open_files():
    try:
        filepath = filedialog.askopenfilename(title="Open an Image",
                                              filetypes=(("Image", "*.jpg\n*.jpeg\n*.png",), ("All files", "*.*")))
        img = Image.open(filepath)
        process_file(img)
    except IOError:
        print("Error")


def process_file(image):
    #Setting up the exit file and the palette
    f = open("Result.txt", "w")
    palette = "@BWM#0Z&8QhkOXbmunzxaocrj1{[I?t!li<+;^:,`. "

    width = image.width
    height = image.height
    #For each pixel determine its brightness, match a symbol, and write it to the exit file
    for j in range(height):
        for i in range(width):
            brightness = image.getpixel((i,j))
            f.write(palette[int(((brightness[0]+brightness[1]+brightness[2])/3)/255*(len(palette)-1))])
        f.write(("\n"))
    print("Done")

def main():

    win = Tk()
    win.geometry("700x300")

    Label(win, text="Click the button to open a dialog", font='Arial 16 bold').pack(pady=100)
    button = Button(win, text="Open", command=open_files)
    button.pack()

    win.mainloop()

if __name__ == "__main__":
    main()
