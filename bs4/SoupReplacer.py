class SoupReplacer:
    def __init__(self, og_tag=None, alt_tag=None, name_xformer=None, attrs_xformer=None, xformer=None):
        self.og_tag = og_tag
        self.alt_tag = alt_tag
        self.name_xformer = name_xformer
        self.attrs_xformer = attrs_xformer
        self.xformer = xformer

    def _replace_name(self, tag):
        # Takes in a `Tag` object, return tag name after transformation
        if self.name_xformer is None:
            return tag.name
        return self.name_xformer(tag)

    def _replace_attrs(self, tag):
        # Takes in a `Tag` object, return tag attributes after transformation
        if self.attrs_xformer is None:
            return tag.attrs
        return self.attrs_xformer(tag)

    def _transform(self, tag):
        # If xformer argument is present, transform a `Tag` object using the provided function
        if self.xformer is None:
            return tag
        else:
            return self.xformer(tag)

    def transform(self, tag):
        if self.og_tag and self.alt_tag and tag.name == self.og_tag:
            tag.name = self.alt_tag
        tag.name = self._replace_name(tag)
        tag.attrs = self._replace_attrs(tag)
        self._transform(tag)
        return tag