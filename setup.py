# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='dikdik',

    version='0.0.1',

    description='A sample Python project',
    long_description=long_description,
    url='https://github.com/brianherman/dikdik',

    author='Brian James Herman',
    author_email='brianherman@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        #'Programming Language :: Python :: 3',
        #'Programming Language :: Python :: 3.3',
        #'Programming Language :: Python :: 3.4',
        #'Programming Language :: Python :: 3.5',
    ],

    keywords='development tools',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=['pyqt4'],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    i# for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },

    entry_points={
        'console_scripts': [
            'dikdik=dikdik:main',
        ],
    },
)
