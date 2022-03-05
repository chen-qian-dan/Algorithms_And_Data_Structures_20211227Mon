"""
ReadMe:
run on terminal : % ./run.sh "Input/close_prices.csv" 3 9 "output.csv"

"""


#!/bin/sh
CWD="$(pwd)"
python3 build.py $1 $2 $3 $4