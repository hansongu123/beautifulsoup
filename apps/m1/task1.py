import sys
from bs4 import BeautifulSoup

with open(sys.argv[1], "rb") as file:
    html_doc = file.read()

if html_doc:
    soup = BeautifulSoup(html_doc, 'lxml', from_encoding="utf-8")
    with open("prettified.html", "w", encoding="utf-8") as file:
        file.write(soup.prettify())
else:
    print("file not found")