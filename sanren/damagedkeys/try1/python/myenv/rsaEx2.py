from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Generate RSA key pair
#key = RSA.generate(2048)

# Get the public and private keys
#public_key = key.publickey()
#private_key = key

# Load the private key from the string
private_key_str = """-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAvLr/JsjzXpYUH0HYItmxoC4kb6cW7Fe2YdRpA5nwZKxOkfK
FesAKGeO0orhhRETV/OR0M/D6SFDLqiHIimZECOTApD6Hon269o9LEU4SWbpgOBP
mub5OlnBi0jg1Hue4UF69B+B7FuFwoytpmHJ5hEI9DIeT4IznSU6joSyUz00oYt7
iXcokjqSVSdAkGPW4a51Aj9xML7UySooanXUcPRSSba3HQIvuIFYJEBNSWbDJk+m
EubvbT7g5Q86SePVpd4IE9sbY43w0j5YjwuA1J0MmY4vfSVhK5LIXO6lsp+3HeBn
AzhAKNSGP+roR2+ulET0nsC1obsL3g4gsqN+WHwIDAQABAoIBAGHO12SWR+oBBTS
dvxFwmGlXAHMMuQiK/G3+0t2W7cp+sclZUmunEpUQORELVP04X13MV5yDinHnzWT
CVVfEYAXr5xo3fbtsRXR6FoFFYKU3vZ3SUoR4Z+n3HH+tuXnmxNKCBp0KbUASXXl
yiisDSI6OdW0E5lI9M6/+HTbuD8DOa/u1NSonSIh8bUICBNEPC9JYOw7ySHLaAJA
u+ZI68nxzWKu/kUP5cMQI4YefX5U+iUU5F3WQd6Fdrbxxv7kRagX4HDqDMNj0JFy
gKov156NFH4VdIQP9Be17qP+BOsRorfoEHskFopXHH7kBqqqBG4eqAmUudM310lX
LkIx5a8ECgYEA4D44pnA3qP5y5ApAhSNTNjg977iaOJCOqAKDvUrmi0tnjgVNHgP
85RzxNjoBWiyG3PtDpLIh/9s4IXzY/IsEq8ukjPJ2tmJcxEsgjbTJmzZSLX+jLeG
ZjXsyNQ3wG6TWSKOfuWiLVrOm/7vg3BiDaLsdJBGTsEhebqEUBT3fkjkCgYEA13V
KXJ1uZ03ywc/sMGC6I6QhnoMpLXtBC8mUv2uMBzmwedjdJBl5cUocwRq+fcO2+Z9
p7sC4TJ9saXdtuv4AZTeXoDdzeZND8JQFIm4zo23viL7KOVdbxkmPJpBqswvPJgy
hKDDQUbwyfqMdj8IsOQOfzXoc8gi0q4eCIC6JCxcCgYEA1CTpUUSe08kNhoHQcmR
uB8CDj/PUKylPXNEsMvvWSfenW2vWfkwFh/eul7+eoeG4IP2xC/HeSoDphHzph1o
5rBG3dgS4nGlIHAh7HrTnemiUrCixhumEbJ4dbKXn/y8d7pClvjGSiQ7jMdNbsr2
aLI3Azuu2DjMY646GM0NK7LkCgYAkWPUiiqyFYPEDIUCHKMo+GQJS622W7qQaiPc
/E7Wbwm+zHpKv9Fw4cHhJW2mnbc0Ab5Q/YuO0iXCQmkU4toD6klZSAQjKCb38Z/w
1wsGTYIh4WTdkVQh2exJbPyHA8s0PbjIBxbpfD5C1LG9gQTGUrLfYwjD/49gW19V
r+G3GIQKBgBZ4MUkoeu2th/o5Gx2PMHHNMsnaCxDNldmW2rRUXWJG2iciHvFpdhR
pNYvKlYfjpR3nesPxBygwJp3EiHGdRo6xGWuett2RIWhJFfqmzOUx7Nt6IuJTFe/
kLypGhzeE407vJej0pXhF05ipFSRYtA4kR//K11EijSe3Wz6e9aoZ
-----END RSA PRIVATE KEY-----"""

private_key = RSA.import_key(private_key_str)

#print("Public Key: ", public_key)
print()
print("Private Key: ", private_key)
print()

# Message to encrypt
#message = b"Hello, world"

# Encrypt the message using the public key
#cipher = PKCS1_OAEP.new(public_key)
#encrypted_message = cipher.encrypt(message)

try:
    with open("cyphertext.txt", "r") as f:
        lines = f.readlines()
    encrypted_message = lines[0]
except FileNotFoundError:
    print("File cannot be found")
except IOError:
    print("Error reading file")
except Exception as e:
    print("an error ocurred: ", e)
else:
    print("File opened successfully")

print("Encrypted message:", encrypted_message)

# # Decrypt the message using the private key
# cipher = PKCS1_OAEP.new(private_key)
# decrypted_message = cipher.decrypt(encrypted_message)

# print("Decrypted message:", decrypted_message.decode())
# Decrypt the message using the private key
cipher = PKCS1_OAEP.new(private_key)
# Convert the encrypted message from string to bytes-like object
encrypted_message_bytes = encrypted_message.encode()
# Decrypt the bytes-like object
decrypted_message = cipher.decrypt(encrypted_message_bytes)
# Print the decrypted message
print("Decrypted message:", decrypted_message.decode())
