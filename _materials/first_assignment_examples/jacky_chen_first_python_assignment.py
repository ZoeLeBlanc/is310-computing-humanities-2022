import pandas as pd

# Task 1:
# Create a data structure to store the table of top DH tools with their year and popularity count

new_dict = dict(
    Python={
    '2015': 9,
    '2016': 22,
    '2017': 27,
    '2018': 32,
    '2019': 35
}, JavaScript={
    '2015': 8,
    '2016': 18,
    '2017': 12,
    '2018': 6,
    '2019': 15
}, Twitter={
    '2015': 10,
    '2016': 18,
    '2017': 26,
    '2018': 16,
    '2019': 12
}, GitHub={
    '2015': 2,
    '2016': 6,
    '2017': 17,
    '2018': 5,
    '2019': 10
}, Gephi={
    '2015': 11,
    '2016': 16,
    '2017': 14,
    '2018': 10,
    '2019': 9
})

print(new_dict)
df = pd.DataFrame(new_dict).T
print(df)  # Use panda to construct a DataFrame

# Task 2:
# Update the data structure to keep a count for overall (that is culminative)
# popularity of each tool over the five years.

a = df.sum(1)
print(type(a), a)

new_df = df.merge(a, df)
print(new_df)


# Task 3:
# Print out the 2015, 2019, and overall values for each tool.

print(new_df.loc[['2015', '2019', 'Sum_over_five_yrs'], :])

















