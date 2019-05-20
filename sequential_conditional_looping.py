x = 5
print("initial value of x")
print(x)
if x > 3 :
        print("bigger than 3")
        print("inside the 1st if statement - conditional code")
print("now out of if - sequential code")
for i in range(5) :
        print("inside a for loop")
        if x > 2 :
                print("Inside the 2nd if statement")
        elif x == 5 :
                print("Inside the else if of statement when x == 5")
        else :
                print("In case 2nd if condition is not met")
        print("Value  of the i iteration", i)
print("Completion of program")
