from difflib import SequenceMatcher

text1 = "This is a sample text."
text2 = "Another sample text here."

matcher = SequenceMatcher(None, text1, text2)
matches = matcher.find_longest_match(0, len(text1), 0, len(text2))

matching_substring = text1[matches.a:matches.a + matches.size]

print("Longest matching substring:", matching_substring)
