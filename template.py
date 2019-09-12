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
BAUD = {}\n\
FREQ = {}\n\
\n"

TEMPLATE = "\
AVR = avr-gcc\n\
AVRHEX = avr-objcopy\n\
AVRDUDE = avrdude\n\
\n\
AVRFLAGS = -mmcu=$(DEVICE) -Os -g\n\
AVRHEXFLAGS = -O ihex\n\
AVRDUDEFLAGS = -p $(DEVICE) -c $(PROGRAMMER) -B $(BITCLOCK) -b $(BAUD) -P $(PORT) -D\n\
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
gdb: $(EXEC).elf\n\
\tavr-gdb -q -s $< -ex 'target remote 127.0.0.1:1234'\n\
\n\
gdb-sim: $(EXEC).hex\n\
\tsimavr -f $(FREQ) -m $(DEVICE) $< -gdb\n\
\n\
upload: all\n\
\t$(AVRDUDE) $(AVRDUDEFLAGS) -U flash:w:$(HEX).hex:i\n\
\n\
clean: \n\
\trm -f *.hex *.elf *.o\n\
\n\
.PHONY: clean\n"

def makefile(device, prog, port, bc, baud, freq):

    h = HEADER.format(device, prog, bc, port, baud, freq)
    
    return h + TEMPLATE

