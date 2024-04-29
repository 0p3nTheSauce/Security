flag = "picoCTF{wELF_d0N3_mate_"
v23 = '4'
v24 = '5'
v25 = '6'
v26 = '3'
v27 = 'e'
v28 = '5'
v29 = 'a'
v30 = 'e'
v31 = 'e'
v32 = 'd'
v33 = 'b'
v34 = 'f'
v35 = '6'
v36 = 'e'
v37 = 'd'
v38 = '8'

if (ord(v24) <= 65):
    flag += v34
if (ord(v35) != 65):
    flag += v37
if ("Hello" == "World"):
    flag += v25
v19 = v26
if (ord(v19) - ord(v30) == 3):
    flag += v26
flag += v25
flag += v28
if (ord(v29) == 71):
    flag += v29
flag += v27
flag += v36
flag += v23
flag += v31
flag += chr(125)

print(flag)
