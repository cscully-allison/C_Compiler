.data                         #GLOBAL   label var0   4 None  
var0: .word                   
.text                         #PROCENTRY   label main   8 8
main:                         
sub $sp, $sp, 16              
li $t0 0                      #LOAD   temp IR5   None   const 0  
li $t2, 4                     
mult $t2, $t0                 #MULT   temp IR6   const 4   temp IR5  
mflo $t1                      

#  var2[0] = 9;
             

#  var2[1] = 10;
            

#  var2[2] = 11;
            
lw $t2, 8($sp)                
add $t0, $t1, $t2             #ADD   addr IR4   temp IR6   local 8  
li $t1 9                      #STORE   addr IR4   None   const 9  
sw $t1 ($t0)                  
li $t1 1                      #LOAD   temp IR9   None   const 1  
li $t3, 4                     
mult $t3, $t1                 #MULT   temp IR10   const 4   temp IR9  
mflo $t2                      
lw $t3, 8($sp)                
add $t1, $t2, $t3             #ADD   addr IR8   temp IR10   local 8  
li $t2 10                     #STORE   addr IR8   None   const 10  
sw $t2 ($t1)                  
li $t2 2                      #LOAD   temp IR13   None   const 2  
li $t4, 4                     
mult $t4, $t2                 #MULT   temp IR14   const 4   temp IR13  
mflo $t3                      
lw $t4, 8($sp)                
add $t2, $t3, $t4             #ADD   addr IR12   temp IR14   local 8  
li $t3 11                     #STORE   addr IR12   None   const 11  
sw $t3 ($t2)                  
