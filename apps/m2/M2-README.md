# Milestone-2
API Functions locations:
BeautifulSoup() ./bs4/__init__.py line 133
SoupStrainer() ./bs4/filter.py line 313
.find() ./bs4/filter.py line 123
.find_all() ./bs4/filter.py line 137
.find_parent() ./bs4/element.py line 992
.get_text() ./bs4/element.py line 524

# SoupReplacer
Add a flag on BeautifulSoup Object similar to parse_only that takes in a SoupReplacer Object
Create a SoupReplacer Object with two attributes og-tag and alt-tag
Edit tag value when replacer flag is enabled during parsing (possible in handle_starttag and handle_endtag)