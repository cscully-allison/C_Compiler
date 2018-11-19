class RegisterTable():
	def __init__ (self):
		self.Registers = []
		self.Registers.append({'register': 'r0', 'assembly name': '$zero', 'value': None, 'data type' : None})
		self.Registers.append({'register': 'r1', 'assembly name': '$at', 'value': None, 'data type' : None})
		self.Registers.append({'register': 'r2', 'assembly name': '$v0', 'value': None, 'data type' : None})
		self.Registers.append({'register': 'r3', 'assembly name': '$v1', 'value': None, 'data type' : None})
		self.Registers.append({'register': 'r4', 'assembly name': '$a0', 'value': None, 'data type' : None})
		self.Registers.append({'register': 'r5', 'assembly name': '$a1', 'value': None, 'data type' : None})
		self.Registers.append({'register': 'r6', 'assembly name': '$a2', 'value': None, 'data type' : None})
		self.Registers.append({'register': 'r7', 'assembly name': '$a3', 'value': None, 'data type' : None})
		self.Registers.append({'register': 'r8', 'assembly name': '$t0', 'value': None, 'data type' : None})
		self.Registers.append({'register': 'r9', 'assembly name': '$t1', 'value': None, 'data type' : None})
		self.Registers.append({'register': 'r10', 'assembly name': '$t2', 'value': None, 'data type' : None})
		self.Registers.append({'register': 'r11', 'assembly name': '$t3', 'value': None, 'data type' : None})
		self.Registers.append({'register': 'r12', 'assembly name': '$t4', 'value': None, 'data type' : None})
		self.Registers.append({'register': 'r13', 'assembly name': '$t5', 'value': None, 'data type' : None})
		self.Registers.append({'register': 'r14', 'assembly name': '$t6', 'value': None, 'data type' : None})
		self.Registers.append({'register': 'r15', 'assembly name': '$t7', 'value': None, 'data type' : None})
		self.Registers.append({'register': 'r16', 'assembly name': '$s0', 'value': None, 'data type' : None})
		self.Registers.append({'register': 'r17', 'assembly name': '$s1', 'value': None, 'data type' : None})
		self.Registers.append({'register': 'r18', 'assembly name': '$s2', 'value': None, 'data type' : None})
		self.Registers.append({'register': 'r19', 'assembly name': '$s3', 'value': None, 'data type' : None})
		self.Registers.append({'register': 'r20', 'assembly name': '$s4', 'value': None, 'data type' : None})
		self.Registers.append({'register': 'r21', 'assembly name': '$s5', 'value': None, 'data type' : None})
		self.Registers.append({'register': 'r22', 'assembly name': '$s6', 'value': None, 'data type' : None})
		self.Registers.append({'register': 'r23', 'assembly name': '$s7', 'value': None, 'data type' : None})
		self.Registers.append({'register': 'r24', 'assembly name': '$t8', 'value': None, 'data type' : None})
		self.Registers.append({'register': 'r25', 'assembly name': '$t9', 'value': None, 'data type' : None})
		self.Registers.append({'register': 'r26', 'assembly name': '$k0', 'value': None, 'data type' : None})
		self.Registers.append({'register': 'r27', 'assembly name': '$k1', 'value': None, 'data type' : None})
		self.Registers.append({'register': 'r28', 'assembly name': '$gp', 'value': None, 'data type' : None})
		self.Registers.append({'register': 'r29', 'assembly name': '$sp', 'value': None, 'data type' : None})
		self.Registers.append({'register': 'r30', 'assembly name': '$fp', 'value': None, 'data type' : None})
		self.Registers.append({'register': 'r31', 'assembly name': '$ra', 'value': None, 'data type' : None})

	def GetRegister(self, RegisterName = None, AssemblyName = None):
		if RegisterName != 'None':
			for elem in self.Registers:
				if elem['register'] == RegisterName:
					return elem
		elif AssemblyName != 'None':
			for elem in self.Registers:
				if elem['assembly name'] == AssemblyName:
					return elem
		else:
			return False