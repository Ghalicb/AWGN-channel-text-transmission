

# ord('a') -> 97  (le numéro ascii de 'a')
# chr(97)  -> 'a' (le charactère associé au 98ème élément de la table ascii)

def symbol_to_codeword(symbol, size_H):
    """

    Function that receive a symbol and the number of row sin the Hadamard matrix and find the corresponding columns with his ascii. 

    Parameters

    symbol :    char
                The symbol for which we need to find the correspond column in the Hadamard matrix

   size_H :     int 
                The size N of the Hadamard matrix (number of rows or number of columns since sysmmetric)
    ----------


    Returns
    sign :      int 
                The sign that wiil be multipled with the selected column of the Hamard matrix (-1,1)
    
    index :     int 
                Return the index of the column that we have sleected (0 < index < N-1)     
    -------

    """
    num_ascii = ord(symbol)
    
    if(num_ascii <size_H):
        sign = 1
        index = num_ascii
    else:
        sign = -1
        index = num_ascii % size_H
    
    return sign, index





def codeword_to_symbol(size_H, sign, index):
    """

    Function that receive a sign and an index in the Hadamard matrix and return the corresponding symbol

    Parameters
    size_H :    int 
                The size N of the Hadamard matrix (number of rows or number of columns since sysmmetric)
    sign :      int {-1,1}
                The sign that wiil be multipled with the selected column of the Hamard matrix 
    index :     int [0, N-1]
                Return the index of the column that we have sleected
    ----------

    Returns
    symbol :    char
                The symbol founded with the sign and the columns index of the Hadamard matrix
    ------
   
    """
    if(sign == 1):
        symbol = chr(index+ size_H)
   
    else :
        symbol = chr(index)

    return symbol
