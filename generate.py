#!/usr/bin/env python3

from template import makefile
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

MAKEFILE = "Makefile"

def main(args):

    m = makefile(args.device, args.prog, args.port, args.bc)

    with open(MAKEFILE, "w") as f:
        f.write(m)

def parse():

    parser = ArgumentParser(
                description='Makefile generator',
                formatter_class=ArgumentDefaultsHelpFormatter)
    
    parser.add_argument(
            '--device',
            help='AVR microcrontroller type'
    )

    parser.add_argument(
            '--prog',
            help='programmer type'
    )

    parser.add_argument(
            '--port',
            default='usb',
            help='connection port type'
    )

    parser.add_argument(
            '--bc',
            help='JTAG/STK500v2 bit clock period (us)'
    )

    args = parser.parse_args()

    return args

if __name__ == "__main__":
    main(parse())

