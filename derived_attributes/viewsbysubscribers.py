import csv

allVideoStatfd = open('../datasets/videoStats.csv', 'r')
allVideoStatdata = csv.DictReader(allVideoStatfd)

idsfile = open('../datasets/videoandchannelid.csv', 'r')
idsdata = csv.DictReader(idsfile)

allChannelStatfd = open('../datasets/channelStats.csv', 'r')
allChannelStats = csv.DictReader(allChannelStatfd)

headings = ('videoId', 'views/subscribers')
viewsbysubsribersfd = open('../datasets/viewsbysubscribers.csv', 'w')
viewsbysubsribersbridge = csv.DictWriter(viewsbysubsribersfd, headings)
viewsbysubsribersbridge.writeheader()

stats = {}
k=0
finishedchannels = []
'''
for vdata in allVideoStatdata:
    #print(vdata['videoId'])
    for idata in idsdata:
        if vdata['videoId'] == idata['videoId']:
            print(idata['channelId'])
'''
'''
for cdata in allChannelStats:
    for idata in idsdata:
        if idata['channelId'] == cdata['channelId']:
            k = k + 1
'''

tempdict = {}
templist = []
for vdata in allVideoStatdata:
    tempdict = {}
    for idata in idsdata:
        if vdata['videoId'] == idata['videoId']:
            #print(idata['channelId'])
            k = k + 1
            tempdict['videoId'] = vdata['videoId']
            tempdict['channelId'] = idata['channelId']
            tempdict['viewCount'] = vdata['viewCount']
            templist.append(tempdict)
            break
#print(len(templist))

clist = []
for cdata in allChannelStats:
    for tdata in templist:
        if cdata['channelId'] == tdata['channelId']:
            tdata['subscriberCount'] = cdata['subscriberCount']
            clist.append(tdata)


print(len(clist))
#print(clist)

statdata = {}
for data in clist:
    statdata['videoId'] = data['videoId']
    if int(data['viewCount']) != -1 and int(data['subscriberCount']) != -1 \
        and int(data['subscriberCount']) != 0:
        statdata[headings[1]] = float(int(data['viewCount']) / int(data['subscriberCount']))
    viewsbysubsribersbridge.writerow(statdata)
'''
for vdata in allVideoStatdata:
    for idata in idsdata:
        if vdata['videoId'] == idata['videoId']:
            channelId = idata['channelId']
            for cdata in allChannelStats:
                if cdata['channelId'] == channelId:
                    stats['videoId'] = vdata['videoId']
                    if int(vdata['viewCount']) != -1 and int(cdata['subscriberCount']) != -1 \
                            and int(cdata['subscriberCount']) != 0:
                        stats[headings[1]] = float(int(vdata['viewCount']) / int(cdata['subscriberCount']))
                    else:
                        stats[headings[1]] = -1

                viewsbysubsribersbridge.writerow(stats)
'''

'''

dislikesbyviewfd = open('../datasets/dislikesbyview.csv', 'w')
headings = ('videoId', 'dislikes/view')
dislikesbyviewbridge = csv.DictWriter(dislikesbyviewfd,headings)
dislikesbyviewbridge.writeheader()
stats = {}

for data in allVideoStatdata:
    stats['videoId'] = data['videoId']
    if int(data['dislikeCount']) != -1 and int(data['viewCount']) != -1 and int(data['viewCount']) != 0:
        stats[headings[1]] = float( int(data['dislikeCount']) / int(data['viewCount']) )
    else:
        stats[headings[1]] = -1

    dislikesbyviewbridge.writerow(stats)

print("FINISHED!!1")
'''