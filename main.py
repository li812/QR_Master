import qrcode
from tkinter import *
from tkinter import filedialog

class QRGenerator:
    def __init__(self, master):
        self.master = master
        master.title("QR Code Generator")
        master.geometry("400x450")

        self.label = Label(master, text="Enter data to generate QR code:")
        self.label.pack()

        self.entry = Entry(master)
        self.entry.pack()

        self.label2 = Label(master, text="Select data type:")
        self.label2.pack()

        self.var = StringVar()
        self.var.set("Text")

        self.r1 = Radiobutton(master, text="Text", variable=self.var, value="Text")
        self.r1.pack()
        self.r2 = Radiobutton(master, text="URL", variable=self.var, value="URL")
        self.r2.pack()
        self.r3 = Radiobutton(master, text="Multi-URL", variable=self.var, value="Multi-URL")
        self.r3.pack()
        self.r4 = Radiobutton(master, text="Phone Number", variable=self.var, value="Phone Number")
        self.r4.pack()
        self.r5 = Radiobutton(master, text="Email", variable=self.var, value="Email")
        self.r5.pack()
        self.r6 = Radiobutton(master, text="SMS Extra", variable=self.var, value="SMS Extra")
        self.r6.pack()

        self.label3 = Label(master, text="Select file type:")
        self.label3.pack()

        self.var2 = StringVar()
        self.var2.set("PNG")

        self.r7 = Radiobutton(master, text="PNG", variable=self.var2, value="PNG")
        self.r7.pack()
        self.r8 = Radiobutton(master, text="JPG", variable=self.var2, value="JPG")
        self.r8.pack()
        self.r9 = Radiobutton(master, text="SVG", variable=self.var2, value="SVG")
        self.r9.pack()

        self.label4 = Label(master, text="Select size (in pixels):")
        self.label4.pack()

        self.entry2 = Entry(master)
        self.entry2.pack()

        self.button = Button(master, text="Generate QR Code", command=self.generate)
        self.button.pack()

        self.button2 = Button(master, text="Save QR Code", command=self.save)
        self.button2.pack()

    def generate(self):
        data = self.entry.get()
        data_type = self.var.get()

        if data_type == "Text":
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(data)
            qr.make(fit=True)
            img = qr.make_image(fill='black', back_color='white')
            self.img = img
        elif data_type == "URL":
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(data)
            qr.make(fit=True)
            img = qr.make_image(fill='black', back_color='white')
            self.img = img
        elif data_type == "Multi-URL":
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(data.split())
            qr.make(fit=True)
            img = qr.make_image(fill='black', back_color='white')
            self.img = img
        elif data_type == "Phone Number":
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(f"tel:{data}")
            qr.make(fit=True)
            img = qr.make_image(fill='black', back_color='white')
            self.img = img
        elif data_type == "Email":
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(f"mailto:{data}")
            qr.make(fit=True)
            img = qr.make_image(fill='black', back_color='white')
            self.img = img
        elif data_type == "SMS Extra":
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            number, message = data.split(',')
            qr.add_data(f"SMSTO:{number}:{message}")
            qr.make(fit=True)
            img = qr.make_image(fill='black', back_color='white')
            self.img = img

        size = self.entry2.get()
        if size:
            size = int(size)
            self.img = self.img.resize((size, size))

        self.img.show()

    def save(self):
        file_type = self.var2.get()
        file_types = [("PNG", "*.png"), ("JPG", "*.jpg"), ("SVG", "*.svg")]

        file_name = filedialog.asksaveasfilename(defaultextension=file_type,
                                                 filetypes=file_types)

        if file_name:
            try:
                self.img.save(file_name)
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while saving the file:\n{e}")
            return
            messagebox.showinfo("Success", "QR code saved successfully!")

root = Tk()
my_gui = QRGenerator(root)
root.mainloop()

