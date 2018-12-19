"""Command line program for gas detection."""

# pylint: disable=C0103
# pylint: disable=R0201

import argparse
import time

from . import GasDetection
from . import ADS1015, ADS1115
from . import P0, ADDRESS

def main():
    """Handle command line program."""

    parser = argparse.ArgumentParser(
        prog=__package__,
        description='Gas detection for Raspberry Pi using ADS1x15 and MQ-2 sensors'
    )

    parser.add_argument("--convertor", choices=['ADS1015', 'ADS1115'], default='ADS1115')
    parser.add_argument("--pin", action='store', default=P0)
    parser.add_argument("--address", action='store', default=ADDRESS)
    parser.add_argument("--ro", action='store', default=None)

    args = parser.parse_args()

    if args.convertor == 'ADS1015':
        convertor = ADS1015
    elif args.convertor == 'ADS1115':
        convertor = ADS1115

    pin = int(str(args.pin), 0)
    address = int(str(args.address), 0)
    ro = int(str(args.ro), 0) if args.ro else None

    if not ro:
        print('Calibrating ...')

    detection = GasDetection(convertor, pin, address, ro)

    if not ro:
        print('Done ...')
        print()

    try:
        while True:
            ppm = detection.percentage()

            print('CO: {} ppm'.format(ppm[detection.CO_GAS]))
            print('H2: {} ppm'.format(ppm[detection.H2_GAS]))
            print('CH4: {} ppm'.format(ppm[detection.CH4_GAS]))
            print('LPG: {} ppm'.format(ppm[detection.LPG_GAS]))
            print('PROPANE: {} ppm'.format(ppm[detection.PROPANE_GAS]))
            print('ALCOHOL: {} ppm'.format(ppm[detection.ALCOHOL_GAS]))
            print('SMOKE: {} ppm\n'.format(ppm[detection.SMOKE_GAS]))

            time.sleep(0.25)

    except KeyboardInterrupt:
        print()
        print('Aborted by user!')

if __name__ == '__main__':
    main()
