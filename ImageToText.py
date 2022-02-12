from tkinter import *
from tkinter import filedialog
from PIL import Image


# Function to open an image in the system
openedImg = Image.Image()
def open_file(goButton):
    try:
        filepath = filedialog.askopenfilename(title="Open an Image",
                                              filetypes=(("Image", "*.jpg\n*.jpeg\n*.png",), ("All files", "*.*")))
        global openedImg
        openedImg = Image.open(filepath)
        print(openedImg.width)
        goButton.config(state=NORMAL)
    except Exception:
        print("Error")


def process_file(finWidthE, finHeightE):
    f = open("Result.txt", "w")

    width = openedImg.width
    height = openedImg.height

    if (finWidthE.get() != ''):
        if(int(finWidthE.get())<1025):
            finWidth = int(finWidthE.get())
        else:
            finWidth = 1025
    else:
        finWidth = 100

    if (finHeightE.get() != ''):
        finHeight = int(finHeightE.get())
    else:
        finHeight = 100

    scaleW = width / finWidth
    scaleH = height / finHeight

    for i in range (finHeight):
        for j in range (finWidth):
            f.write(determine_character(j * scaleW, i * scaleH, (j + 1) * scaleW, (i + 1) * scaleH))

        f.write("\n")

    print("Done")

def determine_character(x1, y1, x2, y2):
    palette = "@BWM#0Z&8QhkOXbmunzxaocrj1{[I?t!li<+;^:,`. "
    scaleW = x2-x1
    scaleH = y2-y1
    brightSum = 0

    y1 = int (y1)
    y2 = int (y2)
    x1 = int (x1)
    x2 = int (x2)

    for i in range (y1, y2):
        for j in range(x1, x2):
            cords = (x1, y1)
            try:
                brightness = openedImg.getpixel(cords)
                brightSum += (brightness[0]+brightness[1]+brightness[2])/3
            except IndexError:
                pass

    try:
        return palette[int((brightSum/255*(len(palette)-1))/(scaleW*scaleH))]
    except IndexError:
        #IDK why, sometimes it breaks
        return '.'



def main():
    win = Tk()
    win.title("ImageToText")
    win.geometry("700x300")

    lb1 = Label(win, text="Please enter the desired width and height of the image", font='Arial 16 bold')

    wLab = Label(win, text="Width: ", font='Arial 8 bold')
    hLab = Label(win, text="Height: ", font='Arial 8 bold')
    wEntr = Entry(win, bg="Black", fg="White", width=5)
    hEntr = Entry(win, bg="Black", fg="White", width=5)

    lb1.pack()
    wLab.pack()
    wEntr.pack()
    hLab.pack()
    hEntr.pack()

    lb2 = Label(win, text="Click the button to select the Image", font='Arial 16 bold')
    imgButton = Button(win, text="Open", command=lambda: open_file(goButton))

    lb2.pack(pady=10)
    imgButton.pack()

    lb3 = Label(win, text="Click the button to process the Image", font='Arial 16 bold')
    goButton = Button(win, text="Process", command=lambda: process_file(wEntr, hEntr), state=DISABLED)
    lb3.pack(pady=10)
    goButton.pack()

    win.mainloop()


if __name__ == "__main__":
    main()
