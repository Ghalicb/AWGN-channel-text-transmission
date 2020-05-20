import numpy as np


def encode():





def create_input_vector(index, sign, N, H_matrix):
    """
    Parameters

    ----------
    Returns

    -------

    """

    col_H = sign * H_matrix[:, index]

    return np.repeat(col_H, N)