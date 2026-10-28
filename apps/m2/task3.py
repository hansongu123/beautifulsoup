import sys
from bs4 import BeautifulSoup, SoupStrainer

with open(sys.argv[1], "rb") as file:
    html_doc = file.read()

only_tags = SoupStrainer(True)
soup = BeautifulSoup(html_doc, "lxml", parse_only=only_tags)

print(soup.prettify())