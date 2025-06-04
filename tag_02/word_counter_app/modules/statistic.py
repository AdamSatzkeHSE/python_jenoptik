# Autor:
# Date:
# Zweck:

import numpy as np
import pandas as pd

""" Funktionen """
def max_word(dictionary):
    return max(dictionary)

def durchschnitt(dictionary):
    return np.mean(dictionary.values())

def std_dev(dictionary):
    return np.std_dev(dictionary.values())