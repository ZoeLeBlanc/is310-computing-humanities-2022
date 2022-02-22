python = {'2015':9,'2016':22,'2017':27,'2018':32,'2019':35,'overall':125}
javascript = {'2015':8,'2016':18,'2017':12,'2018':6,'2019':15,'overall':59}
twitter = {'2015':10,'2016':18,'2017':26,'2018':16,'2019':12,'overall':82}
github = {'2015':2,'2016':6,'2017':17,'2018':5,'2019':10,'overall':40}
gephi = {'2015':11,'2016':16,'2017':14,'2018':10,'2019':9,'overall':60}
geonames = {'2015':2,'2016':4,'2017':3,'2018':1,'2019':8,'overall':18}
trans = {'2015':0,'2016':1,'2017':2,'2018':1,'2019':8,'overall':12}
excel = {'2015':5,'2016':9,'2017':3,'2018':6,'2019':7,'overall':26}
sql = {'2015':0,'2016':6,'2017':9,'2018':5,'2019':7,'overall':27}


frame = {'Python':python,'JavaScript':javascript,'Twitter':twitter,'GitHub':github,'Gephi':gephi,
'GeoNames':geonames,'Transkribus':trans,'Excel':excel,'MySQL':sql}


for tool in frame.values():
    #tooling = frame{tool}
    tool15 = tool['2015']
    tool19 = tool['2019']
    toolover = tool['overall']
    print(f'2015:{tool15}, 2019:{tool19}, overall:{toolover}')
    #print(tool['2015'])