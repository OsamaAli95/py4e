name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

hours = list()

for line in handle:
    if line.startswith('From '):
        line = line.split()
        time = line[5]
        stime = time[:2]
        hours.append(stime)

counts = dict()

for hour in hours:
    counts[hour] = counts.get(hour,0)+1

for k,v in sorted(counts.items()) :
    print(k,v)
