from os import PathLike

import cv2
from numpy import ndarray
from numpy import uint8
from numpy import zeros

type Image = ndarray[uint8]


def readImageRGB(filename: PathLike | str, /) -> Image:
    return cv2.cvtColor(cv2.imread(filename, cv2.IMREAD_COLOR), cv2.COLOR_BGR2RGB)


def saveImageRGB(filename: PathLike | str, image: Image, /) -> None:
    cv2.imwrite(filename, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))


def getContourImage(image: Image, thresh: int = 100) -> Image:
    _, thresh_img = cv2.threshold(cv2.cvtColor(image, cv2.COLOR_RGB2GRAY), thresh, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return cv2.drawContours(zeros(image.shape, dtype=uint8), contours, -1, (255, 255, 255), 1)
