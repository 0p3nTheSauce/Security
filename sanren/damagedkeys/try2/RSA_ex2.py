from Crypto.PublicKey import RSA

try:
    # Example parameters (replace with your actual values)
    n = 1234567890
    e = 65537
    d = 1234567890
    p = 1234567
    dp = 1234567
    dq = 1234567

    # Ensure that the modulus is an odd number
    if n % 2 == 0:
        n += 1

    # Create an RSA key object
    key = RSA.construct((n, e, d, p, dp, dq))

    # Example ciphertext (replace with your actual ciphertext)
    ciphertext = b'\x01\x02\x03\x04\x05'

    # Decrypt the ciphertext
    plaintext = key.decrypt(ciphertext)

    print("Decrypted plaintext:", plaintext)

except ValueError as ve:
    print("ValueError:", ve)
except Exception as e:
    print("Error:", e)
