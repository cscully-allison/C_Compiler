.text                         #PROCENTRY   label main   8 0
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
sub $sp, $sp, 8               
li $t0 5                      #STORE   local 0   None   const 5  
sw $t0 0($sp)                 
li $a0 10                     #VALOUT   const 10   None   None  
sub $sp, $sp, 4               #CALL   label fact   None   None  
sw $ra 0($sp)                 
jal fact                      
lw $ra 0($sp)                 
add $sp, $sp, 4               
move $t0 $v0                  #LOAD   temp IR10   None   const return  
sw $t0 4($sp)                 #STORE   local 4   None   temp IR10  
lw $a0 4($sp)                 #VALOUT   local 4   None   None  
sub $sp, $sp, 4               #CALL   label PrintInt   None   None  
sw $ra 0($sp)                 
jal PrintInt                  
lw $ra 0($sp)                 
add $sp, $sp, 4               
move $t0 $v0                  #LOAD   temp IR12   None   const return  
li $a0 ' '                    #VALOUT   const ' '   None   None  
sub $sp, $sp, 4               #CALL   label PrintChar   None   None  
sw $ra 0($sp)                 
jal PrintChar                 
lw $ra 0($sp)                 
add $sp, $sp, 4               
move $t1 $v0                  #LOAD   temp IR13   None   const return  
li $a0 '-'                    #VALOUT   const '-'   None   None  
sub $sp, $sp, 4               #CALL   label PrintChar   None   None  
sw $ra 0($sp)                 
jal PrintChar                 
lw $ra 0($sp)                 
add $sp, $sp, 4               
move $t2 $v0                  #LOAD   temp IR14   None   const return  
li $a0 ' '                    #VALOUT   const ' '   None   None  
sub $sp, $sp, 4               #CALL   label PrintChar   None   None  
sw $ra 0($sp)                 
jal PrintChar                 
lw $ra 0($sp)                 
add $sp, $sp, 4               
move $t3 $v0                  #LOAD   temp IR15   None   const return  
lw $a0 0($sp)                 #VALOUT   local 0   None   None  
sub $sp, $sp, 4               #CALL   label fact   None   None  
sw $ra 0($sp)                 
jal fact                      
lw $ra 0($sp)                 
add $sp, $sp, 4               
move $t4 $v0                  #LOAD   temp IR16   None   const return  
sw $t4 4($sp)                 #STORE   local 4   None   temp IR16  
lw $a0 4($sp)                 #VALOUT   local 4   None   None  
sub $sp, $sp, 4               #CALL   label PrintInt   None   None  
sw $ra 0($sp)                 
jal PrintInt                  
lw $ra 0($sp)                 
add $sp, $sp, 4               
move $t4 $v0                  #LOAD   temp IR18   None   const return  
add $sp, $sp, 8               
jr $ra                        
fact:                         
sub $sp, $sp, 12              
sw $a0 0($sp)                 
lw $t5, 0($sp)                
li $t6, 1                     
bgt $t5, $t6, L9              
li $v0 1                      #LOAD   return   None   const 1  
add $sp, $sp, 12              
jr $ra                        
j L10                         #JUMP   label L10   None   None  
L9:                           #LABEL   label L9   None   None  
lw $t6, 0($sp)                
li $t7, 1                     
sub $t5, $t6, $t7             #SUB   temp IR5   local 0   const 1  
sw $t5 4($sp)                 #STORE   local 4   None   temp IR5  
lw $a0 4($sp)                 #VALOUT   local 4   None   None  
sub $sp, $sp, 4               #CALL   label fact   None   None  
sw $ra 0($sp)                 
jal fact                      
lw $ra 0($sp)                 
add $sp, $sp, 4               
move $t5 $v0                  #LOAD   temp IR20   None   const return  
sw $t5 8($sp)                 #STORE   local 8   None   temp IR20  
lw $t6, 8($sp)                
lw $t7, 0($sp)                
mult $t6, $t7                 #MULT   temp IR8   local 8   local 0  
mflo $t5                      
move $v0 $t5                  #LOAD   return   None   temp IR8  
add $sp, $sp, 12              
jr $ra                        
L10:                          #LABEL   label L10   None   None  
add $sp, $sp, 12              
jr $ra                        
