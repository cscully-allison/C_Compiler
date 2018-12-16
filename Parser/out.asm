.text
main:
sub $sp, $sp, 20
mult 4, None
mflo $t0
lw $t2, 4($sp)
add $t1, $t0, $t2
li $t2 5
sw $t2 addr IR5($sp)
mult 4, None
mflo $t2
lw $t4, 4($sp)
add $t3, $t2, $t4
li $t4 8
sw $t4 addr IR9($sp)
mult 4, None
mflo $t4
lw $t6, 4($sp)
add $t5, $t4, $t6
mult 4, None
mflo $t6
lw $t8, 4($sp)
add $t7, $t6, $t8
mult 4, None
mflo $t8
lw False, 4($sp)
add $t9, $t8, False
add False, None, None
sw False addr IR13($sp)
