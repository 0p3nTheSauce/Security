def bruteForce(ciphertext):
    #crossingtherubicon`aqjsscr
    print(ciphertext)
    # i assume the first 18 characters are encrypted seperatly to the last 8
    
    for j in range(127):
        decrypt = ""
        for c in ciphertext:
            ordc = ord(c)
            ordd = (ordc + j) % 127
            if (ordd < 33):
                ordd += 33
            d = chr(ordd)
            
            decrypt += d   
            
        # for c in ciphertext:
        #     ordc = ord(c)
        #     ordd = ordc + j
        #     if ordd > 122:
        #         ordd = (ordd - 122) + 96
        #     d = chr(ordd)
        #     decrypt += d   
        print(decrypt)
        
def bruteForceExt(ciphertext):
    #crossingtherubicon`aqjsscr
    print(ciphertext)
    # i assume the first 18 characters are encrypted seperatly to the last 8
    
    for j in range(257):
        decrypt = ""
        for c in ciphertext:
            ordc = ord(c)
            # ordd = (ordc + j) % 257
            # if (ordd < 33):
            #     ordd += 33
            ordd = ordc + j
            d = chr(ordd)
            
            decrypt += d    
        print(decrypt)

def test(ciphertext):
    print(ciphertext)
    decrypt = ""
    for c in ciphertext:
        ordc = ord(c)
        ordd = ordc + 25
        if ordd > 122:
            ordd = (ordd - 122) + 96
        d = chr(ordd)
        decrypt += d    
    print(decrypt)
    
# def test2(ciphertext):
#     print(ciphertext)
#     decrypt = ""
#     for c in ciphertext:
        

def first18(ciphertext):
    first18 = ciphertext[:18]
    print(first18)
    decrypt = ""
    for c in first18:
        ordc = ord(c)
        ordd = ordc + 128
        d = chr(ordd % 126)
        decrypt += d    
    print(decrypt)

def last8(ciphertext):
    last8 = ciphertext[18:len(ciphertext)]
    bruteForceExt(last8)
    

def getInput(path):
    try:
        # Open the file in read mode ('r' for reading)
        with open(path, 'r') as file:
            # Read the contents of the file
            file_contents = file.read()
            return file_contents
    except FileNotFoundError:
        print("No file found")
    except IOError:
        print("Error reading the file.")
    except Exception as e:
        print("An error occurred:", e)

def main():
    input = getInput('ciphertext')
    significant = input[8:len(input)-1]
    #test(significant)
    bruteForce(significant)
    #first18(significant)
    #last8(significant)

if __name__ == "__main__":
    main()