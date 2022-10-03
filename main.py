from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont, ImageShow
import PIL

def open_file():
    filename = filedialog.askopenfilename(
        filetypes= (("PNG Picture","*.png"),
                    ("JPEG Picture","*.jpg"),
                    ("BMP Picture", "*.bmp"),
                    ("GIF Picture", "*.gif"),
                    ("all files","*.*"))
        )
    try:
        with Image.open(filename) as im1:
            # Convert im1 to RGBA mode.
            im1 = im1.convert('RGBA')
            # Create image watermark
            with Image.open('mask.png') as im2:
                im2 = im2.resize((im1.width, im1.height)).convert('RGBA')
            im3 = Image.blend(im1, im2, 0.09)
            ImageShow.show(im3, 'Image with Watermark')
        return
    except PIL.UnidentifiedImageError:
        messagebox.showinfo('File Error', 'Please select an image file.')
        return
    
#Create the window
window = Tk()
window.title("Water Marking Software")
window.minsize(width=400, height=400)
window.config(padx=40, pady=10)

#Create labels
label_upload = Label(text="Upload Your Image: ")
label_upload.grid(column=0, row=2)
#Create button
button_browse = Button(text="Browse", command=open_file)
button_browse.grid(column=2, row=2)
#Create canvas
canvas = Canvas(width=300, height=300, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(150, 150, image=logo_img)
canvas.grid(row=3, column=0, columnspan=3)

#Must put at the end
window.mainloop()