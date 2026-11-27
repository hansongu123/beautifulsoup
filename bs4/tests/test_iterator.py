from bs4 import BeautifulSoup, SoupStrainer, SoupReplacer

class TestSoupIterator:
    def test_iterator_one_tag(self):
        markup = "<b>Yes</b>"
        soup = BeautifulSoup(markup, "html.parser")
        res = []
        i = 0
        for node in soup:
            res.append(str(node))
            i += 1

        assert i == 1
        assert "".join(res) == markup

    def test_iterator_nested_tags(self):
        # Test nested tags
        markup = "No<b>Yes</b>No<b>Yes <c>Yes</c></b>"
        soup = BeautifulSoup(markup, "html.parser")
        res = []
        i = 0
        for node in soup:
            res.append(str(node))
            i += 1

        # Iterator should ignore elements other than Tag
        assert i == 3
        assert "".join(res) == "<b>Yes</b><b>Yes <c>Yes</c></b><c>Yes</c>"

        # Iterating through a BeautifulSoup object should behave exactly like .find_all(True)
        expected = []
        for node in soup.find_all(True):
            expected.append(str(node))

        assert "".join(res) == "".join(expected)

    def test_iterator_with_strainer(self):
        # Iterating through a BeautifulSoup object with SoupStrainer applied
        markup = "<a>abcd</a>No<b>Yes</b><a>abcd</a>No<b>Yes <c>Yes</c></b><a>abcd</a>"
        soup = BeautifulSoup(markup, "html.parser", parse_only= SoupStrainer("b"))
        res = []
        for node in soup:
            res.append(str(node))

        expected = []
        for node in soup.find_all(True):
            expected.append(str(node))

        assert "".join(res) == "".join(expected)

    def test_iterator_with_replacer_constructor(self):
        # Test iterator with SoupReplacer enabled (constructor only)
        markup = "No<b>Yes</b>No<b>Yes <c>Yes</c></b>"
        b_to_d = SoupReplacer('b', 'd')
        soup = BeautifulSoup(markup, "html.parser", replacer=b_to_d)

        res = []
        for node in soup:
            res.append(str(node))

        assert "".join(res) == "<d>Yes</d><d>Yes <c>Yes</c></d><c>Yes</c>"

        expected = []
        for node in soup.find_all(True):
            expected.append(str(node))

        assert "".join(res) == "".join(expected)

    def test_iterator_with_replacer_xformer(self):
        # Test iterator with SoupReplacer enabled (w/ transformer)
        def b_to_d(tag):
            if tag.name == 'b':
                tag.name = 'd'
        markup = "No<b>Yes</b>No<b>Yes <c>Yes</c></b>"
        sr = SoupReplacer(xformer=b_to_d)
        soup = BeautifulSoup(markup, "html.parser", replacer=sr)

        res = []
        for node in soup:
            res.append(str(node))

        assert "".join(res) == "<d>Yes</d><d>Yes <c>Yes</c></d><c>Yes</c>"

        expected = []
        for node in soup.find_all(True):
            expected.append(str(node))

        assert "".join(res) == "".join(expected)      