#takes value from input and stores into $t1 after the function readint is called
somecode:
	jal ReadInt
	move $a1, $v1
	jal PrintInt
	
	#tells system program is done
	li $v0, 10
	syscall

ReadInt:
	li $v0, 5
	syscall
	move $v1, $v0
	jr $ra
	
PrintInt:
	li $v0, 1
	add $a0, $zero, $a1
	syscall
	jr $ra
