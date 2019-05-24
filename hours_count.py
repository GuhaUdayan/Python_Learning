# Program to write a code to identify the occurrences of "hours" in a text file

#Question 10.2 -Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox_short.txt"
handle = open(name)
words = list()
hours = list()
di = dict()
hours_lst = list()
new_list = list()

for line in handle :
    if not line.startswith("From ") : continue
    line = line.rstrip()
    words = line.split()
  #  print(words)
    hours_lst.append(words[5])

#print(hours_lst)
for i in hours_lst :
    new_list.append(i.split(":")[0])
print(new_list)

for word in new_list :
    di[word] = di.get(word, 0) + 1
#    print("dictionary is printed", di, "having counter mail id as :", word )

print("Final dictionary", di)
lst = list()

print("Hours and their occurrences are printed below in sorted order of items:")
for (k,v) in sorted(di.items()) :
    print(k,v)
