.text                         #PROCENTRY   label main   4 0
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
sub $sp, $sp, 4               
li $t0 1                      #STORE   local 0   None   const 1  
sw $t0 0($sp)                 
L3:                           #LABEL   label L3   None   None  
lw $t0, 0($sp)                
li $t1, 10                    
bgt $t0, $t1, L4              
lw $a0 0($sp)                 #VALOUT   local 0   None   None  
sub $sp, $sp, 4               #CALL   label PrintInt   None   None  
sw $ra 0($sp)                 
jal PrintInt                  
lw $ra 0($sp)                 
add $sp, $sp, 4               
move $t0 $v0                  #LOAD   temp IR5   None   const return  
li $a0 '-'                    #VALOUT   const '-'   None   None  
sub $sp, $sp, 4               #CALL   label PrintChar   None   None  
sw $ra 0($sp)                 
jal PrintChar                 
lw $ra 0($sp)                 
add $sp, $sp, 4               
move $t1 $v0                  #LOAD   temp IR6   None   const return  
lw $t2 0($sp)                 #LOAD   temp IR7   None   local 0  
li $t3, 1                     
add $t2, $t2, $t3             #ADD   temp IR7   temp IR7   const 1  
sw $t2 0($sp)                 #STORE   local 0   None   temp IR7  
j L3                          #JUMP   label L3   None   None  
L4:                           #LABEL   label L4   None   None  
L7:                           #LABEL   label L7   None   None  
lw $a0 0($sp)                 #VALOUT   local 0   None   None  
sub $sp, $sp, 4               #CALL   label PrintInt   None   None  
sw $ra 0($sp)                 
jal PrintInt                  
lw $ra 0($sp)                 
add $sp, $sp, 4               
move $t2 $v0                  #LOAD   temp IR8   None   const return  
li $a0 '-'                    #VALOUT   const '-'   None   None  
sub $sp, $sp, 4               #CALL   label PrintChar   None   None  
sw $ra 0($sp)                 
jal PrintChar                 
lw $ra 0($sp)                 
add $sp, $sp, 4               
move $t3 $v0                  #LOAD   temp IR9   None   const return  
lw $t4, 0($sp)                
li $t5, 0                     
ble $t4, $t5, L8              
j L7                          #JUMP   label L7   None   None  
L8:                           #LABEL   label L8   None   None  
li $v0 0                      #LOAD   return   None   const 0  
add $sp, $sp, 4               
jr $ra                        
add $sp, $sp, 4               
jr $ra                        
