from RegisterTable import RegisterTable
from ASTWalker import CodeGenerator
from Utils import Format3ACLine

class AssemblyGenerator():
	def __init__ (self, AddressTable = None, ThreeAC = None, Filename = None):
		self.RegisterTable = RegisterTable("TargetMachine.config")
		self.AddressTable = AddressTable
		self.ThreeAC = ThreeAC
		self.Filename = Filename
		self.Output = []
		self.PriorLine = {}
		self.PriorIns = None
		for items in self.ThreeAC:
			self.GenerateAssemblyCode(items)
			self.PriorIns = items['Instruction']

		with open(Filename, 'w') as Asmout:
			for Line in self.Output:
				Asmout.write(Line + '\n')

	def AssignRegister(self, ThreeACLine, Op):
		VReg = ThreeACLine[Op]

		if 'f' not in VReg:
			Reg = self.RegisterTable.FindRegisterWithVReg(VReg)
			if Reg is None:
				Reg = self.RegisterTable.GetFirstOpenRegister('t')
				self.RegisterTable.SetRegisterData(AssemblyName=Reg, NewValue=VReg)
			return Reg
		else:
			Reg = self.RegisterTable.FindRegisterWithVReg(VReg)
			if Reg is None:
				Reg = self.RegisterTable.GetFirstOpenRegister('f')
				self.RegisterTable.SetRegisterData(AssemblyName=Reg, NewValue=VReg)
			return Reg



	def AddLineToASM(self, line, ThreeACLine=None):
		if ThreeACLine is not None and ThreeACLine is not self.PriorLine:
			self.Output.append(line.ljust(30) + '\#' + Format3ACLine(ThreeACLine))
			print(line.ljust(30) + '#' + Format3ACLine(ThreeACLine))
		else:
			self.Output.append(line.ljust(30))
			print(line.ljust(30))

		self.PriorLine = ThreeACLine


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

	def CONVERT(self, ThreeACLine):
		pass

	def LABEL(self, ThreeACLine):
		Template = "%s:"
		Template = Template % ThreeACLine['Dest'].replace('label ', '')

		self.AddLineToASM(Template, ThreeACLine)

	def JUMP(self, ThreeACLine):
		Tmplt = 'j {}'

		Tmplt = Tmplt.format(ThreeACLine['Dest'].replace('label ', ''))
		self.AddLineToASM(Tmplt, ThreeACLine)

	def LoadWord(self, ThreeACLine):
		LW = 'lw {} {}({})'
		FLW = 'lwc1 {} {}'
		DestReg = self.AssignRegister(ThreeACLine, 'Dest')
		StackPtr = self.RegisterTable.GetStackPtr()['assembly name']

		if 'local' in ThreeACLine['OpB']:
			StackOffset = ThreeACLine['OpB'].replace('local ', '')
			LW = LW.format(DestReg, StackOffset, StackPtr)

		elif 'f' in ThreeACLine['OpB']:
			if 'addr' in ThreeACLine['OpB']:
				#Src =
				# LW = FLW.Format(DestReg, )
				pass
		else:
			pass


		return LW

	def Move(self, ThreeACLine):
		Move = 'move {} {}'
		DestReg = self.AssignRegister(ThreeACLine, 'Dest')
		SrcReg = self.AssignRegister(ThreeACLine, 'OpB')

		Move = Move.format(DestReg, SrcReg)

		self.RegisterTable.ClearRegister(SrcReg)

		return Move

	def LoadImmediate(self, ThreeACLine):
		LI = 'li {} {}'
		DestReg = self.AssignRegister(ThreeACLine, 'Dest')
		ImmediateVal = ThreeACLine['OpB'].replace('const ', '')

		LI = LI.format(DestReg, ImmediateVal)

		return LI

	def LOAD(self, ThreeACLine):
		AsmLine = ''

		#load immediate
		if 'const' in ThreeACLine['OpB']:
			AsmLine = self.LoadImmediate(ThreeACLine)

		#move condition
		elif 'temp' in ThreeACLine['OpB'] and 'temp' in ThreeACLine['Dest']:
			AsmLine = self.Move(ThreeACLine)
			# clear register if used on RHS

		#load word condition
		elif 'temp' in ThreeACLine['Dest'] and ('local' in ThreeACLine['OpB'] or 'addr' in ThreeACLine['OpB']):
			AsmLine = self.LoadWord(ThreeACLine)


		self.AddLineToASM(AsmLine, ThreeACLine)


	def STORE(self, ThreeACLine):
		# if local then do thing
		Reg = ''
		Store = "sw {} {}"
		Deref = "{}({})"

		#case for storage from an address to an addr holding temp
		if 'local' in ThreeACLine['OpB'] and 'addr' in ThreeACLine['Dest']:
			LoadWord = "lw {} {}"
			WordLoc = ThreeACLine['OpB'].replace('local ', '')
			StackPtr = self.RegisterTable.GetStackPtr()['assembly name']

			#get register for the vlaue we are storing from
			SrcReg = self.RegisterTable.GetFirstOpenRegister('t')
			self.RegisterTable.SetRegisterData(AssemblyName=Reg, NewValue=ThreeACLine['OpB'])

			#load word
			LoadWord = LoadWord.format(SrcReg, Deref.format(WordLoc, StackPtr))
			self.AddLineToASM(LoadWord, ThreeACLine)


			#load contents of SrcReg into addr of Reg
			VReg = ThreeACLine['Dest']
			Reg = self.RegisterTable.FindRegisterWithVReg(VReg)
			Store = Store.format(SrcReg, Deref.format('', Reg))
			self.AddLineToASM(Store)

			self.RegisterTable.ClearRegister(SrcReg)


		else:
			#case for storage from a normal temp
			if 'temp' in ThreeACLine['OpB']:
				VReg = ThreeACLine['OpB']
				Reg = self.RegisterTable.FindRegisterWithVReg(VReg)
				if Reg is None:
					Reg = self.RegisterTable.GetFirstOpenRegister('t')
					self.RegisterTable.SetRegisterData(AssemblyName=Reg, NewValue=VReg)

			#case for floating point constant
			elif 'const' in ThreeACLine['OpB']:
				#get a register
				Reg = self.RegisterTable.GetFirstOpenRegister('t')
				self.RegisterTable.SetRegisterData(AssemblyName=Reg, NewValue=ThreeACLine['OpB'])

				LoadImmediate = "li {} {}"
				LoadImmediate = LoadImmediate.format( Reg, ThreeACLine['OpB'].replace('const ', ''))
				self.AddLineToASM(LoadImmediate, ThreeACLine)

			#user register to STORE
			WordLoc = ThreeACLine['Dest'].replace('local ', '')
			StackPtr = self.RegisterTable.GetStackPtr()['assembly name']
			Store = Store.format(Reg, Deref.format(WordLoc, StackPtr))
			self.AddLineToASM(Store, ThreeACLine)


			#blow away register
			self.RegisterTable.ClearRegister(Reg)


	def PROCENTRY(self, ThreeACLine):
		# if self.PriorIns is not None and self.PriorIns == 'GLOBAL':
		self.AddLineToASM('.text', ThreeACLine)

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
			self.AddLineToASM('.data', ThreeACLine)

		GlobalLine = "{}: {} {}"
		if ThreeACLine['OpA'] == '4':
			GlobalLine = GlobalLine.format(ThreeACLine['Dest'].replace('label ', ''), '.word', "")
			self.AddLineToASM(GlobalLine, ThreeACLine)

	def ADD(self, ThreeACLine):
		#staging strings used for assembly generation
		add = "add {}, {}, {}"
		storeA = "lw {}, {}"
		storeB = "lw {}, {}"
		RegA = None
		RegB = None

		#find register location for where its getting stored
		if 'IR' in ThreeACLine['Dest'] or 'FR' in ThreeACLine['Dest']:
			VReg = ThreeACLine['Dest']
			Reg = self.RegisterTable.FindRegisterWithVReg(VReg)

			#if the reister isnt already in use, find a new one to place data in
			if Reg is None:
				Reg = self.RegisterTable.GetFirstOpenRegister('t')
				self.RegisterTable.SetRegisterData(AssemblyName=Reg, NewValue=VReg)



		#if the first operand is a const, remove the const
		if 'const' in ThreeACLine['OpA']:
			OpA = ThreeACLine['OpA']
			OpAout = OpA.replace('const ', '')

		#if the first operand is a local variable, load it into a register for use
		elif 'local' in ThreeACLine['OpA']:
			OpA = ThreeACLine['OpA']
			OpA = OpA.replace('local ', '')
			OpAout = "{}({})"
			SP = self.RegisterTable.GetStackPtr()['assembly name']

			#loads data from stack pointer and puts it into register for later use
			OpAout = OpAout.format(OpA, SP)
			RegA = self.RegisterTable.GetFirstOpenRegister('t')
			self.RegisterTable.SetRegisterData(AssemblyName=RegA, NewValue=ThreeACLine['OpA'])
			storeA = storeA.format(RegA, OpAout)
			self.AddLineToASM(storeA, ThreeACLine)

			#set the register name to the main output of the function
			OpAout = RegA

		#if the value is already in a register, find the register
		elif 'IR' in ThreeACLine['OpA'] or 'FR' in ThreeACLine['OpA']:
			RegA = self.RegisterTable.FindRegisterWithVReg(ThreeACLine['OpA'])
			#set the register name to the main output of the function
			OpAout = RegA

		#if the first operand is a const, remove the const
		if 'const' in ThreeACLine['OpB']:
			OpB = ThreeACLine['OpB']
			OpBout = OpB.replace('const ', '')

		#if the first operand is a local variable, load it into a register for use
		elif 'local' in ThreeACLine['OpB']:
			OpB = ThreeACLine['OpB']
			OpB = OpB.replace('local ', '')
			OpBout = "{}({})"
			SP = self.RegisterTable.GetStackPtr()['assembly name']

			#loads data from stack pointer and puts it into register for later use
			OpBout = OpBout.format(OpB, SP)
			RegB = self.RegisterTable.GetFirstOpenRegister('t')
			self.RegisterTable.SetRegisterData(AssemblyName=RegB, NewValue=ThreeACLine['OpB'])
			storeB = storeB.format(RegB, OpBout)
			self.AddLineToASM(storeB, ThreeACLine)

			#set the register name to the main output of the function
			OpBout = RegB

		#if the value is already in a register, find the register
		elif 'IR' in ThreeACLine['OpB'] or 'FR' in ThreeACLine['OpB']:
			OpBout = self.RegisterTable.FindRegisterWithVReg(ThreeACLine['OpB'])


		#format assembly function calls then send them off
		add = add.format(Reg, OpAout, OpBout)
		self.AddLineToASM(add, ThreeACLine)

		#clear registers from temp stores after operation is done
		if RegA is not None:
			self.RegisterTable.ClearRegister(RegA)
		if RegB is not None:
			self.RegisterTable.ClearRegister(RegB)



	def SUB(self, ThreeACLine):
		#staging strings used for assembly generation
		sub = "sub {}, {}, {}"
		storeA = "lw {}, {}"
		storeB = "lw {}, {}"
		RegA = None
		RegB = None

		#find register location for where its getting stored
		if 'IR' in ThreeACLine['Dest'] or 'FR' in ThreeACLine['Dest']:
			VReg = ThreeACLine['Dest']
			Reg = self.RegisterTable.FindRegisterWithVReg(VReg)

			#if the reister isnt already in use, find a new one to place data in
			if Reg is None:
				Reg = self.RegisterTable.GetFirstOpenRegister('t')
				self.RegisterTable.SetRegisterData(AssemblyName=Reg, NewValue=VReg)

		#if the first operand is a const, remove the const
		if 'const' in ThreeACLine['OpA']:
			OpA = ThreeACLine['OpA']
			OpAout = OpA.replace('const ', '')

		#if the first operand is a local variable, load it into a register for use
		elif 'local' in ThreeACLine['OpA']:
			OpA = ThreeACLine['OpA']
			OpA = OpA.replace('local ', '')
			OpAout = "{}({})"
			SP = self.RegisterTable.GetStackPtr()['assembly name']

			#loads data from stack pointer and puts it into register for later use
			OpAout = OpAout.format(OpA, SP)
			RegA = self.RegisterTable.GetFirstOpenRegister('t')
			self.RegisterTable.SetRegisterData(AssemblyName=RegA, NewValue=ThreeACLine['OpA'])
			storeA = storeA.format(RegA, OpAout)
			self.AddLineToASM(storeA, ThreeACLine)

			#set the register name to the main output of the function
			OpAout = RegA

		#if the value is already in a register, find the register
		elif 'IR' in ThreeACLine['OpA'] or 'FR' in ThreeACLine['OpA']:
			OpAout = self.RegisterTable.FindRegisterWithVReg(ThreeACLine['OpA'])

		#if the first operand is a const, remove the const
		if 'const' in ThreeACLine['OpB']:
			OpB = ThreeACLine['OpB']
			OpBout = OpB.replace('const ', '')

		#if the first operand is a local variable, load it into a register for use
		elif 'local' in ThreeACLine['OpB']:
			OpB = ThreeACLine['OpB']
			OpB = OpB.replace('local ', '')
			OpBout = "{}({})"
			SP = self.RegisterTable.GetStackPtr()['assembly name']

			#loads data from stack pointer and puts it into register for later use
			OpBout = OpBout.format(OpB, SP)
			RegB = self.RegisterTable.GetFirstOpenRegister('t')
			self.RegisterTable.SetRegisterData(AssemblyName=RegB, NewValue=ThreeACLine['OpB'])
			storeB = storeB.format(RegB, OpBout)
			self.AddLineToASM(storeB, ThreeACLine)

			#set the register name to the main output of the function
			OpBout = RegB

		#if the value is already in a register, find the register
		elif 'IR' in ThreeACLine['OpB'] or 'FR' in ThreeACLine['OpB']:
			OpBout = self.RegisterTable.FindRegisterWithVReg(ThreeACLine['OpB'])

		#format assembly function calls then send them off
		sub = sub.format(Reg, OpAout, OpBout)
		self.AddLineToASM(sub, ThreeACLine)

		#clear registers from temp stores after operation is done
		if RegA is not None:
			self.RegisterTable.ClearRegister(RegA)
		if RegB is not None:
			self.RegisterTable.ClearRegister(RegB)

	def MULT(self, ThreeACLine):
		#staging strings used for assembly generation
		mult = "mult {}, {}"
		mflo = "mflo {}"
		storeA = "lw {}, {}"
		storeB = "lw {}, {}"
		RegA = None
		RegB = None

		#find register location for where its getting stored
		if 'IR' in ThreeACLine['Dest'] or 'FR' in ThreeACLine['Dest']:
			VReg = ThreeACLine['Dest']
			Reg = self.RegisterTable.FindRegisterWithVReg(VReg)

			#if the reister isnt already in use, find a new one to place data in
			if Reg is None:
				Reg = self.RegisterTable.GetFirstOpenRegister('t')
				self.RegisterTable.SetRegisterData(AssemblyName=Reg, NewValue=VReg)

		#if the first operand is a const, remove the const
		if 'const' in ThreeACLine['OpA']:
			OpA = ThreeACLine['OpA']
			OpAout = OpA.replace('const ', '')

		#if the first operand is a local variable, load it into a register for use
		elif 'local' in ThreeACLine['OpA']:
			OpA = ThreeACLine['OpA']
			OpA = OpA.replace('local ', '')
			OpAout = "{}({})"
			SP = self.RegisterTable.GetStackPtr()['assembly name']

			#loads data from stack pointer and puts it into register for later use
			OpAout = OpAout.format(OpA, SP)
			RegA = self.RegisterTable.GetFirstOpenRegister('t')
			self.RegisterTable.SetRegisterData(AssemblyName=RegA, NewValue=ThreeACLine['OpA'])
			storeA = storeA.format(RegA, OpAout)
			self.AddLineToASM(storeA, ThreeACLine)

			#set the register name to the main output of the function
			OpAout = RegA

		#if the value is already in a register, find the register
		elif 'IR' in ThreeACLine['OpA'] or 'FR' in ThreeACLine['OpA']:
			OpAout = self.RegisterTable.FindRegisterWithVReg(ThreeACLine['OpA'])

			if OpAout is None:
				OpAout = self.RegisterTable.GetFirstOpenRegister('t')
				self.RegisterTable.SetRegisterData(AssemblyName=OpAout, NewValue=VReg)

		#if the first operand is a const, remove the const
		if 'const' in ThreeACLine['OpB']:
			OpB = ThreeACLine['OpB']
			OpBout = OpB.replace('const ', '')

		#if the first operand is a local variable, load it into a register for use
		elif 'local' in ThreeACLine['OpB']:
			OpB = ThreeACLine['OpB']
			OpB = OpB.replace('local ', '')
			OpBout = "{}({})"
			SP = self.RegisterTable.GetStackPtr()['assembly name']
			OpBout = OpBout.format(OpB, SP)

			#loads data from stack pointer and puts it into register for later use
			RegB = self.RegisterTable.GetFirstOpenRegister('t')
			self.RegisterTable.SetRegisterData(AssemblyName=RegB, NewValue=ThreeACLine['OpB'])
			storeB = storeB.format(RegB, OpBout)
			self.AddLineToASM(storeB, ThreeACLine)

			#set the register name to the main output of the function
			OpBout = RegB

		#if the value is already in a register, find the register
		elif 'IR' in ThreeACLine['OpB'] or 'FR' in ThreeACLine['OpB']:
			OpBout = self.RegisterTable.FindRegisterWithVReg(ThreeACLine['OpB'])

		#format assembly function calls then send them off
		mult = mult.format(OpAout, OpBout)
		mflo = mflo.format(Reg)
		self.AddLineToASM(mult, ThreeACLine)
		self.AddLineToASM(mflo, ThreeACLine)

		#clear registers from temp stores after operation is done
		if RegA is not None:
			self.RegisterTable.ClearRegister(RegA)
		if RegB is not None:
			self.RegisterTable.ClearRegister(RegB)

	def DIV(self, ThreeACLine):
		#staging strings used for assembly generation
		div = "div {}, {}"
		mflo = "mflo {}"
		storeA = "lw {}, {}"
		storeB = "lw {}, {}"
		RegA = None
		RegB = None

		#find register location for where its getting stored
		if 'IR' in ThreeACLine['Dest'] or 'FR' in ThreeACLine['Dest']:
			VReg = ThreeACLine['Dest']
			Reg = self.RegisterTable.FindRegisterWithVReg(VReg)

			#if the reister isnt already in use, find a new one to place data in
			if Reg is None:
				Reg = self.RegisterTable.GetFirstOpenRegister('t')
				self.RegisterTable.SetRegisterData(AssemblyName=Reg, NewValue=VReg)

		#if the first operand is a const, remove the const
		if 'const' in ThreeACLine['OpA']:
			OpA = ThreeACLine['OpA']
			OpAout = OpA.replace('const ', '')

		#if the first operand is a local variable, load it into a register for use
		elif 'local' in ThreeACLine['OpA']:
			OpA = ThreeACLine['OpA']
			OpA = OpA.replace('local ', '')
			OpAout = "{}({})"
			SP = self.RegisterTable.GetStackPtr()['assembly name']

			#loads data from stack pointer and puts it into register for later use
			OpAout = OpAout.format(OpA, SP)
			RegA = self.RegisterTable.GetFirstOpenRegister('t')
			self.RegisterTable.SetRegisterData(AssemblyName=RegA, NewValue=ThreeACLine['OpA'])
			storeA = storeA.format(RegA, OpAout)
			self.AddLineToASM(storeA, ThreeACLine)

			#set the register name to the main output of the function
			OpAout = RegA

		#if the value is already in a register, find the register
		elif 'IR' in ThreeACLine['OpA'] or 'FR' in ThreeACLine['OpA']:
			OpAout = self.RegisterTable.FindRegisterWithVReg(ThreeACLine['OpA'])

		#if the first operand is a const, remove the const
		if 'const' in ThreeACLine['OpB']:
			OpB = ThreeACLine['OpB']
			OpBout = OpB.replace('const ', '')

		#if the first operand is a local variable, load it into a register for use
		elif 'local' in ThreeACLine['OpB']:
			OpB = ThreeACLine['OpB']
			OpB = OpB.replace('local ', '')
			OpBout = "{}({})"
			SP = self.RegisterTable.GetStackPtr()['assembly name']

			#loads data from stack pointer and puts it into register for later use
			OpBout = OpBout.format(OpB, SP)
			RegB = self.RegisterTable.GetFirstOpenRegister('t')
			self.RegisterTable.SetRegisterData(AssemblyName=RegB, NewValue=ThreeACLine['OpB'])
			storeB = storeB.format(RegB, OpBout)
			self.AddLineToASM(storeB, ThreeACLine)

			#set the register name to the main output of the function
			OpBout = RegB

		#if the value is already in a register, find the register
		elif 'IR' in ThreeACLine['OpB'] or 'FR' in ThreeACLine['OpB']:
			OpBout = self.RegisterTable.FindRegisterWithVReg(ThreeACLine['OpB'])

		#format assembly function calls then send them off
		div = div.format(OpAout, OpBout)
		mflo = mflo.format(Reg)
		self.AddLineToASM(div, ThreeACLine)
		self.AddLineToASM(mflo, ThreeACLine)

		#clear registers from temp stores after operation is done
		if RegA is not None:
			self.RegisterTable.ClearRegister(RegA)
		if RegB is not None:
			self.RegisterTable.ClearRegister(RegB)

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
