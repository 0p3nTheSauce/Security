import hashlib

def read_lines(path):
    lines = [] 
    try:
        with open(path, 'r') as file:
            for line in file:
                # Remove trailing newline character and add the line to the list
                lines.append(line.rstrip())
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
    except IOError:
        print(f"Error: Unable to read file '{path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        print("File read successfully.")
        return lines

def calculate_md5(string):
    md5_hash = hashlib.md5()
    md5_hash.update(string.encode('utf-8'))  # Update the hash object with the string encoded as bytes
    return md5_hash.hexdigest()  # Get the hexadecimal representation of the hash

def breakmd5(wordlist, match):
    lines = read_lines(wordlist)
    for line in lines:
        if (match == calculate_md5(line)):
            return line        
    

def main():
    print(breakmd5('wordlist.txt', 'aaedfac4a732ad7608d720886b69f289'))

if __name__ == "__main__":
    main()