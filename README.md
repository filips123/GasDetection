Gas detection
=============

[![Latest Version][icon-version]][link-pypi]
[![Total Downloads][icon-downloads]][link-pypi]
[![License][icon-license]][link-license]
[![Build Status][icon-travis]][link-travis]

Gas detection for Raspberry Pi using ADS1x15 and MQ-2 sensors.

## Description

The MQ-2 sensor can detect multiple gases (CO, H2, CH4, LPG, propane, alcohol, smoke) and outputs analog voltage. This project can convert it to digital using ADS1015 or ADS1115 and filter out the target gases.

The sensor can be inaccurate so don't use those measurements if you need them for security purposes. Use some professional measurement device if you need to do this.

## Usage

The detection class uses ADS1115 and it's I2C address `0x48` by default. It assumes the sensor is connected to `P0`. You can also pass them to arguments.

The `ro` value is about `1000`, but it needs to be calibrated. This is done automatically if it is not specified. The calibration must be done in good fresh air to make measurements more accurate. Alternativly, you can save the calibration value and later pass it as `ro` argument.

```python
from gas_detection import GasDetection

detection = GasDetection()
```

You can then read percentage of gases in parts per million (ppm). The measurements are returned as dictionary and gas be accessed by `GAS_XX` constant.

```python
ppm = detection.percentage()

print('CO: {} ppm'.format(ppm[detection.CO_GAS]))
print('H2: {} ppm'.format(ppm[detection.H2_GAS]))
print('CH4: {} ppm'.format(ppm[detection.CH4_GAS]))
print('LPG: {} ppm'.format(ppm[detection.LPG_GAS]))
print('PROPANE: {} ppm'.format(ppm[detection.PROPANE_GAS]))
print('ALCOHOL: {} ppm'.format(ppm[detection.ALCOHOL_GAS]))
print('SMOKE: {} ppm\n'.format(ppm[detection.SMOKE_GAS]))
```

You can also look to [example file][link-example] for more examples. For more details how the values are calculated you can read [tutorial on Raspberry Pi Tutorials][link-tutorial].

## Versioning

This library uses [SemVer][link-semver] for versioning. For the versions available, see [the tags][link-tags] on this repository.

## License

This library is licensed under the GPLv3+ license. See the [LICENSE][link-license-file] file for details.

A lot of code has been taken from [Raspberry-Pi-Gas-Sensor-MQ][link-source]. Thank you @tutRPi and others who contributed to that repository.

[icon-version]: https://img.shields.io/pypi/v/gas-detection.svg?style=flat-square&label=version
[icon-downloads]: https://img.shields.io/pypi/dm/gas-detection.svg?style=flat-square&label=downloads
[icon-license]: https://img.shields.io/pypi/l/gas-detection.svg?style=flat-square&label=license
[icon-travis]: https://img.shields.io/travis/com/filips123/GasDetection.svg?style=flat-square&label=build+status

[link-pypi]: https://pypi.org/project/gas-detection/
[link-license]: https://choosealicense.com/licenses/gpl-3.0/
[link-semver]: https://semver.org/
[link-travis]: https://travis-ci.com/filips123/GasDetection/

[link-example]: https://github.com/filips123/GasDetection/blob/master/example.py
[link-tags]: https://github.com/filips123/GasDetection/tags/
[link-license-file]: https://github.com/filips123/GasDetection/blob/master/LICENSE

[link-tutorial]: https://tutorials-raspberrypi.com/configure-and-read-out-the-raspberry-pi-gas-sensor-mq-x/
[link-source]: https://github.com/tutRPi/Raspberry-Pi-Gas-Sensor-MQ/
