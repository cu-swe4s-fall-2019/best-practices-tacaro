import sys
import math
import argparse


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
    sum(V)/len(V)
    return m


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
    math.sqrt(sum([(mean-x)**2 for x in V]) / len(V))
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

    mean = "N/A"  # setting N/A to default value
    stdev = "N/A"
    V = []
    bad_vals = []

    for l in f:
        try:
            A = [x for x in l.split()]  # splits rows into individual elements
            V.append(int(A[col_num]))
        except ValueError:
            bad_vals.append(A[col_num])  # we're dumping bad vals into a list
            continue
        print(V)

    if len(V) != 0:
        mean = sum(V)/len(V)
        stdev = math.sqrt(sum([(mean-x)**2 for x in V]) / len(V))
    else:
        print("No workable values!")
    if len(bad_vals) != 0:
        print("The following values are not integers and were excluded:")
        print(bad_vals)

    print('mean:', mean)
    print('stdev:', stdev)


if __name__ == "__main__":
    main()
