#!/usr/bin/env bash

# User arguments 
first_week=${1}
last_week=${2}
bit_width=${3}
destination=${4}

# Constants
year=2018
data_dir="data/full_sets/full.${year}-W"

i=${first_week}
while [[ ${i} -lt ${last_week} ]]
do
w1_numeric=`printf %02d ${i}`
w2_numeric=`printf %02d $[ ${i} + 1 ]`
s1="${data_dir}${w1_numeric}.set"
s2="${data_dir}${w2_numeric}.set"
dfile="${destination}/volatility.${bit_width}.${year}.${w2_numeric}.csv"
echo "Calculating data to output to ${dfile}"
python ./calculate_weekly_map.py ${bit_width} ${s1} ${s2} > ${dfile}
i=$[ ${i} + 1 ]
done
