#!/usr/bin/env python3
"""
Cloud Coverage Analysis.

Given an image whose path is received as the first argument when calling the
program, return the Cloud Coverage Index.

The Cloud Coverage Index is given by _CCI = N/C_ where _N_ stands for the
amount of pixels classified as cloud, and _C_ is the number of pixels in
the valid area of the given picture.

An optional flag "s" or "S" may be given, which indicates that the resulting
image after classifying every pixel should be saved to a file named:
`image-seg.jpg`
assuming that the given file was originally called `image.jpg`
"""

__author__ = "Juan Pablo Yamamoto Zazueta and Luis Edgar Flores Ayala"
__version__ = "0.1.0"
__license__ = "MIT"

import argparse
from proyecto2.cloud_coverage import CloudCoverage
from proyecto2.io import IO


def main(args):
    """ Main entry point of the app """
    image_path = args.image_path
    export = bool(args.S)

    image = IO.read(image_path)
    index, new_image = CloudCoverage.compute(image)

    if export:
        IO.write(new_image)

    print("El índice de cobertura nubosa es: {}".format(index))


if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser(prog = 'main.py',
                                     usage = '%(prog)s image_path [s|S]',
                                     description = 'Determine the Cloud Coverage Index of the given image.')

    # Positional arguments
    parser.add_argument("image_path", help="The name of the image to analyze")
    parser.add_argument("S", nargs="?", choices=("S", "s"), default=False,
                        help="Passed if the output image should be saved to <image_path>-seg.jpg")

    args = parser.parse_args()
    main(args)
