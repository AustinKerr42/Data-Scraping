# Data-Scraping
A data scrapinng project to display events in Des Moines, Iowa.


## To Use
Navigate to [url not setup](http://www.google.com) to view the webpage. Events are added to the page as they are posted on the various sites that the scrapers get their data from.

### Software Used
```
Python 2.7.13:
-Flask
-Selenium
Webpage:
-GoDaddy.com
-HTML, JavaScript, JQuery
-https://datatables.net
```

### scrap_dsmEvents.py
This is the main scraper for the website. It goes to the [Iowa Events Center](http://www.iowaeventscenter.com/events) to find all the events and adds them to the database.
