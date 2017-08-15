import csv

allVideoStatfd = open('../datasets/videoStats.csv', 'r')
allVideoStatdata = csv.DictReader(allVideoStatfd)

likesbyviewfd = open('../datasets/likesbyviews.csv', 'w')
headings = ('videoId', 'likes/view')
likesbyviewbridge = csv.DictWriter(likesbyviewfd,headings)
likesbyviewbridge.writeheader()
stats = {}

for data in allVideoStatdata:
    stats['videoId'] = data['videoId']
    if int(data['likeCount']) != -1 and int(data['viewCount']) != -1 and int(data['viewCount']) != 0:
        stats[headings[1]] = float( int(data['likeCount']) / int(data['viewCount']) )
    else:
        stats[headings[1]] = -1

    likesbyviewbridge.writerow(stats)

print("FINISHED!!1")