import bs4 as bs
import urllib.request

#Reads the table of contents to try and generate a sitemap for the serial.

#I would use the actual sitemap but this is easier since the sitemap is in reverse chronological
#order whereas this is in the actual chronological order and is formatted better.
source = urllib.request.urlopen('https://pactwebserial.wordpress.com/table-of-contents/').read()

#Creates required object.
soup = bs.BeautifulSoup(source,'lxml')

#Opens a text file and writes all required URL's into it.
file = open("pact-sitemap.txt","w")
print("File opened\n")

#Finds all anchor tags and gets the links they point to.
for url in soup.find_all('a'):
    current = url.get('href')

#We do not need any URL's after this one, since this is the end of the serial.
    if(current=="https://pactwebserial.wordpress.com/2015/02/28/judgment-16-12/"):
        file.write("https://pactwebserial.wordpress.com/2015/02/28/judgment-16-12/")
        print("All done! \o/ URL file generated")
        break

#The URL's vary a lot with title so I had to get creative on how to get only those we needed. Not the best way but it works.
    if "2013" in current or "2014" in current or "2015" in current and current is not "https://pactwebserial.wordpress.com/2015/02/28/judgment-16-12/":
        if "https://" not in current:
                file.write("https://" + current + "\n")
        else:
            file.write(current + "\n")
            print("Getting link " + url.get('href') + "\n")
file.close()
