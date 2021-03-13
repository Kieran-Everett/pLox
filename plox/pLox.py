import sys

class Lox():

    def __init__(self):
        pass

    def runFile(self, path):
        pass

    def runPrompt(self):
        pass

    def main(self):
        
        if ( len(sys.argv) > 2 ):
            print("Usage: python3 pLox.py [script]")
            sys.exit(64)
        elif ( len(sys.argv) == 2 ):
            self.runFile(sys.argv[1])
        else:
            self.runPrompt()


if __name__ == "__main__":
    pLox = Lox()
    pLox.main()