somecode:
	jal ReadFloat
	move $a1, $v1
	jal WriteFloat

	#tells system program is done
	li $v0, 10
	syscall
	
ReadFloat:
	li, $v0, 6
	syscall
	jr $ra

WriteFloat:
	li $v0, 2
	mov.s $f12, $f0
	syscall
	jr $ra