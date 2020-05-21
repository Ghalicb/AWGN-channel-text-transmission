import numpy as np

import utility as utl
import parsing as prs
from constant import SIZE_H, REPETITIONS, INPUT_FILE


def encode(list_symbols):
    """
    Encode a list of symbols into codewords and write them in a predefined file, ready to be send by the transmitter.

    Parameters
    ----------
    list_symbols :  list
                    A list of symbol to encode

    """
    list_col = [utl.symbol_to_col(s, SIZE_H) for s in list_symbols]
    hadamard_matrix = utl.create_hadamard_matrix(SIZE_H)

    list_codewords = []
    for t in list_col:
        codeword_rep = create_codeword(t[1], t[0], hadamard_matrix, REPETITIONS)
        for c in codeword_rep:
            list_codewords.append(c)

    prs.write_input(list_codewords, INPUT_FILE)


def create_codeword(index, sign, H_matrix, rep=1):
    """
    Create a codeword based on the column and the sign of a Hadamard matrix.
    This codeword can be repeated multiple time.

    Parameters
    ----------
    index :     int [0, N-1]
                The index of the column we want to retrieve in the Hadamard matrix

    sign :      int {-1, 1}
                The sign of the column we retrieve

    H_matrix :  :py:class:`~numpy.ndarray`
                A NxN Hadamard matrix

    rep :       int
                The number of time we repeat the codeword (by default we do not repeat the codeword)

    Returns
    -------
    rep_col_H : list
                A list containing repeated copy of a codeword

    """
    col_H = sign * H_matrix[:, index]
    rep_col_H = [list(col_H) for _ in range(rep)]
    return rep_col_H
