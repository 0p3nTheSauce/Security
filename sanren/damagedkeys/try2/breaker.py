from difflib import SequenceMatcher

# ANSI escape codes for text colors
class colors:
    RESET = '\033[0m'
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

def getLine(path):
    try:
        with open(path, "r") as file:
            line = file.readline()
    except FileNotFoundError:
        print("File not found.")
    return line

def getSubstrings(string, deliminator):
    substrings = string.split(deliminator)
    return substrings
    
def highLight(string, substring):
    substrings = getSubstrings(string, substring)
    print(substrings[0])
    for i in range(1, len(substrings)):
        print(colors.RED + substring + colors.RESET)
        print(substrings[i])
            

def main():
    print("spit out patterns")
    
    dummyKey = getLine("dummykey_baked")
    partialKey = getLine("partialKey_baked")
    deliminator = '028201'
    print("Dummy key: ")
    highLight(dummyKey, deliminator)
    print()
    print("Partial key:")
    highLight(partialKey, deliminator)
    
if __name__ == "__main__":
    main()