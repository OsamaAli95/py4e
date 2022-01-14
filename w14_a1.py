import re

x = open('ActualData.txt')
y = list()
for line in x:
    line = re.findall('[0-9]+', line)
    y = y + line


sum = 0
for s in y:
    sum = sum + int(s)

print(sum)
