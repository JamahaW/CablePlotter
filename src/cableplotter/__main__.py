import cv2

from cableplotter.ui import CheckBox
from cableplotter.ui import TrackBar
from cableplotter.ui import Window
from cableplotter.util.image import Image
from cableplotter.util.image import getContourImage
from cableplotter.util.image import readImageBGR


class App:

    def __init__(self):
        self.image = readImageBGR("./data/in/bear.png")

        self.image_height, self.image_width, _ = self.image.shape

        self.rotation_matrix = self.createRotationMatrix(0)

        self.window = Window("main")
        self.bar_high = TrackBar(self.window, "high", 0, 255)
        self.bar_low = TrackBar(self.window, "low", 0, 255)
        self.bar_turn = TrackBar(self.window, "turn", 0, 720, self.updateRotationMatrix)

        self.checkbox = CheckBox(self.window, "checkbox")

    def createRotationMatrix(self, angle: int):
        return cv2.getRotationMatrix2D((self.image_width // 2, self.image_height // 2), angle, 1.0)

    def updateRotationMatrix(self, angle: int) -> None:
        self.rotation_matrix = self.createRotationMatrix(angle)

    def rotateImage(self, image: Image) -> Image:
        return cv2.warpAffine(image, self.rotation_matrix, (self.image_width, self.image_height))

    def update(self):
        src = self.getSourceImage()

        src = self.rotateImage(src)

        self.window.show(src)

    def getSourceImage(self) -> Image:
        if self.checkbox.get():
            return self.image

        return getContourImage(self.image, self.bar_high.get(), self.bar_low.get())

    def run(self):
        while True:
            self.update()

            if cv2.waitKey(1) == ord('q'):
                break

        Window.destroyAll()


if __name__ == '__main__':
    App().run()
