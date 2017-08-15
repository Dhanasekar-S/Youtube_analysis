import csv
from itertools import repeat
allvideostatfd = open('../datasets/videoStats.csv', 'r')
allVideoStats = csv.DictReader(allvideostatfd)

allLikesByViews = open('../datasets/likesbyviews.csv', 'r')
allLikesByViewsStats = csv.DictReader(allLikesByViews)

allDislikesByViews = open('../datasets/dislikesbyview.csv', 'r')
allDisikesByViewsStats = csv.DictReader(allDislikesByViews)

allLikesByDislikes = open('../datasets/likesbydislikes.csv', 'r')
allLikesByDislikesStat = csv.DictReader(allLikesByDislikes)

allCommentsByViews = open('../datasets/commentsbyviews.csv', 'r')
allCommentByViewsStat = csv.DictReader(allCommentsByViews)

allViewsBySubscribers = open('../datasets/viewsbysubscribers.csv', 'r')
allViewsBySubscribersStat = csv.DictReader(allViewsBySubscribers)

fullDataSetfd = open('../datasets/updatedFullDataSet.csv', 'w')
headings = ('videoId', 'likeCount', 'commentCount', 'dislikeCount', 'viewCount', 'likes/view', 'dislikes/view',
            'comments/views', 'likes/dislikes', 'views/subscribers')

fullDataSetBridge = csv.DictWriter(fullDataSetfd,headings)
fullDataSetBridge.writeheader()

stat = {}


for data, lvdata, dvdata, cvdata, lddata, vsdata in zip(allVideoStats, allLikesByViewsStats, allDisikesByViewsStats,
                                                        allCommentByViewsStat, allLikesByDislikesStat, allViewsBySubscribersStat):
    stat[headings[0]] = data[headings[0]]
    stat[headings[1]] = data[headings[1]]
    stat[headings[2]] = data[headings[2]]
    stat[headings[3]] = data[headings[3]]
    stat[headings[4]] = data[headings[4]]
    stat[headings[5]] = lvdata[headings[5]]
    stat[headings[6]] = dvdata[headings[6]]
    stat[headings[7]] = cvdata[headings[7]]
    stat[headings[8]] = lddata[headings[8]]
    stat[headings[9]] = vsdata[headings[9]]

    fullDataSetBridge.writerow(stat)



