import cv2
from .image import Image

class IO:
    @staticmethod
    def read(image_path):
        pixels = cv2.imread(image_path)

        if pixels is None:
            raise IOError("Image does not exist.")

        pixels = cv2.cvtColor(pixels , cv2.COLOR_BGR2BGRA)
        return Image(image_path, pixels)

    @staticmethod
    def write(image):
        cv2.imwrite(image.name + '.' + image.extension, image.pixels)

