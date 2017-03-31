from bs4 import BeautifulSoup
import requests
source_code = requests.get("https://en.wikipedia.org/wiki/Main_Page").text
soup = BeautifulSoup(source_code)
# print soup.find_all('title')[0].text
# print soup.find_all('div',{"class":"potd-recent"})[0]
print soup.find_all('a')