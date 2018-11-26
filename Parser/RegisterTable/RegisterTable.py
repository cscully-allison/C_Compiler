from ConfigManager import ConfigManager

class RegisterTable():
	def __init__ (self, filepath = None):
		
		self.Registers = []

		#get data from file
		manager = ConfigManager(filepath)
		root = manager.Tree.getroot()
		
		#set prefixes and declare base number of registers
		regPrefix = '$'
		a = 'a'
		aNum = None
		f = 'f'
		fNum = None
		v = 'v'
		vNUm = None
		t = 't'
		tNum = None
		s = 's'
		sNum = None
		
		#add default registers
		self.Registers.append({'assembly name': '$zero', 'value': 0, 'data type': 'Int'})
		self.Registers.append({'assembly name': '$sp', 'value': None, 'data type': None})
		self.Registers.append({'assembly name': '$ra', 'value': None, 'data type': None})

		for Argument in root.iter('Argument'):
			for things in Argument:
				if things.tag == 'Number':
					aNum = things.text
					for i in range(int(aNum)):
						self.Registers.append({'assembly name': regPrefix+a+str(i), 'value': None, 'data type' : None})	

		for Argument in root.iter('Return'):
			for things in Argument:
				if things.tag == 'Number':
					vNum = things.text
					for i in range(int(vNum)):
						self.Registers.append({'assembly name': regPrefix+v+str(i), 'value': None, 'data type' : None})

		for Argument in root.iter('Temporary'):
			for things in Argument:
				if things.tag == 'Number':
					tNum = things.text
					for i in range(int(tNum)):
						self.Registers.append({'assembly name': regPrefix+t+str(i), 'value': None, 'data type' : None})

		for Argument in root.iter('SavedTemporary'):
			for things in Argument:
				if things.tag == 'Number':
					sNum = things.text
					for i in range(int(sNum)):
						self.Registers.append({'assembly name': regPrefix+s+str(i), 'value': None, 'data type' : None})

		for Argument in root.iter('FTemp'):
			for things in Argument:
				if things.tag == 'Number':
					fNum = things.text
					for i in range(int(fNum)):
						self.Registers.append({'assembly name': regPrefix+f+str(i), 'value': None, 'data type' : 'Float'})


	def GetRegisterData(self, AssemblyName = None):
		if AssemblyName is not None:
			for elem in self.Registers:
				if elem['assembly name'] == AssemblyName:
					return elem
		else:
			return False

	def SetRegisterData(self, AssemblyName = None, NewValue = None, NewDataType = None):
		for elem in self.Registers:
			if elem['assembly name'] == AssemblyName:
				elem['value'] = NewValue
				elem['data type'] = NewDataType
				return True

		#no register found
		return False

	def SetSRegister(self, NewValue = None, NewDataType = None):
		RegisterName = self.GetFirstOpenRegister('$s')
		if RegisterName is not False:
			self.SetRegisterData(RegisterName, NewValue, NewDataType)
		else:
			self.RegisterOverflow()
	
	def SetTRegister(self, NewValue = None, NewDataType = None):
		RegisterName = self.GetFirstOpenRegister('$t')
		if RegisterName is not False:
			self.SetRegisterData(RegisterName, NewValue, NewDataType)
		else:
			self.RegisterOverflow()


	def SetARegister(self, NewValue = None, NewDataType = None):
		RegisterName = self.GetFirstOpenRegister('$a')
		if RegisterName is not False:
			self.SetRegisterData(RegisterName, NewValue, NewDataType)
		else:
			self.RegisterOverflow()

	def RegisterOverflow(self):
		#this will be filled out later with better knowledge of overflow
		print('Register Overflow Called')
		pass
	
	def GetFirstOpenRegister(self, RegisterType = None):
		for elem in self.Registers:
			if RegisterType in elem['assembly name'] and elem['assembly name'] != '$at' and elem['assembly name'] != '$sp':
				if elem['value'] is None and elem['data type'] is None:
					return elem['assembly name']
		return False

	def ClearRegister(self, RegisterToClear):
		for elem in self.Registers:
			if elem['assembly name'] == RegisterToClear:
				elem['value'] = None
				elem['data type'] = None
				return True