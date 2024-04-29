import re
from Crypto.Util.number import *

with open("cyphertext.txt", "rb") as file:
 ct = bytes_to_long(file.read())

partial_priv_hex = "b9be4e967062d238351ee7b8505ebd07e07b16e170a32b6998727984423d0c8793e08ce7494ea3a12c94cf4d2862dee25dca248ea49549d02418f5b86b9d408fdc4c2fb5324a8a1a9d751c3d14926dadc7408bee20560910135259b0c993e984b9bbdb4fb83943ce9278f569778204f6c6d8e37c348f9623c2e035274326638bdf49584ae4b2173ba96ca7edc77819c0ce100a35218ffaba11dbeba5113d27b02d686ec2f783882ca8df961f02030100010282010061ced7649647ea0105349dbf117098695700730cb9088afc6dfed2dd96edca7eb1c959526ba712951039110b54fd385f5dcc579c838a71e7cd64c25557c46005ebe71a377dbb6c45747a16814560a537bd9dd252847867e9f71c7fadb979e6c4d282069d0a6d40125d79728a2b03488e8e756d04e6523d33affe1d36ee0fc0ce6bfbb5352a2748887c6d420204d10f0bd2583b0ef24872da00902ef9923af27c7358abbf9143f970c408e1879f5f953e89453917759077a15dadbc71bfb9116a05f81c3a8330d8f4245ca02a8bf5e7a3451f855d2103fd05ed7ba8ff813ac468adfa041ec905a295c71fb901aaaa811b87aa02652e74cdf5d255cb908c796bc102818100e03e38a67037a8fe72e40a4085235336383defb89a38908ea80283bd4ae68b4b678e054d1e03fce51cf1363a015a2c86dcfb43a4b221ffdb38217cd8fc8b04abcba48cf276b6625cc44b208db4c99b36522d7fa32de1998d7b32350df01ba4d648a39fb9688b56b3a6ffbbe0dc188368bb1d241193b0485e6ea114053ddf923902818100d7754a5c9d6e674df2c1cfec3060ba23a4219e83292d7b410bc994bf6b8c0739b079d8dd241979714a1cc11abe7dc3b6f99f69eec0b84c9f6c69776dbafe00653797a03773799343f09405226e33a36def88beca39575bc6498f26906ab30bcf260ca12830d051bc327ea31d8fc22c39039fcd7a1cf208b4ab8782202e890b1702818100d424e951449ed3c90d8681d072646e07c0838ff3d42b294f5cd12c32fbd649f7a75b6bd67e4c0587f7ae97bf9ea1e1b820fdb10bf1de4a80e9847ce9875a39ac11b77604b89c69481c087b1eb4e77a6894ac28b186e9846c9e1d6ca5e7ff2f1dee90a5be3192890ee331d35bb2bd9a2c8dc0ceebb60e3318eb8e8633434aecb90281802458f5228aac8560f10321408728ca3e190252eb6d96eea41a88f73f13b59bc26fb31e92aff45c387078495b69a76dcd006f943f62e3b48970909a4538b680fa9256520108ca09bdfc67fc35c2c1936088785937645508767b125b3f21c0f2cd0f6e3201c5ba5f0f90b52c6f60413194acb7d8c230ffe3d816d7d56bf86dc62102818016783149287aedad87fa391b1d8f3071cd32c9da0b10cd95d996dab4545d6246da27221ef169761469358bca9587e3a51de77ac3f1072830269dc488719d468eb1196b9eb6dd9121684915faa6cce531ecdb7a22e25315efe42f2a46873784e34eef25e8f4a57845d398a9152458b40e2447ffcad751228d27b75b3e9ef5aa19"
e = 65537
delimiters = ["010001", "02820100", "02818100"]

pattern = f"({'|'.join(map(re.escape, delimiters))})"
result = re.split(pattern, partial_priv_hex)

# Remove empty strings and delimiters from the result
result = [sub for sub in result if sub not in delimiters and sub != ""]

# print(result)
print(f"end_of_n: {result[0]}")
print(f"decryption_key(d): {result[1]}")
print(f"prime(p): {result[2]}")
print(f"prime(q): {result[3]}")
print(f"dp: {result[4]}")
#print(f"dq: {result[5]}")

d = int(result[1],16)
p = int(result[2],16)
q = int(result[3],16)
dp = int(result[4],16)
#dq = int(result[5],16)

#contruction of n
n = p * q

#decryption of message
m = pow(ct,d,n)
print(f"Decrypted Cipher Text as Flag:{long_to_bytes(m)}")

#Decrypted Cipher Text as Flag:b'Hey Bob this is Alice.\nI want to let you know that the Flag is 
#gctf{7hi5_k3y_can_b3_r3c0ns7ruc7ed}\'

from Crypto.PublicKey import RSA

key = RSA.construct((n,e,d,p,q))
pem = key.export_key('PEM')
print(pem.decode())