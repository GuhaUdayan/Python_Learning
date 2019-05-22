# calculate best sell and buy price for a stock from a list
stock_price_lst = list()
stock_price_lst = [10,22,5,75,65,80]
#stock_price_lst = [50,40,35,15,7,32,45,49]
smallest = None
largest = None
i = 0
j = 0
while i < len(stock_price_lst) :
    if stock_price_lst[i] > largest :
    	largest = stock_price_lst[i]
        e = i
        print(i, largest, stock_price_lst[i], e)
    i = i + 1

while j < len(stock_price_lst) :
    if smallest is None :
        smallest = stock_price_lst[j]
    elif stock_price_lst[j] < smallest :
    	smallest = stock_price_lst[j]
        d = j
        print(j, smallest, stock_price_lst[j], d)
    j = j + 1

print("Best price to purchase is",smallest, "on the day:", d)
print("Best price to sell is",largest, "on the day:", e)
