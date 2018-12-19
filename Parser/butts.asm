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
la $t2, 12($sp)               
add $t1, $t0, $t2             #ADD   addr IR30   temp IR32   local 12  

#      a[i][j] = 3;
         
li $t0 3                      #STORE   addr IR30   None   const 3  
sw $t0 ($t1)                  

#      b[i][j] = 2;
         
li $t0 2                      #LOAD   temp IR34   None   const 2  

#      c[i][j] = 0;
         
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

#          c[i][k] += a[i][j] * b[j][k];

li $t0 2                      #LOAD   temp IR41   None   const 2  
lw $t4, 0($sp)                
mult $t0, $t4                 #MULT   temp IR43   temp IR41   local 0  
mflo $t3                      
move $t0 $t3                  #LOAD   temp IR42   None   temp IR43  
lw $t4, 4($sp)                
add $t3, $t0, $t4             #ADD   temp IR45   temp IR42   local 4  
li $t4, 4                     
mult $t4, $t3                 #MULT   temp IR46   const 4   temp IR45  
mflo $t0                      
la $t4, 44($sp)               
add $t3, $t0, $t4             #ADD   addr IR44   temp IR46   local 44  

#      out = c[i][j];
       
li $t0 0                      #STORE   addr IR44   None   const 0  
sw $t0 ($t3)                  
lw $t0 4($sp)                 #LOAD   temp IR48   None   local 4  
li $t4, 1                     
add $t0, $t0, $t4             #ADD   temp IR48   temp IR48   const 1  
sw $t0 4($sp)                 #STORE   local 4   None   temp IR48  
j L1                          #JUMP   label L1   None   None  
L2:                           #LABEL   label L2   None   None  
lw $t0 0($sp)                 #LOAD   temp IR49   None   local 0  
li $t4, 1                     
add $t0, $t0, $t4             #ADD   temp IR49   temp IR49   const 1  
sw $t0 0($sp)                 #STORE   local 0   None   temp IR49  
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
li $t0 2                      #LOAD   temp IR53   None   const 2  
lw $t5, 0($sp)                
mult $t0, $t5                 #MULT   temp IR55   temp IR53   local 0  
mflo $t4                      
move $t0 $t4                  #LOAD   temp IR54   None   temp IR55  
lw $t5, 8($sp)                
add $t4, $t0, $t5             #ADD   temp IR57   temp IR54   local 8  
li $t5, 4                     
mult $t5, $t4                 #MULT   temp IR58   const 4   temp IR57  
mflo $t0                      
la $t5, 44($sp)               
add $t4, $t0, $t5             #ADD   addr IR56   temp IR58   local 44  
li $t0 2                      #LOAD   temp IR59   None   const 2  
lw $t6, 0($sp)                
mult $t0, $t6                 #MULT   temp IR61   temp IR59   local 0  
mflo $t5                      
move $t0 $t5                  #LOAD   temp IR60   None   temp IR61  
lw $t6, 4($sp)                
add $t5, $t0, $t6             #ADD   temp IR63   temp IR60   local 4  
li $t6, 4                     
mult $t6, $t5                 #MULT   temp IR64   const 4   temp IR63  
mflo $t0                      
la $t6, 12($sp)               
add $t5, $t0, $t6             #ADD   addr IR62   temp IR64   local 12  
li $t0 2                      #LOAD   temp IR65   None   const 2  
lw $t7, 4($sp)                
mult $t0, $t7                 #MULT   temp IR67   temp IR65   local 4  
mflo $t6                      
move $t0 $t6                  #LOAD   temp IR66   None   temp IR67  
lw $t7, 8($sp)                
add $t6, $t0, $t7             #ADD   temp IR69   temp IR66   local 8  
li $t7, 4                     
mult $t7, $t6                 #MULT   temp IR70   const 4   temp IR69  
mflo $t0                      
la $t7, 28($sp)               
add $t6, $t0, $t7             #ADD   addr IR68   temp IR70   local 28  
lw $t0 ($t5)                  #LOAD   temp IR71   None   addr IR62  
lw $t7 ($t6)                  #LOAD   temp IR72   None   addr IR68  
mult $t0, $t7                 #MULT   temp IR16   temp IR71   temp IR72  
mflo $t8                      
lw $t0 ($t4)                  #LOAD   temp IR74   None   addr IR56  
add $t7, $t0, $t8             #ADD   temp IR73   temp IR74   temp IR16  
sw $t7 ($t4)                  #STORE   addr IR56   None   temp IR73  
lw $t0 8($sp)                 #LOAD   temp IR75   None   local 8  
li $t7, 1                     
add $t0, $t0, $t7             #ADD   temp IR75   temp IR75   const 1  
sw $t0 8($sp)                 #STORE   local 8   None   temp IR75  
j L5                          #JUMP   label L5   None   None  
L6:                           #LABEL   label L6   None   None  
lw $t0 4($sp)                 #LOAD   temp IR76   None   local 4  
li $t7, 1                     
add $t0, $t0, $t7             #ADD   temp IR76   temp IR76   const 1  
sw $t0 4($sp)                 #STORE   local 4   None   temp IR76  
j L7                          #JUMP   label L7   None   None  
L8:                           #LABEL   label L8   None   None  
lw $t0 0($sp)                 #LOAD   temp IR77   None   local 0  
li $t7, 1                     
add $t0, $t0, $t7             #ADD   temp IR77   temp IR77   const 1  
sw $t0 0($sp)                 #STORE   local 0   None   temp IR77  
j L9                          #JUMP   label L9   None   None  
L10:                          #LABEL   label L10   None   None  
li $t0 0                      #STORE   local 0   None   const 0  
sw $t0 0($sp)                 
L15:                          #LABEL   label L15   None   None  
lw $t0, 0($sp)                
li $t7, 2                     
bge $t0, $t7, L16             
li $t0 0                      #STORE   local 4   None   const 0  
sw $t0 4($sp)                 
L13:                          #LABEL   label L13   None   None  
lw $t0, 4($sp)                
li $t7, 2                     
bge $t0, $t7, L14             
li $t0 2                      #LOAD   temp IR80   None   const 2  
lw $t8, 0($sp)                
mult $t0, $t8                 #MULT   temp IR82   temp IR80   local 0  
mflo $t7                      
move $t0 $t7                  #LOAD   temp IR81   None   temp IR82  
lw $t8, 4($sp)                
add $t7, $t0, $t8             #ADD   temp IR84   temp IR81   local 4  
li $t8, 4                     
mult $t8, $t7                 #MULT   temp IR85   const 4   temp IR84  
mflo $t0                      
la $t8, 44($sp)               
add $t7, $t0, $t8             #ADD   addr IR83   temp IR85   local 44  
lw $t7 ($t7)                  #STORE   local 68   None   addr IR83  
sw $t7 68($sp)                
lw $a0 68($sp)                #VALOUT   local 68   None   None  
sub $sp, $sp, 4               #CALL   label PrintInt   None   None  
sw $ra 0($sp)                 
jal PrintInt                  
lw $ra 0($sp)                 
add $sp, $sp, 4               
move $t0 $v0                  #LOAD   temp IR87   None   const return  
li $a0 '-'                    #VALOUT   const '-'   None   None  
sub $sp, $sp, 4               #CALL   label PrintChar   None   None  
sw $ra 0($sp)                 
jal PrintChar                 
lw $ra 0($sp)                 
add $sp, $sp, 4               
move $t7 $v0                  #LOAD   temp IR88   None   const return  
lw $t8 4($sp)                 #LOAD   temp IR89   None   local 4  
li $t9, 1                     
add $t8, $t8, $t9             #ADD   temp IR89   temp IR89   const 1  
sw $t8 4($sp)                 #STORE   local 4   None   temp IR89  
j L13                         #JUMP   label L13   None   None  
L14:                          #LABEL   label L14   None   None  
lw $t8 0($sp)                 #LOAD   temp IR90   None   local 0  
li $t9, 1                     
add $t8, $t8, $t9             #ADD   temp IR90   temp IR90   const 1  
sw $t8 0($sp)                 #STORE   local 0   None   temp IR90  
j L15                         #JUMP   label L15   None   None  
L16:                          #LABEL   label L16   None   None  
li $v0 0                      #LOAD   return   None   const 0  
add $sp, $sp, 72              
jr $ra                        
add $sp, $sp, 72              
jr $ra                        
