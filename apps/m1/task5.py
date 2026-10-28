import sys
from bs4 import BeautifulSoup

with open(sys.argv[1], "r") as file:
    html_doc = file.read()

if html_doc:
    soup = BeautifulSoup(html_doc, 'lxml')
    # If we have access to one element, we can scrape the entire table by using find_parent()
    cell = soup.find(string="Main Framework Router") # Replace with file-specific string
    row = cell.find_parent('tr')
    table = row.find_parent('tbody')
    print(table)

    # Or we can use it to group content
    section = soup.find(string="Ordered step number one") # Replace with file-specific string
    container = section.find_parent('section')
    if container and container.get('id') == 'lists':
        print("Found a valid section!")
else:
    print("file not found")