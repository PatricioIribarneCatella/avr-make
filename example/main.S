#include "avrx.h"

#define ACUM r16
#define I r17
#define SIZE 8

DSEG
V: BYTE SIZE
M: BYTE 1

CSEG
ORG 100
	rjmp main

.global main
main:
	call init_v

	ldi XH, HIGH(V)
	ldi XL, LOW(V)

	call promedio

	ldi YH, HIGH(M)
	ldi YL, LOW(M)

	st Y, ACUM

here: rjmp here

init_v:
	ldi XH, HIGH(V)
	ldi XL, LOW(V)

	ldi r18, 1
	st X+, r18
	ldi r18, 2
	st X+, r18
	ldi r18, 3
	st X+, r18
	ldi r18, 4
	st X+, r18
	ldi r18, 5
	st X+, r18
	ldi r18, 6
	st X+, r18
	ldi r18, 7
	st X+, r18
	ldi r18, 4
	st X+, r18
	ret

promedio:

	ldi ACUM, 0
	ldi I, 8

loop:
	ld r10, X+
	add ACUM, r10
	dec I
	breq exit
	rjmp loop

exit:
	asr ACUM
	asr ACUM
	asr ACUM

	ret

