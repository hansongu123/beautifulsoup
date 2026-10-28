import sys
from bs4 import BeautifulSoup

with open(sys.argv[1], "rb") as file:
    html_doc = file.read()

if html_doc:
    soup = BeautifulSoup(html_doc, 'lxml', from_encoding="utf-8")
    print(soup.find_all('a'))
else:
    print("file not found")