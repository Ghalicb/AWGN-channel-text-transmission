import numpy as np


def decode():
    """

    """
    # Read the output

    # Mean of each repeated element in the output to get Y

    # Project the output
    # U = project_output(...)

    # Find the argmax of U
    # i = np.argmax(np.abs(U))
    # sign ----> to take into account when translating codeword

    # Return the symbol corresponding
    # return codeword_to_symbol(U[i], i)


def project_output(M, Y):
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