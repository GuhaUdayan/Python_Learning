fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
i = 0
unique = list()
for line in fh :
       if not line.startswith("From") : continue
       line.rstrip()
       words = line.split()
      # print(words)
       if len(words) < 6 : continue

       print(words[1])
       count = count + 1


print("There were", count, "lines in the file with From as the first word")
