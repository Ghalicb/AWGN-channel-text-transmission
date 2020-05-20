


def write_input(codewords, input_file):

    with open(input_file, 'w') as i_f:
        for codeword in codewords:
            for x in codeword:
                i_f.write(str(x) + ' ')



def read_output(output_file, codeword_size):

    with open(output_file) as o_f:
        return


#l = [[1, 1, 1, 1, -1, -1, -1, -1], [1, 1, 1, 1, -1, -1, -1, -1],
#     [-1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1]]
#write_input(l, 'test.txt')