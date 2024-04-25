from sympy import mod_inverse

# Define the number and modulus
a = 7
m = 11
#(a*b)%m =1
# Find the multiplicative modular inverse
b = mod_inverse(a, m)

print("Multiplicative modular inverse of", a, "modulo", m, "is:", b)
