# avr-make

Generates _Makefile_ for **AVR** microcontroller project (for _linux_ users). It also includes a linux header file _avrx.h_ which has some constants defines and usually used _AVR_ header files.

## Dependencies

```bash
 $ ./install.sh
```

or

```bash
$ sudo apt install gcc-avr\
	binutils-avr\
	avr-libc\
	avrdude gdb-avr\
       	simavr libsimavr-dev gtkwave
```

## Generate _Makefile_

```bash
$ ./generate.py --device=DEVICE --prog=PROGRAMMER --port=PORT --bc=BITCLOCK --baud=BAUD-RATE --freq=FREQ
```

- `DEVICE`: _AVR_ microcontroller
- `PROGRAMMER`: programmer type
- `PORT`: connection port (usually it's in `/dev` directory, under the name of _tty*_)
- `BITCLOCK`: _JTAG/STK500v2_ bit clock period (us)
  - default: 0.5
- `BAUD-RATE`: baud rate
  - default: 115200
- `FREQ`: microcontroller's clock frequency

### _Makefile_: Targets

- **make**: Compiles the project. Generates _main_.hex. (_main.S_ is the main file)
- **upload**: Writes the _hex_ file into the _microcontroller_
- **clean**: Deletes _hex_ and intermidiate files

- _Simulation_
  - **gdb-sim**: runs [simavr](https://github.com/buserror/simavr) with the final _.hex_ file and connects to the remote _GDB_ target.
  - **gdb**: runs the _GDB_ version for _AVR_ (`avr-gdb`) and connects to the remote target `127.0.0.1:1234`

You first need to run `make gdb-sim` and then open another terminal, and run `make gdb`.

## Example

```bash
 $ cd example
 $ make
``` 

