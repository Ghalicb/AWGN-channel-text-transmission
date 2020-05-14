"""
To estimate the first two moments of the noise in the channel :

    1. Fill the file input.txt with many "0 0 ... 0 0" (not too much or it will raise an error)
    2. Execute the client/client.py (see instructions in client.py file + be connected to the EPFL network)
    3. Execute estimate_channel_noise.py
"""

import numpy as np


def estimate_channel_noise():
    """
    Estimate the mean and the variance of the noise in the given channel (using the values in output.txt).
    """
    output_list = [float(line.rstrip('\n')) for line in open("res/output.txt")]
    (mean, variance) = (np.mean(output_list), np.std(output_list)**2)

    print("\nMean: {}   Variance: {}\n".format(mean, variance))


estimate_channel_noise()