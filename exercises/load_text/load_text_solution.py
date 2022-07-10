"""
© 2001-2022, Enthought, Inc.
All Rights Reserved. Use only permitted under license. Copying, sharing, redistributing or other unauthorized use strictly prohibited.
All trademarks and registered trademarks are the property of their respective owners.
Enthought, Inc.
200 W Cesar Chavez Suite 202
Austin, TX 78701
www.enthought.com


Load Array from Text File
-------------------------

0. From the IPython prompt, type::

        In [1]: loadtxt?

   to see the options on how to use the loadtxt command.


1. Use loadtxt to load in a 2D array of floating point values from
   'float_data.txt'.  The data in the file looks like::

        1 2 3 4
        5 6 7 8

   The resulting data should be a 2x4 array of floating point values.

2. In the second example, the file 'float_data_with_header.txt' has
   strings as column names in the first row::

        c1 c2 c3 c4
         1  2  3  4
         5  6  7  8

   Ignore these column names, and read the remainder of the data into
   a 2D array.

   Later on, we'll learn how to create a "structured array" using
   these column names to create fields within an array.

Bonus
~~~~~

3. A third example is more involved. It contains comments in multiple
   locations, uses multiple formats, and includes a useless column to
   skip::

    -- THIS IS THE BEGINNING OF THE FILE --
    % This is a more complex file to read!

    % Day,  Month,  Year, Useless Col, Avg Power
       01,     01,  2000,      ad766,         30
       02,     01,  2000,       t873,         41
    % we don't have Jan 03rd!
       04,     01,  2000,       r441,         55
       05,     01,  2000,       s345,         78
       06,     01,  2000,       x273,        134 % that day was crazy
       07,     01,  2000,       x355,         42

    %-- THIS IS THE END OF THE FILE --
"""

from numpy import loadtxt

#############################################################################
# 1. Simple example loading a 2x4 array of floats from a file.
#############################################################################
ary1 = loadtxt('float_data.txt')

print('example 1:')
print(ary1)


#############################################################################
# 2. Same example, but skipping the first row of column headers
#############################################################################
ary2 = loadtxt('float_data_with_header.txt', skiprows=1)

print('example 2:')
print(ary2)

#############################################################################
# 3. More complex example with comments and columns to skip
#############################################################################
def head(filename, n_lines=10, show_lines=False):
    """
    Print the first n_lines of a file.
    Parameters
    ----------
    filename : str
        The path to the file that should be parsed.
    n_lines : int, default: 10
        The number of lines to parse from the file.
    show_lines : bool, default: False
        Whether or not to show the line number of each parsed line.
    """
    with open(filename) as f:
        for i, line in zip(range(n_lines), f):
            print(i, line.strip()) if show_lines else print(line.strip())

print(head("complex_data_file.txt"))

ary3 = loadtxt("complex_data_file.txt", delimiter=",", comments="%",
               usecols=(0, 1, 2, 4), dtype=int, skiprows=1)

print('example 3:')
print(ary3)
