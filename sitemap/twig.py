from bs4 import BeautifulSoup
import requests

# I switched around to the requests module on this one because I was told it yields better results.

# Also unlike worm or pact there was no table of contents so I had to scrape from the sitemap.
req = requests.get("https://twigserial.wordpress.com/sitemap.xml")
xml = req.text
soup = BeautifulSoup(xml,"lxml")

# Finds all url tags within the xml file.
sitemapTags = soup.find_all("url")

dictionary = {}
i = 0

# Opens the output sitemap file.
file = open("twig-sitemap.txt","w")

# Finds every url in the sitemap that hold 2014/15/16/17/18 since that's the naming convention followed,
# and adds it to a dictionary.
for sitemap in sitemapTags:
    current = sitemap.findNext("loc").text
    Keywords = ['2014','2015','2016','2017','2018']
    if any(keys in current for keys in Keywords):
        dictionary[i] = current
        i+=1

# The sitemap holds the urls in reverse chronological order so I can to reverse the entire URL list.
while i > 0:
    print("Getting link : " + dictionary[i-1] + "\n" )

# Writing URL's in chronological order to the file.
    file.write(dictionary[i-1])
    file.write("\n")
    i-=1

print("All done! URL file generated. \n")
file.close()
