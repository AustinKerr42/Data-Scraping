from bs4 import BeautifulSoup
import requests
import re
import arrow

stories = []

url = "http://www.bbc.co.uk/search?q=store+opening"

page  = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

ol = soup.find("ol", class_="search-results results")
for tag in ol.find_all("li"):
    h1 = tag.find("h1")
    link = list(h1.children)[0]
    href = link['href']
    title = link.get_text()
    date_div = tag.find("time", class_="display-date")
    date = date_div.get_text(strip=True)
    try:
        date = arrow.get(date, 'D MMM YYYY').format('DD-MM-YYYY')
    except:
        print("Date could not be standardized." + date)

    nextStory = [href, title, date]
    stories.append(nextStory)


def printStories():
    for x in stories:
        print(x)

printStories()