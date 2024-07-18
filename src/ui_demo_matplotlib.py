from typing import Callable
from typing import Optional

from matplotlib import pyplot
from matplotlib import pyplot
from matplotlib.widgets import Slider
from numpy import exp
from numpy import linspace
from numpy import pi
from numpy import sqrt


class Gauss:
    @staticmethod
    def gaussian(sigma, mu, x):
        return 1.0 / (sigma * sqrt(2.0 * pi)) * exp(-((x - mu) ** 2) / (2 * sigma ** 2))

    def __init__(self):
        SLIDER_SIZE = (0.8, 0.05)
        SLIDER_VALUES = (0.1, 1.0)

        fig, self.graph_axes = pyplot.subplots()
        self.graph_axes.grid()

        fig.subplots_adjust(left=0.07, right=0.95, top=0.95, bottom=0.4)

        self.slider_sigma = createMPLSlider('σ', (0.25, 0.05), SLIDER_SIZE, SLIDER_VALUES, self.__updateGraph)
        self.slider_mu = createMPLSlider('μ', (0.17, 0.05), SLIDER_SIZE, SLIDER_VALUES, self.__updateGraph)

        self.__updateGraph(0)

    @staticmethod
    def run():
        pyplot.show()

    def __updateGraph(self, _: float):
        x = linspace(-5.0, 5.0, 50)
        y = self.gaussian(self.slider_sigma.val, self.slider_mu.val, x)

        self.graph_axes.clear()
        self.graph_axes.plot(x, y)
        pyplot.draw()


if __name__ == '__main__':
    Gauss().run()


def createMPLSlider(
        label,
        pos: tuple[float, float],
        size: tuple[float, float],
        value_range: tuple[float, float],
        /,
        callback: Optional[Callable[[float], None]] = None,
        *,
        digits: tuple[float, float] = (3, 3)
):
    x_pos, y_pos = pos
    width, height = size
    v_min, v_max = value_range
    d_a, d_b = digits

    s = Slider(
        pyplot.axes((y_pos, x_pos, width, height)),
        label=label,
        valmin=v_min,
        valmax=v_max,
        valinit=((v_min + v_max) / 2),
        valfmt=f"%{d_a}.{d_b}f"
    )

    if callback is not None:
        s.on_changed(callback)

    return s
