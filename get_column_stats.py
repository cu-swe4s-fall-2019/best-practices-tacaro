import sys
import math
import argparse

def Main():
    print("testing")
    parser = argparse.ArgumentParser(
                description='Open a file, generate stats of a given column',
                prog='bay')

    parser.add_argument('-i' #input file, from user
                        '--input_file',
                        type=str,
                        help="File Name: Tab Separated Files",
                        required=True)

    parser.add_argument('-c' #desired column, from user
                        '--column_number',
                        type=int,
                        help='Column number: which column would you like to read?',
                        required=True)

    args = parser.parse_args()
    file_name = args.input_file
    col_num = args.column_number

    f = open(file_name, 'r')

    V = []

    for l in f:
        A = [int(x) for x in l.split()]
        V.append(A[col_num])

    mean = sum(V)/len(V)

    stdev = math.sqrt(sum([(mean-x)**2 for x in V]) / len(V))

    print('mean:', mean)
    print('stdev:', stdev)
