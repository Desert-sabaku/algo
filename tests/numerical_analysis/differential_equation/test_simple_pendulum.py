"""Tests for simple pendulum numerical helpers."""

import math

import pytest

from numerical_analysis.differential_equation.simple_pendulum import (
    SIMULATION_DT,
    analytical_theta,
    derivatives,
    pendulum_states,
)


def test_derivatives_follow_pendulum_equation() -> None:
    """Derivative helper returns expected theta' and omega'."""
    theta_dot, omega_dot = derivatives(theta=0.2, omega=0.5, g=9.8, length=2.0)

    assert theta_dot == 0.5
    assert omega_dot == pytest.approx(-(9.8 / 2.0) * math.sin(0.2))


def test_analytical_theta_at_zero_time_is_initial_angle() -> None:
    """Linearized analytical solution keeps initial angle at t=0."""
    theta0 = math.radians(20.0)
    theta = analytical_theta(time=0.0, theta0=theta0, g=9.8, length=1.0)
    assert theta == theta0


def test_pendulum_states_progresses_time_by_fixed_dt() -> None:
    """RK4 pendulum generator advances time by SIMULATION_DT."""
    states = list(
        pendulum_states(
            fn=derivatives,
            theta=math.radians(10.0),
            omega=0.0,
            g=9.8,
            length=1.0,
            end_time=0.03,
        )
    )

    assert len(states) == 3
    assert states[0][0] == pytest.approx(SIMULATION_DT)
    assert states[1][0] == pytest.approx(2 * SIMULATION_DT)
    assert states[2][0] == pytest.approx(3 * SIMULATION_DT)
