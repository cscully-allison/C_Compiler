<<<<<<< HEAD
.text                         #PROCENTRY   label main   32   0
jal main
li $v0, 10
syscall
=======
.text                         #PROCENTRY   label main   160   4
jal main                      
li $v0, 10                    
syscall                       
>>>>>>> 6c7cd8291b20172d324a52591bed9d017f506ba1

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
<<<<<<< HEAD
main:
sub $sp, $sp, 32
li $t0 1                      #STORE   local 0   None   const 1
sw $t0 0($sp)
li $t0 3                      #STORE   local 4   None   const 3
sw $t0 4($sp)
li $t0 4                      #STORE   local 8   None   const 4
sw $t0 8($sp)
li $t0 1                      #STORE   local 28   None   const 1
sw $t0 28($sp)
li $t0 2                      #LOAD   temp IR13   None   const 2
li $t2, 2
mult $t0, $t2                 #MULT   temp IR15   temp IR13   const 2
mflo $t1
move $t0 $t1                  #LOAD   temp IR14   None   temp IR15
li $t2, 1
add $t1, $t0, $t2             #ADD   temp IR17   temp IR14   const 1
li $t2, 4
mult $t2, $t1                 #MULT   temp IR18   const 4   temp IR17
mflo $t0

#  arr[2][1] = 43;


#  i = arr[2][1];

la $t2, 12($sp)
add $t1, $t0, $t2             #ADD   addr IR16   temp IR18   local 12
li $t0 43                     #STORE   addr IR16   None   const 43
sw $t0 ($t1)
li $t0 2                      #LOAD   temp IR20   None   const 2
li $t3, 2
mult $t0, $t3                 #MULT   temp IR22   temp IR20   const 2
mflo $t2                      
move $t0 $t2                  #LOAD   temp IR21   None   temp IR22
li $t3, 1
add $t2, $t0, $t3             #ADD   temp IR24   temp IR21   const 1
li $t3, 4
mult $t3, $t2                 #MULT   temp IR25   const 4   temp IR24
mflo $t0
la $t3, 12($sp)
add $t2, $t0, $t3             #ADD   addr IR23   temp IR25   local 12
lw $t2 ($t2)                  #STORE   local 4   None   addr IR23
sw $t2 4($sp)
lw $a0 4($sp)                 #VALOUT   local 4   None   None
sub $sp, $sp, 4               #CALL   label PrintInt   None   None
sw $ra 0($sp)
jal PrintInt
lw $ra 0($sp)
add $sp, $sp, 4
move $t0 $v0                  #LOAD   temp IR27   None   const return
L5:                           #LABEL   label L5   None   None
lw $t2, 0($sp)
li $t3, 10
bgt $t2, $t3, L6
lw $a0 0($sp)                 #VALOUT   local 0   None   None
sub $sp, $sp, 4               #CALL   label PrintInt   None   None
sw $ra 0($sp)
jal PrintInt
lw $ra 0($sp)
add $sp, $sp, 4
move $t2 $v0                  #LOAD   temp IR28   None   const return
li $a0 '-'                    #VALOUT   const '-'   None   None
sub $sp, $sp, 4               #CALL   label PrintChar   None   None
sw $ra 0($sp)
jal PrintChar
lw $ra 0($sp)
add $sp, $sp, 4
move $t3 $v0                  #LOAD   temp IR29   None   const return
lw $t4 0($sp)                 #LOAD   temp IR30   None   local 0
li $t5, 1
add $t4, $t4, $t5             #ADD   temp IR30   temp IR30   const 1
sw $t4 0($sp)                 #STORE   local 0   None   temp IR30
lw $t4 4($sp)                 #LOAD   temp IR31   None   local 4
li $t5, 1
add $t4, $t4, $t5             #ADD   temp IR31   temp IR31   const 1
sw $t4 4($sp)                 #STORE   local 4   None   temp IR31
lw $t4 8($sp)                 #LOAD   temp IR32   None   local 8
li $t5, 1
add $t4, $t4, $t5             #ADD   temp IR32   temp IR32   const 1
sw $t4 8($sp)                 #STORE   local 8   None   temp IR32
lw $a0 4($sp)                 #VALOUT   local 4   None   None
sub $sp, $sp, 4               #CALL   label PrintInt   None   None
sw $ra 0($sp)
jal PrintInt
lw $ra 0($sp)
add $sp, $sp, 4
move $t4 $v0                  #LOAD   temp IR33   None   const return
j L5                          #JUMP   label L5   None   None
L6:                           #LABEL   label L6   None   None
L7:                           #LABEL   label L7   None   None
lw $t5 0($sp)                 #LOAD   temp IR34   None   local 0
li $t6, 1
add $t5, $t5, $t6             #ADD   temp IR34   temp IR34   const 1
sw $t5 0($sp)                 #STORE   local 0   None   temp IR34
lw $t5, 0($sp)
li $t6, 20
bge $t5, $t6, L8
j L7                          #JUMP   label L7   None   None
L8:                           #LABEL   label L8   None   None
li $v0 0                      #LOAD   return   None   const 0
add $sp, $sp, 32
jr $ra
add $sp, $sp, 32
jr $ra
=======
main:                         
sub $sp, $sp, 164             
sw $a0 0($sp)                 
                              #LOAD   temp IR6   None    
li $t1, 4                     
mult $t1, None                #MULT   temp IR7   const 4   temp IR6  
mflo $t0                      
la $t2, 4($sp)                
add $t1, $t0, $t2             #ADD   addr IR5   temp IR7   local 4  

#	arr1[1 + 2]=3;
            

#	arr2[3][6] = arr1[3];
     

#	arr1[2] = arr2[3][6];
     
li $t0 3                      #STORE   addr IR5   None   const 3  
sw $t0 ($t1)                  
li $t0 7                      #LOAD   temp IR9   None   const 7  
li $t3, 3                     
mult $t0, $t3                 #MULT   temp IR11   temp IR9   const 3  
mflo $t2                      
move $t0 $t2                  #LOAD   temp IR10   None   temp IR11  
li $t3, 6                     
add $t2, $t0, $t3             #ADD   temp IR13   temp IR10   const 6  
li $t3, 4                     
mult $t3, $t2                 #MULT   temp IR14   const 4   temp IR13  
mflo $t0                      
la $t3, 24($sp)               
add $t2, $t0, $t3             #ADD   addr IR12   temp IR14   local 24  
li $t0 3                      #LOAD   temp IR16   None   const 3  
li $t4, 4                     
mult $t4, $t0                 #MULT   temp IR17   const 4   temp IR16  
mflo $t3                      
la $t4, 4($sp)                
add $t0, $t3, $t4             #ADD   addr IR15   temp IR17   local 4  
lw $t0 ($t0)                  #STORE   addr IR12   None   addr IR15  
sw $t0 ($t2)                  
li $t0 2                      #LOAD   temp IR20   None   const 2  
li $t4, 4                     
mult $t4, $t0                 #MULT   temp IR21   const 4   temp IR20  
mflo $t3                      
la $t4, 4($sp)                
add $t0, $t3, $t4             #ADD   addr IR19   temp IR21   local 4  
li $t3 7                      #LOAD   temp IR22   None   const 7  
li $t5, 3                     
mult $t3, $t5                 #MULT   temp IR24   temp IR22   const 3  
mflo $t4                      
move $t3 $t4                  #LOAD   temp IR23   None   temp IR24  
li $t5, 6                     
add $t4, $t3, $t5             #ADD   temp IR26   temp IR23   const 6  
li $t5, 4                     
mult $t5, $t4                 #MULT   temp IR27   const 4   temp IR26  
mflo $t3                      
la $t5, 24($sp)               
add $t4, $t3, $t5             #ADD   addr IR25   temp IR27   local 24  
lw $t4 ($t4)                  #STORE   addr IR19   None   addr IR25  
sw $t4 ($t0)                  
add $sp, $sp, 164             
jr $ra                        
>>>>>>> 6c7cd8291b20172d324a52591bed9d017f506ba1
