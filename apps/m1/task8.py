import sys
from bs4 import BeautifulSoup

with open(sys.argv[1], "r") as file:
    html_doc = file.read()

if html_doc:
    soup = BeautifulSoup(html_doc, 'lxml')
    # Get plain text from an element and its children
    text = soup.get_text(separator="|", strip=True)
    print(text)
else:
    print("file not found")