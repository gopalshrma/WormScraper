import bs4 as bs
import urllib.request

#Reads the table of contents to try and generate a sitemap for the serial.

#I would use the actual sitemap but this is easier since the sitemap is in reverse chronological
#order whereas this is in the actual chronological order and is formatted better.
source = urllib.request.urlopen('https://parahumans.wordpress.com/table-of-contents/').read()

#Creates required object.
soup = bs.BeautifulSoup(source,'lxml')

#Opens a text file and writes all required URL's into it.
file = open("worm-sitemap.txt","w")
print("File opened\n")

#Finds all anchor tags and gets the links they point to.
for url in soup.find_all('a'):

#We do not need any URL's after this one, since this is the end of the serial.
    current = url.get('href')
    if(current=="parahumans.wordpress.com/2013/11/19/interlude-end/"):

        file.write("https://parahumans.wordpress.com/2013/11/19/interlude-end/")
        print("All done! \o/ URL file generated")
        break

#The URL's vary a lot with title so I had to get creative on how to get only those we needed. Not the best way but it works.
    if "2012" in current or "2013" in current or "category" in current and current is not "parahumans.wordpress.com/2013/11/19/interlude-end/":

        requiredURL = url.get('href')
        requiredURL = requiredURL.replace("½","&#189;")
        file.write(requiredURL + "\n")
        print("Getting link " + url.get('href') + "\n")

file.close()
