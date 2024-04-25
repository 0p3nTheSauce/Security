from breaker import getLine

def getStrings(string, delimiters):
    # Split the string iteratively based on each delimiter
    for delimiter in delimiters:
        string = ' '.join(string.split(delimiter))

    # Split the string based on whitespace to remove any additional spaces introduced
    substrings = string.split()
    return substrings

def writeStrings(path, strings):
    try:
        with open(path, "w") as file:
            idx = 0
            for string in strings:
                info = "String number " + str(idx)
                file.write(info)
                file.write("\n")
                file.write(string)
                file.write("\n")
                idx += 1
    except FileNotFoundError:
        print("File not found")
    except IOError as e:
        print("An error occured while writing to the file: ", e)
        
def main():
    print("Builder")
    dummyKey = getLine("dummykey_baked")
    delimiters = ['028201', '02818100', '010001']
    #delimiters = ['0282', '010001']
    substrings = getStrings(dummyKey, delimiters)
    writeStrings("testbuilder.txt", substrings)
    

if __name__ =="__main__":
    main()