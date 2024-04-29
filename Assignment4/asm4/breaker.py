def asm4(px8):
    x10 = int("0x252", 16)
    xc = int("0x0", 16)
    edx = xc
    eax = px8
    eax += edx
    if (eax != 0){
        xc += int("0x1", 16)
        edx = xc 
        eax = px8
        eax += edx
        
    } else {
        #mx8 = int("0x1", 16)
    }

def main():
    print()

if __name__ == "__main__":
    main()