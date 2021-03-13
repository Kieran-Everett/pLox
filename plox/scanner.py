import token
import tokenType

class Scanner():

    def __init__(self, source):

        self.source = source
        self.tokens = []

        self.start = 0
        self.current = 0
        self.line = 1

    def addToken(self, type, literal=None): # Overloading is neat

        text = self.source[self.start:self.current]
        self.tokens.append(token(type, text, literal, line))

    def advance(self):

        self.current = self.current + 1
        return self.source[self.current - 1]
    
    def scanToken(self):
        
        c = advance()
        if c == '(':
            addToken(tokenType.TokenType.LEFT_PAREN.name)
        elif c == ')':
            addToken(tokenType.TokenType.RIGHT_PAREN.name)
        elif c == '{':
            addToken(tokenType.TokenType.LEFT_BRACE.name)
        elif c == '}':
            addToken(tokenType.TokenType.RIGHT_BRACE.name)
        elif c == ',':
            addToken(tokenType.TokenType.COMMA.name)
        elif c == '.':
            addToken(tokenType.TokenType.DOT.name)
        elif c == '-':
            addToken(tokenType.TokenType.MINUS.name)
        elif c == '+':
            addToken(tokenType.TokenType.PLUS.name)
        elif c == ';':
            addToken(tokenType.TokenType.SEMICOLON.name)
        elif c == '*':
            addToken(tokenType.TokenType.STAR.name)
    
    def isAtEnd(self):
        return self.current >= len(self.source)
    
    def scanTokens(self):
        
        while ( isAtEnd == False ):
            start = current
            self.scanToken()
        
        newToken = token('EOF', "", None, line)
        self.tokens.append(newToken.toString())
        return self.tokens