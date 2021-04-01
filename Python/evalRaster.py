#!/usr/bin/python3

# evalRaster.py
#
# Perform basic mathematical operations on the supplied raster, save it as the
# file name indicated.
import argparse
import sys

import include.ascFile as ascFile


def main(input, output, equation):
    # Load the input raster file
    [header, data] = ascFile.load_asc(input)

    # Iterate over the input raster, which will be saved as the output
    for row in range(header['nrows']):
        for col in range(header['ncols']):

            # Pass on no data
            if data[row][col] == header['nodata']:
                continue

            # Perform the operation
            data[row][col] = eval(equation, {"x": data[row][col]})

    # Save the updated raster as the output
    ascFile.write_asc(header, data, output)


if __name__ == "__main__":
    # Parse the parameters
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', action='store', dest='input', required=True,
        help='Raster file to apply the operation to')
    parser.add_argument('-o', action='store', dest='output', required=True,
        help='File to save the results as, will override existing file')
    parser.add_argument('-e', action='store', dest='equation', required=True,
        help='Mathematical operation to perform, x represents the value in the raster file (e.g., y = x * 42)')
    args = parser.parse_args()

    # Defer to main
    main(args.input, args.output, args.equation)