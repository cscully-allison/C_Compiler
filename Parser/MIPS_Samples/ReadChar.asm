somecode:
	jal ReadChar
	move $a1, $v1
	jal PrintChar

	#tells system program is done
	li $v0, 10
	syscall

ReadChar:
	li $v0, 12
	syscall
	move $v1, $v0
	jr $ra

PrintChar:
	li $v0, 11
	add $a0, $zero, $a1
	syscall
	jr $ra
