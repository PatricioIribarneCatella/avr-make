AVR = avr-gcc
AVRHEX = avr-objcopy
AVRDUDE = avrdude

AVRFLAGS = -mmcu=$(DEVICE) -Os -g
AVRHEXFLAGS = -O ihex
AVRDUDEFLAGS = -p $(DEVICE) -c $(PROGRAMMER) -B $(BITCLOCK) -P $(PORT) -D

all: test.hex

%.o: %.S
	$(AVR) $(AVRFLAGS) $^ -o $@

%.hex: %.o
	$(AVRHEX) $(AVRHEXFLAGS) $^ $@

clean:
	rm -f *.hex *.o

.PHONY: clean
