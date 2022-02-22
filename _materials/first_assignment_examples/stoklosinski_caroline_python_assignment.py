import pandas as pd

new_dict = dict( 
    "Python"={
        "2015" : 9
        "2016" : 22
        "2017" : 27
        "2018" : 32
        "2019" : 35
    }, "JavaScript"={
        "2015" : 8
        "2016" : 18
        "2017" : 12
        "2018" : 6
        "2019" : 15
    }, "Twitter"={
        "2015" : 10
        "2016" : 18
        "2017" : 26
        "2018" : 16
        "2019" : 12
    }, "GitHub"={
        "2015" : 2
        "2016" : 6
        "2017" : 17
        "2018" : 5
        "2019" : 10
    }, "Gephi"={
        "2015" : 11
        "2016" : 16
        "2017" : 14
        "2018" : 10
        "2019" : 9
    }, "GeoNames"={
        "2015" : 2
        "2016" : 4
        "2017" : 3
        "2018" : 1
        "2019" : 8
    }, "Transkribus"={
        "2015" : 0
        "2016" : 1
        "2017" : 2
        "2018" : 1
        "2019" : 8
    }, "Excel"={
        "2015" : 5
        "2016" : 9
        "2017" : 3
        "2018" : 6
        "2019" : 7
    }, "MySQL"={
        "2015" : 0
        "2016" : 6
        "2017" : 9
        "2018" : 5
        "2019" : 7
    })

print(new_dict)

df = pd.DataFrame(new_dict)

print(df)  

for item in new_dict:
    new_dict[item]['Overall_sum'] = sum(new_dict[item].values())

new_df = pd.DataFrame(new_dict)
print(new_df)


print(new_df.loc[['2015', '2019', 'Overall_sum']])

