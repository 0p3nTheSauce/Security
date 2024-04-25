#!/bin/bash

# Replace these variables with the actual filenames
PRIVATE_KEY="private.pem"
ENCRYPTED_FLAG="flag.txt.enc"


# Decrypt the flag
openssl rsautl -decrypt -inkey "$PRIVATE_KEY" -in "$ENCRYPTED_FLAG"
