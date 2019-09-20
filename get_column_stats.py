import sys
import math
import argparse
import unittest


def mean(V):
    """
    Compute the arithmetic mean of an array
    Parameters
    ----------
    V : list of int
        Non-empty array containing values of which to compute mean

    Returns
    --------
    m
        The arithmetic mean of array V
    """
    good_vals = []
    bad_mn_vals = []
    for i in V:
        try:
            good_vals.append(int(i))
        except ValueError:
            bad_mn_vals.append(i)
            continue

    if len(good_vals) < 1:
        print(good_vals)
        print(bad_mn_vals)
        raise ValueError("Can't give mean of zero values!")

    mn = sum(good_vals)/len(good_vals)
    if len(bad_mn_vals) > 0:
        print("The following values were non-numerical and excluded:")
        print(bad_mn_vals)
    return mn


def stdev(V):
    """
    The standard deviation of a list of values
    Parameters
    -----------
    V : list of int
        Non-empty array containing values of which to compute stdev

    Returns
    --------
    std
        Standard deviation of the values in V

    """
    good_vals = []
    bad_mn_vals = []
    for i in V:
        try:
            good_vals.append(int(i))
        except ValueError:
            bad_mn_vals.append(i)
            continue

    if len(V) < 2:
        raise ValueError("Standard Deviation requires at least 2 data points!")
    std = math.sqrt(sum([(mean(good_vals)-x)**2 for x in good_vals]) /
                    len(good_vals))
    return std


def main():
    parser = argparse.ArgumentParser(
                description='Open a file, generate stats of a given column',
                prog='bay')

    parser.add_argument('-i',  # input file, from user
                        '--input_file',
                        type=str,
                        help="File Name: Tab Separated Files",
                        required=True)

    parser.add_argument('-c',  # desired column, from user
                        '--column_number',
                        type=int,
                        help='Column number: which column to read?',
                        required=True)

    args = parser.parse_args()
    file_name = args.input_file
    col_num = args.column_number

    try:  # first, we need to make sure the file exists/permitted
        f = open(file_name, 'r')
    except FileNotFoundError:
        print("File does not exist, or you do not have correct permissions.")
        sys.exit(1)  # sets the exit code!

    V = []
    bad_vals = []
    reported_mean = None
    reported_stdev = None

    for l in f:
        try:
            A = [x for x in l.split()]  # splits rows into individual elements
            V.append(int(A[col_num]))
        except ValueError:
            print(col_num)
            bad_vals.append(A[col_num])  # we're dumping bad vals into a list
            continue

    if len(V) != 0:
        if all(isinstance(i, int) for i in V):
            print(V)
            reported_mean = mean(V)
            reported_stdev = stdev(V)
        else:
            print("Something isn't an integer here!")
    else:
        print("No workable values!")

    if len(bad_vals) != 0:
        print("The following values are not integers and were excluded:")
        print(bad_vals)

    print('mean:', reported_mean)
    print('stdev:', reported_stdev)


if __name__ == "__main__":
    main()
