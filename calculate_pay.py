hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate per hour:")
r = float(rate)
ex = h - 40.0
if ex > 0 :
    p = ex * 1.5 * r
    pay = ((h - ex) * r) + p
elif ex == 0 :
        pay = h* r
print("Salary of employee:")
print(pay)
