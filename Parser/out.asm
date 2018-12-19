.text                         #PROCENTRY   label main   160   4
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
