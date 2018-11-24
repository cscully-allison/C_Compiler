def ReadInInt():
	ReadInt = input()
	if ReadInt.__class__.__name__ == 'int':
		return ReadInt
	else:
		print ("not an int")
		return False

def WriteInt(IntToWrite):
	if IntToWrite.__class__.__name__ == 'int':
		print (IntToWrite)
	else:
		print ("not an int")

def ReadInFloat():
	ReadFloat = input()
	if ReadFloat.__class__.__name__ == 'float':
		return ReadFloat
	else:
		print ("not a float")
		return False

def WriteFloat(FloatToWrite):
	if FloatToWrite.__class__.__name__ == 'float':
		print (FloatToWrite)
	else:
		print ("not a float")

def ReadInChar():
	ReadChar = raw_input()
	if ReadChar.__class__.__name__ == 'str' and len(ReadChar) == 1:
		return ReadChar
	else:
		if ReadChar.__class__.__name__ != 'str':
			print ("not string")
		if len(ReadChar) > 1:
			print ("length > 1")

def WriteChar(CharToWrite):
	if CharToWrite.__class__.__name__ == 'str' and len(CharToWrite) == 1:
		print (CharToWrite)
	else:
		print ("not string or length > 1")