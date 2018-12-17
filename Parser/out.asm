.text                         #PROCENTRY   label main   52   0
main:                         
sub $sp, $sp, 52              
li $t0 0                      #STORE   local 0   None   const 0  
sw $t0 0($sp)                 
L1:                           #LABEL   label L1   None   None  
lw $t0, 0($sp)                
li $t1, 10                    
bge $t0, $t1, L2              
lw $t0 0($sp)                 #LOAD   temp IR18   None   local 0  
li $t2, 4                     
mult $t2, $t0                 #MULT   temp IR19   const 4   temp IR18  
mflo $t1                      
lw $t2, 8($sp)                #ADD   addr IR17   temp IR19   local 8  
add $t0, $t1, $t2             
li $t2, 10                    
lw $t3, 0($sp)                #SUB   temp IR3   const 10   local 0  
sub $t1, $t2, $t3             

#		vals[a] = 10 - a;
        
sw $t1 addr IR17($sp)         #STORE   addr IR17   None   temp IR3  
lw $t1 0($sp)                 #LOAD   temp IR21   None   local 0  
li $t2, 1                     
add $t1, $t1, $t2             #ADD   temp IR21   temp IR21   const 1  
sw $t1 0($sp)                 #STORE   local 0   None   temp IR21  
j L1                          #JUMP   label L1   None   None  
L2:                           #LABEL   label L2   None   None  
li $t1 0                      #STORE   local 0   None   const 0  
sw $t1 0($sp)                 
L7:                           #LABEL   label L7   None   None  

#			if (vals[b] > vals[b + 1])

lw $t1, 0($sp)                
li $t2, 10                    
bge $t1, $t2, L8              
li $t1 0                      #STORE   local 4   None   const 0  
sw $t1 4($sp)                 

#				c = vals[b];
           

#				vals[b] = vals[b + 1];
 

#				vals[b + 1]= c;
        
L5:                           #LABEL   label L5   None   None  
lw $t1, 4($sp)                
li $t2, 9                     
bge $t1, $t2, L6              
lw $t1 4($sp)                 #LOAD   temp IR25   None   local 4  
li $t3, 4                     
mult $t3, $t1                 #MULT   temp IR26   const 4   temp IR25  
mflo $t2                      
lw $t3, 8($sp)                #ADD   addr IR24   temp IR26   local 8  
add $t1, $t2, $t3             
                              #LOAD   temp IR28   None    
li $t3, 4                     
mult $t3, None                #MULT   temp IR29   const 4   temp IR28  
mflo $t2                      
lw $t4, 8($sp)                #ADD   addr IR27   temp IR29   local 8  
add $t3, $t2, $t4             
lw {} {}({})                  #LOAD   temp IR30   None   addr IR24  
lw {} {}({})                  #LOAD   temp IR31   None   addr IR27  
ble $t2, $t4, L3              
lw $t2 4($sp)                 #LOAD   temp IR33   None   local 4  
li $t5, 4                     
mult $t5, $t2                 #MULT   temp IR34   const 4   temp IR33  
mflo $t4                      
lw $t5, 8($sp)                #ADD   addr IR32   temp IR34   local 8  
add $t2, $t4, $t5             
sw  48($sp)                   #STORE   local 48   None   addr IR32  
lw $t4 4($sp)                 #LOAD   temp IR37   None   local 4  
li $t6, 4                     
mult $t6, $t4                 #MULT   temp IR38   const 4   temp IR37  
mflo $t5                      
lw $t6, 8($sp)                #ADD   addr IR36   temp IR38   local 8  
add $t4, $t5, $t6             
                              #LOAD   temp IR40   None    
li $t6, 4                     
mult $t6, None                #MULT   temp IR41   const 4   temp IR40  
mflo $t5                      
lw $t7, 8($sp)                #ADD   addr IR39   temp IR41   local 8  
add $t6, $t5, $t7             
sw  addr IR36($sp)            #STORE   addr IR36   None   addr IR39  
                              #LOAD   temp IR44   None    
li $t7, 4                     
mult $t7, None                #MULT   temp IR45   const 4   temp IR44  
mflo $t5                      
lw $t8, 8($sp)                #ADD   addr IR43   temp IR45   local 8  
add $t7, $t5, $t8             
lw $t5 48($sp)                #STORE   addr IR43   None   local 48  
sw $t5 ($t7)                  
j L4                          #JUMP   label L4   None   None  
L3:                           #LABEL   label L3   None   None  
L4:                           #LABEL   label L4   None   None  
lw $t5 4($sp)                 #LOAD   temp IR47   None   local 4  
li $t8, 1                     
add $t5, $t5, $t8             #ADD   temp IR47   temp IR47   const 1  
sw $t5 4($sp)                 #STORE   local 4   None   temp IR47  
j L5                          #JUMP   label L5   None   None  
L6:                           #LABEL   label L6   None   None  
lw $t5 0($sp)                 #LOAD   temp IR48   None   local 0  
li $t8, 1                     
add $t5, $t5, $t8             #ADD   temp IR48   temp IR48   const 1  
sw $t5 0($sp)                 #STORE   local 0   None   temp IR48  
j L7                          #JUMP   label L7   None   None  
L8:                           #LABEL   label L8   None   None  
