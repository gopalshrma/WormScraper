import bs4 as bs
import urllib.request

ScraperURL = []

with open('url.txt') as f:
    ScraperURL = f.read()
    ScraperURL = ScraperURL.split("\n")

file = open("text.txt","w")
for aa in ScraperURL:
    SourceURL=aa
    source = urllib.request.urlopen(SourceURL).read()
    soup = bs.BeautifulSoup(source,'lxml')
    print("Starting "+ SourceURL +"\n")
    file.write(soup.title.text)
    file.write("\n\n\n\n")
    for paragraph in soup.find_all('p'):
        if(paragraph.string!=None):
            file.write(paragraph.string)
            file.write("\n\n")
        else:
            continue
    file.write("\n\n\n\n")
    print("Done with Chapter\n")
file.close()
