from bs4 import BeautifulSoup, SoupReplacer

markup = "No<b>Yes</b>No<b>Yes <c>Yes</c></b>"
b_to_d = SoupReplacer('b', 'd')
soup = BeautifulSoup(markup, "html.parser", replacer=b_to_d)

for node in soup:
    print(node)