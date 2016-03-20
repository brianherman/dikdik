import sys
import argparse
from dikdik import MainWindow

def main():
    parser = argparse.ArgumentParser(description='Create a tree visualization of a python dictionary.')
    parser.add_argument("input", help='Input File')
    parser.add_argument('--type', help='Enter the type of the input file.')
    args = parser.parse_args()
    MainWindow.show(args)

if __name__ == "__main__":
    main()
