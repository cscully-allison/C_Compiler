.text                         #PROCENTRY   label main   68   0
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
sub $sp, $sp, 68              
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
li $t0 2                      #LOAD   temp IR26   None   const 2  
lw $t2, 0($sp)                
mult $t0, $t2                 #MULT   temp IR28   temp IR26   local 0  
mflo $t1                      
move $t0 $t1                  #LOAD   temp IR27   None   temp IR28  
lw $t2, 4($sp)                
add $t1, $t0, $t2             #ADD   temp IR30   temp IR27   local 4  

#      a[i][j] = aval;
      

#      b[i][j] = bval;
      

#      c[i][j] = 0;
         
li $t2, 4                     
mult $t2, $t1                 #MULT   temp IR31   const 4   temp IR30  
mflo $t0                      
la $t2, 12($sp)               
add $t1, $t0, $t2             #ADD   addr IR29   temp IR31   local 12  
lw $t0 60($sp)                #STORE   addr IR29   None   local 60  
sw $t0 ($t1)                  
li $t0 2                      #LOAD   temp IR33   None   const 2  
lw $t3, 0($sp)                
mult $t0, $t3                 #MULT   temp IR35   temp IR33   local 0  
mflo $t2                      
move $t0 $t2                  #LOAD   temp IR34   None   temp IR35  
lw $t3, 4($sp)                
add $t2, $t0, $t3             #ADD   temp IR37   temp IR34   local 4  
li $t3, 4                     
mult $t3, $t2                 #MULT   temp IR38   const 4   temp IR37  
mflo $t0                      
la $t3, 28($sp)               
add $t2, $t0, $t3             #ADD   addr IR36   temp IR38   local 28  

#          c[i][k] += a[i][j] * b[j][k];

lw $t0 64($sp)                #STORE   addr IR36   None   local 64  
sw $t0 ($t2)                  
li $t0 2                      #LOAD   temp IR40   None   const 2  
lw $t4, 0($sp)                
mult $t0, $t4                 #MULT   temp IR42   temp IR40   local 0  
mflo $t3                      
move $t0 $t3                  #LOAD   temp IR41   None   temp IR42  
lw $t4, 4($sp)                
add $t3, $t0, $t4             #ADD   temp IR44   temp IR41   local 4  
li $t4, 4                     
mult $t4, $t3                 #MULT   temp IR45   const 4   temp IR44  
mflo $t0                      
la $t4, 44($sp)               
add $t3, $t0, $t4             #ADD   addr IR43   temp IR45   local 44  
li $t0 0                      #STORE   addr IR43   None   const 0  
sw $t0 ($t3)                  

#      PrintInt(c[i][j]);
   
lw $t0 60($sp)                #LOAD   temp IR47   None   local 60  
li $t4, 1                     
add $t0, $t0, $t4             #ADD   temp IR47   temp IR47   const 1  
sw $t0 60($sp)                #STORE   local 60   None   temp IR47  
lw $t0 64($sp)                #LOAD   temp IR48   None   local 64  
li $t4, 1                     
add $t0, $t0, $t4             #ADD   temp IR48   temp IR48   const 1  
sw $t0 64($sp)                #STORE   local 64   None   temp IR48  
lw $t0 4($sp)                 #LOAD   temp IR49   None   local 4  
li $t4, 1                     
add $t0, $t0, $t4             #ADD   temp IR49   temp IR49   const 1  
sw $t0 4($sp)                 #STORE   local 4   None   temp IR49  
j L1                          #JUMP   label L1   None   None  
L2:                           #LABEL   label L2   None   None  
lw $t0 0($sp)                 #LOAD   temp IR50   None   local 0  
li $t4, 1                     
add $t0, $t0, $t4             #ADD   temp IR50   temp IR50   const 1  
sw $t0 0($sp)                 #STORE   local 0   None   temp IR50  
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
li $t0 2                      #LOAD   temp IR54   None   const 2  
lw $t5, 0($sp)                
mult $t0, $t5                 #MULT   temp IR56   temp IR54   local 0  
mflo $t4                      
move $t0 $t4                  #LOAD   temp IR55   None   temp IR56  
lw $t5, 8($sp)                
add $t4, $t0, $t5             #ADD   temp IR58   temp IR55   local 8  
li $t5, 4                     
mult $t5, $t4                 #MULT   temp IR59   const 4   temp IR58  
mflo $t0                      
la $t5, 44($sp)               
add $t4, $t0, $t5             #ADD   addr IR57   temp IR59   local 44  
li $t0 2                      #LOAD   temp IR60   None   const 2  
lw $t6, 0($sp)                
mult $t0, $t6                 #MULT   temp IR62   temp IR60   local 0  
mflo $t5                      
move $t0 $t5                  #LOAD   temp IR61   None   temp IR62  
lw $t6, 4($sp)                
add $t5, $t0, $t6             #ADD   temp IR64   temp IR61   local 4  
li $t6, 4                     
mult $t6, $t5                 #MULT   temp IR65   const 4   temp IR64  
mflo $t0                      
la $t6, 12($sp)               
add $t5, $t0, $t6             #ADD   addr IR63   temp IR65   local 12  
li $t0 2                      #LOAD   temp IR66   None   const 2  
lw $t7, 4($sp)                
mult $t0, $t7                 #MULT   temp IR68   temp IR66   local 4  
mflo $t6                      
move $t0 $t6                  #LOAD   temp IR67   None   temp IR68  
lw $t7, 8($sp)                
add $t6, $t0, $t7             #ADD   temp IR70   temp IR67   local 8  
li $t7, 4                     
mult $t7, $t6                 #MULT   temp IR71   const 4   temp IR70  
mflo $t0                      
la $t7, 28($sp)               
add $t6, $t0, $t7             #ADD   addr IR69   temp IR71   local 28  
lw $t0 ($t5)                  #LOAD   temp IR72   None   addr IR63  
lw $t7 ($t6)                  #LOAD   temp IR73   None   addr IR69  
mult $t0, $t7                 #MULT   temp IR16   temp IR72   temp IR73  
mflo $t8                      
lw $t0 ($t4)                  #LOAD   temp IR75   None   addr IR57  
add $t7, $t0, $t8             #ADD   temp IR74   temp IR75   temp IR16  
sw $t7 ($t4)                  #STORE   addr IR57   None   temp IR74  
lw $t0 8($sp)                 #LOAD   temp IR76   None   local 8  
li $t7, 1                     
add $t0, $t0, $t7             #ADD   temp IR76   temp IR76   const 1  
sw $t0 8($sp)                 #STORE   local 8   None   temp IR76  
j L5                          #JUMP   label L5   None   None  
L6:                           #LABEL   label L6   None   None  
lw $t0 4($sp)                 #LOAD   temp IR77   None   local 4  
li $t7, 1                     
add $t0, $t0, $t7             #ADD   temp IR77   temp IR77   const 1  
sw $t0 4($sp)                 #STORE   local 4   None   temp IR77  
j L7                          #JUMP   label L7   None   None  
L8:                           #LABEL   label L8   None   None  
lw $t0 0($sp)                 #LOAD   temp IR78   None   local 0  
li $t7, 1                     
add $t0, $t0, $t7             #ADD   temp IR78   temp IR78   const 1  
sw $t0 0($sp)                 #STORE   local 0   None   temp IR78  
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
lw $t0 0($sp)                 #LOAD   temp IR83   None   local 0  
li $t8, 4                     
mult $t8, $t0                 #MULT   temp IR84   const 4   temp IR83  
mflo $t7                      
la $t8, 44($sp)               
add $t0, $t7, $t8             #ADD   addr IR82   temp IR84   local 44  
lw $a0 4($sp)                 #VALOUT   local 4   None   None  
sub $sp, $sp, 4               #CALL   label PrintInt   None   None  
sw $ra 0($sp)                 
jal PrintInt                  
lw $ra 0($sp)                 
add $sp, $sp, 4               
move $t7 $v0                  #LOAD   temp IR81   None   const return  
lw $t8 4($sp)                 #LOAD   temp IR85   None   local 4  
li $t9, 1                     
add $t8, $t8, $t9             #ADD   temp IR85   temp IR85   const 1  
sw $t8 4($sp)                 #STORE   local 4   None   temp IR85  
j L12                         #JUMP   label L12   None   None  
L13:                          #LABEL   label L13   None   None  
lw $t8 0($sp)                 #LOAD   temp IR86   None   local 0  
li $t9, 1                     
add $t8, $t8, $t9             #ADD   temp IR86   temp IR86   const 1  
sw $t8 0($sp)                 #STORE   local 0   None   temp IR86  
j L14                         #JUMP   label L14   None   None  
L15:                          #LABEL   label L15   None   None  
li $v0 0                      #LOAD   return   None   const 0  
add $sp, $sp, 68              
jr $ra                        
add $sp, $sp, 68              
jr $ra                        
