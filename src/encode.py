import numpy as np
import create_hadamard_matrix as chm
import symbol_codeword_translation as sct

SIZE_H = 128
REPETITIONS = 1


def read_text(given_text):
    """
    Parameters
    ----------
    Returns

    -------
    """
    return list(open(given_text, "r"))


def encode(list_symbols, intput_file):
    """
    Parameters
    ----------
    Returns

    -------
    """

    list_col = [sct.symbol_to_col(s, SIZE_H) for s in list_symbols]

    hadamard_matrix = chm.create_hadamard_matrix(SIZE_H)

    list_codewords = [create_codewords(t[1], t[0], REPETITIONS, hadamard_matrix) for t in list_col]

    # Fonction de Ghali
    write_input(list_codewords, input_file)


def create_codewords(index, sign, N, H_matrix):
    """
    Parameters
    ----------
    Returns

    -------
    """

    col_H = sign * H_matrix[:, index]

    return np.repeat(col_H, N)
