import numpy as np

import src.utility as utl
import src.parsing as prs
from src.constant import SIZE_H, REPETITIONS, OUTPUT_FILE


def decode():
    """
    Read the receiver output and decode its content to recover the list of symbols sent by the transmitter.

    Returns
    -------
    list_symbols :  list
                    The recovered symbols sent by the transmitter

    """
    codewords_rep = prs.read_output(OUTPUT_FILE, SIZE_H)
    codewords = average_codewords(codewords_rep, REPETITIONS)
    hadamard_matrix = utl.create_hadamard_matrix(SIZE_H)
    
    list_U = [utl.hadamard_multiplication(hadamard_matrix, y) for y in codewords]

    list_symbols = [recover_symbol(u)for u in list_U]

    return list_symbols


def average_codewords(codewords_rep, rep):
    """
    Perform an average between each repeated codeword in order to reduce the impact of the white gaussian noise.

    Parameters
    ----------
    codewords_rep : list
                    A list of codeword repeated a certain number of time

    rep :           int
                    Number of time each codeword is repeated

    Returns
    -------
    codewords :     list
                    A list of averaged codewords

    """
    codewords = []

    for i in range(0, len(codewords_rep), rep):
        codeword = np.mean(codewords_rep[i:i+rep], axis=0)
        codewords.append(codeword)

    return codewords


def recover_symbol(U):
    """
    Recover a symbol based on the projection of the associated noisy codeword in the Hadamard matrix.

    The elements of this projection indicate which column of the Hadamard matrix is the closest from the noisy codeword
    (high value for an element indicates high chance for the associated column of being the correct codeword).

    Parameters
    ----------
    U :         :py:class:`~numpy.ndarray`
                The projection of the noisy codeword

    Returns
    -------
    symbol :    char
                The guessed symbol
    """
    col = np.argmax(np.absolute(U))
    symbol = utl.col_to_symbol(col, np.sign(U[col]), U.shape[0])

    return symbol
