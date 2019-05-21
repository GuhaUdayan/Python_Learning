largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        nu_num = int(num)
    except :
        print("Invalid input")
        continue
    #print(num)


    if smallest is None :
    	smallest = nu_num
    elif nu_num < smallest :
    	smallest = nu_num
    elif nu_num > largest :
    	largest = nu_num


print("Maximum number entered is",largest)
print("Minimum number entered is",smallest)
