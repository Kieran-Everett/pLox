import sys

from scanner import Scanner

class Lox():

    def __init__(self):
        
        self.hadError = False

    def report(self, line, where, message):
        
        print("[line "+ line + "] Error" + where + ": " + message)
        self.hadError = True

    def error(self, line, message):
        
        self.report(line, "", message)

    def run(self, source):
        
        scanner = Scanner(source)
        tokens = scanner.scanTokens()

        for token in tokens:
            print(token)

    def runFile(self, path):
        
        file = open(path, "rb") # With how python handles this stuff, this bit might need to be re-written so that it normally reads the file and then just appends everything into a string
        fileBytes = file.read()
        file.close()
        
        self.run(fileBytes)

        if ( self.hadError ):
            sys.exit(65) # EX_DATAERR (65) User's data is incorrect, not system files

    def runPrompt(self):
        
        while True:
            line = input("> ")
            if ( line == "" ):
                break
            self.run(line)
            self.hadError = False:

    def main(self):
        
        if ( len(sys.argv) > 2 ): # sys.argv includes the filename in its' first index so it needs to check for the second
            print("Usage: python3 pLox.py [script]")
            sys.exit(64) # EX_USAGE (64) Command was used incorrectly
        elif ( len(sys.argv) == 2 ): # Run from a file
            self.runFile(sys.argv[1])
        else:
            self.runPrompt() # An interactive prompt


if __name__ == "__main__":
    pLox = Lox()
    pLox.main()