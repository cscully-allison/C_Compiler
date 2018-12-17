.text                         #PROCENTRY   label main   16   4
main:                         
sub $sp, $sp, 20              
li $t1, 2                     
li $t2, 1                     
div $t1, $t2                  #DIV   temp IR1   const 2   const 1  
mflo $t0                      
sw $t0 4($sp)                 #STORE   local 4   None   temp IR1  
lw $t1, 4($sp)                
li $t2, 1                     
div $t1, $t2                  #DIV   temp IR3   local 4   const 1  
mflo $t0                      
sw $t0 8($sp)                 #STORE   local 8   None   temp IR3  
li $t1, 3                     
lw $t2, 8($sp)                
div $t1, $t2                  #DIV   temp IR5   const 3   local 8  
mflo $t0                      
sw $t0 12($sp)                #STORE   local 12   None   temp IR5  
lw $t1, 12($sp)               
lw $t2, 8($sp)                
div $t1, $t2                  #DIV   temp IR7   local 12   local 8  
mflo $t0                      
sw $t0 16($sp)                #STORE   local 16   None   temp IR7  
