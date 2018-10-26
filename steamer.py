#!/usr/bin/env python3
# Import regular expressions
import re
# steamer function
def steamer(incoming):
    #Colour Codes
    col_gr = '\033[92m'
    col_db = '\033[94m'
    col_lb = '\033[93m'
    col_no = '\033[0m'
    #Regular Expressions
    square_start = re.compile(r'^Square.*')
    grains_start = re.compile(r'^That\'s.*')
    other_stuff_start = re.compile(r' - .*')
    colour_end = re.compile(r'ice\.$|rve\.$|ess\.$|ths\.$|ngs\.$|ics\.$|tal\.$')
    #The Business End
    square = square_start.search(incoming)
    if square != None:
        square_output = col_gr + square.group() + col_no
        print(square_output)
    grains = grains_start.search(incoming)
    if grains != None:
        grains_output = col_db + grains.group() + col_db
        print(grains_output)
    other_stuff = other_stuff_start.search(incoming)
    if other_stuff != None:
        other_stuff_output = col_lb + other_stuff.group() + col_no
        print(other_stuff_output)