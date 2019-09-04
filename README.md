# avr-make

Generates _Makefile_ for **AVR** microcontroller project

## Dependencies

```bash
 $ ./install.sh
```

or

```bash
$ sudo apt install gcc-avr binutils-avr avr-libc avrdude gdb-avr
```

## Generate _Makefile_

```bash
$ ./generate.py --device=DEVICE --prog=PROGRAMMER --port=PORT --bc=BITCLOCK
```

- `DEVICE`: _AVR_ microcontroller
- `PROGRAMMER`: programmer type
- `BITCLOCK`: _JTAG/STK500v2_ bit clock period (us)
- `PORT`: connection port

### _Makefile_: Targets

- **make**: Compiles the project. Generates _main_.hex. (_main.S_ is the main file)
- **upload**: Writes the _hex_ file into the _microcontroller_
- **clean**: Deletes _hex_ and intermidiate files

## Example

```bash
 $ cd tests
 $ make
``` 
