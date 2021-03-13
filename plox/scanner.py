class Scanner():

    def __init__(self, in_line):

        self.source = in_line
    
    def scanTokens(self):
        
        tokens = [self.source]
        return tokens