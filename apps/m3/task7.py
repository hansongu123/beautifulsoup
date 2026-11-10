import sys
from bs4 import BeautifulSoup
from bs4.SoupReplacer import SoupReplacer

with open(sys.argv[1], "r") as file:
    html_doc = file.read()

if html_doc:
    # Add or replace all <p> tags with class="test"
    def add_test_to_p(tag):
        if tag.name == 'p':
            tag.attrs["class"] = "test"
    sp = SoupReplacer(xformer=add_test_to_p)
    soup = BeautifulSoup(html_doc, 'lxml', replacer=sp)
    with open("output.html", "w", encoding="utf-8") as file:
        file.write(soup.prettify())

else:
    print("file not found")