


class Paragraph(object):
    def __init__(self, file_name, nb, keywords):
        self.file=file_name
        self.nb=nb#of the pargraph in the file
        self.keywords=keywords
    def __str__(self):
        return str(self.file)+' §'+str(self.nb)+' - '+str(self.keywords)
    def __repr__(self):
        return self.__str__()
    


    
        
