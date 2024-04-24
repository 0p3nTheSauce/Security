# Example string with multiple delimiters
string = "Hello, world; this|is-a;sample,string"

# List of delimiters
delimiters = [',', ';', '|', '-']

# Split the string iteratively based on each delimiter
for delimiter in delimiters:
    string = ' '.join(string.split(delimiter))

# Split the string based on whitespace to remove any additional spaces introduced
substrings = string.split()

print(substrings)
