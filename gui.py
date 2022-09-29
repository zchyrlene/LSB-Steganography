from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import LEFT, ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from PIL import ImageTk
from PIL import Image
from io import BytesIO
import  os
import pygame #for mp3 files
from tkVideoPlayer import TkinterVideo #for mp4 files
from tkinter import filedialog

window = tk.Tk()#tkinter window
window.title('ACW1 Group 8')
pygame.mixer.init()# initialise the pygame

#All frames in initialization
frm_buttons = tk.Frame(window, relief= tk.RAISED,bd = 2)
frm_encode = tk.Frame(window)
frm_encode_options = tk.Frame(window)
frm_decode = tk.Frame(window)

fName=""
text_bx=""
my_img=None

def OpenEncodeOptionsFrame():
    title = tk.Label(frm_encode_options,text='ENCODE DATA',font=('Arial',15))
    title.grid(row= 0,column= 1,columnspan= 2,padx= 5,pady= 5,sticky= 'new')
    option1=Button(frm_encode_options, text='Encode Text in Image',relief=GROOVE, command=OpenEncodeTextInImageFrame)
    option1.grid(row=1,column=0)
    option2=Button(frm_encode_options, text='Encode Image in Image',relief=GROOVE, command=OpenEncodeImageInImageFrame)
    option2.grid(row=1,column=1)
    option3=Button(frm_encode_options, text='Encode Image in Text',relief=GROOVE, command=OpenEncodeImageInTextFrame)
    option3.grid(row=2,column=0)
    frm_encode_options.grid(row=0,column=1,sticky='nsw')

def OpenEncodeTextInImageFrame():
    frm_encode_options.grid_remove()
    frm_decode.grid_remove()
    
    #Frame Title (Encode) R0
    label_title = tk.Label(frm_encode,text='Encode Text in Image',font=('Arial',15))
    label_title.grid(row= 0,column= 0,columnspan= 2,padx= 5,pady= 5,sticky= 'new')

    #Payload object label & button (Encode) R1-R2
    label_inputPayload = tk.Label(frm_encode,text="Input Payload File")
    label_inputPayload.grid(row=1,column=0,padx= 0,pady= 5,sticky= 'nw')
    label_inputPayloadPath = tk.Label(frm_encode,text='Payload file path ...',relief=tk.GROOVE,width=50,anchor='w',)
    label_inputPayloadPath.grid(row= 2,column= 0)
    btn_inputPayload = tk.Button(frm_encode,text = 'Select',command=openPayload)
    btn_inputPayload.grid(row=2,column=1)

    ###Cover object label & button (Encode) R3-R5
    label_text = tk.Label(frm_encode,text='Enter Text')
    label_text.grid(row=3,column=0,padx= 0,pady= 5,sticky= 'nw')
    text_a = Text(frm_encode, width=50, height=5)
    text_a.grid(row=4,column=0)

    ###Ouput Stego file (Encode) R5-R6
    label_output = tk.Label(frm_encode,text="Output Encoded File Location")
    label_output.grid(row=7,column=0,padx= 0,pady= 5,sticky= 'nw')
    label_outputPath = tk.Label(frm_encode,text='Select file location to save...',relief=tk.GROOVE,width=50,anchor='w')
    label_outputPath.grid(row= 8,column= 0)
    btn_output = tk.Button(frm_encode,text = 'Select',command=save)
    btn_output.grid(row=8,column=1)

    ###Select bits (Encode) R7
    label_bits = tk.Label(frm_encode,text="Select number of bits: ")
    label_bits.grid(row=9,column=0,padx= 0,pady= 5,sticky= 'nw')
    numberOfBits = [0,1,2,3,4,5,6,7]
    choiceVar = tk.StringVar()
    bitsComboBox = ttk.Combobox(frm_encode,textvariable=choiceVar,values=numberOfBits)
    bitsComboBox.grid(row=9,column=1,pady= 5)

    #Start encoding (Encode) R8
    btn_encode = tk.Button(frm_encode, text= 'Start Encoding',command=enc_fun(text_a,my_img))
    btn_encode.grid(row=11,column=0,columnspan= 2,sticky= 'ew',padx = 5, pady = 5)

    frm_encode.grid(row=0,column=1,sticky='nsw')

def OpenEncodeImageInImageFrame():
    frm_encode_options.grid_remove()
    frm_decode.grid_remove()
    
    #Frame Title (Encode) R0
    label_title = tk.Label(frm_encode,text='Encode Image in Image',font=('Arial',15))
    label_title.grid(row= 0,column= 0,columnspan= 2,padx= 5,pady= 5,sticky= 'new')

    #Payload object label & button (Encode) R1-R2
    label_inputPayload = tk.Label(frm_encode,text="Input Payload File")
    label_inputPayload.grid(row=1,column=0,padx= 0,pady= 5,sticky= 'nw')
    label_inputPayloadPath = tk.Label(frm_encode,text='Payload file path ...',relief=tk.GROOVE,width=50,anchor='w',)
    label_inputPayloadPath.grid(row= 2,column= 0)
    btn_inputPayload = tk.Button(frm_encode,text = 'Select',command=openPayload)
    btn_inputPayload.grid(row=2,column=1)

    #Cover object label & button (Encode) R3-R5
    label_inputCover = tk.Label(frm_encode,text="Input Cover Object file")
    label_inputCover.grid(row=5,column=0,padx= 0,pady= 5,sticky= 'nw')
    label_inputCoverPath = tk.Label(frm_encode,text='Cover Object file path ...',relief=tk.GROOVE,width=50,anchor='w')
    label_inputCoverPath.grid(row= 6,column= 0)
    btn_inputCover = tk.Button(frm_encode,text = 'Select',command=openCoverload)
    btn_inputCover.grid(row=6,column=1)

    ###Ouput Stego file (Encode) R5-R6
    label_output = tk.Label(frm_encode,text="Output Encoded File Location")
    label_output.grid(row=7,column=0,padx= 0,pady= 5,sticky= 'nw')
    label_outputPath = tk.Label(frm_encode,text='Select file location to save...',relief=tk.GROOVE,width=50,anchor='w')
    label_outputPath.grid(row= 8,column= 0)
    btn_output = tk.Button(frm_encode,text = 'Select',command=save)
    btn_output.grid(row=8,column=1)

    ###Select bits (Encode) R7
    label_bits = tk.Label(frm_encode,text="Select number of bits: ")
    label_bits.grid(row=9,column=0,padx= 0,pady= 5,sticky= 'nw')
    numberOfBits = [0,1,2,3,4,5,6,7]
    choiceVar = tk.StringVar()
    bitsComboBox = ttk.Combobox(frm_encode,textvariable=choiceVar,values=numberOfBits)
    bitsComboBox.grid(row=9,column=1,pady= 5)

    #Start encoding (Encode) R8
    btn_encode = tk.Button(frm_encode, text= 'Start Encoding')
    btn_encode.grid(row=11,column=0,columnspan= 2,sticky= 'ew',padx = 5, pady = 5)

    frm_encode.grid(row=0,column=1,sticky='nsw')

def OpenEncodeImageInTextFrame():
    frm_encode_options.grid_remove()
    frm_decode.grid_remove()
    
    #Frame Title (Encode) R0
    label_title = tk.Label(frm_encode,text='Encode Image in Text',font=('Arial',15))
    label_title.grid(row= 0,column= 0,columnspan= 2,padx= 5,pady= 5,sticky= 'new')

    #Payload object label & button (Encode) R1-R2
    label_inputPayload = tk.Label(frm_encode,text="Input Payload File")
    label_inputPayload.grid(row=1,column=0,padx= 0,pady= 5,sticky= 'nw')
    label_inputPayloadPath = tk.Label(frm_encode,text='Payload file path ...',relief=tk.GROOVE,width=50,anchor='w',)
    label_inputPayloadPath.grid(row= 2,column= 0)
    btn_inputPayload = tk.Button(frm_encode,text = 'Select',command=openPayload)
    btn_inputPayload.grid(row=2,column=1)

    #Cover object label & button (Encode) R3-R5
    label_inputCover = tk.Label(frm_encode,text="Input Cover Object file")
    label_inputCover.grid(row=5,column=0,padx= 0,pady= 5,sticky= 'nw')
    label_inputCoverPath = tk.Label(frm_encode,text='Cover Object file path ...',relief=tk.GROOVE,width=50,anchor='w')
    label_inputCoverPath.grid(row= 6,column= 0)
    btn_inputCover = tk.Button(frm_encode,text = 'Select',command=openCoverload)
    btn_inputCover.grid(row=6,column=1)

    ###Ouput Stego file (Encode) R5-R6
    label_output = tk.Label(frm_encode,text="Output Encoded File Location")
    label_output.grid(row=7,column=0,padx= 0,pady= 5,sticky= 'nw')
    label_outputPath = tk.Label(frm_encode,text='Select file location to save...',relief=tk.GROOVE,width=50,anchor='w')
    label_outputPath.grid(row= 8,column= 0)
    btn_output = tk.Button(frm_encode,text = 'Select',command=save)
    btn_output.grid(row=8,column=1)

    ###Select bits (Encode) R7
    label_bits = tk.Label(frm_encode,text="Select number of bits: ")
    label_bits.grid(row=9,column=0,padx= 0,pady= 5,sticky= 'nw')
    numberOfBits = [0,1,2,3,4,5,6,7]
    choiceVar = tk.StringVar()
    bitsComboBox = ttk.Combobox(frm_encode,textvariable=choiceVar,values=numberOfBits)
    bitsComboBox.grid(row=9,column=1,pady= 5)

    #Start encoding (Encode) R8
    btn_encode = tk.Button(frm_encode, text= 'Start Encoding')
    btn_encode.grid(row=11,column=0,columnspan= 2,sticky= 'ew',padx = 5, pady = 5)

    frm_encode.grid(row=0,column=1,sticky='nsw')

def OpenDecodeFrame():
    frm_encode.grid_remove()
    frm_decode.grid(row=0,column=1,sticky='nsw')

def openPayload():
    filePath = filedialog.askopenfilename(initialdir="/Desktop", title="SelectFile",
                                   filetypes=(('png', '*.png'), ('jpeg', '*.jpeg'), ('jpg', '*.jpg'),
                                              ("all type of files", "*.*")))
    global fName
    fName=filePath
    label_inputPayloadPath = tk.Label(frm_encode,text=filePath,relief=tk.GROOVE,width=50,anchor='w',)
    label_inputPayloadPath.grid(row= 2,column= 0)

    if not filePath:
        messagebox.showerror("Error","Please select file")
    else:
        i = Image.open(filePath)
        r = i.resize((300, 200))
        img = ImageTk.PhotoImage(r)
        #image = ImageTk.PhotoImage((Image.open(filePath)))
        global my_img
        my_img=i
        label_image = Label(frm_encode, image = img)
        label_image.image=img
        label_image.grid(row=10,column=0,padx= 0,pady= 0)
    # else:
    #     if filePath.lower().endswith(('.png', '.jpg', '.jpeg')):#display image
    #         i = Image.open(filePath)
    #         r = i.resize((300, 200))
    #         img = ImageTk.PhotoImage(r)
    #         #image = ImageTk.PhotoImage((Image.open(filePath)))
    #         global my_img
    #         my_img=i
    #         label_image = Label(frm_encode, image = img)
    #         label_image.image=img
    #         label_image.grid(row=10,column=0,padx= 0,pady= 0)

    #         img_option1 = Button(frm_encode, text='Encode Text in Image',relief=GROOVE, command=textbox_display)
    #         img_option1.grid(row=4,column=0)
    #         # img_option2 = Button(frm_encode, text='Encode Image in Image',relief=GROOVE, command=)
    #         # img_option2.grid(row=4,column=1)

    #     elif filePath.lower().endswith('.mp3'):#play mp3
    #         play_btn()
    #     elif filePath.lower().endswith('.mp4'):#play mp4
    #         videoplayer = TkinterVideo(master=frm_encode, scaled=True)
    #         videoplayer.load(filePath)
    #         videoplayer.grid(row=8,column=0,padx= 0,pady= 0)
    #         videoplayer.play() # play the video
    #     elif filePath.lower().endswith('.txt'):
    #         pathh = Entry(frm_encode)    
    #         pathh.insert(END, filePath)
    #         filePath = open(filePath) 
    #         data = filePath.read()
    #         txtarea = Text(frm_encode, width=40, height=10)
    #         txtarea.insert(END, data)
    #         filePath.close()
    #         pathh.grid(row=8,column=0,padx= 0,pady= 0)
    #         txtarea.grid(row=8,column=0,padx= 0,pady= 0)

def play():
    pygame.mixer.music.load(fName)
    pygame.mixer.music.play(loops=0)

def play_btn():
    play_button = Button(frm_encode, text='Play mp3 file',relief=GROOVE, command=play)
    play_button.grid(row=8,column=0)
    
def openCoverload():
    filePath = filedialog.askopenfilename()
    #label_inputCoverPath.configure(text=filePath)
    label_inputCoverPath = tk.Label(frm_encode,text=filePath,relief=tk.GROOVE,width=50,anchor='w')
    label_inputCoverPath.grid(row= 6,column= 0)

def save():
    filePath = filedialog.askdirectory()
    #label_outputPath.configure(text=filePath)
    label_outputPath = tk.Label(frm_encode,text=filePath,relief=tk.GROOVE,width=50,anchor='w')
    label_outputPath.grid(row= 6,column= 0)

def generate_Data(data):
    new_data = []

    for i in data:
        new_data.append(format(ord(i), '08b'))
        return new_data

# function to modify the pixels of image
def modify_Pix(pix, data):
    dataList = generate_Data(data)
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
def encode_enc(newImg, data):
    w = newImg.size[0]
    (x, y) = (0, 0)

    for pixel in modify_Pix(newImg.getdata(), data):

        # Putting modified pixels in the new image
        newImg.putpixel((x, y), pixel)
        if (x == w - 1):
            x = 0
            y += 1
        else:
            x += 1

#encode text in image
def enc_fun(text_a, myImg):
    data = text_a.get("1.0", "end-1c")
    if (len(data) == 0):
        messagebox.showinfo("Alert", "Kindly enter text in TextBox")
    else:
        newImg = myImg.copy()
        encode_enc(newImg, data)
        my_file = BytesIO()
        temp = os.path.splitext(os.path.basename(myImg.filename))[0]
        newImg.save(filedialog.asksaveasfilename(initialfile=temp, filetypes=([('png', '*.png')]),defaultextension=".png"))
        #image_size = my_file.tell()
        # d_image_w, d_image_h = newImg.size
        messagebox.showinfo("Success",
                            "Encoding Successful\nFile is saved as Image_with_hiddentext.png in the same directory")

window.rowconfigure(0,minsize= 500,weight= 1)
window.columnconfigure(1,minsize= 600, weight= 1)

# #Frame Title (Encode) R0
# label_title = tk.Label(frm_encode,text='ENCODE DATA',font=('Arial',15))
# label_title.grid(row= 0,column= 0,columnspan= 2,padx= 5,pady= 5,sticky= 'new')

# #Payload object label & button (Encode) R1-R2
# label_inputPayload = tk.Label(frm_encode,text="Input Payload File")
# label_inputPayload.grid(row=1,column=0,padx= 0,pady= 5,sticky= 'nw')
# label_inputPayloadPath = tk.Label(frm_encode,text='Payload file path ...',relief=tk.GROOVE,width=50,anchor='w',)
# label_inputPayloadPath.grid(row= 2,column= 0)
# btn_inputPayload = tk.Button(frm_encode,text = 'Select',command=openPayload)
# btn_inputPayload.grid(row=2,column=1)

# ###Cover object label & button (Encode) R3-R5
# label_inputCover = tk.Label(frm_encode,text="Input Cover Object file")
# label_inputCover.grid(row=5,column=0,padx= 0,pady= 5,sticky= 'nw')
# label_inputCoverPath = tk.Label(frm_encode,text='Cover Object file path ...',relief=tk.GROOVE,width=50,anchor='w')
# label_inputCoverPath.grid(row= 6,column= 0)
# btn_inputCover = tk.Button(frm_encode,text = 'Select',command=openCoverload)
# btn_inputCover.grid(row=6,column=1)

# ###Ouput Stego file (Encode) R5-R6
# label_output = tk.Label(frm_encode,text="Output Encoded File Location")
# label_output.grid(row=7,column=0,padx= 0,pady= 5,sticky= 'nw')
# label_outputPath = tk.Label(frm_encode,text='Select file location to save...',relief=tk.GROOVE,width=50,anchor='w')
# label_outputPath.grid(row= 8,column= 0)
# btn_output = tk.Button(frm_encode,text = 'Select',command=save)
# btn_output.grid(row=8,column=1)

# ###Select bits (Encode) R7
# label_bits = tk.Label(frm_encode,text="Select number of bits: ")
# label_bits.grid(row=9,column=0,padx= 0,pady= 5,sticky= 'nw')
# numberOfBits = [0,1,2,3,4,5,6,7]
# choiceVar = tk.StringVar()
# bitsComboBox = ttk.Combobox(frm_encode,textvariable=choiceVar,values=numberOfBits)
# bitsComboBox.grid(row=9,column=1,pady= 5)

# #Start encoding (Encode) R8
# btn_encode = tk.Button(frm_encode, text= 'Start Encoding',command=enc_fun(text_bx,my_img))
# btn_encode.grid(row=11,column=0,columnspan= 2,sticky= 'ew',padx = 5, pady = 5)

#Encode button on left side of window
btn_encode = tk.Button(frm_buttons, text= 'Encode',command=OpenEncodeOptionsFrame)
btn_encode.grid(row=0,column=0,sticky= 'ew',padx = 5, pady = 5)

#Decode button on right side of window
btn_decode = tk.Button(frm_buttons, text= 'Decode',command=OpenDecodeFrame)
btn_decode.grid(row=1,column=0,sticky= 'ew',padx = 5, pady = 5)

frm_buttons.grid(row=0,column=0,sticky= 'ns')

play_button = Button(frm_encode, text='Play mp3 file', font=("Arial", 12),relief=GROOVE, command=play)

window.mainloop()
