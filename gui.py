import tkinter as tk
from tkinter import LEFT, ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename

window = tk.Tk()
window.title('ACW1 Group 8')

#All frames in initialization
frm_buttons = tk.Frame(window, relief= tk.RAISED,bd = 2)
frm_encode = tk.Frame(window)
frm_decode = tk.Frame(window)

def OpenEncodeFrame():
    frm_decode.grid_remove()
    frm_encode.grid(row=0,column=1,sticky='nsw')

def OpenDecodeFrame():
    frm_encode.grid_remove()
    frm_decode.grid(row=0,column=1,sticky='nsw')

def openPayload():
    filePath = filedialog.askopenfilename()
    label_inputPayloadPath.configure(text=filePath)

def openCoverload():
    filePath = filedialog.askopenfilename()
    label_inputCoverPath.configure(text=filePath)

def save():
    filePath = filedialog.askdirectory()
    label_outputPath.configure(text=filePath)

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
btn_inputPayload = tk.Button(frm_encode,text = 'Select',command=openPayload)
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
label_outputPath = tk.Label(frm_encode,text='Select file location to save...',relief=tk.GROOVE,width=50,anchor='w')
label_outputPath.grid(row= 6,column= 0)
btn_output = tk.Button(frm_encode,text = 'Select',command=save)
btn_output.grid(row=6,column=1)

#Select bits (Encode) R7
label_bits = tk.Label(frm_encode,text="Select number of bits: ")
label_bits.grid(row=7,column=0,padx= 0,pady= 5,sticky= 'nw')
numberOfBits = [0,1,2,3,4,5,6,7]
choiceVar = tk.StringVar()
bitsComboBox = ttk.Combobox(frm_encode,textvariable=choiceVar,values=numberOfBits)
bitsComboBox.grid(row=7,column=1,pady= 5)

#Start encoding (Encode) R8
btn_encode = tk.Button(frm_encode, text= 'Start Encoding')
btn_encode.grid(row=8,column=0,columnspan= 2,sticky= 'ew',padx = 5, pady = 5)

#Encode button on left side of window
btn_encode = tk.Button(frm_buttons, text= 'Encode',command=OpenEncodeFrame)
btn_encode.grid(row=0,column=0,sticky= 'ew',padx = 5, pady = 5)

#Decode button on right side of window
btn_decode = tk.Button(frm_buttons, text= 'Decode',command=OpenDecodeFrame)
btn_decode.grid(row=1,column=0,sticky= 'ew',padx = 5, pady = 5)

frm_buttons.grid(row=0,column=0,sticky= 'ns')

window.mainloop()