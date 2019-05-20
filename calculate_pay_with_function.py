def computepay(h,r):
    if(h > 40) :
        pay = ((h - 40.0) * 1.5 * r) + (40.0 * r)
    elif (h<=40) :
    	pay = h * r
    return pay

hrs = input("Enter Hours:")
rate = input("Enter rate:")
h = float(hrs)
r = float(rate)

p = computepay(h,r)
print(p)
