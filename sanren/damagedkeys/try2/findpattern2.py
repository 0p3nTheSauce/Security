from difflib import SequenceMatcher

def find_matching_strings(text1, text2, substring_length=6):
    matches = []
    for i in range(len(text1) - substring_length + 1):
        substring = text1[i:i + substring_length]
        matcher = SequenceMatcher(None, substring, text2)
        match = matcher.find_longest_match(0, len(substring), 0, len(text2))
        if match.size == substring_length:
            matches.append(substring)
    return matches

text1 = "This is a sample text with a matching substring: 123456 and another one: 654321."
text2 = "Another sample text with a matching substring: 654321 and another one: 123456."

matches = find_matching_strings(text1, text2)
print("Matching strings of length 6:", matches)
