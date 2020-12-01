import pytest
import numpy as np
import random
import cv2
from proyecto2.io import IO
from proyecto2.image import Image

class TestIO:

    TEST1 = [[[124, 177, 144, 255], [ 54, 104,  72, 255], [151, 192, 165, 255], [200, 236, 214, 255], [103, 129, 116, 255]],
       [[ 96, 133,  99, 255], [  7,  37,  12, 255], [113, 128, 120, 255], [133, 138, 137, 255], [ 50,  50,  50, 255]],
       [[145, 152, 117, 255], [125, 118, 103, 255], [118,  77, 105, 255], [ 66,  10,  53, 255], [175, 120, 147, 255]],
       [[157, 131, 125, 255], [219, 176, 191, 255], [134,  59, 115, 255], [102,  21,  76, 255], [173, 118, 127, 255]],
       [[176, 108, 163, 255], [153,  79, 139, 255], [142,  53, 126, 255], [ 92,  29,  61, 255], [125, 122,  67, 255]]]

    def test_read(self):
        image = IO.read("./test/images/test_1.jpg")
        assert (image.pixels == np.array(self.TEST1)).all()

    def test_read_non_existent(self):
        with pytest.raises(IOError):
            IO.read("./test/images/fake.jpg")

    def test_write(self, tmpdir):
        matrix = np.array(self.TEST1)
        image = Image(matrix)

        IO.write(image, "./test/images_test/test.png")

        new_image = IO.read("./test/images_test/test.png")
        assert (new_image.pixels == matrix).all()

