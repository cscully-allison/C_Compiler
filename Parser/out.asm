<<<<<<< HEAD
.text                         \#PROCENTRY   label main   212   0
main:                         
sub $sp, $sp, 212             
li $t0 1                      \#STORE   local 204   None   const 1  
sw $t0 204($sp)               
li $t0 2                      \#STORE   local 208   None   const 2  
sw $t0 208($sp)               
li $t0 0                      \#STORE   local 0   None   const 0  
sw $t0 0($sp)                 
L3:                           \#LABEL   label L3   None   None  
li $t0 0                      \#STORE   local 4   None   const 0  
sw $t0 4($sp)                 
L1:                           \#LABEL   label L1   None   None  
li $t0 4                      \#LOAD   temp IR21   None   const 4  
lw $t2, 0($sp)                \#MULT   temp IR23   temp IR21   local 0  
mult $t0, $t2                 
mflo $t1                      
move $t2 $t1                  \#LOAD   temp IR22   None   temp IR23  
lw $t3, 4($sp)                \#ADD   temp IR25   temp IR22   local 4  
add $t1, $t2, $t3             
mult 4, $t1                   \#MULT   temp IR26   const 4   temp IR25  
mflo $t2                      
lw $t4, 12($sp)               \#ADD   faddr IR24   temp IR26   local 12  
add $t3, $t2, $t4             
lw $t2 204($sp)               \#STORE   faddr IR24   None   local 204  
sw $t2 ($t3)                  
li $t2 4                      \#LOAD   temp IR28   None   const 4  
lw $t5, 0($sp)                \#MULT   temp IR30   temp IR28   local 0  
mult $t2, $t5                 
mflo $t4                      
move $t5 $t4                  \#LOAD   temp IR29   None   temp IR30  
lw $t6, 4($sp)                \#ADD   temp IR32   temp IR29   local 4  
add $t4, $t5, $t6             
mult 4, $t4                   \#MULT   temp IR33   const 4   temp IR32  
mflo $t5                      
lw $t7, 76($sp)               \#ADD   faddr IR31   temp IR33   local 76  
add $t6, $t5, $t7             
lw $t5 208($sp)               \#STORE   faddr IR31   None   local 208  
sw $t5 ($t6)                  
li $t5 4                      \#LOAD   temp IR35   None   const 4  
lw $t8, 0($sp)                \#MULT   temp IR37   temp IR35   local 0  
mult $t5, $t8                 
mflo $t7                      
move $t8 $t7                  \#LOAD   temp IR36   None   temp IR37  
lw $t9, 4($sp)                \#ADD   temp IR39   temp IR36   local 4  
add $t7, $t8, $t9             
mult 4, $t7                   \#MULT   temp IR40   const 4   temp IR39  
mflo $t8                      
lw False, 140($sp)            \#ADD   faddr IR38   temp IR40   local 140  
add $t9, $t8, False           
li $t8 f0.0                   \#STORE   faddr IR38   None   fconst 0.0  
sw $t8 faddr IR38($sp)        
                              \#LOAD   temp IR42   None   local 204  
add $t8, $t8, 1               \#ADD   temp IR42   temp IR42   const 1  
sw $t8 204($sp)               \#STORE   local 204   None   temp IR42  
                              \#LOAD   temp IR43   None   local 208  
add $t8, $t8, 1               \#ADD   temp IR43   temp IR43   const 1  
sw $t8 208($sp)               \#STORE   local 208   None   temp IR43  
                              \#LOAD   temp IR44   None   local 4  
add $t8, $t8, 1               \#ADD   temp IR44   temp IR44   const 1  
sw $t8 4($sp)                 \#STORE   local 4   None   temp IR44  
j L1                          \#JUMP   label L1   None   None  
L2:                           \#LABEL   label L2   None   None  
                              \#LOAD   temp IR45   None   local 0  
add $t8, $t8, 1               \#ADD   temp IR45   temp IR45   const 1  
sw $t8 0($sp)                 \#STORE   local 0   None   temp IR45  
j L3                          \#JUMP   label L3   None   None  
L4:                           \#LABEL   label L4   None   None  
li $t8 0                      \#STORE   local 0   None   const 0  
sw $t8 0($sp)                 
L9:                           \#LABEL   label L9   None   None  
li $t8 0                      \#STORE   local 4   None   const 0  
sw $t8 4($sp)                 
L7:                           \#LABEL   label L7   None   None  
li $t8 0                      \#STORE   local 8   None   const 0  
sw $t8 8($sp)                 
L5:                           \#LABEL   label L5   None   None  
li $t8 4                      \#LOAD   temp IR49   None   const 4  
lw False, 0($sp)              \#MULT   temp IR51   temp IR49   local 0  
mult $t8, False               
mflo False                    
move False False              \#LOAD   temp IR50   None   temp IR51  
lw False, 8($sp)              \#ADD   temp IR53   temp IR50   local 8  
add False, None, False        
mult 4, None                  \#MULT   temp IR54   const 4   temp IR53  
mflo False                    
lw False, 12($sp)             \#ADD   faddr IR52   temp IR54   local 12  
add False, None, False        
li False 4                    \#LOAD   temp IR55   None   const 4  
lw False, 0($sp)              \#MULT   temp IR57   temp IR55   local 0  
mult False, False             
mflo False                    
move False False              \#LOAD   temp IR56   None   temp IR57  
lw False, 4($sp)              \#ADD   temp IR59   temp IR56   local 4  
add False, None, False        
mult 4, None                  \#MULT   temp IR60   const 4   temp IR59  
mflo False                    
lw False, 76($sp)             \#ADD   faddr IR58   temp IR60   local 76  
add False, None, False        
li False 4                    \#LOAD   temp IR61   None   const 4  
lw False, 4($sp)              \#MULT   temp IR63   temp IR61   local 4  
mult False, False             
mflo False                    
move False False              \#LOAD   temp IR62   None   temp IR63  
lw False, 8($sp)              \#ADD   temp IR65   temp IR62   local 8  
add False, None, False        
mult 4, None                  \#MULT   temp IR66   const 4   temp IR65  
mflo False                    
lw False, 140($sp)            \#ADD   faddr IR64   temp IR66   local 140  
add False, None, False        
                              \#LOAD   ftemp FR2   None   faddr IR58  
                              \#LOAD   ftemp FR3   None   faddr IR64  
mult False, None              \#MULT   ftemp FR1   ftemp FR2   ftemp FR3  
mflo False                    
sw False faddr IR52($sp)      \#STORE   faddr IR52   None   ftemp FR1  
                              \#LOAD   temp IR68   None   local 8  
add False, None, 1            \#ADD   temp IR68   temp IR68   const 1  
sw False 8($sp)               \#STORE   local 8   None   temp IR68  
j L5                          \#JUMP   label L5   None   None  
L6:                           \#LABEL   label L6   None   None  
                              \#LOAD   temp IR69   None   local 4  
add False, None, 1            \#ADD   temp IR69   temp IR69   const 1  
sw False 4($sp)               \#STORE   local 4   None   temp IR69  
j L7                          \#JUMP   label L7   None   None  
L8:                           \#LABEL   label L8   None   None  
                              \#LOAD   temp IR70   None   local 0  
add False, None, 1            \#ADD   temp IR70   temp IR70   const 1  
sw False 0($sp)               \#STORE   local 0   None   temp IR70  
j L9                          \#JUMP   label L9   None   None  
L10:                          \#LABEL   label L10   None   None  
li False 0                    \#LOAD   return   None   const 0  
=======
.text
main:
sub $sp, $sp, 20
li $t0 3
sw $t0 4($sp)
lw $t1, 4($sp)
add $t0, $t1, 3
sw $t0 8($sp)
li $t1, 16
lw $t2, 8($sp)
sub $t0, $t1, $t2
sw $t0 12($sp)
li $t1, 5
li $t2, 10
mult $t1, $t2
mflo $t0
sw $t0 16($sp)
lw $t1, 16($sp)
lw $t2, 12($sp)
div $t1, $t2
mflo $t0
sw $t0 4($sp)
>>>>>>> kurt
