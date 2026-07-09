from typing import Callable, TypeAlias

fn: TypeAlias = Callable[[float, float], float]


def generateSolver(fn: fn, t: float, y: float, max: float, h: float = 0.1):
    while t < max:
        gradient = fn(t, y)
        y = y + h * gradient
        yield t, y
        t += h


def main():
    print("y(t)の関数値")
    for t, y in generateSolver(lambda _, y: -y, 0, 1, 1):
        print(f"{t:3f}, {y:3f}")
    # この微分方程式は dy/dt = -y であり、初期条件 y(0) = 1。特殊解は y(t) = e^(-t)。


if __name__ == "__main__":
    main()
