# read a file and calculate the 10 most common words and show them
input_file = raw_input("enter a file:")
handle = open(input_file)
words = list()
di = dict()
for line in handle :
    line = line.rstrip()
    words = line.split()
    for word in words :
        di[word] = di.get(word, 0) + 1
    print("dictionary is printed", di, "having count :", word )

print("Final dictionary", di)
lst = list()
for (k,v) in di.items() :
    newtup = (v,k)
    print("New tuple is printed", newtup)
    lst.append(newtup)
    print("New list is printed" , lst)

lst = sorted(lst, reverse = True)

for (k,v) in lst[:10] :
    print(v,k)

    w5670002 user
