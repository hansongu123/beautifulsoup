import sys
from bs4 import BeautifulSoup, SoupStrainer

with open(sys.argv[1], "rb") as file:
    html_doc = file.read()

tags_with_id = SoupStrainer(id=True)
soup = BeautifulSoup(html_doc, "lxml", parse_only=tags_with_id)

print(soup.prettify())