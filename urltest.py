import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('span')
y = list()

for tag in tags:
    spans = str(tag)
    x = re.findall('[0-9]+', spans)
    y = y + x

sum = 0
for s in y:
    sum = sum + int(s)

print(sum)
