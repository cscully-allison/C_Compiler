.text                         #PROCENTRY   label main   212   0
main:                         
sub $sp, $sp, 212             
li $t0 1                      #STORE   local 204   None   const 1  
sw $t0 204($sp)               
li $t0 2                      #STORE   local 208   None   const 2  
sw $t0 208($sp)               
li $t0 0                      #STORE   local 0   None   const 0  
sw $t0 0($sp)                 
L3:                           #LABEL   label L3   None   None  
li $t0 0                      #STORE   local 4   None   const 0  
sw $t0 4($sp)                 
L1:                           #LABEL   label L1   None   None  
li $t0 4                      #LOAD   temp IR21   None   const 4  
lw $t2, 0($sp)                #MULT   temp IR23   temp IR21   local 0  
mult $t0, $t2                 
mflo $t1                      
move $t2 $t1                  #LOAD   temp IR22   None   temp IR23  
lw $t3, 4($sp)                #ADD   temp IR25   temp IR22   local 4  
add $t1, $t2, $t3             
mult 4, $t1                   #MULT   temp IR26   const 4   temp IR25  
mflo $t2                      
lw $t4, 12($sp)               #ADD   faddr IR24   temp IR26   local 12  
add $t3, $t2, $t4             
lw $t2 204($sp)               #STORE   faddr IR24   None   local 204  
sw $t2 ($t3)                  
li $t2 4                      #LOAD   temp IR28   None   const 4  
lw $t5, 0($sp)                #MULT   temp IR30   temp IR28   local 0  
mult $t2, $t5                 
mflo $t4                      
move $t5 $t4                  #LOAD   temp IR29   None   temp IR30  
lw $t6, 4($sp)                #ADD   temp IR32   temp IR29   local 4  
add $t4, $t5, $t6             
mult 4, $t4                   #MULT   temp IR33   const 4   temp IR32  
mflo $t5                      
lw $t7, 76($sp)               #ADD   faddr IR31   temp IR33   local 76  
add $t6, $t5, $t7             
lw $t5 208($sp)               #STORE   faddr IR31   None   local 208  
sw $t5 ($t6)                  
li $t5 4                      #LOAD   temp IR35   None   const 4  
lw $t8, 0($sp)                #MULT   temp IR37   temp IR35   local 0  
mult $t5, $t8                 
mflo $t7                      
move $t8 $t7                  #LOAD   temp IR36   None   temp IR37  
lw $t9, 4($sp)                #ADD   temp IR39   temp IR36   local 4  
add $t7, $t8, $t9             
mult 4, $t7                   #MULT   temp IR40   const 4   temp IR39  
mflo $t8                      