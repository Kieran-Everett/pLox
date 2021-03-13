import token
import tokenType

class Scanner():

    def __init__(self, source):

        self.source = source
        self.tokens = []

        self.start = 0
        self.current = 0
        self.line = 1
    
    def isAtEnd(self):
        return self.current >= len(self.source)

    def scanToken(self):
        pass
    
    def scanTokens(self):
        
        while ( isAtEnd == False ):
            start = current
            self.scanToken()
        
        newToken = token('EOF', "", None, line)
        self.tokens.append(newToken.toString())
        return self.tokens