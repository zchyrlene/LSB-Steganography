import wave

def case(a):
	if a == 1:
		encode()
	elif a == 2:
		decode()
	elif a == 3:
		quit()
	else:
		print("\nEnter valid Choice!")

#Encode
def encode():
	print("Encoding")


	#Read audio file
	audio = wave.open("sound.wav",mode="rb")

	#Read frames and convert to byte array
	frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))

	#User enter text to encode
	string = input("Enter secret text: ")

	#Append dummy data to fill out bytes. Receiver will detect and remove filler chars
	string = string + int((len(frame_bytes)-(len(string)*8*8))/8) *'#'

	#Convert text to bit array
	bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in string])))

	#Replace LSBs of each byte to audio by 1 from text bit array
	for i, bit in enumerate(bits):
	    frame_bytes[i] = (frame_bytes[i] & 254) | bit

	#Get modified frames
	frame_modified = bytes(frame_bytes)

	for i in range(0,10):
		print(frame_bytes[i])
	newAudio =  wave.open('encodedsound.wav', 'wb')
	newAudio.setparams(audio.getparams())
	newAudio.writeframes(frame_modified)

	newAudio.close()
	audio.close()
	print("Succesfully encoded inside encodedsound.wav")

#Decoding
def decode():
	print("Decoding")
	file_to_decode = input("Enter file name to decode: ")

	#audio = wave.open("encodedsound.wav", mode='rb')
	try:
		audio = wave.open(file_to_decode, mode="rb")
	except Exception as e:
		print("Please enter a valid file")
		quit()

	#Convert audio to byte array
	frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))

	#Extract LSB of each byte
	extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]

	#Convert byte array back to string
	string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))

	#Cut off filler chars
	decoded = string.split("###")[0]
	print("Sucessfully decoded: "+decoded)
	audio.close()

while(1):
	print("\nSelect an option: \n1)Encode\n2)Decode\n3)exit")
	val = int(input("\nChoice:"))
	case(val)