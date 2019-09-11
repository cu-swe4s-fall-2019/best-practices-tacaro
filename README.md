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

## basics_test.sh
Using this shell script, we can create tests for our column_stats.py program. basics_test.sh creates three text files:
* 6 columns, with random integers and the string "-e"
* 6 columns, with integer "1" and the string "-e"
* 7 columns, with alternating integers and strings

The script executes get_column_stats.py with a variety of column numbers to make sure that the program can still compute column statistics, even when non-integer values are present in the user-defined column.