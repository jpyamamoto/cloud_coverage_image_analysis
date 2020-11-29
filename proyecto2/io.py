import cv2
from .image import Image

class IO:
    """Input/Output related functions.
    """

    @staticmethod
    def read(image_path):
        """Return the image at the specified image path.

        Reads the image at the specified image path as a 2x2 matrix and
        converts each pixel's representation as an array in the shape
        [blue, green, red, alpha]. That is wrapped by an Image instance.

        Args:
            image_path: The path where the image is located.

        Returns:
            An Image instance that contains the data of the given image.

        Raises:
            IOError: An error occurred reading the image.
        """
        pixels = cv2.imread(image_path)

        if pixels is None:
            raise IOError("Image does not exist.")

        pixels = cv2.cvtColor(pixels , cv2.COLOR_BGR2BGRA)
        return Image(pixels)

    @staticmethod
    def write(image, path):
        """Return the image at the specified image path.

        Write the image to the specified location.
        image itself.

        Args:
            image: The instance with the data of the image.
            path: The path to which the image should be writen.

        Raises:
            IOError: An error occurred writing the image.
        """
        cv2.imwrite(path, image.pixels)

