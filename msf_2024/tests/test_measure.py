
import numpy as np
from msf_2024 import measure


def test_calculate_angle() -> None:
    rA = np.array([0, 0, 1])
    rB = np.array([0, 0, 0])
    rC = np.array([1, 0, 0])

    angle_deg = measure.calculate_angle(rA, rB, rC, degrees=True)
    assert angle_deg == 90.0

    angle_rad = measure.calculate_angle(rA, rB, rC, degrees=False)
    assert angle_rad == (np.pi/2)