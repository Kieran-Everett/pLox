import sys

class Lox():

    def __init__(self):
        pass

    def run(self, toRun):
        print(toRun)

    def runFile(self, path):
        
        file = open(path, "rb") # With how python handles this stuff, this bit might need to be re-written so that it normally reads the file and then just appends everything into a string
        fileBytes = file.read()
        file.close()
        
        self.run(fileBytes)

    def runPrompt(self):
        
        while True:
            line = input("> ")
            if ( line == "" ):
                break
            self.run(line)

    def main(self):
        
        if ( len(sys.argv) > 2 ): # sys.argv includes the filename in its' first index so it needs to check for the second
            print("Usage: python3 pLox.py [script]")
            sys.exit(64)
        elif ( len(sys.argv) == 2 ): # Run from a file
            self.runFile(sys.argv[1])
        else:
            self.runPrompt() # An interactive prompt


if __name__ == "__main__":
    pLox = Lox()
    pLox.main()