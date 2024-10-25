#!/usr/bin/python3


class Text(str):
    """A Text class to represent a text you could use with your HTML elements."""
    def __str__(self):
        return (super().__str__()
                .replace('&', '&amp;')
                .replace('<', '&lt;')
                .replace('>', '&gt;')
                .replace('"', '&quot;')
                .replace('\n', '\n<br />\n'))

class Elem:
    """
    Elem will permit us to represent our HTML elements.
    """
    class ValidationError(Exception):
        """Custom exception for invalid content types in Elem."""
        pass

    def __init__(self, tag='div', attr=None, content=None, tag_type='double'):
        """
        __init__() method.
        Obviously.
        """
        self.tag = tag
        self.attr = attr if attr is not None else {}
        self.content = []
        if content is not None:
            self.add_content(content)
        self.tag_type = tag_type

    def __str__(self):
        """
        The __str__() method will permit us to make a plain HTML representation
        of our elements.
        Make sure it renders everything (tag, attributes, embedded
        elements...).
        """
        if self.tag_type == 'double':
            result = f"<{self.tag}{self.__make_attr()}> {self.__make_content()}"
            result += '</' + self.tag + '>'
        elif self.tag_type == 'simple':
            result = '<' + self.tag + self.__make_attr() + ' />'
        return result

    def __make_attr(self):
        """
        Here is a function to render our elements attributes.
        """
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        """
        Here is a method to render the content, including embedded elements.
        """
        if len(self.content) == 0:
            return ''
        result = '\n'
        for elem in self.content:
            result += '  ' + str(elem).replace('\n', '\n  ').strip() + '\n'
        return result


    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError("Invalid content type.")
        if type(content) == list:
            self.content += [elem for elem in content if elem != Text('')]
        elif content != Text(''):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        """
        Is this object a HTML-compatible Text instance or a Elem, or even a
        list of both?
        """
        return (isinstance(content, Elem) or isinstance(content, Text) or
                (isinstance(content, list) and all(isinstance(elem, (Text, Elem)) for elem in content)))


if __name__ == '__main__':
    # Test of the Elem class
    elem1 = Elem(tag='html', attr={'class': 'container'}, content=[
                                                            Elem('head', {},content=[
                                                                Elem('title', {}, Text('Hello ground!'))
                                                            ]),
                                                            Elem('body', {}, content=[
                                                                Elem('h1', {}, Text('Oh no, not again')),
                                                                Elem('img', {'src' : "http://i.imgur.com/pfp3T.jp"}, [], 'simple'),
                                                            ])
                                                        ])
    print(elem1)