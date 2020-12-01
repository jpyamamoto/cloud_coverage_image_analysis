import cv2
import numpy as np
from .image import Image

RADIUS = 1324
CENTER_X = 2184
CENTER_Y = 1456

class CloudCoverage:
    """Cloud cover index calculation related functions.
    """

    @classmethod
    def get_mask(cls, image):
        """Return the transparency mask for the pixels outside of de image
        circunference. Calculates the circumference of the image that can
        be used for de calculus of cloud coverage by using the radius of
        the circle, calculates the distance from the center of every pixel
        and creates a mask that makes the pixels outside of the circle
        completly translucid by setting to 0 all of its values in BGRA format.

        Args:
            image: A numpy ndarray. The array that contains all the pixels of the image.

        Returns:
            The mask of translucid pixels outside of the circle.
        """
        rows, cols, _ = image.shape
        y, x = np.ogrid[:rows, :cols]

        distance_from_center = np.sqrt((x - CENTER_X) ** 2 + (y - CENTER_Y) ** 2)
        mask = distance_from_center > RADIUS

        return mask


    @classmethod
    def apply_mask(cls, image):
        """Return the modified mumpy ndarray by aplying the mask of translucid
        pixels to it, the pixels outside of the circle will be translucid by
        setting the pixel in the mask to 0.

        Args:
            image: A numpy ndarray. The array that contains all the pixels of the image.

        Returns:
            numpy.ndarray: The modified ndarray with the pixels outside of the circle translucid.
        """
        image[cls.get_mask(image)] = 0

        return image


    @classmethod
    def classify(cls, image):
        """Return the modified mumpy ndarray where all pixels have been
        setting to black or white by obtaining the original BGRA format of
        every pixel in the array and dividing its red value and its blue value,
        the result of the division will be a mask for the ndarray;
        if the division of red and blue values
        of a pixel its greater than or equal to 0.95, the pixel will be set to
        black, other case the pixel will be set to white, for all the pixels in
        the array that are not translucid.

        Args:
            image: A numpy ndarray. The array that contains all the pixels of the image.

        Returns:
            numpy.ndarray: A numpy ndarray.

            The modified array whith the pixels inside of the circle setting to black or
            white depending of its ratio red/blue.
        """
        blue, red, alpha = image[:, :, 0], image[:, :, 2], image[:, :, 3]

        ratios = np.divide(red, blue, out=np.ones(red.shape, dtype=float), where=blue != 0)
        mask = ratios >= 0.95

        image[(alpha != 0) & mask] = [255,255,255,255]
        image[(alpha != 0) & ~mask] = [0,0,0,255]

        return image


    @classmethod
    def ratio(cls, image):
        """Return the cloud cover index by dividing the number of pixels that
        are cloud and the total number of pixels in the circle.

        Args:
            image: A numpy ndarray. The array that contains all the pixels of the image.

        Returns:
            int: Cloud cover index.

            The result of dividing the cloud pixels and the total pixels in the circle.
        """
        sky = np.count_nonzero(np.all(image==[0, 0, 0, 255],axis=2))
        cloud = np.count_nonzero(np.all(image==[255, 255, 255, 255],axis=2))

        return cloud / (cloud + sky)


    @classmethod
    def compute(cls, image):
        """Return a tuple with cloud cover index and the new image with its
        cloud pixels in white, the sky pixels in black and the pixels out of the
        circle settint translucid.

        Args:
            image: An image object containing the pixels as a numpy ndarray.

        Returns:
            (int, numpy.ndarray): Cloud cover index and the modified image.

            The result of dividing the cloud pixels and the total pixels in
            the circle, and a copy of the image with black and white pixels
            correspondig to sky and cloud.
        """
        modified_image = image.pixels.copy()
        modified_image = cls.apply_mask(image.pixels)
        modified_image = cls.classify(modified_image)
        count = cls.ratio(modified_image)

        new_image = Image(modified_image)
        return (count, new_image)

