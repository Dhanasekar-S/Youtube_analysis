import requests
import csv
import json

#url = "https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics&id=UCr-gTfI7au9UaEjNCbnp_Nw" \
      #"&key=AIzaSyD1fGnUYGPjdfpklW9PmjbQkOqlUKxQ3o8"

#r = requests.get(url)
#data = r.json()

donechannels = []
filebridge = open('../datasets/videoandchannelid.csv', 'r')
dataset = csv.DictReader(filebridge)
headers = ("channelId", "publishedAt", "viewCount", "commentCount",
           "subscriberCount", "videoCount")
channeldatafile = open('channelStats.csv', 'w')
channelstatbridge = csv.DictWriter(channeldatafile,headers)
channelstatbridge.writeheader()
i = 1
for data in dataset:
      print(i)
      if data['channelId'] not in donechannels:
            payload = "https://www.googleapis.com/youtube/v3/channels?key=AIzaSyDraPMr8KRfkux5u9DgCjfWh1SA_xJmIl8&part=snippet,statistics" \
                "&id="+data['channelId']
            r = requests.get(url=payload)
      else:
            continue
      raw_data = r.json()
      dataitem = raw_data["items"]
      details ={}
      details["channelId"] = data['channelId']
      if "publishedAt" in dataitem[0]["snippet"].keys():
            details["publishedAt"] = dataitem[0]["snippet"]["publishedAt"]
      else:
            details["publishedAt"] = "NULL"

      if "viewCount" in dataitem[0]["statistics"].keys():
            details["viewCount"] = dataitem[0]["statistics"]["viewCount"]
      else:
            details["viewCount"] = -1

      if "commentCount" in dataitem[0]["statistics"].keys():
            details["commentCount"] = dataitem[0]["statistics"]["commentCount"]
      else:
            details["commentCount"] = -1

      if "subscriberCount" in dataitem[0]["statistics"].keys():
            details["subscriberCount"] = dataitem[0]["statistics"]["subscriberCount"]
      else:
            details["subscriberCount"] = -1

      if "videoCount" in dataitem[0]["statistics"].keys():
            details["videoCount"] = dataitem[0]["statistics"]["videoCount"]
      else:
            details["videoCount"] = -1
      i=i+1
      donechannels.append(data['channelId'])
      channelstatbridge.writerow(details)

#print(data)
