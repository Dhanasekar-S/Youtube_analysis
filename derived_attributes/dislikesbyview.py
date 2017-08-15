import csv

allVideoStatfd = open('../datasets/videoStats.csv', 'r')
allVideoStatdata = csv.DictReader(allVideoStatfd)

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