from dataclasses import dataclass
import numpy

@dataclass()
class Image:
    """Instance that contains the image's data.

    Attributes:
        pixels (numpy.ndarray): A numpy 2x2 matrix with pixels [blue, green, red, alpha].
    """

    pixels: numpy.ndarray

