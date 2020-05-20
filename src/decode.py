import numpy as np
import symbol_codeword_translation as sct
import create_hadamard_matrix as chm

def write_guess(list_symbols, guess_file):
    """
    Parameters

    ----------
    Returns
   
    -------

    """
    x = ' '
    string = x.join(list_symbols)
    file = open(guess_file,"w") 
    file.writelines(string) 
    file.close() 

def decode(output_file, size_codewords, repetition):
    """
    Parameters

    ----------
    Returns
   
    -------

    """
    list_vectors_rep = read_output(output_file, size_codewords)

    list_vectors = [retrieve_output_vector(v, repetition) for v in list_vectors_rep]

    hadamard_matrix = chm.create_hadamard_matrix(len(list_vectors[0]))
    
    list_U = [ hadamard_multiplication(hadamard_matrix, y) for y in list_vectors]

    list_symbols = [retrieve_symbol(u)for u in list_U]

    return list_symbols


def retrieve_output_vector(vect, N):
    """
    Parameters

    ----------
    Returns
   
    -------

    """
    len_chunks = len(vect)/N
    if(type(len_chunks)== float):
        print('Error in retrieve_input_vector : N is not a multiple of the length of the vector.')
    vector_array = np.array([vect[i:i + len_chunks] for i in range(0, len(vect),len_chunks)])

    return np.mean(vector_array, axis = 1)


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

def retrieve_symbol(U):
    
    """

    Parameters
    ----------

    Returns
    -------

    """

    axis = np.argmax( np.absolute(U))
    symbol = sct.col_to_symbol(U.shape[0], np.sign(U[axis]), axis)

    return symbol


