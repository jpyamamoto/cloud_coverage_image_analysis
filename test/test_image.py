import numpy as np
import random
from proyecto2.image import Image

class TestImage:

    def test_pixels(self):
        for _ in range(5):
            x = random.randrange(1920, 4368, 1)
            y = random.randrange(1080, 2912, 1)
            matrix = np.random.rand(y, x)
            image = Image(matrix)
            assert (matrix == image.pixels).all()

