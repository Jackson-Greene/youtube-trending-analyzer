import requests
from bs4 import BeautifulSoup
import os
from Video import Video


def getTrendingData():

  url = "https://www.youtube.com/feed/trending"

  if os.path.exists("trending_videos_data.csv"):
    os.remove("trending_videos_data.csv")
  else:
    ...

  response = requests.get(url)

  soup = BeautifulSoup(response.text, features="lxml")
  videos_list = []
  for content in soup.findAll("div", class_= "yt-lockup-content"):
      
      try:
          title = content.h3.a.text

          video_href = content.h3.a.get("href")

          description = content.find('div', class_="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2").text

          curr_video = Video(title, description, video_href, [1,2,3,4])
    
          videos_list.append(curr_video)

      except Exception as e:
          description = None


  for video in videos_list: 
    print(video.getTags())