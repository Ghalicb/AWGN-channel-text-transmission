import numpy as np


def read_message(message_file):
    """
    Read the given message and store each characters in a list.

    Parameters
    ----------
    message_file :  string
                    File path containing the message to read

    Returns
    -------
    chars :         list
                    A list containing each character of the message
    """
    chars = []

    with open(message_file) as f:
        for line in f:
            for char in line:
                chars.append(char)

    return chars


def write_input(codewords, input_file):
    """
    Write a list of codewords in the given input file.

    Parameters
    ----------
    codewords :     list
                    A list of codewords, each containing N elements in {-1, 1}

    input_file:     string
                    Name of the file where the codewords will be stored
    """
    with open(input_file, 'w') as f:
        for codeword in codewords:
            for x in codeword:
                f.write(str(x) + ' ')


def read_output(output_file, codeword_size):
    """
    Read the output and store it as a list of codeword.

    It raises an error if the length of the content of output_file is not a multiple of codeword_size.

    Parameters
    ----------
    output_file :   string
                    File path containing the output of the receiver
    codeword_size : int
                    The size of the codeword that were used to encode the original symbols

    Returns
    -------
    codewords :     list
                    A list containing each codeword received
    """

    with open(output_file) as f:
        xs = ' '.join(str(elem) for elem in list(f))

    codewords = np.array(xs.split()).reshape((-1, codeword_size))

    return codewords


def write_guess(list_symbols, guess_file):
    """
    Write the recovered message in a file.

    Parameters
    ----------
    list_symbols :  list
                    A list of recovered symbols

    guess_file:     string
                    Name of the file where the recovered message will be stored
    """
    string = ''.join(list_symbols)

    with open(guess_file, 'w') as f:
        f.writelines(string)
