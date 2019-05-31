# Introduction to Data Science in Python - Week 2 - Assignment 2

# Assignment 2 - Pandas Introduction
# All questions are weighted the same in this assignment.
#
# Part 1
# The following code loads the olympics dataset (olympics.csv), which was derrived from the Wikipedia entry on All Time Olympic Games Medals, and does some basic data cleaning.
#
# The columns are organized as # of Summer games, Summer medals, # of Winter games, Winter medals, total # number of games, total # of medals. Use this dataset to answer the questions below.

import pandas as pd
​
df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)
​
for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)
​
names_ids = df.index.str.split('\s\(') # split the index by '('
​
df.index = names_ids.str[0] # the [0] element is the country name (new index)
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)
​
df = df.drop('Totals')
df.head()
# # Summer	Gold	Silver	Bronze	Total	# Winter	Gold.1	Silver.1	Bronze.1	Total.1	# Games	Gold.2	Silver.2	Bronze.2	Combined total	ID
# Afghanistan	13	0	0	2	2	0	0	0	0	0	13	0	0	2	2	AFG
# Algeria	12	5	2	8	15	3	0	0	0	0	15	5	2	8	15	ALG
# Argentina	23	18	24	28	70	18	0	0	0	0	41	18	24	28	70	ARG
# Armenia	5	1	2	9	12	6	0	0	0	0	11	1	2	9	12	ARM
# Australasia	2	3	4	5	12	0	0	0	0	0	2	3	4	5	12	ANZ
# Question 0 (Example)
# What is the first country in df?
#
# This function should return a Series.

df.iloc[0]
# You should write your whole answer within the function provided. The autograder will call
# this function and compare the return value against the correct solution value
def answer_zero():
    # This function returns the row for Afghanistan, which is a Series object. The assignment
    # question description will tell you the general format the autograder is expecting

    return df.iloc[0]
​
# You can examine what your function returns by calling it in the cell. If you have questions
# about the assignment formats, check out the discussion forums for any FAQs
answer_zero().name
# 'Afghanistan'


# Question 1
# Which country has won the most gold medals in summer games?
#
# This function should return a single string value.

def answer_one():
    return df['Gold'].argmax()


# Question 2
# Which country had the biggest difference between their summer and winter gold medal counts?
#
# This function should return a single string value.

def answer_two():
    return (df['Gold'] - df['Gold.1']).argmax()
answer_two()


# Question 3
# Which country has the biggest difference between their summer gold medal counts and winter gold medal counts relative to their total gold medal count?
#
# Summer Gold−Winter GoldTotal Gold
# Summer Gold−Winter GoldTotal Gold
# Only include countries that have won at least 1 gold in both summer and winter.
#
# This function should return a single string value.

def answer_three():
    only_gold = df.where((df['Gold'] > 0) & (df['Gold.1'] > 0))
    only_gold = only_gold.dropna()
    return (abs((only_gold['Gold'] - only_gold['Gold.1']) / only_gold['Gold.2'])).idxmax()
​
answer_three()


# Question 4
# Write a function that creates a Series called "Points" which is a weighted value where each gold medal (Gold.2) counts for 3 points, silver medals (Silver.2) for 2 points, and bronze medals (Bronze.2) for 1 point. The function should return only the column (a Series object) which you created, with the country names as indices.
#
# This function should return a Series named Points of length 146


def answer_four():
     df['Points'] = df['Gold.2']*3 + df['Silver.2']*2 + df['Bronze.2']*1
     return df['Points']
​
answer_four()


#############################################################################
# Part 2
# For the next set of questions, we will be using census data from the United States Census Bureau. Counties are political and geographic subdivisions of states in the United States. This dataset contains population data for counties and states in the US from 2010 to 2015. See this document for a description of the variable names.
#
# The census dataset (census.csv) should be loaded as census_df. Answer questions using this as appropriate.
#
# Question 5
# Which state has the most counties in it? (hint: consider the sumlevel key carefully! You'll need this for future questions too...)
#
# This function should return a single string value.
#
# census_df = pd.read_csv('census.csv')
# census_df.head()
# SUMLEV	REGION	DIVISION	STATE	COUNTY	STNAME	CTYNAME	CENSUS2010POP	ESTIMATESBASE2010	POPESTIMATE2010	...	RDOMESTICMIG2011	RDOMESTICMIG2012	RDOMESTICMIG2013	RDOMESTICMIG2014	RDOMESTICMIG2015	RNETMIG2011	RNETMIG2012	RNETMIG2013	RNETMIG2014	RNETMIG2015
# 0	40	3	6	1	0	Alabama	Alabama	4779736	4780127	4785161	...	0.002295	-0.193196	0.381066	0.582002	-0.467369	1.030015	0.826644	1.383282	1.724718	0.712594
# 1	50	3	6	1	1	Alabama	Autauga County	54571	54571	54660	...	7.242091	-2.915927	-3.012349	2.265971	-2.530799	7.606016	-2.626146	-2.722002	2.592270	-2.187333
# 2	50	3	6	1	3	Alabama	Baldwin County	182265	182265	183193	...	14.832960	17.647293	21.845705	19.243287	17.197872	15.844176	18.559627	22.727626	20.317142	18.293499
# 3	50	3	6	1	5	Alabama	Barbour County	27457	27457	27341	...	-4.728132	-2.500690	-7.056824	-3.904217	-10.543299	-4.874741	-2.758113	-7.167664	-3.978583	-10.543299
# 4	50	3	6	1	7	Alabama	Bibb County	22915	22919	22861	...	-5.527043	-5.068871	-6.201001	-0.177537	0.177258	-5.088389	-4.363636	-5.403729	0.754533	1.107861
# 5 rows × 100 columns

def answer_five():
    new_df = census_df[census_df['SUMLEV'] == 50]
    return new_df.groupby('STNAME').count()['SUMLEV'].idxmax()
​
answer_five()
# Question 6
# Only looking at the three most populous counties for each state, what are the three most populous states (in order of highest population to lowest population)? Use CENSUS2010POP.
#
# This function should return a list of string values.

def answer_six():
    df=census_df[census_df['SUMLEV'] == 50]
    df1=df.sort(['STNAME','POPESTIMATE2015'],ascending=False).groupby('STNAME').head(3).copy()
    df2 = df1.reset_index().groupby("STNAME").sum().sort(['POPESTIMATE2015'],ascending=False).head(3).copy()
    return list(df2.index.values)
​
answer_six()

# Question 7
# Which county has had the largest absolute change in population within the period 2010-2015? (Hint: population values are stored in columns POPESTIMATE2010 through POPESTIMATE2015, you need to consider all six columns.)
#
# e.g. If County Population in the 5 year period is 100, 120, 80, 105, 100, 130, then its largest change in the period would be |130-80| = 50.
#
# This function should return a single string value.

def answer_seven():
    df=census_df[census_df['SUMLEV'] == 50]
    df['STDEV'] = df[['POPESTIMATE2010','POPESTIMATE2011','POPESTIMATE2012',
                      'POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']].std(axis=1)
    return df.loc[df['STDEV'].idxmax()]['CTYNAME']
​
answer_seven()
#
# Question 8
# In this datafile, the United States is broken up into four regions using the "REGION" column.
#
# Create a query that finds the counties that belong to regions 1 or 2, whose name starts with 'Washington', and whose POPESTIMATE2015 was greater than their POPESTIMATE 2014.
#
# This function should return a 5x2 DataFrame with the columns = ['STNAME', 'CTYNAME'] and the same index ID as the census_df (sorted ascending by index).

def answer_eight():
    df=census_df[census_df['SUMLEV'] == 50]
    region1 = df['REGION'] == 1
    region2 = df['REGION'] == 2
    county_name = df['CTYNAME'].str.startswith('Washington')
    pop_estim = df['POPESTIMATE2015'] > df['POPESTIMATE2014']
    df = df[(region2|region1)&county_name&pop_estim]
    return df[['STNAME', 'CTYNAME']]
​
answer_eight()
