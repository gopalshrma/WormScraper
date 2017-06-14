# WormScraper
A web scraper to obtain a text file for Wildbow's Worm or Pact.

## Dependencies
1. [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
2. [lxml parser](http://lxml.de/)

Included in requirements.txt
Can be installed with
```
pip install -r requiremennts.txt
```

## Instructions

1. Clone the repo whereever required with
```
git clone https://github.com/gopal131072/WormScraper
```
2. Make sure all dependencies are installed.

3. Run worm.py or pact.py depending on which web serial you want with
```
python worm.py 
```
or
```
python pact.py
```
This generates url.txt which contains all the links to parse.

4. Run scrape.py with
```
python scrape.py
```
This generates worm.txt (or) pact.txt which the final text file.

If you want both worm and pact then run worm.py then scrape.py followed by pact.py and scrape.py.

5. Convert the text file into desired format. Personally I recommend [calibre](https://calibre-ebook.com/)
