# pyright: reportUnknownMemberType=false

# 単振り子の方程式を考えてみる．
# 運動方程式は以下のように書けるが
# theta''(t) + (g/l) * sin(theta(t)) = 0
# 初等関数で記述できないので，近似してやる．
# theta''(t) + (g/l) * theta(t) = 0
# これを解くと
# theta(t) = theta(0) * cos(sqrt(g/l) * t)
#
# 一方RK4で数値的に解くならば
# 二階の微分方程式を二つの一次の微分方程式に変換する必要がある．
# つまり，以下のように
# omega(t) = theta'(t)
# omega'(t) = - (g/l) * sin(theta(t))
# これで，各々の微分方程式を解く．

import math
from collections.abc import Generator
from pathlib import Path
from typing import Callable

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

SIMULATION_DT = 0.01


def derivatives(theta: float, omega: float, g: float, length: float) -> tuple[float, float]:
    """Return the time derivatives for the pendulum state."""

    return omega, -(g / length) * math.sin(theta)


def analytical_theta(time: float, theta0: float, g: float, length: float) -> float:
    """Return the analytical solution of the linearized pendulum equation."""

    return theta0 * math.cos(math.sqrt(g / length) * time)


def pendulum_states(
    fn: Callable[[float, float, float, float], tuple[float, float]],
    theta: float,
    omega: float,
    g: float,
    length: float,
    end_time: float,
) -> Generator[tuple[float, float, float], None, None]:
    """Yield pendulum states computed with RK4."""

    time = 0.0

    while time < end_time:
        k1_theta, k1_omega = fn(theta, omega, g, length)
        k2_theta, k2_omega = fn(
            theta + 0.5 * SIMULATION_DT * k1_theta,
            omega + 0.5 * SIMULATION_DT * k1_omega,
            g,
            length,
        )
        k3_theta, k3_omega = fn(
            theta + 0.5 * SIMULATION_DT * k2_theta,
            omega + 0.5 * SIMULATION_DT * k2_omega,
            g,
            length,
        )
        k4_theta, k4_omega = fn(
            theta + SIMULATION_DT * k3_theta,
            omega + SIMULATION_DT * k3_omega,
            g,
            length,
        )

        theta += SIMULATION_DT * (k1_theta + 2.0 * k2_theta + 2.0 * k3_theta + k4_theta) / 6.0
        omega += SIMULATION_DT * (k1_omega + 2.0 * k2_omega + 2.0 * k3_omega + k4_omega) / 6.0
        time += SIMULATION_DT
        yield time, theta, omega


def main():
    """Simulate a simple pendulum with RK4."""

    theta0 = math.radians(60.0)
    omega = 0.0
    g = 9.8
    length = 1.0
    end_time = 10
    times = [0.0]
    numerical_thetas = [theta0]
    analytical_thetas = [analytical_theta(0.0, theta0, g, length)]

    for time, theta, omega in pendulum_states(derivatives, theta0, omega, g, length, end_time):
        times.append(time)
        numerical_thetas.append(theta)
        analytical_thetas.append(analytical_theta(time, theta0, g, length))

    plt.figure(figsize=(8, 4))
    plt.plot(times, numerical_thetas, label="numerical (RK4)")
    plt.plot(times, analytical_thetas, label="analytical (linearized)", linestyle="--")
    plt.xlabel("time")
    plt.ylabel("theta")
    plt.title("Simple pendulum: numerical vs analytical")
    plt.grid(True, alpha=0.3)
    plt.legend()

    output_path = Path("notes/numerical/differential_equation/simple_pendulum.png")
    plt.tight_layout()
    output_path.parent.mkdir(parents=True, exist_ok=True)  
    plt.savefig(output_path)
    print(f"saved plot to {output_path}")


if __name__ == "__main__":
    main()
