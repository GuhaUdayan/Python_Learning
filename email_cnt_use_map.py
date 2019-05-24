#use input file mbox_short.txt to identify all emails "From" and get the maximum count of them using dict

# # QUESTION: Write a program to read through the mbox-short.txt
# and figure out who has sent the greatest number of mail messages.
#  The program looks for 'From ' lines and takes the second word of those lines as
#   the person who sent the mail.
#    The program creates a Python dictionary that maps the sender's mail address
#     to a count of the number of times they appear in the file. After the dictionary is produced,
# the program reads through the dictionary using a maximum loop to find the most prolific committer.

# Start of code
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
x = list()
for line in handle :
    if not line.startswith ("From ") : continue # Here "From" needs to be present instead. This is a stop gal solution.

    line.rstrip()
    words = line.split()
 #   print(line)
    if len(line) >= 7 : # this is not working. Why is that ?
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
