import sys
from bs4 import BeautifulSoup

with open(sys.argv[1], "r") as file:
    html_doc = file.read()

if html_doc:
    soup = BeautifulSoup(html_doc, 'lxml')
    # Change all <b> to <blockquote>
    for tag in soup.find_all('b'):
            tag.name = "blockquote"
    with open("prettified.html", "w", encoding="utf-8") as file:
        file.write(soup.prettify())
else:
    print("file not found")