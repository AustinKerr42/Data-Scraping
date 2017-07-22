# DONE now add selenium to get all results
from bs4 import BeautifulSoup
import requests
import re
import arrow

stories = []

url = "http://www.iowaeventscenter.com/events"

page  = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

eventList = soup.find(class_="m-eventList__wrapper")
for event in eventList.find_all(class_="m-eventItem"):
    info = event.find(class_="m-eventItem__info")

    # Link and title
    h3 = info.find("h3", class_="m-eventItem__title")
    link = list(h3.children)[1]
    href = link['href']
    title = link.get_text()

    # Date
    date_div = list(info.find(class_="m-eventItem__date"))[1]
    day_start = date_div.find(class_="m-date__day").get_text(strip=True)
    day_end = ""

    month = date_div.find(class_="m-date__month").get_text(strip=True)
    month = arrow.get(month, 'MMM').format('MM')

    # Date could be two seperate formats so we need a try/except block
    try:
        year = date_div.find(class_="m-date__year").get_text(strip=True)[2:]
    except:
        date_div2 = list(info.find(class_="m-eventItem__date"))[3]
        year = date_div2.find(class_="m-date__year").get_text()[2:]
        day_end = date_div2.find(class_="m-date__day").get_text(strip=True)

    # Location
    location = info.find("h5", class_="m-eventItem__location").get_text(strip=True)

    # Format day and Combine date fields
    day_start = arrow.get(day_start, 'Do').format('DD')
    startDate = year + month + day_start
    if(day_end):
        day_end = arrow.get(day_end, 'Do').format('DD')
        endDate = year + month + day_end
    else:
        endDate = "none"

    nextStory = [href, title, location, startDate, endDate]
    stories.append(nextStory)


def printStories():
    for x in stories:
        print(x)

# printStories()