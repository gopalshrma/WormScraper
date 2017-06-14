import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://pactwebserial.wordpress.com/table-of-contents/').read()

soup = bs.BeautifulSoup(source,'lxml')

file = open("url.txt","w")
print("File opened\n")
for url in soup.find_all('a'):
    current = url.get('href')
    if(current=="https://pactwebserial.wordpress.com/2015/02/28/judgment-16-12/"):
        file.write("https://pactwebserial.wordpress.com/2015/02/28/judgment-16-12/")
        print("All done! \o/ URL file generated")
        break
    if "2013" in current or "2014" in current or "2015" in current and current is not "https://pactwebserial.wordpress.com/2015/02/28/judgment-16-12/":
        if "https://" not in current:
                file.write("https://" + current + "\n")
        else:
            file.write(current + "\n")
            print("Getting link " + url.get('href') + "\n")
file.close()
