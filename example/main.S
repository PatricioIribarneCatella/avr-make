#include "avrx.h"

.text
.global main

main:
	sbi _SFR_IO_ADDR(PORTB), 0
	call loop

