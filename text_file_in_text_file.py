from PIL import Image
import os, numpy as np
import docx2txt
import docx
import aspose.words as aw

MAX_COLOR_VALUE = 255
MAX_BIT_VALUE = 8

def valid_xml_char_ordinal(c):
    codepoint = ord(c)
    # conditions ordered by presumed frequency
    return (
        0x20 <= codepoint <= 0xD7FF or
        codepoint in (0x9, 0xA, 0xD) or
        0xE000 <= codepoint <= 0xFFFD or
        0x10000 <= codepoint <= 0x10FFFF
        )

def to_bin(data):
    """Convert `data` to binary format as string"""
    if isinstance(data, str):
        return ''.join([ format(ord(i), "08b") for i in data ])
    elif isinstance(data, bytes) or isinstance(data, np.ndarray):
        return [ format(i, "08b") for i in data ]
    elif isinstance(data, int) or isinstance(data, np.uint8):
        return format(data, "08b")
    else:
        raise TypeError("Type not supported.")
        
# Creates an image with the RGB values
def createImage(data, resolution):
    image = Image.new("RGB", resolution)
    image.putdata(data)
    return image


def remove_n_least_significant_bits(value, n):
    value = value >> n
    return value << n


def get_n_least_significant_bits(value, n):
    value = value << MAX_BIT_VALUE - n
    value = value % MAX_COLOR_VALUE
    return value >> MAX_BIT_VALUE - n


def get_n_most_significant_bits(value, n):
    return value >> MAX_BIT_VALUE - n


def shift_n_bits_to_8(value, n):
    return value << MAX_BIT_VALUE - n


# Function to encode the image that we want to hide, into the cover image
def encodeTextFile(file_to_hide, file_to_hide_in, n_bits):


    # List to store the ascii values from the content of the file
    payload_bytes = []

    with open(file_to_hide, "rb") as out:
        while True:
            c = out.read(1)
            if not c:
                print("End of file")
                break
            payload_bytes.append(ord(c))
    #print(payload_bytes)

    cover_bytes = []

    with open(file_to_hide_in, "rb") as out:
        while True:
            c = out.read(1)
            if not c:
                print("End of file")
                break
            cover_bytes.append(ord(c))
    print(cover_bytes)

    """fullText = []
    doc = docx.Document(file_to_hide)
    for i in doc.paragraphs:
        #print(i.text)
        fullText.append(i.text)
    docText = '\n'.join(fullText)
    for i in docText:
        #print(ord(i))
        file_bytes.append(ord(i))"""

    payload_size = os.path.getsize(file_to_hide)  # file_size is the same as len(file_bytes)
    print("The payload file size is ", payload_size)

    cover_size = os.path.getsize(file_to_hide_in)
    print("The cover file size is ", cover_size)

    # Check if cover file size is smaller than payload img size
    if (cover_size < payload_size):
        print("Cover object size is smaller than payload size")
        quit()

    data = []
    for i in range(len(payload_bytes)):
        char_hide = payload_bytes[i]
        char_hide = get_n_most_significant_bits(char_hide, n_bits)

        char_hide_in = cover_bytes[i]
        char_hide_in = remove_n_least_significant_bits(char_hide_in, n_bits)

        data.append(char_hide + char_hide_in)

    with open("encoded_file.txt", "w", encoding="utf-8") as f:
        for i in data:
            f.write(chr(i))
    print(data)
    
    return None


#Decode image and n_bits as parameters.
def decodeFile(file_to_decode, n_bits):
    asciiArray = []
    with open(file_to_decode, "r", encoding="utf-8") as f:
        for i in f.read():
            #print(i)
            asciiArray.append(ord(i))
    
    print(asciiArray)

    data = ""
    for i in range(len(asciiArray)):
        char_encoded = asciiArray[i]
        char_encoded = get_n_least_significant_bits(char_encoded, n_bits)

        char_encoded = shift_n_bits_to_8(char_encoded, n_bits)

        print(chr(char_encoded))
        data += chr(char_encoded)

    with open("decoded_file.txt", "w", encoding="utf-8") as f:
        f.write(data)
    return None

# # Running encode function
# # no. of bits
n_bits = 7
# # path of files replace them as per your need.
#image_to_hide_path = "tree2.jpg"
#image_to_hide_in_path = "test.txt"
#image_to_hide_in_path = "wordTest.docx"
#image_to_hide_in_path = "excel.xlsx"
file_to_hide_path = "payload_file.txt"
cover_file_path = "test.txt"
#image_to_hide = Image.open(cover_img_path)
#height, width = encodeImage(image_to_hide, image_to_hide_in_path, n_bits)
encodeTextFile(file_to_hide_path, cover_file_path, n_bits)
print("File encoded Successfully!")
#
# # running the decode function
n_bits = 7
#
# # path where you would want to save decoded Image.
decoded_file_path = "decoded_file.txt"
file_to_decode_path = "encoded_file.txt"
decodeFile(file_to_decode_path, n_bits)
print("Image decoded Successfully!")
