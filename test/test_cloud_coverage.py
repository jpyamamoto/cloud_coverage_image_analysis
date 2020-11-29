import numpy as np
import random
from proyecto2.cloud_coverage import CloudCoverage
from proyecto2.io import IO

class TestCloudCoverage:
    TEST_MASK_IMAGE = "./test/images/test_3.jpg"
    TEST_CLASSIFY_IMAGE = "./test/images/test_4.jpg"

    def mask_for_test(self, image):
        rows, cols, _ = image.shape
        y, x = np.ogrid[:rows, :cols]

        distance = np.sqrt((x - (cols // 2)) ** 2 + (y - (rows // 2)) ** 2)
        mask = distance > 1324

        return mask

    def mid_width(self, image):
        _, x, _ = image.pixels.shape

        return x // 2

    def test_mask(self):
        image = IO.read(self.TEST_MASK_IMAGE)
        image_mask = CloudCoverage.apply_mask(image.pixels)

        mask = self.mask_for_test(image_mask)

        assert np.all(image_mask[mask] == [0, 0, 0, 0])
        assert np.all(image_mask[~mask][:,3] == 255)

    def test_classify(self):
        image = IO.read(self.TEST_CLASSIFY_IMAGE)
        image_classified = CloudCoverage.classify(image.pixels)

        mid = self.mid_width(image)

        assert np.all(image_classified[:, mid:] == [255, 255, 255, 255])
        assert np.all(image_classified[:, :mid] == [0, 0, 0, 255])

    def test_ratio(self):
        image = IO.read(self.TEST_CLASSIFY_IMAGE)
        classified_pixels = CloudCoverage.classify(image.pixels)
        ratio = CloudCoverage.ratio(classified_pixels)

        assert ratio == 0.5

    def test_compute(self):
        image = IO.read(self.TEST_CLASSIFY_IMAGE)
        count, classified_image = CloudCoverage.compute(image)

        mid = self.mid_width(image)

        rows, cols, _ = classified_image.pixels.shape
        _, x = np.ogrid[:rows, :cols]

        mask = self.mask_for_test(classified_image.pixels)

        assert abs(count - 0.5) < 0.001
        assert np.all(classified_image.pixels[(~mask) & (x > mid)] == [255, 255, 255, 255])
        assert np.all(classified_image.pixels[(~mask) & (x < mid)] == [0, 0, 0, 255])

