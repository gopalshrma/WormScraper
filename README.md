# WormScraper
A web scraper to obtain a text file for Wildbow's Worm which can be found [here](https://parahumans.wordpress.com/).

## Dependencies
1. [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
2. [lxml parser](http://lxml.de/)

You can install both with pip.
If you cloned the repo you can simply run pip install -r requirements.txt

## Instructions

1. Clone the repo whereever required with
```
git clone https://github.com/gopal131072/WormScraper
```
2. Make sure all dependencies are installed.

3. Run bot.py with
```
python bot.py
```
This generates url.txt which contains all the links to parse.

4. Run bot2.py with
```
python bot2.py
```
This generates worm.txt which the final text file.

5. Convert the text file with calibre into desired format. 
