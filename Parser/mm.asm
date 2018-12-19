.text                         #PROCENTRY   label main   72   0
jal main
li $v0, 10
syscall

ReadChar:
	li $v0, 12
	syscall
	move $v1, $v0
	jr $ra

PrintChar:
	li $v0, 11
	syscall
	jr $ra

ReadFloat:
	li, $v0, 6
	syscall
	jr $ra

WriteFloat:
	li $v0, 2
	mov.s $f12, $f0
	syscall
	jr $ra

ReadInt:
	li $v0, 5
	syscall
	move $v1, $v0
	jr $ra

PrintInt:
	li $v0, 1
	syscall
	jr $ra
main:
sub $sp, $sp, 72
li $t0 3                      #STORE   local 60   None   const 3
sw $t0 60($sp)
li $t0 2                      #STORE   local 64   None   const 2
sw $t0 64($sp)
li $t0 0                      #STORE   local 0   None   const 0
sw $t0 0($sp)
L3:                           #LABEL   label L3   None   None
lw $t0, 0($sp)
li $t1, 2
bge $t0, $t1, L4
li $t0 0                      #STORE   local 4   None   const 0
sw $t0 4($sp)
L1:                           #LABEL   label L1   None   None
lw $t0, 4($sp)
li $t1, 2
bge $t0, $t1, L2
li $t0 2                      #LOAD   temp IR27   None   const 2
lw $t2, 0($sp)
mult $t0, $t2                 #MULT   temp IR29   temp IR27   local 0
mflo $t1
move $t0 $t1                  #LOAD   temp IR28   None   temp IR29
lw $t2, 4($sp)
add $t1, $t0, $t2             #ADD   temp IR31   temp IR28   local 4
li $t2, 4
mult $t2, $t1                 #MULT   temp IR32   const 4   temp IR31
mflo $t0

#      a[i][j] = 3;

la $t2, 12($sp)
add $t1, $t0, $t2             #ADD   addr IR30   temp IR32   local 12

#      b[i][j] = 2;

li $t0 3                      #STORE   addr IR30   None   const 3
sw $t0 ($t1)

#      c[i][j] = 0;

li $t0 2                      #LOAD   temp IR34   None   const 2
lw $t3, 0($sp)
mult $t0, $t3                 #MULT   temp IR36   temp IR34   local 0
mflo $t2
move $t0 $t2                  #LOAD   temp IR35   None   temp IR36
lw $t3, 4($sp)
add $t2, $t0, $t3             #ADD   temp IR38   temp IR35   local 4
li $t3, 4
mult $t3, $t2                 #MULT   temp IR39   const 4   temp IR38
mflo $t0
la $t3, 28($sp)
add $t2, $t0, $t3             #ADD   addr IR37   temp IR39   local 28
li $t0 2                      #STORE   addr IR37   None   const 2
sw $t0 ($t2)
li $t0 2                      #LOAD   temp IR41   None   const 2
lw $t4, 0($sp)
mult $t0, $t4                 #MULT   temp IR43   temp IR41   local 0
mflo $t3

#          c[i][k] += a[i][j] * b[j][k];

move $t0 $t3                  #LOAD   temp IR42   None   temp IR43
lw $t4, 4($sp)
add $t3, $t0, $t4             #ADD   temp IR45   temp IR42   local 4
li $t4, 4
mult $t4, $t3                 #MULT   temp IR46   const 4   temp IR45
mflo $t0
la $t4, 44($sp)
add $t3, $t0, $t4             #ADD   addr IR44   temp IR46   local 44
li $t0 0                      #STORE   addr IR44   None   const 0
sw $t0 ($t3)
lw $t0 60($sp)                #LOAD   temp IR48   None   local 60

#      out = c[i][j];

li $t4, 1
add $t0, $t0, $t4             #ADD   temp IR48   temp IR48   const 1
sw $t0 60($sp)                #STORE   local 60   None   temp IR48
lw $t0 64($sp)                #LOAD   temp IR49   None   local 64
li $t4, 1
add $t0, $t0, $t4             #ADD   temp IR49   temp IR49   const 1
sw $t0 64($sp)                #STORE   local 64   None   temp IR49
lw $t0 4($sp)                 #LOAD   temp IR50   None   local 4
li $t4, 1
add $t0, $t0, $t4             #ADD   temp IR50   temp IR50   const 1
sw $t0 4($sp)                 #STORE   local 4   None   temp IR50
j L1                          #JUMP   label L1   None   None
L2:                           #LABEL   label L2   None   None
lw $t0 0($sp)                 #LOAD   temp IR51   None   local 0
li $t4, 1
add $t0, $t0, $t4             #ADD   temp IR51   temp IR51   const 1
sw $t0 0($sp)                 #STORE   local 0   None   temp IR51
j L3                          #JUMP   label L3   None   None
L4:                           #LABEL   label L4   None   None
li $t0 0                      #STORE   local 0   None   const 0
sw $t0 0($sp)
L9:                           #LABEL   label L9   None   None
lw $t0, 0($sp)
li $t4, 2
bge $t0, $t4, L10
li $t0 0                      #STORE   local 4   None   const 0
sw $t0 4($sp)
L7:                           #LABEL   label L7   None   None
lw $t0, 4($sp)
li $t4, 2
bge $t0, $t4, L8
li $t0 0                      #STORE   local 8   None   const 0
sw $t0 8($sp)
L5:                           #LABEL   label L5   None   None
lw $t0, 8($sp)
li $t4, 2
bge $t0, $t4, L6
li $t0 2                      #LOAD   temp IR55   None   const 2
lw $t5, 0($sp)
mult $t0, $t5                 #MULT   temp IR57   temp IR55   local 0
mflo $t4
move $t0 $t4                  #LOAD   temp IR56   None   temp IR57
lw $t5, 8($sp)
add $t4, $t0, $t5             #ADD   temp IR59   temp IR56   local 8
li $t5, 4
mult $t5, $t4                 #MULT   temp IR60   const 4   temp IR59
mflo $t0
la $t5, 44($sp)
add $t4, $t0, $t5             #ADD   addr IR58   temp IR60   local 44
li $t0 2                      #LOAD   temp IR61   None   const 2
lw $t6, 0($sp)
mult $t0, $t6                 #MULT   temp IR63   temp IR61   local 0
mflo $t5
move $t0 $t5                  #LOAD   temp IR62   None   temp IR63
lw $t6, 4($sp)
add $t5, $t0, $t6             #ADD   temp IR65   temp IR62   local 4
li $t6, 4
mult $t6, $t5                 #MULT   temp IR66   const 4   temp IR65
mflo $t0
la $t6, 12($sp)
add $t5, $t0, $t6             #ADD   addr IR64   temp IR66   local 12
li $t0 2                      #LOAD   temp IR67   None   const 2
lw $t7, 4($sp)
mult $t0, $t7                 #MULT   temp IR69   temp IR67   local 4
mflo $t6
move $t0 $t6                  #LOAD   temp IR68   None   temp IR69
lw $t7, 8($sp)
add $t6, $t0, $t7             #ADD   temp IR71   temp IR68   local 8
li $t7, 4
mult $t7, $t6                 #MULT   temp IR72   const 4   temp IR71
mflo $t0
la $t7, 28($sp)
add $t6, $t0, $t7             #ADD   addr IR70   temp IR72   local 28
lw $t0 ($t5)                  #LOAD   temp IR73   None   addr IR64
lw $t7 ($t6)                  #LOAD   temp IR74   None   addr IR70
mult $t0, $t7                 #MULT   temp IR16   temp IR73   temp IR74
mflo $t8
lw $t0 ($t4)                  #LOAD   temp IR76   None   addr IR58
add $t7, $t0, $t8             #ADD   temp IR75   temp IR76   temp IR16
sw $t7 ($t4)                  #STORE   addr IR58   None   temp IR75
lw $t0 8($sp)                 #LOAD   temp IR77   None   local 8
li $t7, 1
add $t0, $t0, $t7             #ADD   temp IR77   temp IR77   const 1
sw $t0 8($sp)                 #STORE   local 8   None   temp IR77
j L5                          #JUMP   label L5   None   None
L6:                           #LABEL   label L6   None   None
lw $t0 4($sp)                 #LOAD   temp IR78   None   local 4
li $t7, 1
add $t0, $t0, $t7             #ADD   temp IR78   temp IR78   const 1
sw $t0 4($sp)                 #STORE   local 4   None   temp IR78
j L7                          #JUMP   label L7   None   None
L8:                           #LABEL   label L8   None   None
lw $t0 0($sp)                 #LOAD   temp IR79   None   local 0
li $t7, 1
add $t0, $t0, $t7             #ADD   temp IR79   temp IR79   const 1
sw $t0 0($sp)                 #STORE   local 0   None   temp IR79
j L9                          #JUMP   label L9   None   None
L10:                          #LABEL   label L10   None   None
li $t0 0                      #STORE   local 0   None   const 0
sw $t0 0($sp)
L14:                          #LABEL   label L14   None   None
lw $t0, 0($sp)
li $t7, 2
bge $t0, $t7, L15
li $t0 0                      #STORE   local 4   None   const 0
sw $t0 4($sp)
L12:                          #LABEL   label L12   None   None
lw $t0, 4($sp)
li $t7, 2
bge $t0, $t7, L13
li $t0 2                      #LOAD   temp IR82   None   const 2
lw $t8, 0($sp)
mult $t0, $t8                 #MULT   temp IR84   temp IR82   local 0
mflo $t7
move $t0 $t7                  #LOAD   temp IR83   None   temp IR84
lw $t8, 4($sp)
add $t7, $t0, $t8             #ADD   temp IR86   temp IR83   local 4
li $t8, 4
mult $t8, $t7                 #MULT   temp IR87   const 4   temp IR86
mflo $t0
la $t8, 44($sp)
add $t7, $t0, $t8             #ADD   addr IR85   temp IR87   local 44
lw $t7 ($t7)                  #STORE   local 68   None   addr IR85
sw $t7 68($sp)
lw $a0 68($sp)                #VALOUT   local 68   None   None
sub $sp, $sp, 4               #CALL   label PrintInt   None   None
sw $ra 0($sp)
jal PrintInt
lw $ra 0($sp)
add $sp, $sp, 4
move $t0 $v0                  #LOAD   temp IR89   None   const return
lw $t7 4($sp)                 #LOAD   temp IR90   None   local 4
li $t8, 1
add $t7, $t7, $t8             #ADD   temp IR90   temp IR90   const 1
sw $t7 4($sp)                 #STORE   local 4   None   temp IR90
j L12                         #JUMP   label L12   None   None
L13:                          #LABEL   label L13   None   None
lw $t7 0($sp)                 #LOAD   temp IR91   None   local 0
li $t8, 1
add $t7, $t7, $t8             #ADD   temp IR91   temp IR91   const 1
sw $t7 0($sp)                 #STORE   local 0   None   temp IR91
j L14                         #JUMP   label L14   None   None
L15:                          #LABEL   label L15   None   None
li $v0 0                      #LOAD   return   None   const 0
add $sp, $sp, 72
jr $ra
add $sp, $sp, 72
jr $ra
