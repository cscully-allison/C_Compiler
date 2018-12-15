.text
main:
sub $sp, $sp, 8
li $t0 5
sw $t0 0($sp)
div 0($sp), 5
mflo destination
sw $t0 4($sp)
