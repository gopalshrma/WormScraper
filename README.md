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
4. This will generate two files, the url file which will be stored as book-sitemap.txt followed by the actual scraped text file (worm.txt or pact.txt or twig.txt).

5. You can keep the sitemap if you want to update it and scrape text later or you can just delete it.

6. I didn't merge generation of sitemap and scraping of the site in one file because I wanted to experiment with the sitemap, if you feel this project would be better served by merging them please feel free to submit a pull request.


## Screenshot

![Here's a screenshot of the output.](https://raw.githubusercontent.com/gopal131072/WormScraper/screenshot.png)

The output can be formatted to your liking by changing line, paragraph and page breaks in scrape.py.
You can also change these while converting it to a readable format on Calibre/another software.
