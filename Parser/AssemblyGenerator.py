from RegisterTable import RegisterTable
from ASTWalker import CodeGenerator

class AssemblyGenerator():
	def __init__ (self, AddressTable = None, ThreeAC = None, Filename = None):
		self.RegisterTable = RegisterTable("TargetMachine.config")
		self.AddressTable = AddressTable
		self.ThreeAC = ThreeAC
		self.Filename = Filename
		self.Output = []
		self.PriorIns = None
		for items in self.ThreeAC:
			self.GenerateAssemblyCode(items)
			self.PriorIns = items['Instruction']

		with open(Filename, 'w') as Asmout:
			for Line in self.Output:
				Asmout.write(Line + '\n')


	def AddLineToASM(self, line):
		self.Output.append(line)
		print(line)


	def GenerateAssemblyCode(self, ThreeACLine):
		if (ThreeACLine['Instruction'] == 'LABEL'):
			self.LABEL(ThreeACLine)
		elif (ThreeACLine['Instruction'] == 'JUMP'):
			self.JUMP(ThreeACLine)
		elif (ThreeACLine['Instruction'] == 'LOAD'):
			self.LOAD(ThreeACLine)
		elif (ThreeACLine['Instruction'] == 'STORE'):
			self.STORE(ThreeACLine)
		elif (ThreeACLine['Instruction'] == 'PROCENTRY'):
			self.PROCENTRY(ThreeACLine)
		elif (ThreeACLine['Instruction'] == 'ENDPROC'):
			self.ENDPROC(ThreeACLine)
		elif (ThreeACLine['Instruction'] == 'RETURN'):
			self.RETURN(ThreeACLine)
		elif (ThreeACLine['Instruction'] == 'GLOBAL'):
			self.GLOBAL(ThreeACLine)
		elif (ThreeACLine['Instruction'] == 'CONVERT'):
			self.CONVERT(ThreeACLine)
		elif (ThreeACLine['Instruction'] == 'ADD'):
			self.ADD(ThreeACLine)
		elif (ThreeACLine['Instruction'] == 'SUB'):
			self.SUB(ThreeACLine)
		elif (ThreeACLine['Instruction'] == 'MULT'):
			self.MULT(ThreeACLine)
		elif (ThreeACLine['Instruction'] == 'DIV'):
			self.DIV(ThreeACLine)
		elif (ThreeACLine['Instruction'] == 'EQ'):
			self.EQ(ThreeACLine)
		elif (ThreeACLine['Instruction'] == 'GT'):
			self.GT(ThreeACLine)
		elif (ThreeACLine['Instruction'] == 'LT'):
			self.LT(ThreeACLine)
		elif (ThreeACLine['Instruction'] == 'GE'):
			self.GE(ThreeACLine)
		elif (ThreeACLine['Instruction'] == 'LE'):
			self.LE(ThreeACLine)
		elif (ThreeACLine['Instruction'] == 'NE'):
			self.NE(ThreeACLine)
		elif (ThreeACLine['Instruction'] == 'NOT'):
			self.NOT(ThreeACLine)
		elif (ThreeACLine['Instruction'] == 'BRNE'):
			self.BRNE(ThreeACLine)
		elif (ThreeACLine['Instruction'] == 'BREQ'):
			self.BREQ(ThreeACLine)
		elif (ThreeACLine ['Instruction']== 'BRGE'):
			self.BRGE(ThreeACLine)
		elif (ThreeACLine['Instruction'] == 'BRLE'):
			self.BRLE(ThreeACLine)
		elif (ThreeACLine['Instruction'] == 'BRLT'):
			self.BRLT(ThreeACLine)
		elif (ThreeACLine['Instruction'] == 'BRGT'):
			self.BRGT(ThreeACLine)
		else:
			print (ThreeACLine['Instruction'])


	def LABEL(self, ThreeACLine):
		Template = "%s:"
		Template = Template % ThreeACLine['Dest'].replace('label ', '')

		self.AddLineToASM(Template)

	def JUMP(self, ThreeACLine):
		print ("in jump")

	def LOAD(self, ThreeACLine):
		#move condition

		#load word condition
		print ("in load")

	def STORE(self, ThreeACLine):
		# if local then do thing
		Reg = ''

		if 'temp' in ThreeACLine['OpB']:
			VReg = ThreeACLine['OpB']
			Reg = self.RegisterTable.FindRegisterWithVReg(VReg)
			if Reg is None:
				Reg = self.RegisterTable.GetFirstOpenRegister('t')
				self.RegisterTable.SetRegisterData(AssemblyName=Reg, NewValue=VReg)

		#case for floating point constant
		if 'const' in ThreeACLine['OpB']:
			#get a register
			Reg = self.RegisterTable.GetFirstOpenRegister('t')
			self.RegisterTable.SetRegisterData(AssemblyName=Reg, NewValue=ThreeACLine['OpB'])
			LoadImmediate = "li {} {}"
			LoadImmediate = LoadImmediate.format( Reg, ThreeACLine['OpB'].replace('const ', ''))
			self.AddLineToASM(LoadImmediate)

		#user register to STORE
		Store = "sw {} {}"
		Deref = "{}({})"
		WordLoc = ThreeACLine['Dest'].replace('local ', '')
		StackPtr = self.RegisterTable.GetStackPtr()['assembly name']
		Store = Store.format(Reg, Deref.format(WordLoc, StackPtr))
		self.AddLineToASM(Store)


		#blow away register
		self.RegisterTable.ClearRegister(Reg)


	def PROCENTRY(self, ThreeACLine):
		# if self.PriorIns is not None and self.PriorIns == 'GLOBAL':
		self.AddLineToASM('.text')

		#declare the function name
		Template = "%s:"
		Template = Template % ThreeACLine['Dest'].replace('label ', '')
		self.AddLineToASM(Template)

		#incrment the stack pointer
		StackUpdate =  'sub {}, {}, {}'
		StackPtr = self.RegisterTable.GetStackPtr()
		Reg = StackPtr['assembly name']
		Offset = int(ThreeACLine['OpA']) + int(ThreeACLine['OpB'])

		StackUpdate = StackUpdate.format(Reg, Reg, Offset)
		self.RegisterTable.PushStackPtr(Offset)
		self.AddLineToASM(StackUpdate)


	def ENDPROC(self, ThreeACLine):
		print ("in endproc")

	def RETURN(self, ThreeACLine):
		print ("in home")

	def GLOBAL(self, ThreeACLine):
		if ThreeACLine['3ACLineNo'] is 0:
			self.AddLineToASM('.data')

		GlobalLine = "{}: {} {}"
		if ThreeACLine['OpA'] == '4':
			GlobalLine = GlobalLine.format(ThreeACLine['Dest'].replace('label ', ''), '.word', "")
			self.AddLineToASM(GlobalLine)

	def ADD(self, ThreeACLine):
		print ("in add")

	def SUB(self, ThreeACLine):
		print ("in sub")

	def MULT(self, ThreeACLine):
		print ("in mult")

	def DIV(self, ThreeACLine):
		print ("in div")

	def EQ(self, ThreeACLine):
		print ("in eq")

	def GT(self, ThreeACLine):
		print ("in gt")

	def LT(self, ThreeACLine):
		print ("in lt")

	def GE(self, ThreeACLine):
		print ("in gt")

	def LE(self, ThreeACLine):
		print ("in le")

	def NE(self, ThreeACLine):
		print ("in ne")

	def NOT(self, ThreeACLine):
		print ("in not")

	def BRNE(self, ThreeACLine):
		print ("in brne")

	def BREQ(self, ThreeACLine):
		print ("in breq")

	def BRGE(self, ThreeACLine):
		print ("in brge")

	def BRLT(self, ThreeACLine):
		print ("in brlt")

	def BRLE(self, ThreeACLine):
		print ("in brle")

	def BRGT(self, ThreeACLine):
		print ("in brgt")
