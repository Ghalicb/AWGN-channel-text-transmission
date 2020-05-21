"""
File containing all the necessary constant for this project
"""

"Size of the Hadamard matrix, allowing an alphabet of 2 * SIZE_H symbols for the message"
SIZE_H = 128

"Number of time we repeat a codeword to improve the chance of recovering it perfectly"
REPETITIONS = 1

"File path for the original message"
MESSAGE_FILE = '../res/message.txt'

"File path for the transmitter input"
INPUT_FILE = '../res/input.txt'

"File path for the receiver output"
OUTPUT_FILE = '../res/output.txt'

"File path for the guess"
GUESS_FILE = '../res/guess.txt'
