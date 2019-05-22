# enter file name as romeo.txt present in the directory
fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
list1 = list()
for line in fh:
    line.splitlines()
    lst.append(line.split())

print(lst)
list1 = list(set([item for sublist in lst for item in sublist]))
list1.sort()

print(list1)
