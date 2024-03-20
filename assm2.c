#include <stdio.h>
#include <string.h>

//int strcmp(int var0, int var1) {
//    int var2 = 66864;
//    int var3 = 32;
//    int var4 = var2 - var3;
//    *(int*)(var4 + 24) = var4;
//    *(int*)(var4 + 20) = var0;
//    *(int*)(var4 + 16) = *(int*)(var4 + 24);
//    *(int*)(var4 + 12) = var1;
//    int var5 = *(int*)(var4 + 24);
//    *(int*)(var4 + 16) = var5;
//    int var6 = *(int*)(var4 + 20);
//    *(int*)(var4 + 12) = var6;
//    while (1) {
//        int var7 = *(int*)(var4 + 16);
//        int var8 = 1;
//        int var9 = var7 + var8;
//        *(int*)(var4 + 16) = var9;
//        int var10 = *(unsigned char*)var7;
//        *(char*)(var4 + 11) = var10;
//        int var11 = *(int*)(var4 + 12);
//        int var12 = 1;
//        int var13 = var11 + var12;
//        *(int*)(var4 + 12) = var13;
//        int var14 = *(unsigned char*)var11;
//        *(char*)(var4 + 10) = var14;
//        int var15 = *(unsigned char*)(var4 + 11);
//        int var16 = 255;
//        int var17 = var15 & var16;
//        if (var17) {
//            int var18 = *(unsigned char*)(var4 + 11);
//            int var19 = 255;
//            int var20 = var18 & var19;
//            int var21 = *(unsigned char*)(var4 + 10);
//            int var22 = 255;
//            int var23 = var21 & var22;
//            int var24 = var20 - var23;
//            *(int*)(var4 + 28) = var24;
//            break;
//        }
//        int var25 = *(unsigned char*)(var4 + 11);
//        int var26 = 255;
//        int var27 = var25 & var26;
//        int var28 = *(unsigned char*)(var4 + 10);
//        int var29 = 255;
//        int var30 = var28 & var29;
//        int var31 = var27 == var30;
//        int var32 = 1;
//        int var33 = var31 & var32;
//        if (var33) {
//            continue;
//        }
//        int var36 = *(unsigned char*)(var4 + 11);
//        int var37 = 255;
//        int var38 = var36 & var37;
//        int var39 = *(unsigned char*)(var4 + 10);
//        int var40 = 255;
//        int var41 = var39 & var40;
//        int var42 = var38 - var41;
//        *(int*)(var4 + 28) = var42;
//        break;
//    }
//    int var43 = *(int*)(var4 + 28);
//    return var43;
//}
//
//int check_flag() {
//    int var0 = 0;
//    int var1 = 1072;
//    int var2 = 1024;
//    int var3 = strcmp(var2, var1);
//    int var4 = var3;
//    int var5 = var0;
//    int var6 = var4 != var5;
//    int var7 = -1;
//    int var8 = var6 ^ var7;
//    int var9 = 1;
//    int var10 = var8 & var9;
//    int var11 = var10;
//    return var11;
//}
//
//void copy_char(int var0, int var1) {
//    int var2 = 66864;
//    int var3 = 16;
//    int var4 = var2 - var3;
//    *(int*)(var4 + 12) = var0;
//    *(int*)(var4 + 8) = var1;
//    int var5 = *(int*)(var4 + 12);
//    int var6 = *(int*)(var4 + 8);
//    *(char*)(var5 + 1072) = var6;
//}

int main() {
    char flag[33] = "\x9d\x6e\x93\xc8\xb2\xb9\x41\x8b\x90\xc2\xdd\x63\x93\x93\x92\x8f\x64\x92\x9f\x94\xd5\x62\x91\xc5\xc0\x8e\xf4\xc4\x97\xc0\x8f\x31\xc1\x90\xc4\x8b\x61\xc2\x94\xc9\x90\x00\x00";
    int key = 1067;
    int i;
    for (i = 0; i < 32; i++) {
        copy_char(key, flag[i]);
    }
    flag[32] = '\0';
    printf("%s\n", flag);
    return 0;
}

