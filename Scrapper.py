import requests
from bs4 import BeautifulSoup
import os
from Video import Video


#gets the current trending data, returns a list of Video (each containing title, desc, [tags])
def getTrendingData():

    url = "https://www.youtube.com/feed/trending"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features="lxml")

    #list that will store Video objects
    videos_list = []

    #finds all the videos in the html
    videos_in_html = soup.findAll("div", class_= "yt-lockup-content")

    #for every video get title, desc and tags then store in a list
    for content in videos_in_html:
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

    return videos_list
####


####
def getTitle(content):
    
    return content.h3.a.text
####


####
def getHref(content):
    
    return content.h3.a.get("href")
####


####
def getDesc(content):
    
    return content.find('div', class_="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2").text
####


#gets tags of a video, need to have the video url to access html that has tags in it
def getTags(video_url):
    
    tag_list = []
    
    response = requests.get(video_url)
    soup = BeautifulSoup(response.text, features="lxml")
    
    tags_in_html = soup.findAll("meta", property="og:video:tag")

    #goes over every tag and adds them to a list
    for tag in tags_in_html:
        tag_list.append(tag.get("content"))
    
    return tag_list
####


#gets tags of a video, need to have the video url to access html that has tags in it
def getTags(video_url):
    
    tag_list = []
    
    response = requests.get(video_url)
    soup = BeautifulSoup(response.text, features="lxml")
    
    tags_in_html = soup.findAll("meta", property="og:video:tag")

    #goes over every tag and adds them to a list
    for tag in tags_in_html:
        tag_list.append(tag.get("content"))
    
    return tag_list
####
