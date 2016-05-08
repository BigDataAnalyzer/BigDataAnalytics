#!/usr/bin/env python
import sys

previous_key = None
count = 0
for line in sys.stdin:
    key,value = line.strip().split("\t")
    if not previous_key or previous_key==key:
        count+=1
    else:
        print previous_key+"\t"+str(count)
        count = 1
    previous_key = key
if previous_key:
    print previous_key+"\t"+str(count)
