import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://parahumans.wordpress.com/table-of-contents/').read()

soup = bs.BeautifulSoup(source,'lxml')

file = open("url.txt","w")
print("File opened\n")
for url in soup.find_all('a'):
    current = url.get('href')
    if(current=="parahumans.wordpress.com/2013/11/19/interlude-end/"):
        file.write("https://parahumans.wordpress.com/2013/11/19/interlude-end/")
        print("All done! \o/ URL file generated")
        break
    if "2012" in current or "2013" in current or "category" in current and current is not "parahumans.wordpress.com/2013/11/19/interlude-end/":
        aa = url.get('href')
        aa = aa.replace("½","&#189;")
        file.write(aa + "\n")
        print("Getting link " + url.get('href') + "\n")
file.close()
