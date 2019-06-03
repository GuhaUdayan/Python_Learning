#
# Here are two DataFrames, products and invoices. The product DataFrame has an identifier and a sticker price. The invoices DataFrame lists the people, product identifiers, and quantity. Assuming that we want to generate totals, how do we join these two DataFrames together so that we have one which lists all of the information we need?
#
# products DataFrame:
#
# Price	Product
# Product ID
# 4109	5.0	Sushi Roll
# 1412	0.5	Egg
# 8931	1.5	Bagel
# invoices DataFrame:
#
# Customer	Product ID	Quantity
# 0	Ali	4109	1
# 1	Eric	1412	12
# 2	Ande	8931	6
# 3	Sam	4109	2
#

print(pd.merge(products, invoices, left_index=True, right_on='Product ID'))

# Suppose we are working on a DataFrame that holds information on our equipment for an upcoming backpacking trip.
#
# Can you use method chaining to modify the DataFrame df in one statement to drop any entries where 'Quantity' is 0 and rename the column 'Weight' to 'Weight (oz.)'?
print(df.drop(df[df['Quantity'] == 0]
        .index)
        .rename(columns={'Weight': 'Weight (oz.)'}))


# Looking at our backpacking equipment DataFrame, suppose we are interested in finding our total weight for each category. Use groupby to group the dataframe, and apply a function to calculate the total weight (Weight x Quantity) by category.

print(df.groupby('Category').apply(lambda df,a,b: sum(df[a] * df[b]), 'Weight (oz.)', 'Quantity'))
