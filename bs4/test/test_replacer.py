# -*- coding: utf-8 -*-
"""Tests of Beautiful Soup as a whole."""

from bs4 import BeautifulSoup

from bs4.SoupReplacer import SoupReplacer

class TestSoupReplacer():
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