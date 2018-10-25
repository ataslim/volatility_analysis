#!/usr/bin/env python
#
#
for i in ${1}/*.csv
do
    rm -f tmpfile.txt
    new_file=`echo ${i} | sed -e 's/csv/png/g'`
    cat ${i} | python ./normalize_for_heatmap.py > tmpfile.txt
    ./ipv4-heatmap < tmpfile.txt
    mv map.png ${new_file}
    rm -f tmpfile.txt
done
