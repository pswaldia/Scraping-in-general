# Scraping-in-general
Contains few use cases of web scraping using Beautiful Soup :

# 1. Stock-Scraper:
In this Use Case , Few details regarding a particular stock ticker is scraped from Yahoo! Finance website. A user needs to supply a TICKER and the information recieved from website will be shown. The website is deployed on heroku and can be accessed through https://stockkk-scraper.herokuapp.com ( `View it on your desktop, It may not be mobile friendly :)` ). Code can be accessed through [`stock-scraper/app.py`](https://github.com/pswaldia/Scraping-in-general/blob/master/stock-scraper/app.py).

# 2. Books-Scraper
In this Use Case , Details regarding top 20 books published in 2018 (according to reader's review on goodreads website) is scraped and is put into a csv file ( https://bit.ly/2VTu9Ca ) and code is written in [`book-scraper/goodreads.py`](https://github.com/pswaldia/Scraping-in-general/blob/master/goodread-scraper/goodreads.py)

# 3. DlBooks-Scraper
In this Use Case , Deep learning books data is being scraped from `Flipkart` books section using `Scrapy`. Multiple pages have been scraped. Data is then dumped into json, xml and csv. This data can be accessed from [`dlBooks/scraped_data/DLBooks.json`]((https://github.com/pswaldia/Scraping-in-general/blob/master/dlbooks/scraped_data/DLBooks.json) ,[`dlbooks/scraped_data/DLBooks.xml`](https://github.com/pswaldia/Scraping-in-general/blob/master/dlbooks/scraped_data/DLBooks.xml) ,[`dlBooks/scraped_data/DLBooks.csv`](https://github.com/pswaldia/Scraping-in-general/blob/master/dlbooks/scraped_data/DLBooks.csv).  The crawler written for the purpose can be found at [`dlbooks/spiders/dl_scrapper.py`](https://github.com/pswaldia/Scraping-in-general/blob/master/dlbooks/spiders/dl_scrapper.py)
