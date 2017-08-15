import requests
import json
import csv
import pickle
import random
from itertools import repeat
import time
api_key = "AIzaSyDraPMr8KRfkux5u9DgCjfWh1SA_xJmIl8"
test_api_key = "AIzaSyD1fGnUYGPjdfpklW9PmjbQkOqlUKxQ3o8"

#r = requests.get(url=url)

#print(r)
#raw_data = r.json()

#item_list = raw_data["items"]
idsfile = open('../datasets/videoandchannelid.csv', "a")
queriesfile = open('../datasets/channel_names.csv', 'r')
queriesfile_csv = csv.reader(queriesfile)
heading = ("videoId", "channelId")
video_channel_id = []
bridge = csv.DictWriter(idsfile, heading)
bridge.writeheader()


for data in queriesfile_csv:
    nextPageToken = ""
    for i in repeat(None,4):
        video_channel_id = []
        url = "https://www.googleapis.com/youtube/v3/search?key=" + test_api_key \
            + "&type=video&part=snippet" \
                "&q="+data[0]+"&maxResults=50&pageToken="+nextPageToken
        r = requests.get(url=url)
        raw_data = r.json()
        item_list = raw_data["items"]
        for item in item_list:
            ids = {}
            #print(item.keys())
            # print(item["id"]["videoId"], end=" ")
            # print(item["snippet"]["channelId"])
            if "videoId" in item["id"].keys() and "channelId" in item["snippet"].keys():
                ids["videoId"] = item["id"]["videoId"]
                ids["channelId"] = item["snippet"]["channelId"]
                print(ids)
                video_channel_id.append(ids)
        for row in video_channel_id:
            bridge.writerow(row)
        nextPageToken = raw_data["nextPageToken"]
    time.sleep(5)



#print(video_channel_id)
bridge = csv.DictWriter(idsfile, heading)
for row in video_channel_id:
    bridge.writerow(row)
