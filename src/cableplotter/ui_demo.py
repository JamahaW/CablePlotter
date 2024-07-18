from typing import Callable
from typing import Optional

import matplotlib.pyplot
# Импортируем класс слайдера
from matplotlib.widgets import Slider
from numpy import exp
from numpy import linspace
from numpy import pi
from numpy import sqrt


class Gauss:

    def __init__(self):
        pass


def gaussian(sigma, mu, x):
    return 1.0 / (sigma * sqrt(2.0 * pi)) * exp(-((x - mu) ** 2) / (2 * sigma ** 2))


def updateGraph(v: float):
    global slider_sigma
    global slider_mu
    global graph_axes

    # Используем атрибут val, чтобы получить значение слайдеров
    x = linspace(-5.0, 5.0, 300)
    y = gaussian(slider_sigma.val, slider_mu.val, x)

    graph_axes.clear()
    graph_axes.plot(x, y)
    matplotlib.pyplot.draw()


def createSlider(
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
        matplotlib.pyplot.axes((y_pos, x_pos, width, height)),
        label=label,
        valmin=v_min,
        valmax=v_max,
        valinit=((v_min + v_max) / 2),
        valfmt=f"%{d_a}.{d_b}f"
    )

    if callback is not None:
        s.on_changed(callback)

    return s


if __name__ == '__main__':
    SLIDER_SIZE = (0.8, 0.05)
    SLIDER_VALUES = (0.01, 1.0)

    fig, graph_axes = matplotlib.pyplot.subplots()
    graph_axes.grid()

    fig.subplots_adjust(left=0.07, right=0.95, top=0.95, bottom=0.4)

    slider_sigma = createSlider('σ', (0.25, 0.05), SLIDER_SIZE, SLIDER_VALUES, updateGraph)
    slider_mu = createSlider('μ', (0.17, 0.05), SLIDER_SIZE, SLIDER_VALUES, updateGraph)

    updateGraph(0)
    matplotlib.pyplot.show()
