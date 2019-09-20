# best-practices

Here we demonstrate the best practices of python coding. We use a script that takes a tab separated array of values in order to compute the mean and standard deviation of a given column.

## style.py
This is an example file showing code that complies with the PEP8 style guide.

## get_column_stats.py
This script takes in a tab separated text (.txt) file and computes the mean and stdev of a single column that is specified by the user.

**Usage**
get_column_stats uses built-in python libraries _sys_, _math_, and _argparse_

get_column_stats.py takes two arguments:
--input_file (-i): a .txt file with tab separated values
--column_number (-c): an integer value representing the column the user would like to summarize. Uses zero index.

If a value in the user specified column is not an integer, the program will move it to a list _bad_vals_, which will be printed at the end of the calculation for user reference.

## basics_test.py (vew with v2.0)
Implements python unittests for the mean and standard deviation methods contained within get_column_stats.py. The script checks whether the mean() and stdev() methods can handle a variety of inputs, and whether they handle exceptions correctly, instead of passing them to the user.

## basics_test.sh
basics_test.sh tests the integrity of our code. First, it asks whether both style.py and get_column_stats.py conform to PEP8 style guides by using pycodestyle.

After completing this (and printing any pycodestyle errors that may arise) the script creates tests for our column_stats.py program.

The script executes get_column_stats.py with a variety of column numbers to make sure that the program can still compute column statistics, even when non-integer values are present in the user-defined column. The final test ensures that the program handles the FileNotFoundError exception.

# Installation
The basics_test.sh shell script uses pycodestyle to check that the python code utilized conforms to the PEP8 style guide. You can install, upgrade, and uninstall *pycodestyle.py* with these commands:
`pip install pycodestyle
pip install --upgrade pycodestyle
pip uninstall pycodestyle`

As of v2.0, the basics_test.sh shell script uses Stupid Simple baSH Testing. To install, enter the following into the command line:
`test -e ssshtest || wget -qhttps://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest 
. ssshtest`

get_column_stats.py does not require any installation, as it uses built-in python libraries _sys_, _math_, and _argparse_.