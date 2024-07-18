from typing import Callable
from typing import Optional

import cv2
from numpy import ndarray


class UIEntity:

    def __init__(self, name: str) -> None:
        self.__name = name

    def getName(self) -> str:
        return self.__name


class Window(UIEntity):

    @staticmethod
    def destroyAll():
        cv2.destroyAllWindows()

    def __init__(self, name: str) -> None:
        super().__init__(name)
        cv2.namedWindow(self.getName(), cv2.WINDOW_AUTOSIZE)

    def destroy(self) -> None:
        cv2.destroyWindow(self.getName())

    def show(self, image: ndarray) -> None:
        cv2.imshow(self.getName(), image)

    def move(self, pos: tuple[int, int]) -> None:
        x, y = pos
        cv2.moveWindow(self.getName(), x, y)


class TrackBar(UIEntity):

    def __init__(self, window: Window, name: str, v_min: int, v_max: int, /, callback: Optional[Callable[[int], None]] = None) -> None:
        super().__init__(name)
        self.__window = window
        cv2.createTrackbar(self.getName(), window.getName(), v_min, v_max, ((lambda x: x) if callback is None else callback))

        self.set((v_min + v_max) // 2)

    def get(self) -> int:
        return cv2.getTrackbarPos(self.getName(), self.__window.getName())

    def set(self, value: int) -> None:
        cv2.setTrackbarPos(self.getName(), self.__window.getName(), value)


class CheckBox(TrackBar):
    def __init__(self, window: Window, name: str, /):
        super().__init__(window, name, 0, 1)
