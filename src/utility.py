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


def hadamard_multiplication(M, Y):
    """
    Use the property of the Hadamard matrix to efficiently compute M @ Y.

    This operation can be seen as a projection of Y into the basis formed
    by the columns/rows of M (as Hadamard matrices are symmetric).

    As Hadamard matrices have orthogonal columns, the resulting vector U
    gives information on which column of M is closest to Y.

    Parameters
    ----------
    M : :py:class:`~numpy.ndarray`
        A Hadamard matrix (of size NxN).

    Y : :py:class:`~numpy.ndarry`
        A vector corresponding to the channel output (of size Nx1).

    Returns
    -------
    U : :py:class:`~numpy.ndarray`
        A vector corresponding to Y written in the basis formed by M (of size Nx1).
    """
    middle_index = int(M.shape[0] / 2)
    M_quarter = M[:middle_index, :middle_index]
    Y_top = Y[:middle_index]
    Y_bot = Y[middle_index:]

    A = M_quarter @ Y_top
    B = M_quarter @ Y_bot

    U = np.concatenate((A+B, A-B))

    return U


def symbol_to_col(symbol, size_H):
    """
    Convert a symbol into its codeword - the column associated in the Hadamard matrix.

    We arbitrarily choose that each ascii symbol's index will directly be associated
    to the index of the column in the Hadamard matrix.

    Parameters
    ----------
    symbol :    char
                The symbol for which we need to find the correspond column in the Hadamard matrix

    size_H :    int
                The size N of the Hadamard matrix (number of rows or number of columns since sysmmetric)

    Returns
    -------
    sign :      int {-1,1}
                The sign that will be multiplied with the selected column of the Hadamard matrix

    index :     int [0, N-1]
                The index of the column corresponding to the given symbol
    """
    num_ascii = ord(symbol)

    index = num_ascii % size_H
    sign = 1 if (num_ascii < size_H) else -1

    return sign, index


def col_to_symbol(index, sign, size_H):
    """
    Convert a codeword - a column of the Hadamard matrix - in the symbol associated to it.

    Parameters
    ----------
    index :     int [0, N-1]
                The index of the column in the Hadamard matrix
    sign :      int {-1,1}
                The sign that will be multiplied with the selected column of the Hadamard matrix
    size_H :    int
                The size N of the Hadamard matrix (number of rows or number of columns since symmetric)

    Returns
    ----------
    symbol :    char
                The symbol associated with the sign and the columns index of the Hadamard matrix

    """
    symbol = chr(index) if (sign == 1) else chr(index + size_H)
    return symbol
