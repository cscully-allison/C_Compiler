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
