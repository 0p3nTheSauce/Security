from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

# Generate RSA keys
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
public_key = private_key.public_key()

# Serialize keys to PEM format
private_key_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    #format=serialization.PrivateFormat.PKCS8,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)
public_key_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)
print(private_key_pem.decode())
# Example plaintext to encrypt
plaintext = b"Hello, RSA encryption!"

# Encrypt the plaintext using the public key
ciphertext = public_key.encrypt(
    plaintext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("Ciphertext:", ciphertext)
try:
    with open("ciphertext.bin", "wb") as file:
        file.write(ciphertext)
except IOError as e:
    print("Error writing to a file: ", e)

# Decrypt the ciphertext using the private key
decrypted_plaintext = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("Decrypted plaintext:", decrypted_plaintext.decode())

# def encryptT(plaintext):
    

# def main():
#     print("RSA example 1")


# if __name__ == "__main__":
#     main()