# WormScraper
A web scraper to obtain a text file for Wildbow's Worm or Pact or Twig.

## Dependencies
1. [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
2. [lxml parser](http://lxml.de/)
3. requests module.

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

3. Run scrape.py with an option to define what book you want to scrape.

  ```
  python scrape.py option
  ```
  where option is one of "worm", "pact" or "twig"

  Ex.

  ```
  python scrape.py worm
  ```
4. This will generate two files, the url file which will be stored as book-sitemap.txt followed by the actual scraped text which (worm.txt or pact.txt or twig.txt).
