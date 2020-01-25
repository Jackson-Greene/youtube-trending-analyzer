import requests
from bs4 import BeautifulSoup
from selenium import webdriver


url = "https://www.youtube.com/feed/trending"

options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome("./chromedriver", chrome_options=options)
driver.get("https://www.youtube.com/feed/trending")

soup = BeautifulSoup(driver.page_source, features="lxml")


#/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer[1]/div[3]/ytd-shelf-renderer/div[1]/div[2]/ytd-expanded-shelf-contents-renderer/div
#this doesn't work
video_list = soup.find("html").find("body").find("ytd-app").find("div").find("ytd-page-manager").find("ytd-browse").find("ytd-two-column-browse-results-renderer").findAll("div")[1].find("ytd-section-list-renderer").findAll("div")[2].findAll("ytd-item-section-renderer")[1].findAll("div")[3].find("ytd-shelf-renderer").find("div")[1].find("div")[2].find("ytd-expanded-shelf-contents-renderer")


driver.quit()

print(video_list.prettify())



response = requests.get(url)
soup = BeautifulSoup(response.text, features="lxml")


#this works but I don't know how
for content in soup.findAll("div", class_= "yt-lockup-content"):
    try:
        title = content.h3.a.text
        print(title)

        description = content.find('div', class_="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2").text
        print(description)

    except Exception as e:
        description = None
 ##############