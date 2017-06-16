from bs4 import BeautifulSoup
import requests

r = requests.get("https://twigserial.wordpress.com/sitemap.xml")
xml = r.text
soup = BeautifulSoup(xml,"lxml")
sitemapTags = soup.find_all("url")

dictionary = {}
i = 0

file = open("twig-sitemap.txt","w")

for sitemap in sitemapTags:
    current = sitemap.findNext("loc").text
    if "2014" in current or "2015" in current or "2016" in current or "2017" in current or "2018" in current:
        dictionary[i] = current
        i+=1

while i > 0:
    print("Getting link : " + dictionary[i-1] + "\n" )
    file.write(dictionary[i-1])
    file.write("\n")
    i-=1

print("All done! \o/ Exiting.")
file.close()
