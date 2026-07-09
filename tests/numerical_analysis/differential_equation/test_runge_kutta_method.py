"""Tests for RK4 solver module."""

import importlib.util
import math
from pathlib import Path


def _load_runge_kutta_module():
    module_path = (
        Path(__file__).resolve().parents[3]
        / "src"
        / "numerical_analysis"
        / "differential_equation"
        / "Runge-Kutta_method.py"
    )
    spec = importlib.util.spec_from_file_location("runge_kutta_method", module_path)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_rk4_solver_matches_exp_decay() -> None:
    """RK4 remains close to the analytical y(t)=e^(-t) for dy/dt=-y."""
    module = _load_runge_kutta_module()
    points = list(module.generateSolver(lambda _t, y: -y, 0.0, 1.0, 0.3, h=0.1))

    assert len(points) == 3
    assert points[0][0] == 0.1
    assert points[1][0] == 0.2
    assert points[2][0] == 0.30000000000000004
    assert math.isclose(points[0][1], math.exp(-0.1), rel_tol=1e-6)
    assert math.isclose(points[1][1], math.exp(-0.2), rel_tol=1e-6)
    assert math.isclose(points[2][1], math.exp(-0.3), rel_tol=1e-6)
