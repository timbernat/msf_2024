import numpy as np
import pytest

from msf_2024.molecule import build_bond_list


@pytest.fixture
def methane_molecule() -> np.ndarray:
    return np.array([
        [ 1.0, 1.0,  1.0],
        [ 2.4, 1.0,  1.0],
        [-0.4, 1.0,  1.0],
        [ 1.0, 1.0,  2.4],
        [ 1.0, 1.0, -0.4]
    ])

@pytest.fixture
def distances(methane_molecule) -> np.ndarray:
    from scipy.spatial.distance import cdist
    
    return cdist(methane_molecule, methane_molecule, metric='euclidean')

def test_build_bond_list(methane_molecule) -> None:
    bonds = build_bond_list(methane_molecule)

    assert len(bonds) == (len(methane_molecule) - 1) # 4 bonds
    for bond_len in bonds.values():
        assert pytest.approx(bond_len) == 1.4 # each length should be 1.4 angstrom

@pytest.mark.parametrize("max_bond", [-1])
@pytest.mark.parametrize("min_bond", [-1])
def test_build_bond_list_neg_values(methane_molecule, max_bond, min_bond) -> None:
    with pytest.raises(ValueError):
        _ = build_bond_list(methane_molecule, min_bond=min_bond, max_bond=max_bond) # EXPECT negative lengths to fail

@pytest.mark.parametrize("max_bond", np.linspace(1, 5, num=4))
@pytest.mark.parametrize("min_bond", np.linspace(1, 5, num=4))
def test_correct_bond_lengths(methane_molecule, max_bond, min_bond) -> None:
    _ = build_bond_list(methane_molecule, min_bond=min_bond, max_bond=max_bond) # EXPECT negative lengths to fail