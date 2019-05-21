# count the number of an alphabet in a word entered by user
x = raw_input("Enter any word or sentence :")
y = raw_input("Enter the alphabet to be counted:")
count = 0
for i in x :
    #print("Alphabet is:", i)
    if(i == y) :
        count = count + 1
print("Count of alphabet ", y, "is:", count)
