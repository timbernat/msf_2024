"""
Functions related to measurement
"""

import numpy as np


def calculate_distance(rA: np.ndarray, rB: np.ndarray) -> float:
    """This function calculates the distance between two points given as numpy arrays."""
    d = rA - rB
    dist = np.linalg.norm(d)
    dist = float(dist)

    return dist


def calculate_angle(
    rA: np.ndarray, rB: np.ndarray, rC: np.ndarray, degrees: bool = False
) -> float:
    """Calculate the angle between three points. Answer is given in radians by default, but can be given in degrees by setting degrees=True"""
    AB = rB - rA
    BC = rB - rC
    theta = np.arccos(np.dot(AB, BC) / (np.linalg.norm(AB) * np.linalg.norm(BC)))

    if degrees:
        return np.degrees(theta)
    else:
        return theta
