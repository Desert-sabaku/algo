from typing import Callable, TypeAlias

fn: TypeAlias = Callable[[float, float], float]


def generateSolver(fn: fn, t: float, y: float, max: float, h: float = 0.1):
    while t < max:
        k1 = fn(t, y)
        k2 = fn(t + h / 2, y + h * k1 / 2)
        k3 = fn(t + h / 2, y + h * k2 / 2)
        k4 = fn(t + h, y + h * k3)
        y = y + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        yield t, y
        t += h


def main():
    print("y(t)の関数値")
    for t, y in generateSolver(lambda _, y: -y, 0, 1, 1):
        print(f"y({t:3f})={y:3f}")
    # この微分方程式は dy/dt = -y であり、初期条件 y(0) = 1。特殊解は y(t) = e^(-t)。


if __name__ == "__main__":
    main()
