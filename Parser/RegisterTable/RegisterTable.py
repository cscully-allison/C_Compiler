class RegisterTable():
	def __init__ (self):
		self.Registers = []
		self.Registers.append({'assembly name': '$zero', 'value': None, 'data type' : None})
		self.Registers.append({'assembly name': '$at', 'value': None, 'data type' : None})
		self.Registers.append({'assembly name': '$v0', 'value': None, 'data type' : None})
		self.Registers.append({'assembly name': '$v1', 'value': None, 'data type' : None})
		self.Registers.append({'assembly name': '$a0', 'value': None, 'data type' : None})
		self.Registers.append({'assembly name': '$a1', 'value': None, 'data type' : None})
		self.Registers.append({'assembly name': '$a2', 'value': None, 'data type' : None})
		self.Registers.append({'assembly name': '$a3', 'value': None, 'data type' : None})
		self.Registers.append({'assembly name': '$t0', 'value': None, 'data type' : None})
		self.Registers.append({'assembly name': '$t1', 'value': None, 'data type' : None})
		self.Registers.append({'assembly name': '$t2', 'value': None, 'data type' : None})
		self.Registers.append({'assembly name': '$t3', 'value': None, 'data type' : None})
		self.Registers.append({'assembly name': '$t4', 'value': None, 'data type' : None})
		self.Registers.append({'assembly name': '$t5', 'value': None, 'data type' : None})
		self.Registers.append({'assembly name': '$t6', 'value': None, 'data type' : None})
		self.Registers.append({'assembly name': '$t7', 'value': None, 'data type' : None})
		self.Registers.append({'assembly name': '$s0', 'value': None, 'data type' : None})
		self.Registers.append({'assembly name': '$s1', 'value': None, 'data type' : None})
		self.Registers.append({'assembly name': '$s2', 'value': None, 'data type' : None})
		self.Registers.append({'assembly name': '$s3', 'value': None, 'data type' : None})
		self.Registers.append({'assembly name': '$s4', 'value': None, 'data type' : None})
		self.Registers.append({'assembly name': '$s5', 'value': None, 'data type' : None})
		self.Registers.append({'assembly name': '$s6', 'value': None, 'data type' : None})
		self.Registers.append({'assembly name': '$s7', 'value': None, 'data type' : None})
		self.Registers.append({'assembly name': '$t8', 'value': None, 'data type' : None})
		self.Registers.append({'assembly name': '$t9', 'value': None, 'data type' : None})
		self.Registers.append({'assembly name': '$k0', 'value': None, 'data type' : None})
		self.Registers.append({'assembly name': '$k1', 'value': None, 'data type' : None})
		self.Registers.append({'assembly name': '$gp', 'value': None, 'data type' : None})
		self.Registers.append({'assembly name': '$sp', 'value': None, 'data type' : None})
		self.Registers.append({'assembly name': '$fp', 'value': None, 'data type' : None})
		self.Registers.append({'assembly name': '$ra', 'value': None, 'data type' : None})

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