from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

def watermark(image_path, logo_path):
    background_image = Image.open(image_path)
    logo_image = Image.open(logo_path).convert("RGBA")

    max_logo_size = (200, 200)  # Adjust the size as needed
    logo_image.thumbnail(max_logo_size, Image.ANTIALIAS)

    result_image = Image.new('RGBA', background_image.size)
    result_image.paste(background_image, (0, 0))

    logo_x = result_image.width - logo_image.width - 10  # Adjust the position as needed
    logo_y = result_image.height - logo_image.height - 10  # Adjust the position as needed

    result_image.paste(logo_image, (logo_x, logo_y), mask=logo_image.split()[3])

    # Display the result in a Tkinter window
    window = Toplevel()
    window.title("Watermarked Image")
    photo = ImageTk.PhotoImage(result_image)
    label = Label(window, image=photo)
    label.image = photo
    label.pack()

def open_file():
    image_path = filedialog.askopenfilename(initialdir='C:\\Users\\PEDION\\Pictures\\')
    open_filelogo()

    def open_filelogo():
        logo_path = filedialog.askopenfilename(initialdir='C:\\Users\\PEDION\\Pictures\\')
        watermark(image_path, logo_path)

window = Tk()
window.title("Water Mark APP")
window.geometry('500x400')

label = Label(text="Select the image", font=("Arial", 25))
label.pack()
label.place(relx=0.5, rely=0.3, anchor=CENTER)

Button1 = Button(text="Select Image", command=open_file)
Button1.pack()
Button1.place(relx=0.5, rely=0.5, anchor=SE)

window.mainloop()