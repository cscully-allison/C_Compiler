from RegisterTable import RegisterTable
from ASTWalker import CodeGenerator
from Utils import Format3ACLine

class AssemblyGenerator():
	def __init__ (self, AddressTable = None, ThreeAC = None, Filename = None):
		self.RegisterTable = RegisterTable("TargetMachine.config")
		self.AddressTable = AddressTable
		self.ThreeAC = ThreeAC
		self.Filename = Filename
		self.PrebuiltFunctionsFile = 'codeinject.asm'
		self.PrebuiltFunctions = ''
		self.Output = []
		self.PriorLine = {}
		self.PriorIns = None
		for items in self.ThreeAC:
			self.GenerateAssemblyCode(items)
			self.PriorIns = items['Instruction']

		with open(self.PrebuiltFunctionsFile, 'r') as F:
			self.PrebuiltFunctions = F.read()

		with open(Filename, 'w') as Asmout:
			for Line in self.Output:
				if 'main:' in Line:
					Asmout.write(self.PrebuiltFunctions)
				Asmout.write(Line + '\n')

	def GetDerefAddr(self, ThreeACLine, Op):
		Tmplt = '{}({})'

		if 'local' in ThreeACLine[Op]:
			WordLoc = ThreeACLine[Op].replace('local ', '')
			StackPtr = self.RegisterTable.GetStackPtr()['assembly name']
			Tmplt = Tmplt.format(WordLoc, StackPtr)
		elif 'addr' in ThreeACLine[Op]:
			WordLoc = self.AssignRegister(ThreeACLine, Op)
			Tmplt = Tmplt.format('',WordLoc)

		return Tmplt

	def AssignArgumentRegister(self, ThreeACLine, Op):
		VReg = ThreeACLine[Op]

		Reg = self.RegisterTable.FindRegisterWithVReg(VReg)
		if Reg is None:
			Reg = self.RegisterTable.GetFirstOpenRegister('$a')
			self.RegisterTable.SetRegisterData(AssemblyName=Reg, NewValue=VReg)
			#if we are out of argument registers store in s
			if Reg is None:
				Reg = self.RegisterTable.GetFirstOpenRegister('$s')
				self.RegisterTable.SetRegisterData(AssemblyName=Reg, NewValue=VReg)
		return Reg

	def AssignRegister(self, ThreeACLine, Op):
		VReg = ThreeACLine[Op]

		if 'f' in VReg and 'IR' not in VReg:
			Reg = self.RegisterTable.FindRegisterWithVReg(VReg)
			if Reg is None:
				Reg = self.RegisterTable.GetFirstOpenRegister('f')
				self.RegisterTable.SetRegisterData(AssemblyName=Reg, NewValue=VReg)
			return Reg
		else:
			Reg = self.RegisterTable.FindRegisterWithVReg(VReg)
			if Reg is None:
				Reg = self.RegisterTable.GetFirstOpenRegister('t')
				self.RegisterTable.SetRegisterData(AssemblyName=Reg, NewValue=VReg)
			return Reg

	def FormatOperand(self, ThreeACOperand, Dest):
		#if the first operand is a const, remove the const
		if 'const' in ThreeACOperand:
			store = "li {}, {}"
			Op = ThreeACOperand
			Opout = Op.replace('const ', '')
			Reg = self.RegisterTable.GetFirstOpenRegister('t')
			self.RegisterTable.SetRegisterData(AssemblyName=Reg, NewValue=ThreeACOperand)
			store = store.format(Reg, Opout)
			self.AddLineToASM(store)


		#if the first operand is a local variable, load it into a register for use
		elif 'local' in ThreeACOperand:
			if 'addr' in Dest:
				store = "la {}, {}"
			else:
				store = "lw {}, {}"
			Op = ThreeACOperand
			Op = Op.replace('local ', '')
			Opout = "{}({})"
			SP = self.RegisterTable.GetStackPtr()['assembly name']

			#loads data from stack pointer and puts it into register for later use
			Opout = Opout.format(Op, SP)
			Reg = self.RegisterTable.GetFirstOpenRegister('t')
			self.RegisterTable.SetRegisterData(AssemblyName=Reg, NewValue=ThreeACOperand)
			store = store.format(Reg, Opout)
			self.AddLineToASM(store)

		#if the value is already in a register, find the register
		elif 'IR' in ThreeACOperand or 'FR' in ThreeACOperand:
			Reg = self.RegisterTable.FindRegisterWithVReg(ThreeACOperand)
			#set the register name to the main output of the function

		return Reg

	def AddLineToASM(self, line, ThreeACLine=None):
		if ThreeACLine is not None and ThreeACLine is not self.PriorLine:
			self.Output.append(line.ljust(30) + '#' + Format3ACLine(ThreeACLine))
			print(line.ljust(30) + '#' + Format3ACLine(ThreeACLine))
		else:
			self.Output.append(line.ljust(30))
			print(line.ljust(30))

		self.PriorLine = ThreeACLine


	def GenerateAssemblyCode(self, ThreeACLine):
		if (ThreeACLine['Instruction'] == 'COMMENT'):
			self.AddLineToASM('\n' + ThreeACLine['Dest'])
		elif (ThreeACLine['Instruction'] == 'LABEL'):
			self.LABEL(ThreeACLine)
		elif (ThreeACLine['Instruction'] == 'JUMP'):
			self.JUMP(ThreeACLine)
		elif (ThreeACLine['Instruction'] == 'LOAD'):
			self.LOAD(ThreeACLine)
		elif (ThreeACLine['Instruction'] == 'STORE'):
			self.STORE(ThreeACLine)
		elif (ThreeACLine['Instruction'] == 'PROCENTRY'):
			self.PROCENTRY(ThreeACLine)
		elif (ThreeACLine['Instruction'] == 'ARGS'):
			self.ARGS(ThreeACLine)
		elif (ThreeACLine['Instruction'] == 'VALOUT'):
			self.VALOUT(ThreeACLine)
		elif (ThreeACLine['Instruction'] == 'CALL'):
			self.CALL(ThreeACLine)
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



	def LoadReturn(self, ThreeACLine):
		LW = 'lw {} {}'
		FLW = 'lwc1 {} ({})'
		LI = 'li {} {}'
		Move = 'move {} {}'
		DestReg = self.RegisterTable.GetReturnReg()
		StackPtr = self.RegisterTable.GetStackPtr()['assembly name']

		if 'const' in ThreeACLine['OpB']:
			Src = ThreeACLine['OpB'].replace('const ', '')
			LW = LI.format(DestReg, Src)

		if 'temp' in ThreeACLine['OpB']:
			Src = self.AssignRegister(ThreeACLine, 'OpB')
			LW = Move.format(DestReg, Src)

		if 'local' in ThreeACLine['OpB']:
			Src = self.GetDerefAddr(ThreeACLine, 'OpB')
			LW = LW.format(DestReg, Src)

		elif 'f' in ThreeACLine['OpB']:
			if 'addr' in ThreeACLine['OpB']:
				Src = self.AssignRegister(ThreeACLine, 'OpB')
				LW = FLW.format(DestReg, Src)
		elif 'addr' in ThreeACLine['OpB']:
			Src = self.GetDerefAddr(ThreeACLine, 'OpB')
			LW = LW.format(DestReg, Src)

		return LW

	def LoadWord(self, ThreeACLine):
		LW = 'lw {} {}'
		FLW = 'lwc1 {} ({})'
		DestReg = self.AssignRegister(ThreeACLine, 'Dest')
		StackPtr = self.RegisterTable.GetStackPtr()['assembly name']

		if 'local' in ThreeACLine['OpB']:
			Src = self.GetDerefAddr(ThreeACLine, 'OpB')
			LW = LW.format(DestReg, Src)

		elif 'f' in ThreeACLine['OpB']:
			if 'addr' in ThreeACLine['OpB']:
				Src = self.AssignRegister(ThreeACLine, 'OpB')
				LW = FLW.format(DestReg, Src)
		elif 'addr' in ThreeACLine['OpB']:
			Dest = self.AssignRegister(ThreeACLine, 'Dest')
			Src = self.GetDerefAddr(ThreeACLine, 'OpB')
			LW = LW.format(Dest, Src)



		return LW

	def Move(self, ThreeACLine):
		Move = 'move {} {}'
		DestReg = self.AssignRegister(ThreeACLine, 'Dest')
		if 'return' in ThreeACLine['OpB']:
			SrcReg = self.RegisterTable.GetReturnReg()
		else:
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

		if 'return' in ThreeACLine['Dest']:
			AsmLine = self.LoadReturn(ThreeACLine)

		elif 'return' in ThreeACLine['OpB']:
			AsmLine = self.Move(ThreeACLine)

		#load immediate
		elif 'const' in ThreeACLine['OpB']:
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
		FLI = "l.s {} {}"
		FSW = "swc1 {} {}"
		LoadWord = "lw {} {}"

		#floating point adressing
		if 'f' in ThreeACLine['OpB']:
				# case for the local
				if 'addr' in ThreeACLine['Dest'] or 'local' in ThreeACLine['Dest']:
					Dest = self.GetDerefAddr(ThreeACLine, 'Dest')

					#case for floating point constant
					if 'const' in ThreeACLine['OpB']:
						#get a register
						Reg = self.AssignRegister(ThreeACLine, 'OpB')
						FLI = FLI.format( Reg, ThreeACLine['OpB'].replace('const ', ''))
						self.AddLineToASM(FLI, ThreeACLine)

					FSW = FSW.format(Reg, Dest)
					self.AddLineToASM(FSW, ThreeACLine)

		#case for storage from an address to an addr holding temp
		elif 'local' in ThreeACLine['OpB'] and 'addr' in ThreeACLine['Dest']:

			Dest = self.GetDerefAddr(ThreeACLine, 'OpB')

			#get register for the vlaue we are storing from
			SrcReg = self.RegisterTable.GetFirstOpenRegister('t')
			self.RegisterTable.SetRegisterData(AssemblyName=Reg, NewValue=ThreeACLine['OpB'])

			#load word
			LoadWord = LoadWord.format(SrcReg, Dest)
			self.AddLineToASM(LoadWord, ThreeACLine)


			#load contents of SrcReg into addr of Reg
			VReg = ThreeACLine['Dest']
			Reg = self.RegisterTable.FindRegisterWithVReg(VReg)
			Store = Store.format(SrcReg, Deref.format('', Reg))
			self.AddLineToASM(Store)

			self.RegisterTable.ClearRegister(SrcReg)


		else:
			if 'addr' in ThreeACLine['OpB']:
				Src = self.GetDerefAddr(ThreeACLine, 'OpB')
				Reg = self.AssignRegister(ThreeACLine, 'OpB')
				LoadWord = LoadWord.format(Reg, Src)
				self.AddLineToASM(LoadWord, ThreeACLine)

			#case for storage from a normal temp
			elif 'temp' in ThreeACLine['OpB']:
				VReg = ThreeACLine['OpB']
				Reg = self.RegisterTable.FindRegisterWithVReg(VReg)
				if Reg is None:
					Reg = self.RegisterTable.GetFirstOpenRegister('t')
					self.RegisterTable.SetRegisterData(AssemblyName=Reg, NewValue=VReg)

			#case for floating point constant
			elif 'const' in ThreeACLine['OpB']:
				#get a register
				Reg = self.AssignRegister(ThreeACLine, 'OpB')
				LoadImmediate = "li {} {}"
				LoadImmediate = LoadImmediate.format( Reg, ThreeACLine['OpB'].replace('const ', ''))
				self.AddLineToASM(LoadImmediate, ThreeACLine)

			#user register to STORE
			Dest = self.GetDerefAddr(ThreeACLine, 'Dest')
			Store = Store.format(Reg, Dest)
			self.AddLineToASM(Store, ThreeACLine)


			#blow away register
			self.RegisterTable.ClearRegister(Reg)

	def CheckForASMCode(self, Code):
		for line in self.Output:
			if Code in line:
				return True
		return False

	def PROCENTRY(self, ThreeACLine):
		# if self.PriorIns is not None and self.PriorIns == 'GLOBAL':
		if not self.CheckForASMCode('.text'):
			self.AddLineToASM('.text', ThreeACLine)
		if not self.CheckForASMCode('jal main'):
			self.AddLineToASM('jal main')
			self.AddLineToASM('li $v0, 10')
			self.AddLineToASM('syscall')


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

		for arg in range(0, int(ThreeACLine['OpB']), 4):
			ArgLoad = "sw $a{} {}({})"
			ArgOffset = arg
			ArgLoad = ArgLoad.format(arg, ArgOffset, Reg)
			self.AddLineToASM(ArgLoad)
			self.RegisterTable.ClearRegister('$a' + str(ArgOffset))


	def ARGS(self, ThreeACLine):
		pass

	def VALOUT(self, ThreeACLine):
		LoadWord = "lw {} {}"
		LoadImmediate = "li {} {}"
		Move = 'move {} {}'
		Asm = ''
		Register = self.AssignArgumentRegister(ThreeACLine, 'Dest')

		if 'const' in ThreeACLine['Dest']:
			Asm = LoadImmediate.format(Register, ThreeACLine['Dest'].replace('const ', ''))

		elif 'local' in ThreeACLine['Dest']:
			Asm = LoadWord.format(Register, self.GetDerefAddr(ThreeACLine, 'Dest'))

		elif 'temp' in ThreeACLine['Dest']:
			SrcRegister = self.AssignRegister(ThreeACLine, 'Dest')
			Asm = Move.format(Register, SrcRegister)

		self.AddLineToASM(Asm, ThreeACLine)

		pass

	def CALL(self, ThreeACLine):
		ra = '$ra'
		StackUpdate =  'sub {}, {}, {}'
		StackReturn = 'add {}, {}, {}'
		StackPtr = self.RegisterTable.GetStackPtr()
		Reg = StackPtr['assembly name']
		Offset = 4

		#decrement stack ptr and keep track of it
		StackUpdate = StackUpdate.format(Reg, Reg, Offset)
		self.RegisterTable.PushStackPtr(Offset)
		self.AddLineToASM(StackUpdate, ThreeACLine)

		#store ra in extra space
		self.AddLineToASM('sw $ra 0($sp)', ThreeACLine)

		#call functions
		self.AddLineToASM('jal ' + ThreeACLine['Dest'].replace('label ', ''), ThreeACLine)

		# reinsert current ra and increment sp back
		self.AddLineToASM('lw $ra 0($sp)', ThreeACLine)

		StackReturn = StackReturn.format(Reg, Reg, Offset)
		self.RegisterTable.PopStackPtr()
		self.AddLineToASM(StackReturn, ThreeACLine)

		self.RegisterTable.ClearArgumentRegisters()


		pass

	def ENDPROC(self, ThreeACLine):
		# StackReturn = 'add {}, {}, {}'
		# StackPtr = self.RegisterTable.GetStackPtr()
		# Reg = StackPtr['assembly name']
		#
		# Decrement = self.RegisterTable.PopStackPtr()
		# StackReturn = StackReturn.format(Reg, Reg, Decrement)
		# self.AddLineToASM(StackReturn)
		pass

	def RETURN(self, ThreeACLine):
		StackReturn = 'add {}, {}, {}'
		StackPtr = self.RegisterTable.GetStackPtr()
		Reg = StackPtr['assembly name']

		Decrement = self.RegisterTable.GetLastStackInc()
		StackReturn = StackReturn.format(Reg, Reg, Decrement)
		self.AddLineToASM(StackReturn)

		self.AddLineToASM('jr $ra')

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

		#find register location for where its getting stored
		if 'IR' in ThreeACLine['Dest'] or 'FR' in ThreeACLine['Dest']:
			VReg = ThreeACLine['Dest']
			Reg = self.RegisterTable.FindRegisterWithVReg(VReg)

			#if the reister isnt already in use, find a new one to place data in
			if Reg is None:
				Reg = self.RegisterTable.GetFirstOpenRegister('t')
				self.RegisterTable.SetRegisterData(AssemblyName=Reg, NewValue=VReg)

		RegA = self.FormatOperand(ThreeACLine['OpA'], ThreeACLine['Dest'])
		RegB = self.FormatOperand(ThreeACLine['OpB'], ThreeACLine['Dest'])


		#format assembly function calls then send them off
		add = add.format(Reg, RegA, RegB)
		self.AddLineToASM(add, ThreeACLine)

		#clear registers from temp stores after operation is done
		if RegA is not None:
			self.RegisterTable.ClearRegister(RegA)
		if RegB is not None:
			self.RegisterTable.ClearRegister(RegB)



	def SUB(self, ThreeACLine):
		#staging strings used for assembly generation
		sub = "sub {}, {}, {}"

		#find register location for where its getting stored
		if 'IR' in ThreeACLine['Dest'] or 'FR' in ThreeACLine['Dest']:
			VReg = ThreeACLine['Dest']
			Reg = self.RegisterTable.FindRegisterWithVReg(VReg)

			#if the reister isnt already in use, find a new one to place data in
			if Reg is None:
				Reg = self.RegisterTable.GetFirstOpenRegister('t')
				self.RegisterTable.SetRegisterData(AssemblyName=Reg, NewValue=VReg)

		RegA = self.FormatOperand(ThreeACLine['OpA'], ThreeACLine['Dest'])
		RegB = self.FormatOperand(ThreeACLine['OpB'], ThreeACLine['Dest'])


		#format assembly function calls then send them off
		sub = sub.format(Reg, RegA, RegB)
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

		#find register location for where its getting stored
		if 'IR' in ThreeACLine['Dest'] or 'FR' in ThreeACLine['Dest']:
			VReg = ThreeACLine['Dest']
			Reg = self.RegisterTable.FindRegisterWithVReg(VReg)

			#if the reister isnt already in use, find a new one to place data in
			if Reg is None:
				Reg = self.RegisterTable.GetFirstOpenRegister('t')
				self.RegisterTable.SetRegisterData(AssemblyName=Reg, NewValue=VReg)

		RegA = self.FormatOperand(ThreeACLine['OpA'], ThreeACLine['Dest'])
		RegB = self.FormatOperand(ThreeACLine['OpB'], ThreeACLine['Dest'])

		#format assembly function calls then send them off
		mult = mult.format(RegA, RegB)
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

		#find register location for where its getting stored
		if 'IR' in ThreeACLine['Dest'] or 'FR' in ThreeACLine['Dest']:
			VReg = ThreeACLine['Dest']
			Reg = self.RegisterTable.FindRegisterWithVReg(VReg)

			#if the reister isnt already in use, find a new one to place data in
			if Reg is None:
				Reg = self.RegisterTable.GetFirstOpenRegister('t')
				self.RegisterTable.SetRegisterData(AssemblyName=Reg, NewValue=VReg)

		RegA = self.FormatOperand(ThreeACLine['OpA'], ThreeACLine['Dest'])
		RegB = self.FormatOperand(ThreeACLine['OpB'], ThreeACLine['Dest'])

		#format assembly function calls then send them off
		div = div.format(RegA, RegB)
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
		ASMout = "bne {}, {}, {}" #t0, t1, target

	def BREQ(self, ThreeACLine):
		ASMout = "beq {}, {}, {}" #to, t1, target

	def BRGE(self, ThreeACLine):
		ASMout = "bge {}, {}, {}"
		Dest = ThreeACLine['Dest']
		Dest = Dest.replace('label ', '')
		OpA = self.FormatOperand(ThreeACLine['OpA'], ThreeACLine['Dest'])
		OpB = self.FormatOperand(ThreeACLine['OpB'], ThreeACLine['Dest'])
		ASMout = ASMout.format(OpA, OpB, Dest)
		self.AddLineToASM(ASMout)

		if OpA is not None:
			self.RegisterTable.ClearRegister(OpA)
		if OpB is not None:
			self.RegisterTable.ClearRegister(OpB)



	def BRLT(self, ThreeACLine):
		ASMout = "blt {}, {}, {}"
		Dest = ThreeACLine['Dest']
		Dest = Dest.replace('label ', '')
		OpA = self.FormatOperand(ThreeACLine['OpA'], ThreeACLine['Dest'])
		OpB = self.FormatOperand(ThreeACLine['OpB'], ThreeACLine['Dest'])
		ASMout = ASMout.format(OpA, OpB, Dest)
		self.AddLineToASM(ASMout)

		if OpA is not None:
			self.RegisterTable.ClearRegister(OpA)
		if OpB is not None:
			self.RegisterTable.ClearRegister(OpB)

	def BRLE(self, ThreeACLine):
		ASMout = "ble {}, {}, {}"
		Dest = ThreeACLine['Dest']
		Dest = Dest.replace('label ', '')
		OpA = self.FormatOperand(ThreeACLine['OpA'], ThreeACLine['Dest'])
		OpB = self.FormatOperand(ThreeACLine['OpB'], ThreeACLine['Dest'])
		ASMout = ASMout.format(OpA, OpB, Dest)
		self.AddLineToASM(ASMout)

		if OpA is not None:
			self.RegisterTable.ClearRegister(OpA)
		if OpB is not None:
			self.RegisterTable.ClearRegister(OpB)

	def BRGT(self, ThreeACLine):
		ASMout = "bgt {}, {}, {}"
		Dest = ThreeACLine['Dest']
		Dest = Dest.replace('label ', '')
		OpA = self.FormatOperand(ThreeACLine['OpA'], ThreeACLine['Dest'])
		OpB = self.FormatOperand(ThreeACLine['OpB'], ThreeACLine['Dest'])
		ASMout = ASMout.format(OpA, OpB, Dest)
		self.AddLineToASM(ASMout)

		if OpA is not None:
			self.RegisterTable.ClearRegister(OpA)
		if OpB is not None:
			self.RegisterTable.ClearRegister(OpB)
