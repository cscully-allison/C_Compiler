.data                         #GLOBAL   label var0   4 None  
var0: .word                   
.text                         #PROCENTRY   label main   8 8
main:                         
sub $sp, $sp, 16              
li $t0 0                      #LOAD   temp IR4   None   const 0  
li $t2, 4                     
mult $t2, $t0                 #MULT   temp IR5   const 4   temp IR4  
mflo $t1                      

#  var2[0] = 9;
             

#  var2[1] = 10;
            
la $t2, 8($sp)                
add $t0, $t1, $t2             #ADD   addr IR3   temp IR5   local 8  
li $t1 9                      #STORE   addr IR3   None   const 9  
sw $t1 ($t0)                  
li $t1 1                      #LOAD   temp IR8   None   const 1  
li $t3, 4                     
mult $t3, $t1                 #MULT   temp IR9   const 4   temp IR8  
mflo $t2                      
la $t3, 8($sp)                
add $t1, $t2, $t3             #ADD   addr IR7   temp IR9   local 8  
li $t2 10                     #STORE   addr IR7   None   const 10  
sw $t2 ($t1)                  
