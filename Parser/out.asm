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
li $t0 3                      #LOAD   temp IR5   None   const 3  
li $t2, 4                     
mult $t2, $t0                 #MULT   temp IR6   const 4   temp IR5  
mflo $t1                      
la $t2, 4($sp)                
add $t0, $t1, $t2             #ADD   addr IR4   temp IR6   local 4  

#	arr1[3]=3;
                

#	arr2[3][6] = arr1[3];
     

#	arr1[2] = arr2[3][6];
     
li $t1 3                      #STORE   addr IR4   None   const 3  
sw $t1 ($t0)                  
li $t1 7                      #LOAD   temp IR8   None   const 7  
li $t3, 3                     
mult $t1, $t3                 #MULT   temp IR10   temp IR8   const 3  
mflo $t2                      
move $t1 $t2                  #LOAD   temp IR9   None   temp IR10  
li $t3, 6                     
add $t2, $t1, $t3             #ADD   temp IR12   temp IR9   const 6  
li $t3, 4                     
mult $t3, $t2                 #MULT   temp IR13   const 4   temp IR12  
mflo $t1                      
la $t3, 24($sp)               
add $t2, $t1, $t3             #ADD   addr IR11   temp IR13   local 24  
li $t1 3                      #LOAD   temp IR15   None   const 3  
li $t4, 4                     
mult $t4, $t1                 #MULT   temp IR16   const 4   temp IR15  
mflo $t3                      
la $t4, 4($sp)                
add $t1, $t3, $t4             #ADD   addr IR14   temp IR16   local 4  
lw $t1 ($t1)                  #STORE   addr IR11   None   addr IR14  
sw $t1 ($t2)                  
li $t1 2                      #LOAD   temp IR19   None   const 2  
li $t4, 4                     
mult $t4, $t1                 #MULT   temp IR20   const 4   temp IR19  
mflo $t3                      
la $t4, 4($sp)                
add $t1, $t3, $t4             #ADD   addr IR18   temp IR20   local 4  
li $t3 7                      #LOAD   temp IR21   None   const 7  
li $t5, 3                     
mult $t3, $t5                 #MULT   temp IR23   temp IR21   const 3  
mflo $t4                      
move $t3 $t4                  #LOAD   temp IR22   None   temp IR23  
li $t5, 6                     
add $t4, $t3, $t5             #ADD   temp IR25   temp IR22   const 6  
li $t5, 4                     
mult $t5, $t4                 #MULT   temp IR26   const 4   temp IR25  
mflo $t3                      
la $t5, 24($sp)               
add $t4, $t3, $t5             #ADD   addr IR24   temp IR26   local 24  
lw $t4 ($t4)                  #STORE   addr IR18   None   addr IR24  
sw $t4 ($t1)                  
add $sp, $sp, 164             
jr $ra                        
