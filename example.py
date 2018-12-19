"""Example for gas detection module."""

import time
from gas_detection import GasDetection

def main():
    """Handle example."""

    print('Calibrating ...')
    detection = GasDetection()

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
        print('\nAborted by user!')

if __name__ == '__main__':
    main()
