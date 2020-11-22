import cv2
from .image import Image

class IO:
    @classmethod
    def read(cls, image_path):
        pixels = cv2.imread(image_path)
        pixels = cv2.cvtColor(pixels , cv2.COLOR_BGR2BGRA)
        return Image(image_path, pixels)

    @classmethod
    def write(cls, image):
        cv2.imwrite(image.name + '.' + image.extension, image.pixels)

