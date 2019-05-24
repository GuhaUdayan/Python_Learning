#
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
x = list()
for line in handle :
    if not line.startswith ("From ") : continue
    line.rstrip()
    words = line.split()
 #   print(line)
    if len(line) >= 7 :
          x.append(words[1])

#print(x)
for word  in x:
     counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word,count in counts.items() :
    if bigcount is None  or count > bigcount :
         bigword = word
         bigcount = count

print(bigword , bigcount)
