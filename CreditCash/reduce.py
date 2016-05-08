#!/usr/bin/env python
import sys
previous_key = None
cash=0
card=0
total=0
for line in sys.stdin:
    key, value = line.split("\t")

    if not previous_key or previous_key == key:
        if value == "CSH":

            cash = cash + 1

        else:# value == "CRD":

            card = card + 1

    else:
        total = cash  + card
        print previous_key + "\t" + (cash/total)*100 + "," + (card/total)*100
        cash=0
        card=0
        if value == "CSH":

            cash = cash + 1

        else :#value == "CRD":

            card = card + 1
    previous_key = key

print previous_key + "\t" + (cash / total) * 100 + "," + (card / total) * 100
