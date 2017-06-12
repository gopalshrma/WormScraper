import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://parahumans.wordpress.com/table-of-contents/').read()

soup = bs.BeautifulSoup(source,'lxml')

ScraperURL = []

file = open("url.txt","w")
for url in soup.find_all('a'):
    current = url.get('href')
    if "2012" in current or "2013" in current or "category" in current:
        file.write(url.get('href') + "\n")
    if(current=="parahumans.wordpress.com/2013/11/19/interlude-end/"):
        break
file.close()

with open('url.txt') as f:
    ScraperURL = f.read()
    ScraperURL = ScraperURL.split("\n")
