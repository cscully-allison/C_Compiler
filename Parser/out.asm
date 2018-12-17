.data                         #GLOBAL   label var0   4 None  
var0: .word                   
.text                         #PROCENTRY   label main   8 8
main:                         
sub $sp, $sp, 16              
li $t0 1                      #LOAD   temp IR3   None   const 1  
li $t2, 4                     
mult $t2, $t0                 #MULT   temp IR4   const 4   temp IR3  
mflo $t1                      

#  var2[1] = 10;
            
lw $t2, 8($sp)                #ADD   addr IR2   temp IR4   local 8  
add $t0, $t1, $t2             
li $t1 10                     #STORE   addr IR2   None   const 10  
sw $t1 ($t0)                  
