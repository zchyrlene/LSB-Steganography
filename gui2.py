from ast import If
from tabnanny import check
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import LEFT, ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from PIL import ImageTk
from PIL import Image
from io import BytesIO
from click import command
import pygame #for mp3 files
from tkVideoPlayer import TkinterVideo #for mp4 files
from tkinter import filedialog

#Global Environment
filepathPayload = ''
filepathCover = ''
filepathOutputE = ''
filepathEncoded = ''
filepathOutputD = ''
numberOfBits = [0,1,2,3,4,5,6,7]
bitsManipulate = None

window = tk.Tk()#tkinter window
window.title('ACW1 Group 8')
pygame.mixer.init()# initialise the pygame

#All frames in initialization
frm_buttons = tk.Frame(window, relief= tk.RAISED,bd = 2)
frm_encode = tk.Frame(window)
frm_decode = tk.Frame(window)

def OpenEncodeFrame():
    '''Button Functionality for encode button.

    Uses grid remove to remove the decode frame. 
    Encode frame on the R0C1'''
    frm_decode.grid_remove()
    frm_encode.grid(row=0,column=1,sticky='nsw')

def OpenDecodeFrame():
    '''Button Functionality for decode button.
    
    Uses grid remove to remove the encode frame. 
    Decode frame on the R0C1'''
    frm_encode.grid_remove()
    frm_decode.grid(row=0,column=1,sticky='nsw')


def openPayloadEncoded():
    '''Uses file dialog to grab the file path of the selected payload file and creates a preview. 
    
    Supports png, jpg, jpeg, mp3, mp4, txt
    Preview is located on R8C0'''
    global filepathPayload
    filePath = filedialog.askopenfilename()
    filepathPayload=filePath
    label_inputPayloadPath.configure(text=filePath)
    if not filePath:
        messagebox.showerror("Error","Please select file")
    else:
        #print(filepathPayload)
        if filePath.lower().endswith(('.png', '.jpg', '.jpeg')):#display image
            img = ImageTk.PhotoImage((Image.open(filePath).resize((300,200))))
            label_image = Label(frm_encode, image = img)
            label_image.image=img
            label_image.grid(row=8,column=0,padx= 0,pady= 0)
        elif filePath.lower().endswith('.mp3'):#play mp3
            play_btn()
        elif filePath.lower().endswith('.mp4'):#play mp4
            videoplayer = TkinterVideo(master=frm_encode, scaled=True)
            videoplayer.load(filePath)
            videoplayer.grid(row=8,column=0,padx= 0,pady= 0)
            videoplayer.play() # play the video
        elif filePath.lower().endswith('.txt'):
            pathh = Entry(frm_encode)    
            pathh.insert(END, filePath)
            filePath = open(filePath) 
            data = filePath.read()
            txtarea = Text(frm_encode, width=40, height=10)
            txtarea.insert(END, data)
            filePath.close()
            pathh.grid(row=8,column=0,padx= 0,pady= 0)
            txtarea.grid(row=8,column=0,padx= 0,pady= 0)

def openEncodedFileDecode():
    '''Uses file dialog to grab the file path of the selected encoded file and creates a preview. 
    
    Supports png, jpg, jpeg, mp3, mp4, txt
    Preview is located on R6C0'''
    filePath = filedialog.askopenfilename()
    global filepathPayload
    filepathPayload=filePath
    label_inputPayloadPath.configure(text=filePath)
    if not filePath:
        messagebox.showerror("Error","Please select file")
    else:
        #print(filepathPayload)
        if filePath.lower().endswith(('.png', '.jpg', '.jpeg')):#display image
            img = ImageTk.PhotoImage((Image.open(filePath).resize((300,200))))
            label_image = Label(frm_decode, image = img)
            label_image.image=img
            label_image.grid(row=6,column=0,padx= 0,pady= 0)
        elif filePath.lower().endswith('.mp3'):#play mp3
            play_btn()
        elif filePath.lower().endswith('.mp4'):#play mp4
            videoplayer = TkinterVideo(master=frm_decode, scaled=True)
            videoplayer.load(filePath)
            videoplayer.grid(row=6,column=0,padx= 0,pady= 0)
            videoplayer.play() # play the video
        elif filePath.lower().endswith('.txt'):
            pathh = Entry(frm_decode)    
            pathh.insert(END, filePath)
            filePath = open(filePath) 
            data = filePath.read()
            txtarea = Text(frm_decode, width=40, height=10)
            txtarea.insert(END, data)
            filePath.close()
            pathh.grid(row=6,column=0,padx= 0,pady= 0)
            txtarea.grid(row=6,column=0,padx= 0,pady= 0)

def play():
    pygame.mixer.music.load(filepathPayload)
    pygame.mixer.music.play(loops=0)

def play_btn():
    play_button = Button(frm_encode, text='Play mp3 file',relief=GROOVE, command=play)
    play_button.grid(row=8,column=0)
    
def openCoverload():
    filePath = filedialog.askopenfilename()
    label_inputCoverPath.configure(text=filePath)

def SaveEncodeOutput():
    filePath = filedialog.askdirectory()
    label_outputPathEncode.configure(text=filePath)

def SaveDecodeOutput():
    filePath = filedialog.askdirectory()
    label_outputPathDecode.configure(text=filePath)

window.rowconfigure(0,minsize= 500,weight= 1)
window.columnconfigure(1,minsize= 600, weight= 1)

#Frame Title (Encode) R0
label_title = tk.Label(frm_encode,text='ENCODE DATA',font=('Arial',15))
label_title.grid(row= 0,column= 0,columnspan= 2,padx= 5,pady= 5,sticky= 'new')

#Payload object label & button (Encode) R1-R2
label_inputPayload = tk.Label(frm_encode,text="Input Payload File")
label_inputPayload.grid(row=1,column=0,padx= 0,pady= 5,sticky= 'nw')
label_inputPayloadPath = tk.Label(frm_encode,text='Payload file path ...',relief=tk.GROOVE,width=50,anchor='w',)
label_inputPayloadPath.grid(row= 2,column= 0)
btn_inputPayload = tk.Button(frm_encode,text = 'Select',command=openPayloadEncoded)
btn_inputPayload.grid(row=2,column=1)

#Cover object label & button (Encode) R3-R5
label_inputCover = tk.Label(frm_encode,text="Input Cover Object file")
label_inputCover.grid(row=3,column=0,padx= 0,pady= 5,sticky= 'nw')
label_inputCoverPath = tk.Label(frm_encode,text='Cover Object file path ...',relief=tk.GROOVE,width=50,anchor='w')
label_inputCoverPath.grid(row= 4,column= 0)
btn_inputCover = tk.Button(frm_encode,text = 'Select',command=openCoverload)
btn_inputCover.grid(row=4,column=1)

#Ouput Stego file (Encode) R5-R6
label_output = tk.Label(frm_encode,text="Output Encoded File Location")
label_output.grid(row=5,column=0,padx= 0,pady= 5,sticky= 'nw')
label_outputPathEncode = tk.Label(frm_encode,text='Select file location to save...',relief=tk.GROOVE,width=50,anchor='w')
label_outputPathEncode.grid(row= 6,column= 0)
btn_outputEncode = tk.Button(frm_encode,text = 'Select',command=SaveEncodeOutput)
btn_outputEncode.grid(row=6,column=1)

#Select bits (Encode) R7
label_bits = tk.Label(frm_encode,text="Select number of bits: ")
label_bits.grid(row=7,column=0,padx= 0,pady= 5,sticky= 'nw')
choiceVar = tk.StringVar()
bitsComboBox = ttk.Combobox(frm_encode,textvariable=choiceVar,values=numberOfBits)
bitsComboBox.grid(row=7,column=1,pady= 5)

#Frame Title (Decode) R0
label_title2 = tk.Label(frm_decode,text='DECODE DATA',font=('Arial',15))
label_title2.grid(row= 0,column= 0,columnspan= 2,padx= 5,pady= 5,sticky= 'new')

#Input Encoded object label & button (Decode) R1-R2
label_inputEncoded = tk.Label(frm_decode,text="Input encoded File")
label_inputEncoded.grid(row=1,column=0,padx= 0,pady= 5,sticky= 'nw')
label_inputEncodedPath = tk.Label(frm_decode,text='Encoded file path ...',relief=tk.GROOVE,width=50,anchor='w',)
label_inputEncodedPath.grid(row= 2,column= 0)
btn_inputEncoded = tk.Button(frm_decode,text = 'Select',command= openEncodedFileDecode)
btn_inputEncoded.grid(row=2,column=1)

#Ouput Stego file (Decode) R3-R4
label_output = tk.Label(frm_decode,text="Output Encoded File Location")
label_output.grid(row=3,column=0,padx= 0,pady= 5,sticky= 'nw')
label_outputPathDecode = tk.Label(frm_decode,text='Select file location to save...',relief=tk.GROOVE,width=50,anchor='w',)
label_outputPathDecode.grid(row= 4,column= 0)
btn_outputDecode = tk.Button(frm_decode,text = 'Select',command= SaveDecodeOutput)
btn_outputDecode.grid(row=4,column=1)

#Select bits (Encode) R5
label_bits = tk.Label(frm_decode,text="Select number of bits: ")
label_bits.grid(row=5,column=0,padx= 0,pady= 5,sticky= 'nw')
bitsComboBox = ttk.Combobox(frm_decode,textvariable=choiceVar,values=numberOfBits)
bitsComboBox.grid(row=5,column=1,pady= 5)

#Encode button on left side of window
btn_encode = tk.Button(frm_buttons, text= 'Encode',command=OpenEncodeFrame)
btn_encode.grid(row=0,column=0,sticky= 'ew',padx = 5, pady = 5)

#Decode button on right side of window
btn_decode = tk.Button(frm_buttons, text= 'Decode',command=OpenDecodeFrame)
btn_decode.grid(row=1,column=0,sticky= 'ew',padx = 5, pady = 5)

frm_buttons.grid(row=0,column=0,sticky= 'ns')

play_button = Button(frm_encode, text='Play mp3 file', font=("Arial", 12),relief=GROOVE, command=play)

#Get user inputs from the label boxes and comboboxes (encode)
def UserInputsEncode():
    global bitsManipulate, filepathPayload, filepathCover, filepathOutputE
    match bitsComboBox.get():
        case '0':
            bitsManipulate = 0
        case '1':
            bitsManipulate = 1
        case '2':
            bitsManipulate = 2
        case '3':
            bitsManipulate = 3
        case '4':
            bitsManipulate = 4
        case '5':
            bitsManipulate = 5
        case '6':
            bitsManipulate = 6
        case '7':
            bitsManipulate = 7
    if bitsManipulate == None:
        messagebox.showerror('No bits inputted')

    filepathPayload = label_inputPayloadPath.cget('text')
    filepathCover = label_inputCoverPath.cget('text')
    filepathOutputE = label_outputPathEncode.cget('text')
    print(bitsManipulate,'\n',filepathPayload,'\n',filepathCover,'\n',filepathOutputE,'\n')

#Start encoding (Encode) R9
btn_encode = tk.Button(frm_encode, text= 'Start Encoding', command= UserInputsEncode)
btn_encode.grid(row=9,column=0,columnspan= 2,sticky= 'ew',padx = 5, pady = 5)

#Get user inputs from the label boxes and comboboxes (decode)
def UserInputsDecode():
    global bitsManipulate, filepathEncoded, filepathOutputD
    match bitsComboBox.get():
        case '0':
            bitsManipulate = 0
        case '1':
            bitsManipulate = 1
        case '2':
            bitsManipulate = 2
        case '3':
            bitsManipulate = 3
        case '4':
            bitsManipulate = 4
        case '5':
            bitsManipulate = 5
        case '6':
            bitsManipulate = 6
        case '7':
            bitsManipulate = 7
    if bitsManipulate == None:
        messagebox.showerror('No bits inputted')

    filepathEncoded = label_inputPayloadPath.cget('text')
    filepathOutputD = label_outputPathDecode.cget('text')
    print(bitsManipulate,'\n',filepathEncoded,'\n',filepathOutputD,'\n',)

#Start decoding (Decode) R7
btn_encode = tk.Button(frm_decode, text= 'Start Decoding',command= UserInputsDecode)
btn_encode.grid(row=7,column=0,columnspan= 2,sticky= 'ew',padx = 5, pady = 5)

window.mainloop()