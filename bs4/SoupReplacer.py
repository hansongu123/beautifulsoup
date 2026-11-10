from .element import Tag

class SoupReplacer:
    def __init__(self, og_tag=None, alt_tag=None, name_xformer=None, attrs_xformer=None, xformer=None):
        self.og_tag = og_tag
        self.alt_tag = alt_tag
        self.name_xformer = name_xformer
        self.attrs_xformer = attrs_xformer
        self.xformer = xformer
        self._open = []

    def on_start(self, tag, name, nsprefix):
        # Apply transformers
        if self.og_tag and self.alt_tag and self.og_tag == tag.name:
            tag.name = self.alt_tag
        if self.name_xformer:
            tag.name = self.name_xformer(tag)
        if self.attrs_xformer:
            tag.attrs = self.attrs_xformer(tag)
        if self.xformer:
            self.xformer(tag)
        # Add state to stack
        self._open.append((name, nsprefix, tag.name))

    def on_end(self, name, nsprefix):
        # Search for matching tag and pop state
        # Ignore stray closing tags and discards mismatched closing tags
        for i in range(len(self._open)-1, -1, -1):
            old_name, prefix, new_name = self._open[i]
            if old_name == name and prefix == nsprefix:
                name = new_name
                del self._open[i:]
                break
        return name

        