import csv

allVideoStatfd = open('../datasets/videoStats.csv', 'r')
allVideoStatdata = csv.DictReader(allVideoStatfd)

dislikesbyviewfd = open('../datasets/commentsbyviews.csv', 'w')
headings = ('videoId', 'comments/views')
dislikesbyviewbridge = csv.DictWriter(dislikesbyviewfd,headings)
dislikesbyviewbridge.writeheader()
stats = {}

for data in allVideoStatdata:
    stats['videoId'] = data['videoId']
    if int(data['commentCount']) != -1 and int(data['viewCount']) != -1 and int(data['viewCount']) != 0:
        stats[headings[1]] = float( int(data['commentCount']) / int(data['viewCount']) )
    else:
        stats[headings[1]] = -1

    dislikesbyviewbridge.writerow(stats)

print("FINISHED!!1")