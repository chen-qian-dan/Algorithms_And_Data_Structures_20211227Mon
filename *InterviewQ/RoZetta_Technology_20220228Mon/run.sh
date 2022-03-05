
# ReadMe:
# run on terminal : % ./run.sh "Input/close_prices.csv" 3 9 "output.csv"
# % ./run.sh '/Users/qianchen/Documents/QC21_03_DOING/github_20210115Fri/Algorithms_And_Data_Structures_20211227Mon/*InterviewQ/RoZetta_Technology_20220228Mon/Input/close_prices.csv' 3 9 "output.csv"




#!/bin/sh
CWD="$(pwd)"
python3 ./source/build.py $1 $2 $3 $4