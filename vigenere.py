# Filename: vigenere.py
# Author: MATH 4175 Group 7 (Andrew Tran, Anthony Tran, Jack Greer, Jason Pak, Michael Peters)
# Date: 23 Sep 2022 (Date Last Modified: 23 Sep 2022, Jack Greer)
# Description: This file contains a Python algorithm that can decrypt a Vigenere cipher.

# Given a text string, return the frequency of each letter in that string
def get_frequency(txt_string):
    # Create list which contains frequency of each letter (consider making this a map)
    alphabet_frequency = [] * 26
    # TODO: Iterate through text string, and fill out alphabet_frequency[]
    return alphabet_frequency

# Given a text string, 
def get_index_of_coincidence(txt_string):
    alphabet_freq = get_frequency(txt_string)

    # Numerator: Sum of nC2 for each letter (e.g. if txt_string = "AABBBC", num = (2*1) + (3*2) + (1*0) = 8)
    numerator = 0
    for i in range(alphabet_freq):
        numerator += alphabet_freq[i] * (alphabet_freq[i] - 1)
    
    # TODO: get proper length function fr
    denominator = length(txt_string) * (length(txt_string) - 1)

    return (numerator / denominator)