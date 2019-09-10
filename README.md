# best-practices
## style.py
This is an example file showing code that complies with the PEP8 style guide.

## get_column_stats.py
This script takes in a tab separated text (.txt) file and computes the mean and stdev of a single column that is specified by the user.
get_column_stats.py takes two arguments:
--input_file (-i): a .txt file with tab separated values
--column_number (-c): an integer value representing the column the user would like to summarize. Uses zero index.

## basics_test.sh
A shell script that runs two tests on get_column_stats. The first uses a test file, data.txt, that is composed of random integers. The second uses a test file, also data.txt, that is composed exclusively of the integer 1. The first column of both test files is "-e" as a test that the program can handle strings without breaking.