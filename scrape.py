import bs4 as bs
import urllib.request
import sys
import os

ScraperURL = []

option = sys.argv[1]

os.system("python " + option + ".py")

with open(option + '-sitemap.txt') as f:
    ScraperURL = f.read()
    ScraperURL = ScraperURL.split("\n")

file = open(option + ".txt","w",encoding="utf-8")
for aa in ScraperURL:
    SourceURL=aa
    source = urllib.request.urlopen(SourceURL).read()
    soup = bs.BeautifulSoup(source,'lxml')
    print("Starting "+ SourceURL +"\n")
    file.write(soup.title.text)
    file.write("\n\n\n\n")
    for paragraph in soup.find_all('p'):
        if(paragraph.string!=None):
            paragh = (paragraph.string)
            file.write(paragh)
            file.write("\n\n")
        else:
            continue
    file.write("\n\n\n\n")
    print("Done with Chapter\n")
print("All done with worm. Use Calibre to convert into preferred format. :]\n")
file.close()
