# import modules
import tkinter
from tkinter import *
from tkinter.filedialog import *
import tkinter.filedialog
from tkinter import messagebox,ttk
from PIL import ImageTk
from PIL import Image
from io import BytesIO
import os

import hide_img_in_cover_img
import hide_img_in_text_file

class IMG_Stegno:

    output_image_size = 0

    # main frame or start page
    def main(self, root):
        root.title('LSB Steganography')
        root.geometry('800x600')
        root.resizable(width=False, height=False)
        root.config(bg='#e3f4f1') 
        frame = Frame(root)
        frame.grid()

        title = Label(frame, text='LSB Steganography')
        title.config(font=('Times new roman', 25, 'bold'))
        title.grid(pady=10)
        title.config(bg='#e3f4f1')
        title.grid(row=1)

        encode = Button(frame, text="Encode", command=lambda: self.choose_frame0(frame), padx=14, bg='#e3f4f1')
        encode.config(font=('Helvetica', 14), bg='#e8c1c7')
        encode.grid(row=2)
        decode = Button(frame, text="Decode", command=lambda: self.decode_frame1(frame), padx=14, bg='#e3f4f1')
        decode.config(font=('Helvetica', 14), bg='#e8c1c7')
        decode.grid(pady=12)
        decode.grid(row=3)

        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)

    # back function to loop back to main screen
    def back(self, frame):
        frame.destroy()
        self.main(root)

    def OpenFile(self):
        global my_img
        FileOpen = StringVar()
        FileOpen = askopenfilename(initialdir="/Desktop", title="SelectFile",
                                   filetypes=(('png', '*.png'), ('jpeg', '*.jpeg'), ('jpg', '*.jpg'),
                                              ("all type of files", "*.*")))
        if not FileOpen:
            messagebox.showerror("Error", "You have selected nothing !")
        else:
            label_inputCoverPath.configure(text=FileOpen)
            my_img = Image.open(FileOpen)

    def OpenImagePayloadFile(self):
        global my_payloadImg
        global image_to_hide
        FileOpen2 = StringVar()
        FileOpen2 = askopenfilename(initialdir="/Desktop", title="SelectFile",
                                   filetypes=(('png', '*.png'), ('jpeg', '*.jpeg'), ('jpg', '*.jpg'),
                                              ("all type of files", "*.*")))
        if not FileOpen2:
            messagebox.showerror("Error", "You have selected nothing !")
        else:
            label_inputPayloadPath.configure(text=FileOpen2)
            my_payloadImg = Image.open(FileOpen2)
            image_to_hide = my_payloadImg.resize(my_img.size)

    def OpenTextFile(self):
        global textfile
        FileOpen = StringVar()
        FileOpen = askopenfilename(initialdir="/Desktop", title="SelectFile",
                                    filetypes=(('text files', '*.txt'),
                                               ("all type of files", "*.*")))
        if not FileOpen:
            messagebox.showerror("Error", "You have selected nothing !")
        else:
            label_inputFilePath.configure(text=FileOpen)
            textfile = FileOpen

    # frame for choosing encoding options
    def choose_frame0(self,F):
        F.destroy()
        F0 = Frame(root)

        button_bws = Button(F0, text='Hide text in image', command=lambda: self.encode_frame1(F0))
        button_bws.config(font=('Helvetica', 18), bg='#e8c1c7')
        button_bws.grid()

        button_bws1 = Button(F0, text='Hide image in image', command=lambda: self.encode_frame2(F0))
        button_bws1.config(font=('Helvetica', 18), bg='#e8c1c7')
        button_bws1.grid()

        button_bws2 = Button(F0, text='Hide text in mp3 file', command=lambda: self.encode_frame3(F0))
        button_bws2.config(font=('Helvetica', 18), bg='#e8c1c7')
        button_bws2.grid()

        button_bws3 = Button(F0, text='Hide text in a file', command=lambda: self.encode_frame4(F0))
        button_bws3.config(font=('Helvetica', 18), bg='#e8c1c7')
        button_bws3.grid()

        button_back = Button(F0, text='Cancel', command=lambda: IMG_Stegno.back(self, F0))
        button_back.config(font=('Helvetica', 18), bg='#e8c1c7')
        button_back.grid(pady=15)
        button_back.grid()
        F0.grid()

    # frame for hiding text in image
    def encode_frame1(self, F):
        global label_inputCoverPath
        F.destroy()
        F2 = Frame(root)
        label1 = Label(F2, text='Select the Image in which you want to hide text :')
        label1.config(font=('Times new roman', 20, 'bold'), bg='#e3f4f1')
        label1.grid(columnspan=5)

        label1 = Label(F2,text="Name of the File")
        label1.config(font=('Helvetica', 14, 'bold'))
        label1.grid(row=3,column=0,padx= 0,pady= 0,sticky= 'nw')

        label_inputCoverPath = Label(F2, text='Cover Object file path ...', relief=GROOVE, width=57)
        label_inputCoverPath.grid(row=3, column= 1,padx=5)

        SelectButton = Button(F2,text="Select the file", command=self.OpenFile)
        SelectButton.grid(row=3,column=2,padx= 5,pady= 0)

        label2 = Label(F2, text='Enter the message')
        label2.config(font=('Helvetica', 14, 'bold'))
        label2.grid(row=4,column=0,padx= 0,sticky='nw')
        text_a = Text(F2, width=50, height=5)
        text_a.grid(row=4,column=1)

        label1 = Label(F2,text="Number of bits")
        label1.config(font=('Helvetica', 14, 'bold'))
        label1.grid(row=5,column=0,padx= 0,pady= 0,sticky= 'nw')

        EncodeButton = Button(F2,text="Encode",command=lambda: [self.enc_fun(text_a, my_img), IMG_Stegno.back(self, F2)])
        EncodeButton.grid(row=6,column=1 ,pady=5,sticky='n')

        numberOfBits = [0, 1, 2, 3, 4, 5, 6, 7]
        choiceVar = StringVar()
        bitsComboBox = ttk.Combobox(F2, textvariable=choiceVar, values=numberOfBits)
        bitsComboBox.grid(row=5, column=1, pady=5)

        button_back = Button(F2, text='Cancel', command=lambda: IMG_Stegno.choose_frame0(self, F2))
        button_back.config(font=('Helvetica', 18), bg='#e8c1c7')
        button_back.grid(pady=15)
        button_back.grid()

        F2.grid(row=0,column=0,padx= 20,pady= 20, sticky='nw')

    # frame for hiding image in image
    def encode_frame2(self, F):
        global label_inputCoverPath
        global label_inputPayloadPath

        F.destroy()
        F2i = Frame(root)
        label1 = Label(F2i, text='Select the Image in which you want to hide image :')
        label1.config(font=('Times new roman', 20, 'bold'), bg='#e3f4f1')
        label1.grid(columnspan=5)

        coverLabel = Label(F2i,text="Cover Image")
        coverLabel.config(font=('Helvetica', 14, 'bold'))
        coverLabel.grid(row=3,column=0,padx= 0,pady= 0,sticky= 'nw')

        label_inputCoverPath = Label(F2i, text='Cover Object file path ...', relief=GROOVE, width=57)
        label_inputCoverPath.grid(row=3, column= 1,padx=5)

        SelectButton = Button(F2i,text="Select the file", command=self.OpenFile)
        SelectButton.grid(row=3,column=2,padx= 5,pady= 0)

        payloadLabel = Label(F2i, text="Payload Image")
        payloadLabel.config(font=('Helvetica', 14, 'bold'))
        payloadLabel.grid(row=4, column=0, padx=0, pady=0, sticky='nw')

        label_inputPayloadPath = Label(F2i, text='Payload file path ...', relief=GROOVE, width=57)
        label_inputPayloadPath.grid(row=4, column=1, padx=5)

        payloadButton = Button(F2i, text="Select the file", command=self.OpenImagePayloadFile)
        payloadButton.grid(row=4, column=2, padx=5, pady=0)

        label1 = Label(F2i,text="Number of bits")
        label1.config(font=('Helvetica', 14, 'bold'))
        label1.grid(row=5,column=0,padx= 0,pady= 0,sticky= 'nw')

        numberOfBits = [0, 1, 2, 3, 4, 5, 6, 7]
        choiceVar2 = IntVar()
        bitsComboBox = ttk.Combobox(F2i, textvariable=choiceVar2, values=numberOfBits)
        bitsComboBox.grid(row=5, column=1, pady=5)
        #current_bit = int(bitsComboBox.get())

        EncodeButton = Button(F2i,text="Encode",command=lambda: [hide_img_in_cover_img.encodeImage(image_to_hide, my_img, int(bitsComboBox.get())).save("encode3.png"),hide_img_in_cover_img.decodeImage(Image.open("encode3.png"), 3).save("decode3.png"),IMG_Stegno.back(self, F2i)])
        EncodeButton.grid(row=6,column=1 ,pady=5,sticky='n')

        button_back = Button(F2i, text='Cancel', command=lambda: IMG_Stegno.choose_frame0(self, F2i))
        button_back.config(font=('Helvetica', 18), bg='#e8c1c7')
        button_back.grid(pady=15)
        button_back.grid()

        F2i.grid(row=0,column=0,padx= 20,pady= 20, sticky='nw')


    # frame for hiding stuff in a music file/video?
    def encode_frame3(self, F):
        F.destroy()
        F3 = Frame(root)
        label1 = Label(F3, text='Select the mp3/mp4 in which you want to hide a payload :')
        label1.config(font=('Times new roman', 20, 'bold'), bg='#e3f4f1')
        label1.grid(columnspan=5)

        #move stuff here

        button_back = Button(F3, text='Cancel', command=lambda: IMG_Stegno.choose_frame0(self, F3))
        button_back.config(font=('Helvetica', 18), bg='#e8c1c7')
        button_back.grid(pady=15)
        button_back.grid()

        F3.grid(row=0,column=0,padx= 20,pady= 20, sticky='nw')

    def height(self):
        height, width = hide_img_in_text_file.encodeImage(my_img, textfile, int(bitsComboBox4.get()))
        return height

    def width(self):
        height, width = hide_img_in_text_file.encodeImage(my_img, textfile, int(bitsComboBox4.get()))
        return width

    # frame for hiding image in a text file
    def encode_frame4(self, F):
        global label_inputFilePath
        global label_inputCoverPath
        global bitsComboBox4
        F.destroy()
        F4 = Frame(root)
        label1 = Label(F4, text='Select the text file in which you want to hide an image :')
        label1.config(font=('Times new roman', 20, 'bold'), bg='#e3f4f1')
        label1.grid(columnspan=5)

        label1 = Label(F4, text="Name of the File")
        label1.config(font=('Helvetica', 14, 'bold'))
        label1.grid(row=3, column=0, padx=0, pady=0, sticky='nw')

        label_inputFilePath = Label(F4, text='Cover Object file path ...', relief=GROOVE, width=57)
        label_inputFilePath.grid(row=3, column=1, padx=5)

        open_button = Button(F4,text='Open Files',command=self.OpenTextFile)
        open_button.grid(row=3,column=2,padx= 5,pady= 0)

        coverLabel = Label(F4, text="Hidden Image")
        coverLabel.config(font=('Helvetica', 14, 'bold'))
        coverLabel.grid(row=4, column=0, padx=0, pady=0, sticky='nw')

        label_inputCoverPath = Label(F4, text='Hidden image file path ...', relief=GROOVE, width=57)
        label_inputCoverPath.grid(row=4, column=1, padx=5)

        SelectButton = Button(F4, text="Select the file", command=self.OpenFile)
        SelectButton.grid(row=4, column=2, padx=5, pady=0)

        label1 = Label(F4, text="Number of bits")
        label1.config(font=('Helvetica', 14, 'bold'))
        label1.grid(row=5, column=0, padx=0, pady=0, sticky='nw')

        numberOfBits = [0, 1, 2, 3, 4, 5, 6, 7]
        choiceVar2 = IntVar()
        bitsComboBox4 = ttk.Combobox(F4, textvariable=choiceVar2, values=numberOfBits)
        bitsComboBox4.grid(row=5, column=1, pady=5)
        # current_bit = int(bitsComboBox.get())


        EncodeButton = Button(F4, text="Encode", command=lambda: [
            hide_img_in_text_file.encodeImage(my_img, textfile, int(bitsComboBox4.get())),
            hide_img_in_text_file.decodeFile("encoded_file.txt", int(bitsComboBox4.get()),self.height(),self.width()).save("decoded_file.png"),
            IMG_Stegno.back(self, F4)])
        EncodeButton.grid(row=6, column=1, pady=5, sticky='n')

        button_back = Button(F4, text='Cancel', command=lambda: IMG_Stegno.choose_frame0(self, F4))
        button_back.config(font=('Helvetica', 18), bg='#e8c1c7')
        button_back.grid(pady=15)
        button_back.grid()

        F4.grid(row=0, column=0, padx=20, pady=20, sticky='nw')

    # frame for decode page
    def decode_frame1(self, F):
        F.destroy()
        d_f2 = Frame(root)
        label1 = Label(d_f2, text='Select Image with Hidden text:')
        label1.config(font=('Times new roman', 25, 'bold'), bg='#e3f4f1')
        label1.grid()
        label1.config(bg='#e3f4f1')
        button_bws = Button(d_f2, text='Select', command=lambda: self.decode_frame2(d_f2))
        button_bws.config(font=('Helvetica', 18), bg='#e8c1c7')
        button_bws.grid()
        button_back = Button(d_f2, text='Cancel', command=lambda: IMG_Stegno.back(self, d_f2))
        button_back.config(font=('Helvetica', 18), bg='#e8c1c7')
        button_back.grid(pady=15)
        button_back.grid()
        d_f2.grid()

    # function to decode image
    def decode_frame2(self, d_F2):
        d_F3 = Frame(root)
        myfiles = tkinter.filedialog.askopenfilename(
            filetypes=([('png', '*.png'), ('jpeg', '*.jpeg'), ('jpg', '*.jpg'), ('All Files', '*.*')]))
        if not myfiles:
            messagebox.showerror("Error", "You have selected nothing! ")
        else:
            my_img = Image.open(myfiles, 'r')
            my_image = my_img.resize((300, 200))
            img = ImageTk.PhotoImage(my_image)
            label4 = Label(d_F3, text='Selected Image :')
            label4.config(font=('Helvetica', 14, 'bold'))
            label4.grid()
            board = Label(d_F3, image=img)
            board.image = img
            board.grid()
            hidden_data = self.decode(my_img)
            label2 = Label(d_F3, text='Hidden data is :')
            label2.config(font=('Helvetica', 14, 'bold'))
            label2.grid(pady=10)
            text_a = Text(d_F3, width=50, height=10)
            text_a.insert(INSERT, hidden_data)
            text_a.configure(state='disabled')
            text_a.grid()
            button_back = Button(d_F3, text='Cancel', command=lambda: self.frame_3(d_F3))
            button_back.config(font=('Helvetica', 14), bg='#e8c1c7')
            button_back.grid(pady=15)
            button_back.grid()
            d_F3.grid(row=1)
            d_F2.destroy()

    # function to decode data
    def decode(self, image):
        image_data = iter(image.getdata())
        data = ''

        while (True):
            pixels = [value for value in image_data.__next__()[:3] +
                      image_data.__next__()[:3] +
                      image_data.__next__()[:3]]
            binary_str = ''
            for i in pixels[:8]:
                if i % 2 == 0:
                    binary_str += '0'
                else:
                    binary_str += '1'

            data += chr(int(binary_str, 2))
            if pixels[-1] % 2 != 0:
                return data

    # function to generate data
    def generate_Data(self, data):
        new_data = []

        for i in data:
            new_data.append(format(ord(i), '08b'))
        return new_data

    # function to modify the pixels of image
    def modify_Pix(self, pix, data):
        dataList = self.generate_Data(data)
        dataLen = len(dataList)
        imgData = iter(pix)
        for i in range(dataLen):
            # Extracting 3 pixels at a time
            pix = [value for value in imgData.__next__()[:3] +
                   imgData.__next__()[:3] +
                   imgData.__next__()[:3]]

            for j in range(0, 8):
                if (dataList[i][j] == '0') and (pix[j] % 2 != 0):
                    if (pix[j] % 2 != 0):
                        pix[j] -= 1

                elif (dataList[i][j] == '1') and (pix[j] % 2 == 0):
                    pix[j] -= 1

            if (i == dataLen - 1):
                if (pix[-1] % 2 == 0):
                    pix[-1] -= 1
            else:
                if (pix[-1] % 2 != 0):
                    pix[-1] -= 1

            pix = tuple(pix)
            yield pix[0:3]
            yield pix[3:6]
            yield pix[6:9]

    # function to enter the data pixels in image
    def encode_enc(self, newImg, data):
        w = newImg.size[0]
        (x, y) = (0, 0)

        for pixel in self.modify_Pix(newImg.getdata(), data):

            # Putting modified pixels in the new image
            newImg.putpixel((x, y), pixel)
            if (x == w - 1):
                x = 0
                y += 1
            else:
                x += 1

    # function to enter hidden text
    def enc_fun(self, text_a, myImg):
        data = text_a.get("1.0", "end-1c")
        if (len(data) == 0):
            messagebox.showinfo("Alert", "Kindly enter text in TextBox")
        else:
            newImg = myImg.copy()
            self.encode_enc(newImg, data)
            my_file = BytesIO()
            temp = os.path.splitext(os.path.basename(myImg.filename))[0]
            newImg.save(tkinter.filedialog.asksaveasfilename(initialfile=temp, filetypes=([('png', '*.png')]),
                                                             defaultextension=".png"))
            self.d_image_size = my_file.tell()
            self.d_image_w, self.d_image_h = newImg.size
            messagebox.showinfo("Success",
                                "Encoding Successful\nFile is saved as Image_with_hiddentext.png in the same directory")

    def frame_3(self, frame):
        frame.destroy()
        self.main(root)


# GUI loop
root = Tk()
o = IMG_Stegno()
o.main(root)
root.mainloop()
