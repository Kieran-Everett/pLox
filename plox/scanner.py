import token
import tokenType
import pLox

class Scanner():

    def __init__(self, source):

        self.source = source
        self.tokens = []

        self.start = 0
        self.current = 0
        self.line = 1

        self.isAtEnd = False
    
    def match(self, expected):
        if ( self.isAtEnd ):
            return False
        if ( self.source[current] != expected ):
            return False
        
        self.current += 1
        return True

    def addToken(self, type, literal=None): # Overloading is neat

        text = self.source[self.start:self.current]
        self.tokens.append(token(type, text, literal, line))

    def advance(self):

        self.current += 1
        return self.source[self.current - 1]
    
    def scanToken(self):
        
        c = self.advance()

        if ( c == '(' ):
            self.addToken(tokenType.TokenType.LEFT_PAREN.name)
        elif ( c == ')' ):
            self.addToken(tokenType.TokenType.RIGHT_PAREN.name)
        elif ( c == '{' ):
            self.addToken(tokenType.TokenType.LEFT_BRACE.name)
        elif ( c == '}' ):
            self.addToken(tokenType.TokenType.RIGHT_BRACE.name)
        elif ( c == ',' ):
            self.addToken(tokenType.TokenType.COMMA.name)
        elif ( c == '.' ):
            self.addToken(tokenType.TokenType.DOT.name)
        elif ( c == '-' ):
            self.addToken(tokenType.TokenType.MINUS.name)
        elif ( c == '+' ):
            self.addToken(tokenType.TokenType.PLUS.name)
        elif ( c == ';' ):
            self.addToken(tokenType.TokenType.SEMICOLON.name)
        elif ( c == '*' ):
            self.addToken(tokenType.TokenType.STAR.name)

        elif ( c == '!' ):
            if ( match('=') ):
                self.addToken(tokenType.TokenType.BANG_EQUAL.name)
            else:
                self.addToken(tokenType.TokenType.BANG.name)
        elif ( c == '=' ):
            if ( match('=') ):
                self.addToken(tokenType.TokenType.EQUAL_EQUAL.name)
            else:
                self.addToken(tokenType.TokenType.EQUAL.name)
        elif ( c == '<' ):
            if ( match('=') ):
                self.addToken(tokenType.TokenType.LESS_EQUAL.name)
            else:
                self.addToken(tokenType.TokenType.LESS.name)
        elif ( c == '>' ):
            if ( match('=') ):
                self.addToken(tokenType.TokenType.GREATER_EQUAL.name)
            else:
                self.addToken(tokenType.TokenType.GREATER.name)

        else:
            pLox.Lox.error(line, "Unexpected character.")
    
    def isAtEnd(self):
        return self.current >= len(self.source)
    
    def scanTokens(self):
        
        while ( self.isAtEnd == False ):
            start = current
            self.scanToken()
        
        newToken = token('EOF', "", None, line)
        self.tokens.append(newToken.toString())
        return self.tokens