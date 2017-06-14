import bs4 as bs
import urllib.request

ScraperURL = []

with open('url.txt') as f:
    ScraperURL = f.read()
    ScraperURL = ScraperURL.split("\n")

file = open("worm.txt","w",encoding="utf-8")
for aa in ScraperURL:
    SourceURL=aa
    source = urllib.request.urlopen(SourceURL).read()
    soup = bs.BeautifulSoup(source,'lxml')
    print("Starting "+ SourceURL +"\n")
    file.write(soup.title.text)
    file.write("\n\n\n\n")
    for paragraph in soup.find_all('p'):
        if(paragraph.string!=None):
            ab = (paragraph.string)
            file.write(ab)
            file.write("\n\n\n\n")
        else:
            continue
    file.write("\n\n\n\n")
    print("Done with Chapter\n")
print("All done with worm. Use Calibre to convert into preferred format. :]\n")
file.close()
