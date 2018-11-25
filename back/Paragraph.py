


class Paragraph(object):
    def __init__(self, file_name, nb, keywords, text):
        self.file=file_name
        self.nb=nb#of the pargraph in the file
        self.keywords=keywords
        self.text=text
    def __str__(self):
        return str(self.file)+' §'+str(self.nb)+' - '+str(self.keywords)
    def __repr__(self):
        return self.__str__()
    def eq(self,other):
        if len(self.keywords)>=3:
            return self.keywords[0] in other.keywords or self.keywords[1] in other.keywords or self.keywords[2] in other.keywords
        else:
            return False
    def common(self,other):
        return set(self.keywords).intersection(set(other.keywords))
