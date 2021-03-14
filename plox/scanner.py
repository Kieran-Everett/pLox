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

        self.keywords = {
            "and": tokenType.TokenType.AND.name,
            "class": tokenType.TokenType.CLASS.name,
            "else": tokenType.TokenType.ELSE.name,
            "false": tokenType.TokenType.FALSE.name,
            "for": tokenType.TokenType.FOR.name,
            "fun": tokenType.TokenType.FUN.name,
            "if": tokenType.TokenType.IF.name,
            "nil": tokenType.TokenType.NIL.name,
            "or": tokenType.TokenType.OR.name,
            "print": tokenType.TokenType.PRINT.name,
            "return": tokenType.TokenType.RETURN.name,
            "super": tokenType.TokenType.SUPER.name,
            "this": tokenType.TokenType.THIS.name,
            "true": tokenType.TokenType.TRUE.name,
            "var": tokenType.TokenType.VAR.name,
            "while": tokenType.TokenType.WHILE.name
        }
    
    # Functions that are called a lot
    def isAtEnd(self):
        return self.current >= len(self.source)
    
    def peek(self): # Looks ahead without consuming the character
        
        if ( self.isAtEnd() ):
            return '\0' # needs to be this because its checking for a str not bool
        
        return self.source[self.current]
    
    def peekNext(self):

        if ( self.isAtEnd() ):
            return '\0'
        
        return self.source[current + 1] # peeks two ahead to skip the decimal without advancing
    
    def addToken(self, type, literal=None): # Overloading is neat

        text = self.source[self.start:self.current]
        self.tokens.append(token(type, text, literal, line))
    
    def advance(self):

        self.current += 1
        return self.source[self.current - 1]
    
    # Functions that are for literals and lexemes

    def isAlpha(self, c):
        # This function is to check to see if something is alpha because default alpha doesn't count '_' as being alpha

        if ( c.isalpha() or c == '_' ):
            return True
        else:
            return False
        
    def isAlphaNumeric(self, c):
        # Similar funciton to the previous but for alphanumeric

        if ( self.isAlpha or c.isnumeric() ):
            return True
        else:
            return False

    def identifier(self):
        
        while ( self.isAlphaNumeric(self.peek()) ):
            self.advance()
        
        text = self.source[self.start, self.current]
        try:
            type = self.keywords[text]
        except:
            type = tokenType.TokenType.IDENTIFIER.name
        self.addToken(type)

    def number(self):

        while ( self.peek().isnumeric() ):
            self.advance()
        
        if ( peek() == '.' and peekNext().isnumeric() ):
            self.advance()

            while ( self.peek().isnumeric() ):
                self.advance()
        
        self.addToken(tokenType.TokenType.NUMBER.name, float(self.source[self.start, self.current]))
    
    def string(self):

        while ( self.peek() != '"' and not(self.isAtEnd()) ):
            if ( self.peek() == '\n' ):
                self.line += 1
                self.advance()
            
        if ( self.isAtEnd() ):
            pLox.Lox.error(line, "Unterminated string.")
            return
        
        self.advance() # The closing "

        value = self.source[start + 1, current - 1]
        self.addToken(tokenType.TokenType.STRING.name, value)
    
    def match(self, expected):
        
        if ( self.isAtEnd() ):
            return False
        if ( self.source[current] != expected ):
            return False
        
        self.current += 1
        return True
    
    # Functions for main stuff
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
            if ( self.match('=') ):
                self.addToken(tokenType.TokenType.BANG_EQUAL.name)
            else:
                self.addToken(tokenType.TokenType.BANG.name)
        elif ( c == '=' ):
            if ( self.match('=') ):
                self.addToken(tokenType.TokenType.EQUAL_EQUAL.name)
            else:
                self.addToken(tokenType.TokenType.EQUAL.name)
        elif ( c == '<' ):
            if ( self.match('=') ):
                self.addToken(tokenType.TokenType.LESS_EQUAL.name)
            else:
                self.addToken(tokenType.TokenType.LESS.name)
        elif ( c == '>' ):
            if ( self.match('=') ):
                self.addToken(tokenType.TokenType.GREATER_EQUAL.name)
            else:
                self.addToken(tokenType.TokenType.GREATER.name)
        
        elif ( c == '/' ): # SLASHes need to be handled differently because they are also used for comments
            if ( self.match('/') ):
                while ( self.peek() != '\n' and not(self.isAtEnd) ):
                    self.advance()
            else:
                self.addToken(tokenType.TokenType.SLASH.name)
        
        # skipping the rest of the random things
        elif ( c == ' ' ):
            pass
        elif ( c == '\r' ):
            pass
        elif ( c == '\t' ):
            pass
        elif ( c == '\n' ):
            self.line += 1
        
        elif ( c == '"' ):
            self.string()

        else:
            if ( c.isnumeric() ): # If it is a number
                self.number()
            elif ( self.isAlpha(c) ): # If it is a word
                self.identifier()
            else:
                pLox.Lox.error(line, "Unexpected character.")
    
    def scanTokens(self):
        
        while ( self.isAtEnd() == False ):
            start = self.current
            self.scanToken()
        
        self.tokens.append(token.Token('EOF', "", None, self.line))
        return self.tokens