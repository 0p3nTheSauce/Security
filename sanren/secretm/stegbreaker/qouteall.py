import sys

# def getLines(passwordList):
#     try:
#         # Open the file in read mode
#         with open(passwordList, "r") as file:
#             # Read all lines from the file into a list
#             lines = file.readlines()
#     except FileNotFoundError:
#         print("File not found!")
#     except IOError as e:
#         print("Error reading the file:", e)
#     else:
#         #return lines 
#         return lines


def getLines(passwordList):
    try:
        # Open the file in read mode, specifying error handling
        with open(passwordList, "r", errors="ignore") as file:
            # Read all lines from the file into a list
            lines = file.readlines()
    except FileNotFoundError:
        print("File not found!")
    except IOError as e:
        print("Error reading the file:", e)
    else:
        return lines


def qoute(file):
    lines = getLines(file)
    try:
        with open(file + 'q', "w") as f:
            for line in lines:
                f.write('\'')
                f.write(line[0:len(line)-1])
                f.write('\'')
                f.write('\n')
    except FileNotFoundError:
        print("File not found!")
    except IOError as e:
        print("Error reading the file:", e)
                

def main():
    print("qoute all")
    if len(sys.argv) != 2:
        print("Usage: python script.py <wordlist>")
        sys.exit(1)
    file = sys.argv[1]
    qoute(file)
    
if __name__ == "__main__":
    main()