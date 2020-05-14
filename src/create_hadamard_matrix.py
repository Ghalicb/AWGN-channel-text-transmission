import math
import numpy as np

def create_hadamard_matrix(N):
    """
    Create a Hadamard matrix of size N.

    Parameters
    ----------
    N : int
        Size of the Hadamard matrix. (A power of 2)

    Returns
    -------
    H_i : :py:class:`~numpy.ndarray`
        A NxN Hadamard matrix.
    """

    if not math.log2(N).is_integer():
        raise ValueError("The size of a Hadamard matrix should be a power of 2.")

    # Create a Hadamard matrix of order 1
    H_i = np.ones(1, dtype=int)

    # Recursively construct Hadamard matrix of size 2^(i+1)
    for i in range(int(math.log2(N))):

        # H_i -> [H_i H_i ; H_i H_i]
        H_i = np.tile(H_i, (2,2))

        # [H_i H_i ; H_i H_i] -> [H_i H_i ; H_i -H_i]
        mid_index = int(2**i)
        H_i[mid_index:,mid_index:] = -1*H_i[mid_index:,mid_index:]

    return H_i