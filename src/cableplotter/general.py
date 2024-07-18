from os import PathLike

import cv2
from numpy import ndarray
from numpy import uint8

type Image = ndarray[uint8]


def imageReadRGB(filename: PathLike | str, /) -> Image:
    return cv2.cvtColor(cv2.imread(filename, cv2.IMREAD_COLOR), cv2.COLOR_BGR2RGB)


def imageSaveRGB(filename: PathLike | str, image: Image, /) -> None:
    cv2.imwrite(filename, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
