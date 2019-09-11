pycodestyle style.py

pycodestyle get_column_stats.py

(for i in `seq 1 100`; do 
    echo -e "$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM";
done )> data.txt

python get_column_stats.py --input_file data.txt --column_num 1


V=1
(for i in `seq 1 100`; do 
    echo -e "$V\t$V\t$V\t$V\t$V";
done )> data.txt

python get_column_stats.py --input_file data.txt --column_num 2

A=4
B="asdf"
(for i in `seq 1 100`; do 
    echo "$RANDOM\t$A\t$B\t$A\t$B\t$A\t$RANDOM";
done )> data.txt

python get_column_stats.py --input_file data.txt --column_num 2
python get_column_stats.py --input_file data.txt --column_num 1
python get_column_stats -i nonexistentfile.txt -c 1