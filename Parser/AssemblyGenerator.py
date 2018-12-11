from RegisterTable import RegisterTable
from ASTWalker import CodeGenerator

class AssemblyGenerator():
	def __init__ (self, RegisterTable = None, AddressTable = None, ThreeAC = None, Filename = None):
		self.RegisterTable = RegisterTable
		self.AddressTable = AddressTable
		self.ThreeAC = ThreeAC
		self.Filename = Filename
		for items in self.ThreeAC:
			self.GenerateAssemblyCode(items)

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
		print ("in label")

	def JUMP(self, ThreeACLine):
		print ("in jump")

	def LOAD(self, ThreeACLine):
		print ("in load")

	def STORE(self, ThreeACLine):
		print ("in store")

	def PROCENTRY(self, ThreeACLine):
		print ("in procentry")

	def ENDPROC(self, ThreeACLine):
		print ("in endproc")

	def RETURN(self, ThreeACLine):
		print ("in home")

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

	