import sys

previous_key = None
total_trips = 0
average = 0.0
average = 365

for line in sys.stdin:
    key, value = line.split("\t")

    if not previous_key or previous_key == key:
        total_trips+=1
    else:
        average = total_trips/365
        print (previous_key+ "\t"+ str(average))
    previous_key = key

average = total_trips/365

print (previous_key+"\t"+str(average))