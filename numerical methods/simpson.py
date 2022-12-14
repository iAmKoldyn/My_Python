import math
from abc import abstractmethod, ABCMeta
from typing import Callable


class MathFuncs:

    @staticmethod
    def get_sqrt(x):
        """Корень"""
        return x / math.sqrt(x ** 2 + 9)

    @staticmethod
    def get_log(x):
        """Логарифм"""
        return (x ** 2) * math.log(x)

    @staticmethod
    def get_sin(x):
        """Синус"""
        return x / math.sin(x)

    @staticmethod
    def get_atan(x):
        """Арктангенс"""
        return math.atan(x) / x


class Figures(metaclass=ABCMeta):
    def __init__(self, task_item: str, func: Callable, a: int, b: int, n: int):
        self.s: float = 0
        self._task_item: str = task_item
        self._func: Callable = func
        self._a: int = a
        self._b: int = b
        self._n: int = n
        self._h: float = 0
        self._x: list = []

    def calculate(self):
        self._set_h()
        self._set_x_list()
        self._set_summa_using_func()
        self._set_s()
        return self

    def _set_h(self):
        self._h = (self._b - self._a) / self._n

    def _set_x_list(self):
        self._x = [self._a + i * self._h for i in range(self._n + 1)]

    @abstractmethod
    def _set_summa_using_func(self):
        """Рассчитать сумму по функции из MathFuncs"""

    @abstractmethod
    def _set_s(self):
        """Рассчитать S"""

    def __str__(self):
        return f"{self._task_item}) {self._func.__doc__ if self._func.__doc__ else 'Лямбда'}({self._n}) = {self.s}"


class Trapezoid(Figures):
    """Задание 1"""

    def __init__(self, task_item: str, func: Callable, a: int, b: int, n: int):
        super().__init__(task_item, func, a, b, n)
        self._summa: float = 0

    def _set_summa_using_func(self):
        self._summa = sum([self._func(self._x[i]) for i in range(1, self._n)])

    def _set_s(self):
        self.s = (self._h / 2) * (self._func(self._x[0]) + 2 * self._summa + self._func(self._x[self._n]))


class Rectangle(Figures):
    """Задание 2"""

    def __init__(self, task_item: str, func: Callable, a: int, b: int, n: int):
        super().__init__(task_item, func, a, b, n)
        self._summa: float = 0

    def _set_summa_using_func(self):
        self._summa = sum([self._func((self._x[i] + self._x[i + 1]) / 2) for i in range(self._n)])

    def _set_s(self):
        self.s = self._h * self._summa


class Simpsons(Figures):
    """Задание 3"""

    def __init__(self, task_item: str, func: Callable, a: int, b: int, n: int):
        super().__init__(task_item, func, a, b, n)
        self._summa1 = 0
        self._summa2 = 0

    def _set_h(self):
        self._h = (self._b - self._a) / (2 * self._n)

    def _set_x_list(self):
        self._x = [self._a + i * self._h for i in range(2 * self._n + 1)]

    def _set_summa_using_func(self):
        self._summa1 = sum(self._func(self._x[2 * i - 1]) for i in range(1, self._n + 1))
        self._summa2 = sum(self._func(self._x[2 * i]) for i in range(1, self._n))

    def _set_s(self):
        self.s = (self._h / 3) * (
            self._func(self._x[0]) + 4 * self._summa1 + 2 * self._summa2 + self._func(self._x[2 * self._n]))


if __name__ == '__main__':

    test_data = (
        (Trapezoid, (
            ("а", MathFuncs.get_sqrt, 0, 4, 16),
            ("а", MathFuncs.get_sqrt, 0, 4, 32),
            ("б", MathFuncs.get_log, 1, 3, 16),
            ("б", MathFuncs.get_log, 1, 3, 32)
        ),
         ),
        (Rectangle, (
            ("а", MathFuncs.get_sin, 0, (math.pi / 2), 16),
            ("а", MathFuncs.get_sin, 0, (math.pi / 2), 32),
            ("б", MathFuncs.get_atan, 0, 1, 16),
            ("б", MathFuncs.get_atan, 0, 1, 32)
        )
         ),
        (Simpsons, (
            ("а", MathFuncs.get_sqrt, 0, 4, 16),
            ("а", MathFuncs.get_sqrt, 0, 4, 32),
            ("а", lambda x: math.sqrt(1 + (3 * (x ** 2)) ** 2), 0, 1, 32),
            ("б", MathFuncs.get_log, 1, 3, 16),
            ("б", MathFuncs.get_log, 1, 3, 32),
            ("б", lambda x: math.sqrt(1 + (- math.cos(x)) ** 2), 0, math.pi, 32),
        )
         ),
    )

    for cls, values in test_data:
        print(cls.__doc__)
        for value in values:
            print(cls(*value).calculate())