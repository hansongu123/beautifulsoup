import sys
from bs4 import BeautifulSoup
# import time

# start = time.perf_counter()

with open(sys.argv[1], "r") as file:
    html_doc = file.read()

if html_doc:
    soup = BeautifulSoup(html_doc, 'lxml')
    # Add or replace all <p> tags with class="test"
    for tag in soup.find_all('p'):
            tag['class'] = "test"
    with open("prettified.html", "w", encoding="utf-8") as file:
        file.write(soup.prettify())

else:
    print("file not found")