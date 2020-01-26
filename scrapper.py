import requests
from bs4 import BeautifulSoup
import os
from Video import Video


def getTrendingData():

    url = "https://www.youtube.com/feed/trending"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features="lxml")
    videos_list = []
    
    print("hi")
    for content in soup.findAll("div", class_= "yt-lockup-content"):
        
        try:
            title = getTitle(content)
            description = getDesc(content)
            video_href = getHref(content)
            video_url = "https://www.youtube.com{}".format(video_href)
            tags = getTags(video_url)

            curr_video = Video(title, description, tags)

            videos_list.append(curr_video)

        except Exception as e:
            ...

    print(str(videos_list[2]))

    return videos_list


def getTitle(content):
    return content.h3.a.text


def getHref(content):
    return content.h3.a.get("href")


def getDesc(content):
    return content.find('div', class_="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2").text


def getTags(video_url):
    return ["test0", "test1"]


getTrendingData()