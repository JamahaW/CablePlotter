from os import PathLike

import cv2
from numpy import ndarray
from numpy import uint8
from numpy import zeros

type Image = ndarray[uint8]


def readImageBGR(filename: PathLike | str, /) -> Image:
    return cv2.imread(filename, cv2.IMREAD_COLOR)


def saveImageRGB(filename: PathLike | str, image: Image, /) -> None:
    cv2.imwrite(filename, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))


def getContourImage(image: Image, thresh: int = 100) -> Image:
    cvt_color = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, thresh_img = cv2.threshold(cvt_color, thresh, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    return cv2.drawContours(zeros(image.shape, dtype=uint8), contours, -1, (255, 255, 255))
