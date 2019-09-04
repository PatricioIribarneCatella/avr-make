DEVICE = atmega328p
PROGRAMMER = usbasp
BITCLOCK = 0.5
PORT = usb

AVR = avr-gcc
AVRHEX = avr-objcopy
AVRDUDE = avrdude

AVRFLAGS = -mmcu=$(DEVICE) -Os -g
AVRHEXFLAGS = -O ihex
AVRDUDEFLAGS = -p $(DEVICE) -c $(PROGRAMMER) -B $(BITCLOCK) -P $(PORT) -D

EXEC = main

BIN = $(wildcard *.S)
OBJFILES = $(BIN:.S=.o)

HEX = $(EXEC).hex

all: $(HEX)

%.o: %.S
	$(AVR) $(AVRFLAGS) -c $< -o $@

$(EXEC).elf: $(OBJFILES)
	$(AVR) $(AVRFLAGS) -o $@ $^

%.hex: $(EXEC).elf
	$(AVRHEX) $(AVRHEXFLAGS) $^ $@

upload: all
	$(AVRDUDE) $(AVRDUDEFLAGS) -U flash:w:$(HEX).hex:i

clean: 
	rm -f *.hex *.elf *.o

.PHONY: clean
