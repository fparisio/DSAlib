"""A test module."""

import numpy as np


def my_func(arr: np.ndarray) -> np.ndarray:
    """Add 1 to each element of the array.

    Parameters
    ----------
    arr : np.ndarray
        Input array.

    Returns
    -------
    np.ndarray
        Output array.
    """
    return arr + 1
