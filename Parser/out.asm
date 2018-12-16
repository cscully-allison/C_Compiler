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
lw $t2, 0($sp)
mult $t1, $t2
mflo $t0
lw $t3, 4($sp)
add $t2, None, $t3
mult 4, $t2
mflo $t3
lw $t5, 12($sp)
add $t4, $t3, $t5
sw  faddr IR24($sp)
lw $t7, 0($sp)
mult $t6, $t7
mflo $t5
lw $t8, 4($sp)
add $t7, None, $t8
mult 4, $t7
mflo $t8
lw False, 76($sp)
add $t9, $t8, False
sw  faddr IR31($sp)
lw False, 0($sp)
mult False, False
mflo False
lw False, 4($sp)
add False, None, False
mult 4, None
mflo False
lw False, 140($sp)
add False, None, False
li False f0.0
sw False faddr IR38($sp)
add False, None, 1
sw  204($sp)
add False, None, 1
sw  208($sp)
add False, None, 1
sw  4($sp)
j L1
L2:
add False, None, 1
sw  0($sp)
j L3
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
mult False, False
mflo False
lw False, 8($sp)
add False, None, False
mult 4, None
mflo False
lw False, 12($sp)
add False, None, False
lw False, 0($sp)
mult False, False
mflo False
lw False, 4($sp)
add False, None, False
mult 4, None
mflo False
lw False, 76($sp)
add False, None, False
lw False, 4($sp)
mult False, False
mflo False
lw False, 8($sp)
add False, None, False
mult 4, None
mflo False
lw False, 140($sp)
add False, None, False
mult False, None
mflo False
sw False faddr IR52($sp)
add False, None, 1
sw  8($sp)
j L5
L6:
add False, None, 1
sw  4($sp)
j L7
L8:
add False, None, 1
sw  0($sp)
j L9
L10:
