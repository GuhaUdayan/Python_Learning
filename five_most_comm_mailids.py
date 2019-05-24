# read a file and calculate the 5 most common words and show their frequency from text file mbox_short.txt
input_file = raw_input("enter a file:")
handle = open(input_file)
words = list()
di = dict()
mail_lst = list()

for line in handle :
    if not line.startswith("From ") : continue
    line = line.rstrip()
    words = line.split()
    mail_lst.append(words[1])
    for word in mail_lst :
        di[word] = di.get(word, 0) + 1
        #print("dictionary is printed", di, "having counter mail id as :", word )

#print("Final dictionary", di)
lst = list()
for (k,v) in di.items() :
    newtup = (v,k)
    #print("New tuple is printed", newtup)
    lst.append(newtup)
    #print("New list is printed" , lst)

lst = sorted(lst, reverse = True)

print("Most common 5 email ids are below :")
for (k,v) in lst[:5] :
    print(v,k)
