#ifndef _AVRX_
#define _AVRX_

// AVR processor-specific file
// containing the I/O port
// definitions  for the device
#include <avr/io.h>
#include <avr/interrupt.h>

// AVR linux defines
//
#define __SFR_OFFSET 0

// Directives
#define CSEG .text
#define DSEG .data
#define DB .byte
#define BYTE .space
#define ORG .org

// Operators
#define LOW(x) lo8(x)
#define HIGH(x) hi8(x)

#endif // _AVRX_
