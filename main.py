#!/usr/bin/env python3
"""
Cloud Coverage Analysis.

Given an image whose path is received as the first argument when calling the
program, return the Cloud Coverage Index.

The Cloud Coverage Index is given by CCI = N/C where N stands for the
amount of pixels classified as cloud, and C is the number of pixels in
the valid area of the given picture.

An optional flag "s" or "S" may be given, which indicates that the resulting
image after classifying every pixel should be saved to a file named:
`image-seg.jpg`
assuming that the given file was originally called `image.jpg`
"""

__author__ = "Juan Pablo Yamamoto Zazueta and Luis Edgar Flores Ayala"
__version__ = "0.1.0"
__license__ = "MIT"

import pandas as pd
import argparse
from proyecto2.cloud_coverage import CloudCoverage
from proyecto2.io import IO


def main(image_path, export):
    """ Main entry point of the app """
    # Newly added Feature(s)
    """
    Included print statement for info/warning/error messages in English
    Added new feature to write computed CCI % values into a DataFrame
    """ 
    # Read the image located in image_path.
    try:
        image = IO.read(image_path)
        IO.write(image, "test.jpg")
        print("Se recibió la imagen {}".format(image_path))
        print("   ")
        print("Translation: Picture was received {}".format(image_path))
    except IOError:
        print("No se pudo leer la imagen {}".format(image_path))
        print("   ")
        print("Translation: Image could not be read {}".format(image_path))
        exit(1)

    # Get and print the cloud coverage index.
    index, new_image = CloudCoverage.compute(image)

    print("El índice de cobertura nubosa es: {}".format(index))
    print("   ")
    print("Translation: The cloud cover index is: {}".format(index))

    # Save image if the export flag was received.
    if export:
        out_path = '.'.join(image_path.split('.')[:-1]) + "-seg.png"
        try:
            IO.write(new_image, out_path)
            print("Se guardó exitosamente la imagen {}".format(out_path))
            print("   ")
            print("Translation: Image was successfully saved {}".format(out_path))
        except:
            print("Ocurrió un error al guardar la imagen {}".format(out_path))
            print("   ")
            print("Translation: An error occurred while saving the image {}".format(out_path))
    
    # Capture the computed CCI % Value into an output DataFrame
    opt_df_path = image_path.replace(image_path.split("/",)[-1],"",) + 'Image-CCI.csv'
    try:
        df = pd.read_csv(opt_df_path)
    except:
        df_new = pd.DataFrame({'Image':[image_path], 'CCI':[index]})
        df_new['Image'] = pd.Series(df_new['Image']).astype('str')
        df_new['CCI'] = pd.Series(df_new['CCI']).astype('float')
        df = df_new.copy()
    else:
        if df.loc[df['Image'] == image_path,].shape[0] > 0:
            df.loc[df['Image'] == image_path, 'CCI'] = index
            df['Image'] = pd.Series(df['Image']).astype('str')
            df['CCI'] = pd.Series(df['CCI']).astype('float')
        else:
            df_new = pd.DataFrame({'Image':[image_path], 'CCI':[index]})
            df_new['Image'] = pd.Series(df_new['Image']).astype('str')
            df_new['CCI'] = pd.Series(df_new['CCI']).astype('float')
            df = pd.concat([df, df_new], axis=0)
    df.to_csv(opt_df_path, index=False)


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
    main(args.image_path, bool(args.S))


