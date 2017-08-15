import csv

ids = open('../datasets/videoandchannelid.csv', 'r')
idsdata = csv.reader(ids)

ids1 = open('../datasets/videoandchannelid.csv', 'r')
ids.__next__()
idsdata1 = csv.reader(ids)

for data in idsdata:
    for data1 in idsdata1:
        if data[1] == data1[0]:
            print(data)



