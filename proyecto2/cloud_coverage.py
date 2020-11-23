import cv2
import numpy as np
from .image import Image

class CloudCoverage:
    RADIUS = 1324

    @classmethod
    def get_mask(cls, image):
        total_row , total_col , _ = image.shape
        x , y = np.ogrid[:total_row , :total_col]
        cen_x , cen_y = total_row/2 , total_col/2

        distance_from_the_center = np.sqrt((x-cen_x)**2 + (y-cen_y)**2)
        outer_mask = distance_from_the_center > cls.RADIUS

        return outer_mask


    @classmethod
    def apply_mask(cls, image):
        image[cls.get_mask(image)] = 0

        return image


    @classmethod
    def classify(cls, image):
        blue, red, alpha = image[:, :, 0], image[:, :, 2], image[:, :, 3]

        ratios = np.divide(red, blue, out=np.ones(red.shape, dtype=float), where=blue != 0)
        mask = ratios >= 0.95

        image[(alpha != 0) & mask] = [255,255,255,255]
        image[(alpha != 0) & ~mask] = [0,0,0,255]

        return image


    @classmethod
    def ratio(cls, image):
        sky = np.count_nonzero(np.all(image==[0, 0, 0, 255],axis=2))
        cloud = np.count_nonzero(np.all(image==[255, 255, 255, 255],axis=2))

        return cloud / (cloud + sky)


    @classmethod
    def compute(cls, image):
        modified_image = image.pixels.copy()
        modified_image = cls.apply_mask(image.pixels)
        modified_image = cls.classify(modified_image)
        count = cls.ratio(modified_image)

        new_image = Image(image.name + "-seg.png", modified_image)
        return (count, new_image)

