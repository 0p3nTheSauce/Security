def revFunction():
    file_path = "flag.txt"  # Change this to your file's path

    try:
        # Open the file in read mode ('r' for reading)
        with open(file_path, 'r') as stream:
            # Read the contents of the file
            file_contents = stream.read()
            ptr = list(file_contents)
    except FileNotFoundError:
        print("No flag found, please make sure this is run on the server")
    except IOError:
        print("Error reading the file.")
    except Exception as e:
        print("An error occurred:", e)
    
    if (len(ptr) <= 0):
        return 
    
    file_path2 = "rev_this"
    try:
        # Open the file in read mode ('a' for appending)
        with open(file_path2, 'a') as v7:
            for i in range(8):
                v11 = ptr[i]
                v7.write(v11)
            for j in range(8, 23):
                v11 = ptr[j]
                # Check if j is odd
                if j & 1 != 0:
                    # Decrement v11 by 2
                    v11ord = ord(v11)
                    v11ord -= 2
                    v11 = chr(v11ord)
                else:
                    # Increment v11 by 5
                    v11ord = ord(v11)
                    v11ord += 5
                    v11 = chr(v11ord)
                # Write the modified value of v11 to the file stream v7
                v7.write(v11)           
            v7.write('}') 
    except FileNotFoundError:
        print("please run this on the server")
    except IOError:
        print("Error writing to the file.")
    except Exception as e:
        print("An error occurred:", e)

def undoRev():
    file_path = "rev_this"  # Change this to your file's path

    try:
        # Open the file in read mode ('r' for reading)
        with open(file_path, 'r') as stream:
            # Read the contents of the file
            file_contents = stream.read()
            ptr = list(file_contents)
    except FileNotFoundError:
        print("No flag found, please make sure this is run on the server")
    except IOError:
        print("Error reading the file.")
    except Exception as e:
        print("An error occurred:", e)
    
    if (len(ptr) <= 0):
        return 
    
    file_path2 = "flag.txt"
    try:
        with open(file_path2, 'a') as v7:
            for i in range(8):
                v11 = ptr[i]
                v7.write(v11)
            for j in range(8, 23):
                v11 = ptr[j]
                if j & 1 != 0:
                    v11ord = ord(v11)
                    v11ord += 2 
                    v11 = chr(v11ord)
                else:
                    v11ord = ord(v11)
                    v11ord -= 5
                    v11 = chr(v11ord)
                v7.write(v11)
            v7.write('}')
    except FileNotFoundError:
        print("please run this on the server")
    except IOError:
        print("Error writing to the file.")
    except Exception as e:
        print("An error occurred:", e)
                
    
    
def main():
    #revFunction()
    undoRev()
    

if __name__ == "__main__":
    main()