import subprocess
import sys
from multiprocessing import Pool

# def decode(image, passphrase):
#     found = False
#     # Command to execute
#     command = ["steghide", "extract", "-sf", image, "-p", passphrase]

#     # Execute the command
#     try:
#         subprocess.run(command, check=True)
#         print("Data extracted successfully!")
#         print("Password: ", passphrase)       
#         found = True
#     except subprocess.CalledProcessError as e:
#         #print("Error:", e)
#         print("Failed: ", passphrase)
        
#     return found

# def encode(image, passphrase, text):
#     #command to execute
#     command = ["steghide", "embed", "-cf", image, "-ef", text, "-sf", "steg"+image, "-p", passphrase]
#     # Execute the command
#     try:
#         subprocess.run(command, check=True)
#         print("Data encoded successfully!")
#     except subprocess.CalledProcessError as e:
#         print("Error:", e)
     
# def bruteForce(image, passwordList):
#     lines = getLines(passwordList)
#     line_count = len(lines)
#     idx = 0
#     for line in lines:
#         found = decode(image, line)
#         print(str(idx) + " / " + str(line_count))
#         idx += 1
#         if (found):
#             return

# def divUpLists(lines):
#     line_count = len(lines)
#     rows = 12 #CPU cores
#     columns = line_count // rows 
#     carryOver = line_count % rows
#     matrix_list = [[0 for j in range(columns)] for i in range(rows)]
#     for i in range(rows):
#         for j in range(columns):
#             matrix_list[i][j] = lines[i + j]
#     return matrix_list, carryOver
 
def getLines(passwordList):
    try:
        # Open the file in read mode
        with open(passwordList, "r") as file:
            # Read all lines from the file into a list
            lines = file.readlines()
    except FileNotFoundError:
        print("File not found!")
    except IOError as e:
        print("Error reading the file:", e)
    else:
        #return lines 
        return lines
        
def parDecode(image_passphrase):
    image, passphrase = image_passphrase
    command = ["steghide", "extract", "-sf", image, "-p", passphrase]
    try:
        subprocess.run(command, check=True)
        print("Data extracted successfully from", image)
        return passphrase
    except subprocess.CalledProcessError:
        return None


def parallelBruteForce(image, passwordList):
    lines = getLines(passwordList)
    #matrixLists, carryOver = divUpLists(lines)
    #print(matrixLists, carryOver)
    
    image_passpharses = [(image, passphrase) for passphrase in lines]
    with Pool() as pool:
        results = pool.map(parDecode, image_passpharses)
    return [result for result in results if result is not None]
    

def main():
    print("stegbreaker")
    #encode("Mario.jpg", "abcd123", "test.txt")
    #decode("stegMario.jpg", "abcd123")
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python script.py <steg.jpg> <wordlist>")
        sys.exit(1)

    # Get the filename argument from the command line
    image = sys.argv[1]
    passwordList = sys.argv[2]
    #bruteForce(image, passwordList)
    passphrase = parallelBruteForce(image, passwordList)
    print("Password: ", passphrase)
    

if __name__ == "__main__":
    main()