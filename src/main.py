import os

from encode import encode
from decode import decode
from parsing import read_message, write_guess
from constant import MESSAGE_FILE, INPUT_FILE, OUTPUT_FILE, GUESS_FILE


def main():
    """ Execute a full transmission of a text file through an Additive Gaussian Noise channel. """

    symbols = read_message(MESSAGE_FILE)
    encode(symbols)

    os.system('python3 ../client/client.py --input_file=' + INPUT_FILE +
              ' --output_file=' + OUTPUT_FILE + ' --srv_hostname=iscsrv72.epfl.ch --srv_port=80')

    recovered_symbols = decode()
    write_guess(recovered_symbols, GUESS_FILE)


if __name__ == "__main__":
    main()
