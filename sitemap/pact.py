import bs4 as bs
import urllib.request
import sys
import os.path

# Reads the table of contents to try and generate a sitemap for the serial.

# I would use the actual sitemap but this is easier since the sitemap is in reverse chronological
# order whereas this is in the actual chronological order and is formatted better.
source = urllib.request.urlopen('https://pactwebserial.wordpress.com/table-of-contents/').read()

# Creates required object.
soup = bs.BeautifulSoup(source,'lxml')

# Opens a text file and writes all required URL's into it.
if(os.path.isfile("pact-sitemap.txt")):
    print("Sitemap already exists, either from a previous scrape, or a custom sitemap.")
    print("Not generating sitemap.")
    sys.exit(0)
else:
    file = open("pact-sitemap.txt","w")
    print("File opened\n")

# Finds all anchor tags and gets the links they point to.
for url in soup.find_all('a'):
    current = url.get('href')

# The URL at which we need to stop scraping.
    lastURL = "https://pactwebserial.wordpress.com/2015/02/28/judgment-16-12/"
# We do not need any URL's after this one, since this is the end of the serial.
    if(current==lastURL):
        file.write(lastURL)
        print("All done! URL file generated\n")
        break

# The URL's vary a lot with title so I had to get creative on how to get only those we needed. Not the best way but it works.
    Keywords = ['2013','2014','2015']
    if any(keys in current for keys in Keywords):
        if "https://" not in current:
                file.write("https://" + current + "\n")
        else:
            file.write(current + "\n")
            print("Getting link " + url.get('href') + "\n")
file.close()
