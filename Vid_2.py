import urllib.request
import re

urls = ["https://archlinux.org","http://nytimes.com","http://cnn.com"]
i=0
regex = '<title>(.+?)</title>'
pattern = re.compile(regex)
while i < len(urls) :

    htmlfile = urllib.request.urlopen(urls[i])
    htmltext = htmlfile.read()
    titles = pattern.findall(str(htmltext))
    print (titles)
    i += 1




