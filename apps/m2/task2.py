import sys
from bs4 import SoupStrainer, BeautifulSoup

with open(sys.argv[1], "rb") as file:
    html_doc = file.read()

only_a_tags = SoupStrainer("a")
soup = BeautifulSoup(html_doc, "lxml", parse_only=only_a_tags)
print(soup.prettify())