hrs = raw_input("Enter Hours:")
rate = raw_input("Enter rate per hour:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Entered values are incorrect!")
    quit()
print("Values to be used for computation are:")
print(h , r)
ex = h - 40.0
if ex > 0 :
    p = ex * 1.5 * r
    pay = ((h - ex) * r) + p
elif ex == 0 :
        pay = h* r
print("Salary of employee:")
print(pay)
