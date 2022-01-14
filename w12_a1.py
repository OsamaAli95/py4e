name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

# create an empty list to store "From " lines
words = list()

#loop through the file to get the email addresses and add them to the list
for line in handle:
    if line.startswith('From '):
        line = line.split()
        words.append(line[1])
        
# create an empty dictionary
count = dict()

# loop through the dictionary to get the values of the keys
for word in words:
    count[word] = count.get(word, 0) + 1

# find the most prolific committer.
bigcount = None
bigword = None

for k,v in count.items():
    if bigcount is None or v > bigcount:
        bigcount = v
        bigword = k

print(bigword, bigcount)
