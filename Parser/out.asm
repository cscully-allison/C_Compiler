.text                         #PROCENTRY   label main   32   0
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
sub $sp, $sp, 32              
li $t0 1                      #STORE   local 0   None   const 1  
sw $t0 0($sp)                 
li $t0 3                      #STORE   local 4   None   const 3  
sw $t0 4($sp)                 
li $t0 4                      #STORE   local 8   None   const 4  
sw $t0 8($sp)                 
li $t0 1                      #STORE   local 28   None   const 1  
sw $t0 28($sp)                
L7:                           #LABEL   label L7   None   None  
lw $t0, 0($sp)                
li $t1, 10                    
bgt $t0, $t1, L8              
lw $a0 0($sp)                 #VALOUT   local 0   None   None  
sub $sp, $sp, 4               #CALL   label PrintInt   None   None  
sw $ra 0($sp)                 
jal PrintInt                  
lw $ra 0($sp)                 
add $sp, $sp, 4               
move $t0 $v0                  #LOAD   temp IR11   None   const return  
li $a0 '-'                    #VALOUT   const '-'   None   None  
sub $sp, $sp, 4               #CALL   label PrintChar   None   None  
sw $ra 0($sp)                 
jal PrintChar                 
lw $ra 0($sp)                 
add $sp, $sp, 4               
move $t1 $v0                  #LOAD   temp IR12   None   const return  
lw $t2 0($sp)                 #LOAD   temp IR13   None   local 0  
li $t3, 1                     
add $t2, $t2, $t3             #ADD   temp IR13   temp IR13   const 1  
sw $t2 0($sp)                 #STORE   local 0   None   temp IR13  
lw $t2 4($sp)                 #LOAD   temp IR14   None   local 4  
li $t3, 1                     
add $t2, $t2, $t3             #ADD   temp IR14   temp IR14   const 1  
sw $t2 4($sp)                 #STORE   local 4   None   temp IR14  
lw $t2 8($sp)                 #LOAD   temp IR15   None   local 8  
li $t3, 1                     
add $t2, $t2, $t3             #ADD   temp IR15   temp IR15   const 1  
sw $t2 8($sp)                 #STORE   local 8   None   temp IR15  
lw $a0 4($sp)                 #VALOUT   local 4   None   None  
sub $sp, $sp, 4               #CALL   label PrintInt   None   None  
sw $ra 0($sp)                 
jal PrintInt                  
lw $ra 0($sp)                 
add $sp, $sp, 4               
move $t2 $v0                  #LOAD   temp IR16   None   const return  
li $a0 '-'                    #VALOUT   const '-'   None   None  
sub $sp, $sp, 4               #CALL   label PrintChar   None   None  
sw $ra 0($sp)                 
jal PrintChar                 
lw $ra 0($sp)                 
add $sp, $sp, 4               
move $t3 $v0                  #LOAD   temp IR17   None   const return  
lw $a0 8($sp)                 #VALOUT   local 8   None   None  
sub $sp, $sp, 4               #CALL   label PrintInt   None   None  
sw $ra 0($sp)                 
jal PrintInt                  
lw $ra 0($sp)                 
add $sp, $sp, 4               
move $t4 $v0                  #LOAD   temp IR18   None   const return  
li $a0 '-'                    #VALOUT   const '-'   None   None  
sub $sp, $sp, 4               #CALL   label PrintChar   None   None  
sw $ra 0($sp)                 
jal PrintChar                 
lw $ra 0($sp)                 
add $sp, $sp, 4               
move $t5 $v0                  #LOAD   temp IR19   None   const return  
j L7                          #JUMP   label L7   None   None  
L8:                           #LABEL   label L8   None   None  
L11:                          #LABEL   label L11   None   None  
lw $a0 0($sp)                 #VALOUT   local 0   None   None  
sub $sp, $sp, 4               #CALL   label PrintInt   None   None  
sw $ra 0($sp)                 
jal PrintInt                  
lw $ra 0($sp)                 
add $sp, $sp, 4               
move $t6 $v0                  #LOAD   temp IR20   None   const return  
li $a0 '-'                    #VALOUT   const '-'   None   None  
sub $sp, $sp, 4               #CALL   label PrintChar   None   None  
sw $ra 0($sp)                 
jal PrintChar                 
lw $ra 0($sp)                 
add $sp, $sp, 4               
move $t7 $v0                  #LOAD   temp IR21   None   const return  
lw $t8 0($sp)                 #LOAD   temp IR22   None   local 0  
li $t9, 1                     
add $t8, $t8, $t9             #ADD   temp IR22   temp IR22   const 1  
sw $t8 0($sp)                 #STORE   local 0   None   temp IR22  
lw $t8, 0($sp)                
li $t9, 20                    
bge $t8, $t9, L12             
j L11                         #JUMP   label L11   None   None  
L12:                          #LABEL   label L12   None   None  
li $v0 0                      #LOAD   return   None   const 0  
add $sp, $sp, 32              
jr $ra                        
add $sp, $sp, 32              
jr $ra                        
