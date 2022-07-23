top_tools = {
    'tool_1':{
        'name':'Python',
        '2015popularity': 9,
        '2016popularity': 22,
        '2017popularity': 27,
        '2018popularity': 32,
        '2019popularity': 35
    },
    'tool_2':{
        'name': 'JavaScript',
        '2015popularity': 8,
        '2016popularity': 18,
        '2017popularity': 12,
        '2018popularity': 6,
        '2019popularity': 15
    },
    'tool_3':{
        'name': 'Twitter',
        '2015popularity': 10,
        '2016popularity': 18,
        '2017popularity': 26,
        '2018popularity': 16,
        '2019popularity': 12
    },
    'tool_4':{
        'name': 'GitHub',
        '2015popularity': 2,
        '2016popularity': 6,
        '2017popularity': 17,
        '2018popularity': 5,
        '2019popularity': 10
    },
    'tool_5':{
        'name': 'Gephi',
        '2015popularity': 11,
        '2016popularity': 16,
        '2017popularity': 14,
        '2018popularity': 10,
        '2019popularity': 9
    },
    'tool_6':{
        'name': 'GeoNames',
        '2015popularity': 2,
        '2016popularity': 4,
        '2017popularity': 3,
        '2018popularity': 1,
        '2019popularity': 8
    },
    'tool_7':{
        'name': 'Transkribus',
        '2015popularity': 0,
        '2016popularity': 1,
        '2017popularity': 2,
        '2018popularity': 1,
        '2019popularity': 8
    },
    'tool_8':{
        'name': 'Excel',
        '2015popularity': 5,
        '2016popularity': 9,
        '2017popularity': 3,
        '2018popularity': 6,
        '2019popularity': 7
    },
    'tool_9':{
        'name': 'MySQL',
        '2015popularity': 0,
        '2016popularity': 6,
        '2017popularity': 9,
        '2018popularity': 5,
        '2019popularity': 7
    },
}

top_tools['tool_1']['overall']=top_tools['tool_1']['2015popularity']+top_tools['tool_1']['2016popularity']+top_tools['tool_1']['2017popularity']+top_tools['tool_1']['2018popularity']+top_tools['tool_1']['2019popularity']
top_tools['tool_2']['overall']=top_tools['tool_2']['2015popularity']+top_tools['tool_2']['2016popularity']+top_tools['tool_2']['2017popularity']+top_tools['tool_2']['2018popularity']+top_tools['tool_2']['2019popularity']
top_tools['tool_3']['overall']=top_tools['tool_3']['2015popularity']+top_tools['tool_3']['2016popularity']+top_tools['tool_3']['2017popularity']+top_tools['tool_3']['2018popularity']+top_tools['tool_3']['2019popularity']
top_tools['tool_4']['overall']=top_tools['tool_4']['2015popularity']+top_tools['tool_4']['2016popularity']+top_tools['tool_4']['2017popularity']+top_tools['tool_4']['2018popularity']+top_tools['tool_4']['2019popularity']
top_tools['tool_5']['overall']=top_tools['tool_5']['2015popularity']+top_tools['tool_5']['2016popularity']+top_tools['tool_5']['2017popularity']+top_tools['tool_5']['2018popularity']+top_tools['tool_5']['2019popularity']
top_tools['tool_6']['overall']=top_tools['tool_6']['2015popularity']+top_tools['tool_6']['2016popularity']+top_tools['tool_6']['2017popularity']+top_tools['tool_6']['2018popularity']+top_tools['tool_6']['2019popularity']
top_tools['tool_7']['overall']=top_tools['tool_7']['2015popularity']+top_tools['tool_7']['2016popularity']+top_tools['tool_7']['2017popularity']+top_tools['tool_7']['2018popularity']+top_tools['tool_7']['2019popularity']
top_tools['tool_8']['overall']=top_tools['tool_8']['2015popularity']+top_tools['tool_8']['2016popularity']+top_tools['tool_8']['2017popularity']+top_tools['tool_8']['2018popularity']+top_tools['tool_8']['2019popularity']
top_tools['tool_9']['overall']=top_tools['tool_9']['2015popularity']+top_tools['tool_9']['2016popularity']+top_tools['tool_9']['2017popularity']+top_tools['tool_9']['2018popularity']+top_tools['tool_9']['2019popularity']
print("2015 popularity of Python: " + str(top_tools['tool_1']['2015popularity']))
print("2019 popularity of Python: " + str(top_tools['tool_1']['2019popularity']))
print("overall popularity of Python: " + str(top_tools['tool_1']['overall']))

print("2015 popularity of JavaScript: " + str(top_tools['tool_2']['2015popularity']))
print("2019 popularity of JavaScript: " + str(top_tools['tool_2']['2019popularity']))
print("overall popularity of JavaScript: " + str(top_tools['tool_2']['overall']))

print("2015 popularity of Twitter: " + str(top_tools['tool_3']['2015popularity']))
print("2019 popularity of Twitter: " + str(top_tools['tool_3']['2019popularity']))
print("overall popularity of Twitter: " + str(top_tools['tool_3']['overall']))

print("2015 popularity of GitHub: " + str(top_tools['tool_4']['2015popularity']))
print("2019 popularity of GitHub: " + str(top_tools['tool_4']['2019popularity']))
print("overall popularity of GitHub: " + str(top_tools['tool_4']['overall']))

print("2015 popularity of Gephi: " + str(top_tools['tool_5']['2015popularity']))
print("2019 popularity of Gephi: " + str(top_tools['tool_5']['2019popularity']))
print("overall popularity of Gephi: " + str(top_tools['tool_5']['overall']))

print("2015 popularity of GeoNames: " + str(top_tools['tool_6']['2015popularity']))
print("2019 popularity of GeoNames: " + str(top_tools['tool_6']['2019popularity']))
print("overall popularity of GeoNames: " + str(top_tools['tool_6']['overall']))

print("2015 popularity of Transkribus: " + str(top_tools['tool_7']['2015popularity']))
print("2019 popularity of Transkribus: " + str(top_tools['tool_7']['2019popularity']))
print("overall popularity of Transkribus: " + str(top_tools['tool_7']['overall']))

print("2015 popularity of Excel: " + str(top_tools['tool_8']['2015popularity']))
print("2019 popularity of Excel: " + str(top_tools['tool_8']['2019popularity']))
print("overall popularity of Excel: " + str(top_tools['tool_8']['overall']))

print("2015 popularity of MySQL: " + str(top_tools['tool_9']['2015popularity']))
print("2019 popularity of MySQL: " + str(top_tools['tool_9']['2019popularity']))
print("overall popularity of MySQL: " + str(top_tools['tool_9']['overall']))