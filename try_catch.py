x = raw_input("Enter your age: ")
try:
  age = int(x)
except:
    age = -1

if age > 0 :
    print( "Valid age entered having value: ")
    print age
elif age < 0:
    print("Invalid age entered. Please re-enter")
