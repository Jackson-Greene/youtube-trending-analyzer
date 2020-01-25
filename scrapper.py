import requests
from bs4 import BeautifulSoup

url = "https://www.youtube.com/feed/trending"
response = requests.get(url)
soup = BeautifulSoup(response.text, features="lxml")

print(soup.nav)

for link in soup.find_all('a'):
    print(link.get('href'))
