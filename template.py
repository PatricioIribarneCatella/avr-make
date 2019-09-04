#
# Generates a Makefile from
# the template with the specified
# arguments
#

HEADER = "\
DEVICE = {}\n\
PROGRAMMER = {}\n\
BITCLOCK = {}\n\
PORT = {}\n\
\n"

TEMPLATE = "\
AVR = avr-gcc\n\
AVRHEX = avr-objcopy\n\
AVRDUDE = avrdude\n\
\n\
AVRFLAGS = -mmcu=$(DEVICE) -Os -g\n\
AVRHEXFLAGS = -O ihex\n\
AVRDUDEFLAGS = -p $(DEVICE) -c $(PROGRAMMER) -B $(BITCLOCK) -P $(PORT) -D\n\
\n\
EXEC = main\n\
\n\
BIN = $(wildcard *.S)\n\
OBJFILES = $(BIN:.S=.o)\n\
\n\
HEX = $(EXEC).hex\n\
\n\
all: $(HEX)\n\
\n\
%.o: %.S\n\
\t$(AVR) $(AVRFLAGS) -c $< -o $@\n\
\n\
$(EXEC).elf: $(OBJFILES)\n\
\t$(AVR) $(AVRFLAGS) -o $@ $^\n\
\n\
%.hex: $(EXEC).elf\n\
\t$(AVRHEX) $(AVRHEXFLAGS) $^ $@\n\
\n\
upload: all\n\
\t$(AVRDUDE) $(AVRDUDEFLAGS) -U flash:w:$(HEX).hex:i\n\
\n\
clean: \n\
\trm -f *.hex *.elf *.o\n\
\n\
.PHONY: clean\n"

def makefile(device, prog, port, bc):

    h = HEADER.format(device, prog, bc, port)
    
    return h + TEMPLATE

