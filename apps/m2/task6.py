import sys
from bs4 import BeautifulSoup
from bs4.SoupReplacer import SoupReplacer

with open(sys.argv[1], "r") as file:
        html_doc = file.read()

if html_doc:
    # Change all <b> to <blockquote>
    b_to_bq = SoupReplacer("b", "blockquote")
    soup = BeautifulSoup(html_doc, 'lxml', replacer=b_to_bq)
    with open("replaced.html", "w", encoding="utf-8") as file:
        file.write(soup.prettify())

    soup = BeautifulSoup(html_doc, 'lxml')
    # Change all <b> to <blockquote>
    for tag in soup.find_all('b'):
            tag.name = "blockquote"
    with open("prettified.html", "w", encoding="utf-8") as file:
        file.write(soup.prettify())
else:
    print("file not found")