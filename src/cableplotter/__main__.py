from pathlib import Path
from typing import Callable

from matplotlib import pyplot
from matplotlib.axes import Axes
from matplotlib.widgets import Slider

from cableplotter.util.image import getContourImage
from cableplotter.util.image import readImageRGB


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

    img = readImageRGB(in_folder / "test_image.png")

    slider = createSlider("level", pyplot.axes((0.05, 0.25, 0.85, 0.04)), print)

    image = getContourImage(img)
    height, width, colors = image.shape
    pyplot.title(f"view {width=}, {height=}, {colors=}")

    pyplot.imshow(image)

    pyplot.show()

    # imageSaveRGB(out_folder / "out_image.png", img)


if __name__ == '__main__':
    main()
