import pandas as pd
assignment = dict()
assignment = {'Tool':['Python','JavaScript','Twitter','GitHub', 'Gephi','GeoNames','Transkribus','Excel','MySQL'],'2015':[9,8,10,2,11,2,0,5,0],'2016':[22,18,18,6,16,4,1,9,6],'2017':[27,12,26,17,14,3,2,3,9],'2018':[32,6,16,5,10,1,1,6,5],'2019':[35,15,12,10,9,8,8,7,7]}
table = pd.DataFrame(assignment)
table
table.loc[:,['2015','2019']]

table['Overall'] = table.sum(axis=1)
table
answer_table = table.loc[:,['Tool','2015','2019','Overall']]
print(answer_table)