# First Test File
(for i in `seq 1 100`; do 
    echo -e "$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM";
done )> data.txt

test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_exit_code python get_column_stats.py -i data.txt -c 1
assert_exit_code 0


run test_style_style pycodestyle style.py
assert_exit_code 0

run test_style_get_column_stats pycodestyle get_column_stats.py
assert_exit_code 0


# Second Test File
V=1
(for i in `seq 1 100`; do 
    echo -e "$V\t$V\t$V\t$V\t$V";
done )> data.txt

run test_rand_values python get_column_stats.py --input_file data.txt --column_num 2
assert_exit_code 0

# Third Test File
A=4
B="asdf"
(for i in `seq 1 100`; do 
    echo "$RANDOM\t$A\t$B\t$A\t$B\t$A\t$RANDOM";
done )> data.txt

run test_strings_present python get_column_stats.py --input_file data.txt --column_num 2
assert_exit_code 0
assert_in_stdout "The following values are not integers and were excluded:"

run test_mean_four python get_column_stats.py --input_file data.txt --column_num 1
assert_exit_code 0
assert_in_stdout "mean: 4.0"
assert_in_stdout "stdev: 0.0"

run test_nonexistent_file python get_column_stats.py -i nonexistentfile.txt -c 1
assert_exit_code 1
assert_in_stdout File does not exist, or you do not have correct permissions.