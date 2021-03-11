# SI 206
# HW6 - Regular Expressions
# Name:
# Who did you work with:　

import re
import os
import unittest

def read_file(filename):
    """ Return a list of the lines in the file with the passed filename """

    # Open the file and get the file object
    source_dir = os.path.dirname(__file__) #<-- directory name
    full_path = os.path.join(source_dir, filename)
    infile = open(full_path,'r', encoding='utf-8')

    # Read the lines from the file object into a list
    lines = infile.readlines()

    # Close the file object
    infile.close()

    # return the list of lines
    return lines


def find_time(string_list):
    """ Return a list of valid times from the list of strings.
        string_list -- the name of the file to read from
        return -- the list of all times from a list of strings
    """
    pass



def find_urls(string_list):

    """ Return a list of valid urls in the list of strings """

    pass


def find_dates(string_list):
    """ Return a list of dates in the list of strings """

    pass

def find_underscore(string_list):
    """returns a list of words containted in underscores like _example_ """
    pass

## Extra credit
def count_char(string_list, char):
    """  return a count of the number of times a specified character appears in a list of strings.
        It should match the character when it starts or ends a word
        (It should not match any characters in the middle of a word)

        string_list -- the list of strings to count the char in
        char -- the character to look for
        return -- a count of the number of times the word or its plural appears in the file
    """

    pass


# Implement your own tests.
class TestAllMethods(unittest.TestCase):


    def test_find_times(self):
        pass

    def test_find_urls(self):
        pass

    def test_find_dates(self):
        pass


    def test_find_underscore(self):
        pass

    def test_count_char(self):
        pass



def main():
	# Use main to test your function.
    # Run unit tests, but feel free to run any additional functions you need
	unittest.main(verbosity = 2)

if __name__ == "__main__":
	main()