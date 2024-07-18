from pathlib import Path
from typing import Callable

import cv2
from matplotlib import pyplot
from matplotlib import pyplot
from matplotlib import pyplot
from matplotlib import pyplot
from matplotlib.axes import Axes
from matplotlib.widgets import Slider
from numpy import uint8
from numpy import zeros

from cableplotter.general import Image
from cableplotter.general import imageReadRGB


def showImage(image: Image):
    height, width, colors = image.shape
    pyplot.title(f"view {width=}, {height=}, {colors=}")
    pyplot.imshow(image)
    pyplot.show()


def getContourImage(image: Image, thresh: int = 100) -> Image:
    _, thresh_img = cv2.threshold(cv2.cvtColor(image, cv2.COLOR_RGB2GRAY), thresh, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return cv2.drawContours(zeros(image.shape, dtype=uint8), contours, -1, (255, 255, 255), 1)


def createSlider(label: str, axes: Axes, callback: Callable[[float], None]) -> Slider:
    ret = Slider(
        axes,
        label=label,
        valmin=0,
        valmax=255,
        valinit=128,
        valfmt='%1.0f'
    )
    ret.on_changed(callback)
    return ret


def main():
    base_folder = Path("./data")
    in_folder = base_folder / "in"
    out_folder = base_folder / "out"

    img = imageReadRGB(in_folder / "test_image.png")

    slider = createSlider("level", pyplot.axes((0.05, 0.25, 0.85, 0.04)), print)

    image = getContourImage(img)
    height, width, colors = image.shape
    pyplot.title(f"view {width=}, {height=}, {colors=}")
    
    pyplot.imshow(image)

    pyplot.show()

    # imageSaveRGB(out_folder / "out_image.png", img)


if __name__ == '__main__':
    main()
