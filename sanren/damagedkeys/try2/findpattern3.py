def find_all_substring_indices(substring, larger_string):
    indices = []
    index = larger_string.find(substring)
    while index != -1:
        indices.append(index)
        index = larger_string.find(substring, index + 1)
    return indices

# Example usage
larger_string = "This is a larger string containing the substring. Another substring is here."
substring = "substring"

indices = find_all_substring_indices(substring, larger_string)
if indices:
    print(f"The substring '{substring}' is found at indices: {indices}.")
else:
    print(f"The substring '{substring}' is not found.")
