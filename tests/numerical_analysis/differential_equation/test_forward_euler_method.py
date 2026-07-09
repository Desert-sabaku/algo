"""Tests for forward Euler method solver."""

from numerical_analysis.differential_equation.forward_euler_method import generateSolver


def test_generate_solver_linear_decay_steps() -> None:
    """Forward Euler follows y_{n+1}=y_n+h*f(t_n, y_n)."""
    points = list(generateSolver(lambda _t, y: -y, 0.0, 1.0, 0.3, h=0.1))

    assert len(points) == 3
    assert points[0] == (0.1, 0.9)
    assert points[1] == (0.2, 0.81)
    assert points[2] == (0.30000000000000004, 0.7290000000000001)


def test_generate_solver_empty_when_at_t_max() -> None:
    """No values are yielded when start time is already at limit."""
    points = list(generateSolver(lambda _t, y: y, 1.0, 2.0, 1.0))
    assert points == []
