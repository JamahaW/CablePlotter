from os import PathLike

import cv2
from numpy import ndarray
from numpy import uint8

type Image = ndarray[uint8]


def readImageBGR(filename: PathLike | str, /) -> Image:
    return cv2.imread(filename, cv2.IMREAD_COLOR)


def saveImageRGB(filename: PathLike | str, image: Image, /) -> None:
    cv2.imwrite(filename, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))


def getContourImage(image: Image, low: int, high: int) -> Image:
    return cv2.Canny(image, low, high, L2gradient=True)
