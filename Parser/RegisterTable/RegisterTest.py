from RegisterTable import RegisterTable

TestReg = RegisterTable()
TestReg.SetARegister('a', 'char')
TestReg.SetTRegister(20, 'int')
TestReg.SetTRegister(21, 'int')
TestReg.SetTRegister(22, 'int')
TestReg.SetTRegister(23, 'int')
TestReg.SetTRegister(24, 'int')
TestReg.SetTRegister(25, 'int')
TestReg.SetTRegister(26, 'int')
TestReg.SetTRegister(27, 'int')
TestReg.SetTRegister(28, 'int')
TestReg.SetTRegister(29, 'int')
TestReg.SetTRegister(30, 'int')

for elem in TestReg.Registers:
	print elem

