import json
from Globals import CM, ST_G, FloatRegister, IntRegister, ErrManager
from Utils import GetBytesFromId, SafeCheckDict
from copy import deepcopy



class CodeGenerator(object):
    def __init__(self, AST, File):
        self.AST = AST
        self.File = File
        self.Output = []
        self.PostDeclaration = False
        self.Source = ST_G.SourceFile
        self.LineNo = 0
        ST_G.PushNewScope()
        self.Output3AC(AST)

    '''
    **********************
    Output functions.
    **********************
    '''

    def GetPads(self):
        Pads = [len('Instruction') + 3, len('Destination') + 3, len('Operand A') + 3, len('Operand B') + 3]

        for line in self.Output:
            line['Dest'] = str(line['Dest'])
            line['OpA'] = str(line['OpA'])
            line['OpB'] = str(line['OpB'])

            if len(line['Instruction']) > Pads[0]: Pads[0] = len(line['Instruction']) + 2
            if len(line['Dest']) > Pads[1]: Pads[1] = len(line['Dest']) + 2
            if len(line['OpA']) > Pads[2]: Pads[2] = len(line['OpA']) + 2
            if len(line['OpB']) > Pads[3]: Pads[3] = len(line['OpB']) + 2

        return Pads

    def PrettyPrint3AC(self):
        Pads = self.GetPads()
        LineNo = -1



        #print("%s %s %s %s" % ('Instruction'.ljust(Pads[0]), 'Destination'.ljust(Pads[1]), 'Operand A'.ljust(Pads[2]), 'Operand B'.ljust(Pads[3])))
        for i, line in enumerate(self.Output):
            if line['LineNo'] is not None and line['LineNo'] > LineNo:
                LineNo = line['LineNo']
                #print line
                with open(self.Source) as file:
                    for i in range(0, LineNo):
                        source = file.readline()
                print('#' + source)
                self.Output.insert(i-1, {'Instruction': "COMMENT", 'Dest': '#'+ source, 'OpA': '', 'OpB': '', 'LineNo': None, '3ACLineNo': None})

        #    print("%s %s %s %s" % ( line['Instruction'].ljust(Pads[0]), line['Dest'].ljust(Pads[1]), line['OpA'].ljust(Pads[2]), line['OpB'].ljust(Pads[3]) ) )


    '''
    **********************
    Auxilary functions.
    **********************
    '''
    def GetStatementRoot(self, FunctSubtree):
        CompoundRoot = None
        StatementIdentifiers = ['StatementList', 'AssignmentExpression', 'SelectionStatement', 'IterationStatement', 'BinOp']
        for Child in FunctSubtree.GetChildren():
            if self.IsNodeType(Child, 'CompoundStatement'):
                CompoundRoot = Child

        for Child in CompoundRoot.GetChildren():
            if self.IsNodeType(Child, 'PassUpNode'):
                if Child.ProductionName in StatementIdentifiers:
                    return Child
            elif Child.__class__.__name__ in StatementIdentifiers:
                return Child

        return None

    def IsNode(self, Node):
        if type(Node) is type("string"):
            return False
        for base in Node.__class__.__bases__:
            if base.__name__ is 'Node':
                return True
        return False

    def IsNodeType(self, Node, Name):
        if self.IsNode(Node):
            if Node.__class__.__name__ == Name:
                return True
        return False

    def AllocateRegister(self, ID):
        Register = None
        if 'float' in ID['Type']:
            Register = FloatRegister.DispenseTicket()
        else:
            Register = IntRegister.DispenseTicket()
        return Register

    def IsIdentifier(self, Node):
        for base in Node.__class__.__bases__:
            if base.__name__ is 'Identifier':
                return True
        return False

    def IsPassUpNode(self, Node):
        if Node.__class__.__name__ == 'PassUpNode':
            return True;
        return False;

    def IsTempReg(self, String):
        if String is None: return False

        if "FR" in String or "IR" in String:
            return True

        return False

    def IsLabel(self, String):
        if String is None: return False
        if 'label' in String:
            return True

        return False

    def GetInsFromOp(self, Operand):
        InsOpMap = { '+': 'ADD', '+=': 'ADD', '-': 'SUB', '-=': 'SUB', '*': 'MULT', '*=': 'MULT', '/': 'DIV', '/=': 'DIV', '==': 'EQ', '>': 'GT', '<': 'LT', '>=': 'GE', '<=': 'LE', '!=': 'NE', '!': 'NOT', '++': 'ADD', '--' : 'SUB'}
        return InsOpMap.get(Operand)

    def GetInverseComparator(self, Operand):
        ComparatorMap = {'EQ':'BRNE', 'NE':'BREQ', 'LT':'BRGE', 'GE': 'BRLT', 'GT': 'BRLE', 'LE':'BRGT'}
        return ComparatorMap.get(Operand)

    def GetFormattedOperand(self, Operand):
        Opcode = ""
        if type(Operand) is type(1):
            Opcode = Operand
        elif not self.IsTempReg(Operand):
            if Operand is not None:
                if 'Global' in Operand and Operand['Global'] is True:
                    Opcode = self.FormatGlobalVarCall(Operand)

                # case for arguments
                elif 'Local Offset' in Operand:
                    Opcode = self.FormatLocalVarCall(Operand)
                elif self.IsLabel(Operand):
                    Opcode = Operand
                else:
                    Opcode = self.FormatConstant(Operand)
        else:
            if 'addr' in Operand or 'faddr' in Operand:
                Opcode = Operand
            elif 'temp' not in Operand:
                if 'FR' in Operand:
                    Opcode = 'ftemp ' + Operand
                else:
                    Opcode = 'temp ' + Operand
            else:
                Opcode = Operand

        return Opcode

    def FormatLocalVarCall(self, ID):
        return('local ' + str(ID['Local Offset']))

    def FormatGlobalVarCall(self, ID):
        return('glob ' + ID['Label'])

    def FormatLabel(self, Label):
        return('label ' + Label)

    def GetTypeString(self, TypeArr):
        Type = ''

        for Value in TypeArr:
            Type += Value + ' '

        Type = Type[:-1]

        return Type

    def HandleAddress(self, Op):
        if 'faddr' in Op:
            Reg = FloatRegister.DispenseTicket()
            Reg = self.GetFormattedOperand(Reg)
            self.Load3AC(Instruction = "LOAD", Dest=Reg, OperandB=Op)
        elif 'addr' in Op:
            Reg = IntRegister.DispenseTicket()
            Reg = self.GetFormattedOperand(Reg)
            self.Load3AC(Instruction = "LOAD", Dest=Reg, OperandB=Op)
        else:
            return Op

        return Reg


    def FormatConstant(self, Const):
        if type(Const) is not type({}):
            return Const
        if 'float' in Const['Type']:
            return('fconst ' + str(Const['Value']))
        return('const ' + str(Const['Value']))

    def GetJumpStatement(self, Quad, Label):
        # evaluate
        Ins = self.GetInverseComparator(Quad.get('Instruction'))
        Quad['Instruction'] = Ins
        Quad['Dest'] = self.FormatLabel(Label)
        return Quad

    def GetArrayOffsetInfo(self, Array, Depth):
        Index = 0
        Arr = deepcopy(Array)
        Temparr = []


        while Index < Depth:
            Temparr.append(Arr.pop())
            Index += 1


        return Temparr

    def Load3AC(self, Instruction = None, Dest = None, OperandA = None, OperandB = None, LineNo = None):
        if OperandA is not None: OperandA = self.GetFormattedOperand(OperandA)
        if OperandB is not None: OperandB = self.GetFormattedOperand(OperandB)
        if Dest is not None: Dest = self.GetFormattedOperand(Dest)



        self.Output.append({'Instruction': Instruction, 'Dest': Dest, 'OpA': OperandA, 'OpB': OperandB, 'LineNo': LineNo, '3ACLineNo': self.LineNo})
        self.LineNo += 1;

    '''
    **********************
    Walking functons.
    **********************
    '''

    def Identifier(self, Subtree):
        ID = ST_G.RecoverMostRecentID(Subtree.Name)
        return ID

    def Constant(self, Subtree):
        return {'Type': [Subtree.DataType], 'Value': Subtree.Child, 'Type Qualifier': ['const']}

    def CastNode(self, Subtree):

        # call more 3AC gen after being called
        CastedReg = self.Output3AC(Subtree.SubExpression)

        CastType = self.GetTypeString(Subtree.CastTo)

        # get dest register
        if 'float' in Subtree.CastTo:
            CastToReg = FloatRegister.DispenseTicket()
        else:
            CastToReg = IntRegister.DispenseTicket()

        self.Load3AC(Instruction = "CONVERT", Dest=CastToReg, OperandA='type ' + CastType, OperandB=CastedReg)

        return CastToReg



    def FunctionCall(self, Subtree):

        Return = self.AllocateRegister(Subtree.IdPtr)

        ArgSize = 0
        for Arg in Subtree.Arguments:
            ArgSize += CM.TypeToBytes(Arg['Type'])

        self.Load3AC(Instruction="ARGS", Dest='const ' + str(ArgSize))


        Arguments = []

        for Argument in Subtree.ArgumentList.GetChildren():
            if Argument is not None:
                Arguments.append(self.Output3AC(Argument))

        for Argument in Arguments:
            Op = self.GetFormattedOperand(Argument)
            if 'const' in Op:
                self.Load3AC(Instruction="VALOUT", Dest=Op )
            if 'local' in Op:
                self.Load3AC(Instruction="VALOUT", Dest=Op )
            elif 'faddr' in Op:
                self.Load3AC(Instruction="REFOUT", Dest=Op )



        self.Load3AC(Instruction="CALL", Dest='label ' + Subtree.IdLabel)

        Return = self.GetFormattedOperand(Return)

        self.Load3AC(Instruction="LOAD", Dest=Return, OperandB="const return")

        return Return
        pass


    def ArrayAccess(self, Subtree, Depth = 0):
        Returned = None
        ArrayAccessRegister = None

        if self.IsNodeType(Subtree, "PrimaryExpression"):
            Returned = self.PrimaryExpression(Subtree)
            return Returned

        elif self.IsNodeType(Subtree, "ArrayAccess"):
            # variables
            ArraySizes = Subtree.SymbolLocation['Array Size']
            ID = Subtree.SymbolLocation
            ArrayType = ID['Type']
            # get a register for this assignment expression


            LHS = self.ArrayAccess(Subtree.ArrayName, Depth + 1)

            # check if we have a recusrive element in the array access area
            if self.IsNodeType(Subtree.ArrayOffset, "ArrayAccess"):
                RHS = self.Output3AC(Subtree.ArrayOffset)
            else:
                RHS = self.ArrayAccess(Subtree.ArrayOffset, Depth + 1)


            Multiplicands = self.GetArrayOffsetInfo(ArraySizes, Depth)


            #### Main output of 3AC ######
            PriorReg = None
            # assume these are integers
            for Scalar in Multiplicands:
                if PriorReg is None:
                    # assign and make register
                    PriorReg = IntRegister.DispenseTicket()
                    ScalarOp = "const " + str(Scalar)
                    self.Load3AC(Instruction = "LOAD", Dest=PriorReg, OperandB=ScalarOp, LineNo=Subtree.Loc[0])
                else:
                    # multiply with prior reg and assign
                    TReg = IntRegister.DispenseTicket()
                    ScalarOp = "const " + str(Scalar)
                    self.Load3AC(Instruction = "MULT", Dest=TReg, OperandA=PriorReg, OperandB=ScalarOp, LineNo=Subtree.Loc[0])
                    PriorReg = TReg


            ArrayAccessRegister = IntRegister.DispenseTicket()
            # we are still calulating dimensional offsets
            if Depth > 0:

                # multiply the size offset with the actual offset value
                OffsetReg = IntRegister.DispenseTicket()
                Offset = self.GetFormattedOperand(RHS)
                self.Load3AC(Instruction = "MULT", Dest=OffsetReg, OperandA=PriorReg, OperandB=Offset, LineNo=Subtree.Loc[0])

                #add with remaining offsets to get our total offset

                if 'Subtype' not in LHS:
                    RemainingOffsets = self.GetFormattedOperand(LHS)
                    self.Load3AC(Instruction = "ADD", Dest=ArrayAccessRegister, OperandA=RemainingOffsets, OperandB=OffsetReg, LineNo=Subtree.Loc[0])
                else:
                    #this is where problems happen for 3ac to reg conv.
                    self.Load3AC(Instruction = "LOAD", Dest=ArrayAccessRegister, OperandB=OffsetReg, LineNo=Subtree.Loc[0])

            # we are not still calculating dimensional offsets
            else:
                Offset = self.GetFormattedOperand(RHS)

                if 'Subtype' not in LHS:
                    FinalOffsetReg = IntRegister.DispenseTicket()
                    RemainingOffsets = self.GetFormattedOperand(LHS)
                    self.Load3AC(Instruction = "ADD", Dest=FinalOffsetReg, OperandA=RemainingOffsets, OperandB=Offset, LineNo=Subtree.Loc[0])
                else:
                    FinalOffsetReg = IntRegister.DispenseTicket()
                    self.Load3AC(Instruction = "LOAD", Dest=FinalOffsetReg, OperandB=Offset, LineNo=Subtree.Loc[0])

                #load address of our current array into temp
                # add int to the address in array
                # access new offset as variable

                OffsetInBytes = IntRegister.DispenseTicket()
                Bytes = 'const ' + str(CM.TypeToBytes(ID['Type']))

                self.Load3AC(Instruction = "MULT", Dest=OffsetInBytes, OperandA=Bytes, OperandB=FinalOffsetReg, LineNo=Subtree.Loc[0])

                if 'float' in ArrayType:
                    ArrayAccessRegister = 'faddr ' + ArrayAccessRegister
                    self.Load3AC(Instruction = "ADD", Dest=ArrayAccessRegister, OperandA=OffsetInBytes, OperandB=self.GetFormattedOperand(ID), LineNo=Subtree.Loc[0])
                else:
                    ArrayAccessRegister = 'addr ' + ArrayAccessRegister
                    self.Load3AC(Instruction = "ADD", Dest=ArrayAccessRegister, OperandA=OffsetInBytes, OperandB=self.GetFormattedOperand(ID), LineNo=Subtree.Loc[0])

            return ArrayAccessRegister



    def PrimaryExpression(self, Subtree):
        return self.Output3AC(Subtree)

    def Return(self, Subtree):
        ReturnOp = None
        ReturnRegister_Const = 'return'

        #check for return vale and call recursion
        if Subtree.ReturnExpression is not None:
            Return = self.Output3AC(Subtree.ReturnExpression)
            ReturnOp = self.GetFormattedOperand(Return)
            #load in special reserved register
            self.Load3AC(Instruction = "LOAD", Dest=ReturnRegister_Const, OperandB=ReturnOp)
            self.Load3AC(Instruction = "RETURN")


    def SelectionStatement(self, Subtree):
        # call Output3AC on the BinOp statement
        result = self.Output3AC(Subtree.IfExpression)

        #build our Jump Statement from the last output
        JumpStatementQuad = self.GetJumpStatement(self.Output.pop(), Subtree.ElseLabel) #then block is our end of block

        #load jump statement into the output
        self.Output.append(JumpStatementQuad)

        #call generate 3AC on then block
        self.Output3AC(Subtree.ThenBlock)
        self.Load3AC(Instruction="JUMP", Dest = self.FormatLabel(Subtree.End))
        #print jump Label
        self.Load3AC(Instruction = "LABEL", Dest=self.FormatLabel(Subtree.ElseLabel))

        if Subtree.ElseBlock is not None:
            self.Output3AC(Subtree.ElseBlock)

        self.Load3AC(Instruction = "LABEL", Dest = self.FormatLabel(Subtree.End))

        pass

    def AssignmentExpression(self, Subtree):
        # assign a register
        AssignRegister = None

        # get either side
        LHS = self.Output3AC(Subtree.Left)
        RHS = self.Output3AC(Subtree.Right)
        LHSOp = self.GetFormattedOperand(LHS)
        RHSOp = self.GetFormattedOperand(RHS)


        # get a register for this assignment expression
        if type(LHS) is not type("string") and 'float' in LHS['Type']:
            AssignRegister = FloatRegister.DispenseTicket()
        else:
            AssignRegister = IntRegister.DispenseTicket()

        # outputting binary operation before assignment
        Ins = self.GetInsFromOp(Subtree.Op)

        # check for compound operation
        if Ins is not None:
            OpA = self.HandleAddress(LHSOp)
            OpB = self.HandleAddress(RHSOp)
            self.Load3AC(Instruction = Ins, Dest=AssignRegister, OperandA = OpA, OperandB = OpB)
            self.Load3AC(Instruction = "STORE", Dest=LHSOp, OperandB=AssignRegister)
        else:
            self.Load3AC(Instruction = "STORE", Dest=LHSOp, OperandB=RHSOp)


    def BinOp(self, Subtree):
        #base case
        if not self.IsNode(Subtree):
            return

        elif self.IsNodeType(Subtree, "CastNode"):
            # this wil be replaced with a cast node output thing
            return self.CastNode(Subtree)

        elif self.IsNodeType(Subtree, 'ArrayAccess'):
            return self.ArrayAccess(Subtree)

        elif self.IsNodeType(Subtree, 'Identifier'):
            ID = ST_G.RecoverMostRecentID(Subtree.Name)
            return ID
            # return data structure

        elif self.IsNodeType(Subtree, "Constant"):
            # return pseudo-identifier
            return {'Type': [Subtree.DataType], 'Value': Subtree.Child, 'Type Qualifier': ['const']}

        elif self.IsNodeType(Subtree, "BinOp"):
            LHSOp = None
            RHSOp = None
            LHS = self.BinOp(Subtree.Left)
            RHS = self.BinOp(Subtree.Right)

            # We need to check some things: casts, identifiers for loading into items
            Ins = self.GetInsFromOp(Subtree.Op)
            LHSOp = self.GetFormattedOperand(LHS)
            RHSOp = self.GetFormattedOperand(RHS)


            if 'faddr' in LHSOp:
                TempOp = FloatRegister.DispenseTicket()
                self.Load3AC(Instruction = 'LOAD', Dest=TempOp, OperandB = LHSOp)
                LHSOp = TempOp
            elif 'addr' in LHSOp:
                TempOp = IntRegister.DispenseTicket()
                self.Load3AC(Instruction = 'LOAD', Dest=TempOp, OperandB = LHSOp)
                LHSOp = TempOp
            if 'faddr' in RHSOp:
                TempOp = FloatRegister.DispenseTicket()
                self.Load3AC(Instruction = 'LOAD', Dest=TempOp, OperandB = RHSOp)
                RHSOp = TempOp
            elif 'addr' in RHSOp:
                TempOp = IntRegister.DispenseTicket()
                self.Load3AC(Instruction = 'LOAD', Dest=TempOp, OperandB = RHSOp)
                RHSOp = TempOp



            self.Load3AC(Instruction = Ins, Dest=Subtree.Register, OperandA = LHSOp, OperandB = RHSOp)

            return Subtree.Register

        else:
            for Child in Subtree.GetChildren():
                return self.BinOp(Child)



    def Declaration(self, DeclNode):
        # add declaration to symbol table
        if self.PostDeclaration is False:
            for ID in DeclNode.ID:
                if not SafeCheckDict(ID, 'Subtype', 'Function Prototype'):
                    ID['Size In Bytes'] = GetBytesFromId(ID, CM.TypeToBytes(ID['Type']))
                    ID['Local Offset'] = ST_G.CalcLocalOffset()
                    if ST_G.IsGlobalScope():
                        ID['Global'] = True
                        self.Load3AC(Instruction = "GLOBAL", Dest='label ' + ID['Label'], OperandA = ID['Size In Bytes'])
                    else:
                        ID['Global'] = False
                    ST_G.InsertSymbol(ID['Label'], ID)


            return DeclNode.Bytes

        return None

    def GetStackFrameSize(self, CompoundStatement):
        if CompoundStatement is None: return 0
        if not self.IsNode(CompoundStatement): return 0
        if CompoundStatement.GetChildren() is None: return 0

        RunningSize = 0

        for Child in CompoundStatement.GetChildren():
            if self.IsNodeType(Child, 'CompoundStatement'):
                RunningSize += self.GetStackFrameSize(Child)
            elif self.IsNodeType(Child, 'Declaration'):
                RunningSize += self.Declaration(Child)
            else:
                RunningSize += self.GetStackFrameSize(Child)

        return RunningSize

    def FunctionDefintion(self, FunctSubtree):
        StackFrameSize = 0
        ArgsSize = 0

        # push a new scope on
        ST_G.PushNewScope()

        # add stack frame size from Arguments
        for Arg in FunctSubtree.FunctionArguments:
            Arg['Size In Bytes'] = GetBytesFromId(Arg, CM.TypeToBytes(Arg['Type']))
            Arg['Local Offset'] = ST_G.CalcLocalOffset()
            ST_G.InsertSymbol(Arg['Label'], Arg)

            ArgsSize += Arg['Size In Bytes']


        # fetch stack frame size from locals
        for Child in FunctSubtree.GetChildren():
            if self.IsNodeType(Child, 'CompoundStatement'):
                StackFrameSize = self.GetStackFrameSize(Child)

        self.PostDeclaration = True

        # Loading label, argsize in bytes, and StackFrameSize in bytes
        self.Load3AC(Instruction = "PROCENTRY", Dest=self.FormatLabel(FunctSubtree.IDPtr['Label']), OperandA = StackFrameSize, OperandB = ArgsSize)



        ST_G.WriteSymbolTableToFile("walkerb.out")

        #recursively call Output 3AC on CompoundStatement to maintain correct scoping in ST
        Statement = self.GetStatementRoot(FunctSubtree)


        if Statement is not None:
            self.Output3AC(Statement)

        #pop scope
        self.PostDeclaration = False
        ST_G.PopScope()

        self.Load3AC(Instruction = "ENDPROC")
        self.Load3AC(Instruction = "RETURN")


    def UnaryExpression(self, Subtree):
        Op = self.GetInsFromOp(Subtree.Op)
        RHS = self.GetFormattedOperand(self.Output3AC(Subtree.Child))
        AssignRegister = None
        TypeCheck = self.Output3AC(Subtree.Child)

        # get a register for this assignment expression
        if type(TypeCheck) is not type("string") and 'float' in TypeCheck['Type']:
            AssignRegister = FloatRegister.DispenseTicket()
        else:
            AssignRegister = IntRegister.DispenseTicket()
        #load into register
        self.Load3AC(Instruction = "LOAD", Dest = AssignRegister, OperandB = RHS)
        self.Load3AC(Instruction = Op, Dest=AssignRegister, OperandA = AssignRegister, OperandB = "const " + str(1))
        self.Load3AC(Instruction = "RETURN", Dest = RHS, OperandB = AssignRegister)


    def UnaryPostfixExpression(self, Subtree):
        Op = self.GetInsFromOp(Subtree.Op)
        LHS = self.GetFormattedOperand(self.Output3AC(Subtree.Child))
        AssignRegister = None
        TypeCheck = self.Output3AC(Subtree.Child)

        # get a register for this assignment expression
        if type(TypeCheck) is not type("string") and 'float' in TypeCheck['Type']:
            AssignRegister = FloatRegister.DispenseTicket()
        else:
            AssignRegister = IntRegister.DispenseTicket()
        #load into register
        self.Load3AC(Instruction = "LOAD", Dest = AssignRegister, OperandB = LHS)
        self.Load3AC(Instruction = Op, Dest=AssignRegister, OperandA = AssignRegister, OperandB = "const " + str(1))
        self.Load3AC(Instruction = "STORE", Dest = LHS, OperandB = AssignRegister)
        return AssignRegister

    def IterationStatement(self, Subtree):
        #do while loop
        if Subtree.IsDo == 'True':
            #set label to go back to the comparison for a for or while loop
            self.Load3AC(Instruction = "LABEL", Dest= self.FormatLabel(Subtree.StartLabel))

            #perform statement prior to conditional expression
            if Subtree.Statement is not None:
                self.Output3AC(Subtree.Statement)

            #if there is a conditional expression, swap the format of it and include the jump label
            #jump to start statement if not true
            if Subtree.ConditionalExpression is not None:
                self.Output3AC(Subtree.ConditionalExpression)
                NewConditionalQuad = self.GetJumpStatement(self.Output.pop(), Subtree.EndLabel)
                self.Output.append(NewConditionalQuad)

            self.Load3AC(Instruction = "JUMP", Dest =  self.FormatLabel(Subtree.StartLabel))
            self.Load3AC(Instruction = "LABEL", Dest= self.FormatLabel(Subtree.EndLabel))

        #for or while loop
        else:
            #if for loop include the initial assignment statement
            if Subtree.AssignmentExpression is not None:
                self.Output3AC(Subtree.AssignmentExpression)

            #set label to go back to the comparison for a for or while loop
            self.Load3AC(Instruction = "LABEL", Dest= self.FormatLabel(Subtree.StartLabel))

            #if there is a conditional expression, swap the format of it and include the jump label
            if Subtree.ConditionalExpression is not None:
                self.Output3AC(Subtree.ConditionalExpression)
                NewConditionalQuad = self.GetJumpStatement(self.Output.pop(), Subtree.EndLabel)
                self.Output.append(NewConditionalQuad)

            #perform statement if conditional expression is not met if there is a statement
            if Subtree.Statement is not None:
                self.Output3AC(Subtree.Statement)

            #do postfix iteration if one exists
            if Subtree.IterativeExpression is not None:
                self.Output3AC(Subtree.IterativeExpression)

            #jump back to conditional expression
            self.Load3AC(Instruction = "JUMP", Dest = self.FormatLabel(Subtree.StartLabel))

            #set end of loop label for conditional to jump to once met
            self.Load3AC(Instruction = "LABEL", Dest= self.FormatLabel(Subtree.EndLabel))

    def Output3AC(self, Subtree):
        # Base Case
        if Subtree is None: return None
        if not self.IsNode(Subtree): return None
        if Subtree.GetChildren() is None: return None



        SideEffect = None

        #Pass Up Node
        if self.IsPassUpNode(Subtree):
            for Child in Subtree.GetChildren():
                self.Output3AC(Child)
        elif self.IsNodeType(Subtree, 'FunctionDefintion'):
            self.FunctionDefintion(Subtree)
        elif self.IsNodeType(Subtree, "Declaration"):
            self.Declaration(Subtree)
        elif self.IsNodeType(Subtree, "BinOp"):
            SideEffect = self.BinOp(Subtree)
        elif self.IsNodeType(Subtree, "AssignmentExpression"):
            self.AssignmentExpression(Subtree)
        elif self.IsNodeType(Subtree, "Identifier"):
            SideEffect = self.Identifier(Subtree)
        elif self.IsNodeType(Subtree, "Constant"):
            SideEffect = self.Constant(Subtree)
        elif self.IsNodeType(Subtree, "SelectionStatement"):
            self.SelectionStatement(Subtree)
        elif self.IsNodeType(Subtree, "ReturnNode"):
            self.Return(Subtree)
        elif self.IsNodeType(Subtree, "ArrayAccess"):
            SideEffect = self.ArrayAccess(Subtree)
        elif self.IsNodeType(Subtree, "UnaryExpression"):
            SideEffect = self.UnaryExpression(Subtree)
        elif self.IsNodeType(Subtree, "UnaryPostfixExpression"):
            SideEffect = self.UnaryPostfixExpression(Subtree)
        elif self.IsNodeType(Subtree, "IterationStatement"):
            self.IterationStatement(Subtree)
        elif self.IsNodeType(Subtree, "FunctionCall"):
            SideEffect = self.FunctionCall(Subtree)
        else:
            for Child in Subtree.GetChildren():
                SideEffect = self.Output3AC(Child)


        return SideEffect




class ASTWalker(object):
    def __init__(self, AST, TreeGraphOut = "TreeGraph.out.py"):
        self.AST = AST
        self.TreeGraphOut = "TreeGraph.out.py"
        self.TreeGraphOutPtr = open(self.TreeGraphOut, "w")

    def IsNode(self, Node):
        for base in Node.__class__.__bases__:
            if base.__name__ is 'Node':
                return True
        return False

    def IsIdentifier(self, Node):
        for base in Node.__class__.__bases__:
            if base.__name__ is 'Identifier':
                return True
        return False



    def PrintASTHelper(self, Root):
        self.TreeGraphOutPtr.write("from anytree import Node, RenderTree \n")
        self.TreeGraphOutPtr.write("from anytree.exporter import DotExporter\n")


        if Root is not None and self.IsNode(Root):
            self.TreeGraphOutPtr.write(Root.BuildTreeOutput(None) + '\n')

            if Root.GetChildren() is not None:
                for SubTree in Root.GetChildren():
                    self.PrintAST(Root, SubTree)
        else:
            return

        # Write out trailing functions
        self.TreeGraphOutPtr.write('''
for pre, fill, node in RenderTree({}):
    if "TokenLocation" in node.name: print("%s%s" % (pre, node.name))
    else: print("%s%s" % (pre, node.name[:-5]) )\n
    '''.format(Root.__class__.__name__ + str(id(Root))))

        self.TreeGraphOutPtr.write('''
def f(node):
    if node.is_leaf and "TokenLocation" in node.name:
        return 'label="%s"' % (node.name)
    return 'label="%s"' % (node.name[:-5])

DotExporter({}, nodeattrfunc=f).to_picture("AST.png")
        '''.format(Root.__class__.__name__ + str(id(Root))))


    def PrintAST(self, Parent, Child):
        ''' This function is called where the child is our current node. Parent was the callee.
        '''
        #base check
        if Child is not None and Child is not False:
            if self.IsNode(Child):
                self.TreeGraphOutPtr.write(Child.BuildTreeOutput(Parent.__class__.__name__ + str(id(Parent))) + '\n')

                #recursive call
                if Child.GetChildren() is not None:
                    for SubTree in Child.GetChildren():
                        self.PrintAST(Child, SubTree)

            # check if child is a dictonary
            elif type(Child) is type({}):
                output = '{} = Node(\"{}\"{})'
                output = output.format("leaf", ', '.join("{!s}={!r}".format(key,val) for (key,val) in Child.items()), ", parent=" +Parent.__class__.__name__ + str(id(Parent)))
                self.TreeGraphOutPtr.write(output + '\n')

            elif type(Child) is type([]):
                    DataType = ''
                    for SubC in Child:
                        DataType += SubC + " "

                    output = '{} = Node(\'{}\'{})'
                    output = output.format("leaf", DataType + "_" + str(id(Parent))[-4:], ", parent=" +Parent.__class__.__name__ + str(id(Parent)))
                    self.TreeGraphOutPtr.write(output + '\n')

            else:
                output = '{} = Node(\"{}\"{})'
                output = output.format("leaf", Child + "_" + str(id(Parent))[-4:], ", parent=" +Parent.__class__.__name__ + str(id(Parent)))
                self.TreeGraphOutPtr.write(output + '\n')

        else:
            return
