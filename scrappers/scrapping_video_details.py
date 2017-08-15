import requests
import csv
import json
from time import sleep


url = "https://www.googleapis.com/youtube/v3/videos?id=7lCDEYXw3mM&key=AIzaSyAjkrSgzR6voSP3ut1Mj1ukkAZ_xYtEC_0&part=snippet,contentDetails,statistics,status"

video_data_reader = open('../datasets/videoandchannelid.csv', 'r')
video_data_reader.__next__()
video_channel_data = csv.reader(video_data_reader)
video_data_writer = open('../datasets/videoStats.csv', 'a')
video_data_headings = ("videoId", "publishTime", "categoryId", "viewCount", "likeCount",
                       "dislikeCount", "favouriteCount", "commentCount")
video_data_bridge = csv.DictWriter(video_data_writer,video_data_headings)
video_data_bridge.writeheader()
ids = {}
for row in video_channel_data:
    payload = "https://www.googleapis.com/youtube/v3/videos?id="+row[0]+ \
            "&key=AIzaSyAjkrSgzR6voSP3ut1Mj1ukkAZ_xYtEC_0&part=snippet,contentDetails,statistics,status"

    r = requests.get(url=payload)
    videoDataRaw = r.json()
    videoData = videoDataRaw["items"][0]
    if "id" in videoData.keys():
        ids["videoId"] = videoData["id"]
    else:
        ids["videoId"] = "NULL"
    if "publishedAt" in videoData["snippet"].keys():
        ids["publishTime"] = videoData["snippet"]["publishedAt"]
    else:
        ids["publishTime"] = "lolcats"
    if "categoryId" in videoData["snippet"].keys():
        ids["categoryId"] = videoData["snippet"]["categoryId"]
    else:
        ids["categoryId"] = "-1"

    if "viewCount" in videoData["statistics"].keys():
        ids["viewCount"] = videoData["statistics"]["viewCount"]
    else:
        ids["viewCount"] = "-1"

    if "likeCount" in videoData["statistics"].keys():
        ids["likeCount"] = videoData["statistics"]["likeCount"]
    else:
        ids["likeCount"] = "-1"

    if "dislikeCount" in videoData["statistics"].keys():
        ids["dislikeCount"] = videoData["statistics"]["dislikeCount"]
    else:
        ids["dislikeCount"] = "-1"

    if "favoriteCount" in videoData["statistics"].keys():
        ids["favouriteCount"] = videoData["statistics"]["favoriteCount"]
    else:
        ids["favouriteCount"] = "-1"

    if "commentCount" in videoData["statistics"].keys():
        ids["commentCount"] = videoData["statistics"]["commentCount"]
    else:
        ids["commentCount"] = "-1"

    #ids["likeCount"] = videoData["statistics"]["likeCount"]
    #ids["dislikeCount"] = videoData["statistics"]["dislikeCount"]
    #ids["favouriteCount"] = videoData["statistics"]["favoriteCount"]
    #ids["commentCount"] = videoData["statistics"]["commentCount"]
    print(ids)
    video_data_bridge.writerow(ids)

