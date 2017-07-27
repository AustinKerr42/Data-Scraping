from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import arrow
from database import insertToTable

eventList = []

driver = webdriver.Chrome()
driver.get("http://www.iowaeventscenter.com/events")

i=0
while(i==0):
    try:
        driver.find_element_by_class_name("m-eventList__showMore").click()
        time.sleep(.5)
    except:
        i=1

events = driver.find_elements_by_class_name("m-eventItem")

for event in events:
    # Link, location, and title
    link = event.find_element_by_class_name("m-eventItem__title")
    href = link.find_element_by_tag_name("a").get_attribute("href")
    title = link.get_attribute("textContent").strip()
    location = event.find_element_by_class_name("m-eventItem__location").get_attribute("textContent").strip()
    
    # Date
    day_start = event.find_element_by_class_name("m-date__day").get_attribute("textContent")
    day_start = arrow.get(day_start, 'D').format('DD')
    day_end = ""

    month = event.find_element_by_class_name("m-date__month").get_attribute("textContent")
    month = arrow.get(month, 'MMM').format('MM')

    year = event.find_element_by_class_name("m-date__year").get_attribute("textContent")[2:]

    # Check for end date with a try/except block
    try:
        date_div2 = event.find_element_by_class_name("m-date__rangeLast")
        day_end = date_div2.find_element_by_class_name("m-date__day").get_attribute("textContent")
        day_end = arrow.get(day_end, 'D').format('DD')
    except:
        pass

    # Format day and Combine date fields
    startDate = year + month + day_start
    if(day_end):
        endDate = year + month + day_end
    else:
        endDate = "NULL"

    nextEvent = [startDate, endDate, title, href, location]
    eventList.append(nextEvent)

driver.close()

def printEvents():
    for x in eventList:
        print(x)

insertToTable("dsmEvents", eventList)
# printEvents()