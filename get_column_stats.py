import sys
import math
import argparse


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

    f = open(file_name, 'r')
    mean = "N/A"
    stdev = "N/A"
    V = []
    baddies = []

    for l in f:
        try:
            A = [x for x in l.split()]  # splits rows into individual elements
            V.append(int(A[col_num]))
        except ValueError:
            baddies.append(A[col_num])
            continue
        print(V)

    if len(V) != 0:
        mean = sum(V)/len(V)
        stdev = math.sqrt(sum([(mean-x)**2 for x in V]) / len(V))
    else:
        print("No workable values!")
    if len(baddies) != 0:
        print("The following values are not integers and were excluded:")
        print(baddies)

    print('mean:', mean)
    print('stdev:', stdev)


if __name__ == "__main__":
    main()
