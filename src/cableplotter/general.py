from os import PathLike

import cv2
from matplotlib import pyplot
from numpy import uint8
from numpy.typing import NDArray


def displayImageFile(filename: PathLike | str):
    img = loadImage(filename)
    pyplot.imshow(img)


def loadImage(filename: PathLike | str) -> NDArray[uint8]:
    return cv2.imread(filename, cv2.IMREAD_COLOR)
