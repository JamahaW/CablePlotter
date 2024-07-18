from typing import Callable
from typing import Final
from typing import Optional

import cv2
from numpy import uint8
from numpy import zeros


class TrackBar:

    def __init__(self, window: str, name: str, v_min: int, v_max: int, /, callback: Optional[Callable[[int], None]] = None) -> None:
        self.name: Final[str] = name
        self.__window = window
        cv2.createTrackbar(self.name, window, v_min, v_max, ((lambda x: x) if callback is None else callback))
        self.set((v_min + v_max) // 2)

    def get(self) -> int:
        return cv2.getTrackbarPos(self.name, self.__window)

    def set(self, value: int) -> None:
        cv2.setTrackbarPos(self.name, self.__window, value)


def main():
    window = "main"
    cv2.namedWindow(window)

    r_bar = TrackBar(window, "R", 0, 255)
    g_bar = TrackBar(window, "G", 0, 255)
    b_bar = TrackBar(window, "B", 0, 255)

    img = zeros((256, 256, 3), uint8)

    while True:
        img[:, :] = (b_bar.get(), g_bar.get(), r_bar.get())

        cv2.imshow(window, img)

        if cv2.waitKey(1) == ord('q'):
            break

    cv2.destroyAllWindows()


main()
