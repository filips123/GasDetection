from setuptools import setup

def readme():
    with open('README.md') as f:
            return f.read()

setup(
    name = 'gas-detection',
    description = 'Gas detection for Raspberry Pi using ADS1x15 and MQ-2 sensors',
    long_description = readme(),
    long_description_content_type='text/markdown',
    license = 'GPLv3+',

    version_format='{tag}',
    setup_requires=['setuptools-git-version'],

    packages = ['gas_detection'],

    entry_points = {
        'console_scripts': ['gas-detection=gas_detection.__main__:main'],
    },

    install_requires = [
        'adafruit-circuitpython-ads1x15',
    ],

    extras_require = {
        'lint': ['pylint'],
    },

    python_requires = '>= 3.4',

    author = 'Filip Š',
    author_email = 'projects@filips.si',
    url = 'https://github.com/filips123/GasDetection/',
    keywords = 'smoke gas detection hardware ads1x115 mq2 RaspberryPi',
    platforms = 'Linux',

    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Physics',
        'Topic :: System :: Hardware',
    ],

    include_package_data = True,
)
