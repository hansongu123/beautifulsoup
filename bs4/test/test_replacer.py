# -*- coding: utf-8 -*-
"""Tests of Beautiful Soup as a whole."""

from bs4 import BeautifulSoup

from bs4.SoupReplacer import SoupReplacer

class TestSoupReplacer():
    # TESTING CONSTRUCTOR ARGUMENTS
    def test_replace_tags(self):
        # Test replacing tags during parse
        markup = "<b>Yes</b>"
        b_to_a = SoupReplacer('b', 'a')
        soup = BeautifulSoup(markup, "html.parser", replacer=b_to_a)
        expected = BeautifulSoup("<a>Yes</a>", "html.parser")
        assert soup.decode_contents() == expected.decode_contents()
        
        # Test nested tags
        markup = "No<b>Yes</b>No<b>Yes <c>Yes</c></b>"
        b_to_d = SoupReplacer('b', 'd')
        soup = BeautifulSoup(markup, "html.parser", replacer=b_to_d)
        expected = BeautifulSoup("No<d>Yes</d>No<d>Yes <c>Yes</c></d>", "html.parser")
        assert soup.decode_contents() == expected.decode_contents()

    def test_empty_tags(self):
        # Test both empty
        markup = "<b>Yes</b>"
        empty = SoupReplacer('', '')
        soup = BeautifulSoup(markup, "html.parser", replacer=empty)
        expected = BeautifulSoup("<b>Yes</b>", "html.parser")
        assert soup.decode_contents() == expected.decode_contents()
        
        # Test left empty
        markup = "<b>Yes</b>"
        no_og = SoupReplacer('', 'a')
        soup = BeautifulSoup(markup, "html.parser", replacer=no_og)
        expected = BeautifulSoup("<b>Yes</b>", "html.parser")
        assert soup.decode_contents() == expected.decode_contents()

        # Test right empty
        markup = "<b>Yes</b>"
        no_alt = SoupReplacer('a', '')
        soup = BeautifulSoup(markup, "html.parser", replacer=no_alt)
        expected = BeautifulSoup("<b>Yes</b>", "html.parser")
        assert soup.decode_contents() == expected.decode_contents()

    # TESTING TRANSFORMERS
    def test_name_xformer(self):
        # Test replacing tags during parse
        markup = "<b>Yes</b>"
        b_to_a = SoupReplacer(name_xformer=lambda tag: "a" if tag.name=="b" else tag.name)
        soup = BeautifulSoup(markup, "html.parser", replacer=b_to_a)
        expected = BeautifulSoup("<a>Yes</a>", "html.parser")
        assert soup.decode_contents() == expected.decode_contents()
        
        # Test nested tags
        markup = "No<b>Yes</b>No<b>Yes <c>Yes</c></b>"
        b_to_d = SoupReplacer(name_xformer=lambda tag: "d" if tag.name=="b" else tag.name)
        soup = BeautifulSoup(markup, "html.parser", replacer=b_to_d)
        expected = BeautifulSoup("No<d>Yes</d>No<d>Yes <c>Yes</c></d>", "html.parser")
        print(soup.decode_contents())
        assert soup.decode_contents() == expected.decode_contents()

    def test_attrs_xformer(self):
        # Test replacing tags during parse
        markup = "<b class='example'>Yes</b>"
        sr = SoupReplacer(attrs_xformer=lambda tag: {'class':"after", 'id':'1'} if tag.name=='b' else tag.attrs)
        soup = BeautifulSoup(markup, "html.parser", replacer=sr)
        expected = BeautifulSoup("<b class='after' id='1'>Yes</b>", "html.parser")
        assert soup.decode_contents() == expected.decode_contents()

        # Test nested tags
        markup = "No<b>Yes</b>No<b>Yes <c>Yes</c></b>"
        sr = SoupReplacer(attrs_xformer=lambda tag: {'class':"after", 'id':'1'} if tag.name=='c' else tag.attrs)
        soup = BeautifulSoup(markup, "html.parser", replacer=sr)
        expected = BeautifulSoup("No<b>Yes</b>No<b>Yes <c class='after' id='1'>Yes</c></b>", "html.parser")
        assert soup.decode_contents() == expected.decode_contents()

    def test_xformer(self):
        # Test delete attribute
        def remove_class_attr(tag):
            if "class" in tag.attrs:
                del tag.attrs["class"]
        markup = "No<b>Yes</b>No<b>Yes <c class='after'>Yes</c></b>"
        sr = SoupReplacer(xformer=remove_class_attr)
        soup = BeautifulSoup(markup, "html.parser", replacer=sr)
        expected = BeautifulSoup("No<b>Yes</b>No<b>Yes <c>Yes</c></b>", "html.parser")
        assert soup.decode_contents() == expected.decode_contents()

        # Test add attribute
        def add_id_attr(tag):
            if "id" not in tag.attrs:
                if tag.name == 'c':
                    tag.attrs["id"] = 1
        markup = "No<b>Yes</b>No<b>Yes <c>Yes</c></b>"
        sr = SoupReplacer(xformer=add_id_attr)
        soup = BeautifulSoup(markup, "html.parser", replacer=sr)
        expected = BeautifulSoup("No<b>Yes</b>No<b>Yes <c id='1'>Yes</c></b>", "html.parser")
        assert soup.decode_contents() == expected.decode_contents()

        # Test replace name
        def b_to_d(tag):
            if tag.name == 'b':
                tag.name = 'd'
        markup = "No<b>Yes</b>No<b>Yes <c>Yes</c></b>"
        sr = SoupReplacer(xformer=b_to_d)
        soup = BeautifulSoup(markup, "html.parser", replacer=sr)
        expected = BeautifulSoup("No<d>Yes</d>No<d>Yes <c>Yes</c></d>", "html.parser")
        assert soup.decode_contents() == expected.decode_contents()     