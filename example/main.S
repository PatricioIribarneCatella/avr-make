#include "avrx.h"
#include "defs.h"

DSEG
V: BYTE SIZE
M: BYTE 1

CSEG
ORG _VECTORS_SIZE
	rjmp main

.global main
main:
	; initialize the stack
	; pointer to RAMEND
	ldi r16, HIGH(RAMEND)
	out _SFR_IO_ADDR(SPH), r16
	ldi r16, LOW(RAMEND)
	out _SFR_IO_ADDR(SPL), r16
	
	ldi XH, HIGH(V)
	ldi XL, LOW(V)

	call load

	ldi XH, HIGH(V)
	ldi XL, LOW(V)

	call average

	ldi YH, HIGH(M)
	ldi YL, LOW(M)

	st Y, ACUM2

here: rjmp here

