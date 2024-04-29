def testSHex(x4, x8):
    while(x8 <= 0xfb46):
        x4 += 0x1
        x8 += 0x74
    return(x4)
    
def testSDec(x4, x8):
    decX4 = int(x4, 16)
    decX8 = int(x8, 16)
    while(decX8 <= int("0xfb46", 16)):
        decX4 += int("0x1", 16)
        decX8 += int("0x74", 16)
    return hex(decX4)

def main():
    print("x4: ", testSHex(0x4, 0x21))
    print("x4: ", testSDec("0x21", "0x4"))

if __name__ == "__main__":
    main()