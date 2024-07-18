from pathlib import Path

import cv2

from cableplotter.ui import TrackBar
from cableplotter.ui import Window
from cableplotter.util.image import getContourImage
from cableplotter.util.image import readImageBGR


def main():
    base_folder = Path("./data")

    image = readImageBGR(f"{base_folder / "in" / "cat.png"}")

    # height, width, colors = image.shape

    window = Window("main")

    bar = TrackBar(window, "bar", 0, 255)

    while True:

        temp = getContourImage(image, bar.get())

        window.show(temp)

        if cv2.waitKey(1) == ord('q'):
            break

    Window.destroyAll()


if __name__ == '__main__':
    main()
