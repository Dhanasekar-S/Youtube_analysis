import csv

allVideoStatfd = open('../datasets/videoStats.csv', 'r')
allVideoStatdata = csv.DictReader(allVideoStatfd)

dislikesbyviewfd = open('../datasets/likesbydislikes.csv', 'w')
headings = ('videoId', 'likes/dislikes')
dislikesbyviewbridge = csv.DictWriter(dislikesbyviewfd,headings)
dislikesbyviewbridge.writeheader()
stats = {}

for data in allVideoStatdata:
    stats['videoId'] = data['videoId']
    if int(data['dislikeCount']) != -1 and int(data['likeCount']) != -1 and int(data['dislikeCount']) != 0\
            and int(data['likeCount']) > 1000:
        stats[headings[1]] = float( int(data['likeCount']) / int(data['dislikeCount']) )
    elif int(data['likeCount']) <1000 and int(data['likeCount']) != -1:
        stats[headings[1]] = -2
    else:
        stats[headings[1]] = -1

    dislikesbyviewbridge.writerow(stats)

print("FINISHED!!1")