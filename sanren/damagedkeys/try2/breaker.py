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
    
def highLight(substrings, delimiter, colour):
    print(substrings[0])
    for i in range(1, len(substrings)):
        colourD(delimiter, colour)
        print(substrings[i])
    
def colourD(string, colour):
    if colour == 0:
        print(colors.RED + string + colors.RESET)
    elif colour == 1:
        print(colors.GREEN + string + colors.RESET)
    elif colour == 2:
        print(colors.BLUE + string + colors.RESET)
    elif colour == 3:
        print(colors.YELLOW + string + colors.RESET)
    else:
        print("colour not available")
            
def restDelimiters(delimiters):
    leftDel = []
    for i in range(1, len(delimiters)):
        leftDel.append(delimiters[i])
    return leftDel
            
def recHighlight(string, delimiters, colour):
    substrings = getSubstrings(string, delimiters[0])
    if len(substrings) and len(delimiters) > 1:
        leftDel = restDelimiters(delimiters)
        recHighlight(substrings[0], leftDel, colour+1)
        for i in range(1, len(substrings)):
            colourD(delimiters[0], colour)
            recHighlight(substrings[i], leftDel, colour+1)
    else:
        highLight(substrings, delimiters[0], colour)
        
    


def main():
    print("spit out patterns")
    
    dummyKey = getLine("dummykey_baked")
    partialKey = getLine("partialKey_baked")
    #deliminator = '028201'
    #delimiters = ['028201', '02818100', '010001']
    delimiters = ['028201', '02818', '010001']
    #delimiters = ['02820101','02820100' '02818100', '010001']
    print("Dummy key: ")
    recHighlight(dummyKey, delimiters, 0)
    print()
    print("Partial key:")
    recHighlight(partialKey, delimiters, 0)
    
if __name__ == "__main__":
    main()