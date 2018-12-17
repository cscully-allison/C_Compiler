.text                         #PROCENTRY   label main   68   0
main:                         
sub $sp, $sp, 68              
li $t0 1                      #STORE   local 60   None   const 1  
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
li $t0 2                      #LOAD   temp IR22   None   const 2  
lw $t2, 0($sp)                
mult $t0, $t2                 #MULT   temp IR24   temp IR22   local 0  
mflo $t1                      
move $t0 $t1                  #LOAD   temp IR23   None   temp IR24  

#      a[i][j] = aval;
      

#      b[i][j] = bval;
      

#      c[i][j] = 0;
         
lw $t2, 4($sp)                
add $t1, $t0, $t2             #ADD   temp IR26   temp IR23   local 4  
li $t2, 4                     
mult $t2, $t1                 #MULT   temp IR27   const 4   temp IR26  
mflo $t0                      
la $t2, 12($sp)               
add $t1, $t0, $t2             #ADD   addr IR25   temp IR27   local 12  
lw $t0 60($sp)                #STORE   addr IR25   None   local 60  
sw $t0 ($t1)                  
li $t0 2                      #LOAD   temp IR29   None   const 2  
lw $t3, 0($sp)                
mult $t0, $t3                 #MULT   temp IR31   temp IR29   local 0  
mflo $t2                      
move $t0 $t2                  #LOAD   temp IR30   None   temp IR31  
lw $t3, 4($sp)                
add $t2, $t0, $t3             #ADD   temp IR33   temp IR30   local 4  
li $t3, 4                     
mult $t3, $t2                 #MULT   temp IR34   const 4   temp IR33  
mflo $t0                      

#          c[i][k] += a[i][j] * b[j][k];

la $t3, 28($sp)               
add $t2, $t0, $t3             #ADD   addr IR32   temp IR34   local 28  
lw $t0 64($sp)                #STORE   addr IR32   None   local 64  
sw $t0 ($t2)                  
li $t0 2                      #LOAD   temp IR36   None   const 2  
lw $t4, 0($sp)                
mult $t0, $t4                 #MULT   temp IR38   temp IR36   local 0  
mflo $t3                      
move $t0 $t3                  #LOAD   temp IR37   None   temp IR38  
lw $t4, 4($sp)                
add $t3, $t0, $t4             #ADD   temp IR40   temp IR37   local 4  
li $t4, 4                     
mult $t4, $t3                 #MULT   temp IR41   const 4   temp IR40  
mflo $t0                      
la $t4, 44($sp)               
add $t3, $t0, $t4             #ADD   addr IR39   temp IR41   local 44  
li $t0 0                      #STORE   addr IR39   None   const 0  
sw $t0 ($t3)                  
lw $t0 60($sp)                #LOAD   temp IR43   None   local 60  
li $t4, 1                     
add $t0, $t0, $t4             #ADD   temp IR43   temp IR43   const 1  
sw $t0 60($sp)                #STORE   local 60   None   temp IR43  
lw $t0 64($sp)                #LOAD   temp IR44   None   local 64  
li $t4, 1                     
add $t0, $t0, $t4             #ADD   temp IR44   temp IR44   const 1  
sw $t0 64($sp)                #STORE   local 64   None   temp IR44  
lw $t0 4($sp)                 #LOAD   temp IR45   None   local 4  
li $t4, 1                     
add $t0, $t0, $t4             #ADD   temp IR45   temp IR45   const 1  
sw $t0 4($sp)                 #STORE   local 4   None   temp IR45  
j L1                          #JUMP   label L1   None   None  
L2:                           #LABEL   label L2   None   None  
lw $t0 0($sp)                 #LOAD   temp IR46   None   local 0  
li $t4, 1                     
add $t0, $t0, $t4             #ADD   temp IR46   temp IR46   const 1  
sw $t0 0($sp)                 #STORE   local 0   None   temp IR46  
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
li $t0 2                      #LOAD   temp IR50   None   const 2  
lw $t5, 0($sp)                
mult $t0, $t5                 #MULT   temp IR52   temp IR50   local 0  
mflo $t4                      
move $t0 $t4                  #LOAD   temp IR51   None   temp IR52  
lw $t5, 8($sp)                
add $t4, $t0, $t5             #ADD   temp IR54   temp IR51   local 8  
li $t5, 4                     
mult $t5, $t4                 #MULT   temp IR55   const 4   temp IR54  
mflo $t0                      
la $t5, 44($sp)               
add $t4, $t0, $t5             #ADD   addr IR53   temp IR55   local 44  
li $t0 2                      #LOAD   temp IR56   None   const 2  
lw $t6, 0($sp)                
mult $t0, $t6                 #MULT   temp IR58   temp IR56   local 0  
mflo $t5                      
move $t0 $t5                  #LOAD   temp IR57   None   temp IR58  
lw $t6, 4($sp)                
add $t5, $t0, $t6             #ADD   temp IR60   temp IR57   local 4  
li $t6, 4                     
mult $t6, $t5                 #MULT   temp IR61   const 4   temp IR60  
mflo $t0                      
la $t6, 12($sp)               
add $t5, $t0, $t6             #ADD   addr IR59   temp IR61   local 12  
li $t0 2                      #LOAD   temp IR62   None   const 2  
lw $t7, 4($sp)                
mult $t0, $t7                 #MULT   temp IR64   temp IR62   local 4  
mflo $t6                      
move $t0 $t6                  #LOAD   temp IR63   None   temp IR64  
lw $t7, 8($sp)                
add $t6, $t0, $t7             #ADD   temp IR66   temp IR63   local 8  
li $t7, 4                     
mult $t7, $t6                 #MULT   temp IR67   const 4   temp IR66  
mflo $t0                      
la $t7, 28($sp)               
add $t6, $t0, $t7             #ADD   addr IR65   temp IR67   local 28  
lw $t0 ($t5)                  #LOAD   temp IR68   None   addr IR59  
lw $t7 ($t6)                  #LOAD   temp IR69   None   addr IR65  
mult $t0, $t7                 #MULT   temp IR16   temp IR68   temp IR69  
mflo $t8                      
add $t0, $t4, $t8             #ADD   temp IR70   addr IR53   temp IR16  
sw $t0 ($t4)                  #STORE   addr IR53   None   temp IR70  
lw $t0 8($sp)                 #LOAD   temp IR71   None   local 8  
li $t7, 1                     
add $t0, $t0, $t7             #ADD   temp IR71   temp IR71   const 1  
sw $t0 8($sp)                 #STORE   local 8   None   temp IR71  
j L5                          #JUMP   label L5   None   None  
L6:                           #LABEL   label L6   None   None  
lw $t0 4($sp)                 #LOAD   temp IR72   None   local 4  
li $t7, 1                     
add $t0, $t0, $t7             #ADD   temp IR72   temp IR72   const 1  
sw $t0 4($sp)                 #STORE   local 4   None   temp IR72  
j L7                          #JUMP   label L7   None   None  
L8:                           #LABEL   label L8   None   None  
lw $t0 0($sp)                 #LOAD   temp IR73   None   local 0  
li $t7, 1                     
add $t0, $t0, $t7             #ADD   temp IR73   temp IR73   const 1  
sw $t0 0($sp)                 #STORE   local 0   None   temp IR73  
j L9                          #JUMP   label L9   None   None  
L10:                          #LABEL   label L10   None   None  
li $t0 0                      #LOAD   return   None   const 0  

	li $v0, 5
	syscall
	move $v1, $v0