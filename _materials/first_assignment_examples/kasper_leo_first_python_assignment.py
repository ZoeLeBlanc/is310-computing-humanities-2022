def overall(row: list):
    count = 0
    for i in range(1, len(row)):
        count += row[i]
    return count

data_table = []
data_table.append(["Tool",
                 "2015",
                 "2016",
                 "2017",
                 "2018",
                 "2019",
                 "Overall"])

data_table.append(["Python",9,22,27,32,35])
data_table[1].append(overall(data_table[1]))
                     
data_table.append(["JavaScript",8,18,12,6,15])
data_table[2].append(overall(data_table[2]))
                     
data_table.append(["Twitter",10,18,26,16,12])
data_table[3].append(overall(data_table[3]))
                     
data_table.append(["GitHub",2,6,17,5,10])
data_table[4].append(overall(data_table[4]))

data_table.append(["Gephi",11,16,14,10,9])
data_table[5].append(overall(data_table[5]))

data_table.append(["GeoNames",2,4,3,1,8])
data_table[6].append(overall(data_table[6]))

data_table.append(["Transkribus",0,1,2,1,8])
data_table[7].append(overall(data_table[7]))

data_table.append(["Excel",5,9,3,6,7])
data_table[8].append(overall(data_table[8]))
                     
data_table.append(["MySQL",0,6,9,5,7])
data_table[9].append(overall(data_table[9]))

for row in data_table:
    print(row[0], row[1], row[5], row[6], sep=' ', end='\n')
                     
                 