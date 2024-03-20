def decode_ascii(encoded_text):
    decoded_text = ""
    # Split the encoded text into chunks of 2 characters
    for i in range(0, len(encoded_text), 2):
        # Convert each chunk from hexadecimal to decimal
        decimal_value = int(encoded_text[i:i+2], 16)
        # Convert decimal value to ASCII character and append to decoded text
        decoded_text += chr(decimal_value)
    return decoded_text

# Example usage:
encoded_text = "11210599111678470123103484810095107491161161213395110499951951074911611612133955599485650491025312510" 
 
decoded_text = decode_ascii(encoded_text)
print("Decoded text:", decoded_text)

