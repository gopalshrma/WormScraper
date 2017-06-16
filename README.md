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

3. Run worm.py or pact.py or twig.py depending on which web serial you want with
  ```
  python worm.py
  ```
  or
  ```
  python pact.py
  ```
  or
  ```
  python twig.py
  ```
  This generates the sitemap which contains all the links to parse.

  This was mostly for my convenience and understanding. If you want to submit a pull request with the sitemap generation and scraping merged I'll gladly accept it.

4. Run scrape.py with
  ```
  python scrape.py option
  ```
  where option is either "worm" or "pact" or "twig"

  This generates "option.txt" which the final text file.

5. Convert the text file into desired format. Personally I recommend [calibre](https://calibre-ebook.com/).

6. You can now delete the sitemap if you don't need it.

7. You can periodically run twig.py to update the sitemap and scrape it as the serial is written.
