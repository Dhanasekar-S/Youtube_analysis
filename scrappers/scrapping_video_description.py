import requests
import csv
import json
from time import sleep


url = "https://www.googleapis.com/youtube/v3/videos?id=7lCDEYXw3mM&key=AIzaSyAjkrSgzR6voSP3ut1Mj1ukkAZ_xYtEC_0&part=snippet,contentDetails,statistics,status"

video_data_reader = open('../datasets/videoandchannelid.csv', 'r')
video_data_reader.__next__()
video_channel_data = csv.reader(video_data_reader)
video_data_writer = open('../datasets/videoDescription.csv', 'w')
video_data_headings = ("videoId", "videoDescription")
video_data_bridge = csv.DictWriter(video_data_writer,video_data_headings)
video_data_bridge.writeheader()
ids = {}
i = 1
for row in video_channel_data:
    print(i)
    payload = "https://www.googleapis.com/youtube/v3/videos?id="+row[0]+ \
            "&key=AIzaSyAjkrSgzR6voSP3ut1Mj1ukkAZ_xYtEC_0&part=snippet"
    r = requests.get(url=payload)
    videoDataRaw = r.json()
    if len(videoDataRaw["items"]) < 1:
        continue
    videoData = videoDataRaw["items"][0]
    if "id" in videoData.keys():
        ids["videoId"] = videoData["id"]
    else:
        ids["videoId"] = "NULL"

    if "description" in videoData["snippet"].keys():
        ids["videoDescription"] = videoData["snippet"]["description"].encode('ascii', 'ignore').decode('ascii')
    else:
        ids["videoDescription"] = "kingini, minginey"
    print(ids)
    i = i+1
    video_data_bridge.writerow(ids)
