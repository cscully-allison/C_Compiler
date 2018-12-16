.text
main:
sub $sp, $sp, 212
li $t0 1
sw $t0 204($sp)
li $t0 2
sw $t0 208($sp)
li $t0 0
sw $t0 0($sp)
L3:
li $t0 0
sw $t0 4($sp)
L1:
lw $t1, 0($sp)
mult None, $t1
mflo $t0
lw $t2, 4($sp)
add $t1, None, $t2
li $t3, 4
mult $t3, $t1
mflo $t2
lw $t3, 12($sp)
add $t1, $t2, $t3
sw  faddr IR24($sp)
lw $t4, 0($sp)
mult None, $t4
mflo $t3
lw $t5, 4($sp)
add $t4, None, $t5
li $t6, 4
mult $t6, $t4
mflo $t5
lw $t6, 76($sp)
add $t4, $t5, $t6
sw  faddr IR31($sp)
lw $t7, 0($sp)
mult None, $t7
mflo $t6
lw $t8, 4($sp)
add $t7, None, $t8
li $t9, 4
mult $t9, $t7
mflo $t8
lw $t9, 140($sp)
add $t7, $t8, $t9
li $t9 f0.0
sw $t9 faddr IR38($sp)
add $t9, $t9, 1
sw  204($sp)
add False, None, 1
sw  208($sp)
add False, None, 1
sw  4($sp)
L2:
add False, None, 1
sw  0($sp)
L4:
li False 0
sw False 0($sp)
L9:
li False 0
sw False 4($sp)
L7:
li False 0
sw False 8($sp)
L5:
lw False, 0($sp)
mult None, False
mflo False
lw False, 8($sp)
add False, None, False
li False, 4
mult False, None
mflo False
lw False, 12($sp)
add False, None, False
lw False, 0($sp)
mult None, False
mflo False
lw False, 4($sp)
add False, None, False
li False, 4
mult False, None
mflo False
lw False, 76($sp)
add False, None, False
lw False, 4($sp)
mult None, False
mflo False
lw False, 8($sp)
add False, None, False
li False, 4
mult False, None
mflo False
lw False, 140($sp)
add False, None, False
mult None, None
mflo False
sw False faddr IR52($sp)
add False, None, 1
sw  8($sp)
L6:
add False, None, 1
sw  4($sp)
L8:
add False, None, 1
sw  0($sp)
L10:
