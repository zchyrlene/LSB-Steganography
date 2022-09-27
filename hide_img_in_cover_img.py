from PIL import Image

MAX_COLOR_VALUE = 255
MAX_BIT_VALUE = 8

#Creates an image with the RGB values
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

def shit_n_bits_to_8(value, n):
    return value << MAX_BIT_VALUE - n

#Function to encode the image that we want to hide, into the cover image
def encodeImage(image_to_hide, image_to_hide_in, n_bits):
    #print("Image to hide in ", image_to_hide_in.load())
    
    width = image_to_hide_in.size[0]
    height = image_to_hide_in.size[1]
    
    #.load() returns the "pixel_access" object that has the data(matrix) of the pixels.
    hide_image = image_to_hide.load()
    hide_in_image = image_to_hide_in.load()

    #this will store the values of each individual pixel as a matrix.
    data = []

    #looping the hide_image object.
    
    for y in range(height):
        for x in range(width):

            # most sig bits
            #print(hide_image[x,y]) #Uncomment this to see the pixel values in r,g,b form. (Shows every pixel's RGB value)
            try:
                #the value of n can be 1 or 2 and you won't see much difference in the encoded image.
                #gets n most significant bits of r,g,b values of image to hide.
                r_hide, g_hide, b_hide= hide_image[x,y]
                r_hide = get_n_most_significant_bits(r_hide, n_bits)
                g_hide = get_n_most_significant_bits(g_hide, n_bits)
                b_hide = get_n_most_significant_bits(b_hide, n_bits)

                # remove least n significant bits of image to hide in so we can store
                # the n most significant bits in that place.
                
                r_hide_in, g_hide_in, b_hide_in= hide_in_image[x,y]
                r_hide_in = remove_n_least_significant_bits(r_hide_in, n_bits)
                g_hide_in = remove_n_least_significant_bits(g_hide_in, n_bits)
                b_hide_in = remove_n_least_significant_bits(b_hide_in, n_bits)

                #Adding each MSB R,G,B from payload to LSB R,G,B cover image
                data.append((r_hide + r_hide_in, 
                             g_hide + g_hide_in,
                             b_hide + b_hide_in))

            #incase of exception it will show the reason.
            except Exception as e:
                print(e)

    #return an Image object from the above data.
    return createImage(data, image_to_hide.size)


#Decode image and n_bits as parameters.
def decodeImage(image_to_decode, n_bits):
    width = image_to_decode.size[0]
    height = image_to_decode.size[1]
    encoded_image = image_to_decode.load()

    #matrix that will store the extracted pixel values from the encoded Image.
    data = []

    #looping through every pixel in the encoded Image.
    for y in range(height):
        for x in range(width):

            #gets rgb values of encoded image.
            r_encoded, g_encoded, b_encoded = encoded_image[x,y]

            #get n least significant bits for each r,g,b value of the encoded image
            r_encoded = get_n_least_significant_bits(r_encoded, n_bits)
            g_encoded = get_n_least_significant_bits(g_encoded, n_bits)
            b_encoded = get_n_least_significant_bits(b_encoded, n_bits)

            #shifts the n bits to right so that they occupy a total of 8 bit spaces.
            #If 10 are the bits then shifting them would look like 10000000
            #this would ofcourse be converted to an int as per python's bit operations.
            
            r_encoded = shit_n_bits_to_8(r_encoded, n_bits)
            g_encoded = shit_n_bits_to_8(g_encoded, n_bits)
            b_encoded = shit_n_bits_to_8(b_encoded, n_bits)

            data.append((r_encoded, g_encoded, b_encoded))
            
    return createImage(data, image_to_decode.size)

#no. of bits
n_bits = 2
#path of files replace them as per your need.
image_to_hide_path = "pic.jpg"
image_to_hide_in_path = "tree.jpg"
#this is the path where we will save the encoded Image.
encoded_image_path = "encoded.png"

#PIL.Image object
image_to_hide = Image.open(image_to_hide_path)
image_to_hide_in = Image.open(image_to_hide_in_path)
print("Image to hide ", image_to_hide)
print("Image to hide in ", image_to_hide_in)      
#to hide an image inside another image it they both need to be of the same size.
image_to_hide=image_to_hide.resize(image_to_hide_in.size)
#encoding the image and saving it in the path
encodeImage(image_to_hide, image_to_hide_in, n_bits).save(encoded_image_path)

print("Image Encoded Successfully.")

#running the decode function
n_bits = 2
encoded_image_path = "encoded.png"

#path where you would want to save decoded Image.
decoded_image_path = "decoded.png"
image_to_decode = Image.open(encoded_image_path)
decodeImage(image_to_decode, n_bits).save(decoded_image_path)
print("Image decoded Successfully!")
