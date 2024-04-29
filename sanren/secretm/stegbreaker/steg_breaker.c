#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define MAX_LINE_LENGTH 28688783

bool decode(const char *image, const char *passphrase) {
    char command[200];
    sprintf(command, "steghide extract -sf %s -p %s", image, passphrase);

    if (system(command) == 0) {
        printf("Data extracted successfully!\n");
        printf("Password: %s\n", passphrase);
        return true;
    } else {
        printf("Failed: %s\n", passphrase);
        return false;
    }
}

// char **getLines(const char *passwordList, int *lineCount) {
//     FILE *file = fopen(passwordList, "r");
//     if (file == NULL) {
//         printf("File not found!\n");
//         exit(1);
//     }

//     char **lines = malloc(MAX_LINE_LENGTH * sizeof(char *));
//     if (lines == NULL) {
//         printf("Memory allocation failed!\n");
//         exit(1);
//     }

//     *lineCount = 0;
//     char buffer[MAX_LINE_LENGTH];
//     while (fgets(buffer, MAX_LINE_LENGTH, file) != NULL) {
//         lines[*lineCount] = strdup(buffer);
//         (*lineCount)++;
//     }

//     fclose(file);
//     return lines;
// }

char **getLines(const char *passwordList, int *lineCount) {
    FILE *file = fopen(passwordList, "r");
    if (file == NULL) {
        printf("File not found!\n");
        exit(1);
    }

    // Allocate initial memory for lines
    int maxLines = 1000; // Change this value as needed
    char **lines = malloc(maxLines * sizeof(char *));
    if (lines == NULL) {
        printf("Memory allocation failed!\n");
        exit(1);
    }

    *lineCount = 0;
    char buffer[MAX_LINE_LENGTH];
    while (fgets(buffer, MAX_LINE_LENGTH, file) != NULL) {
        // Allocate memory for each line
        lines[*lineCount] = strdup(buffer);
        (*lineCount)++;

        // If we exceed the current allocation, reallocate memory
        if (*lineCount >= maxLines) {
            maxLines += 1000; // Change this increment value as needed
            char **temp = realloc(lines, maxLines * sizeof(char *));
            if (temp == NULL) {
                printf("Memory reallocation failed!\n");
                exit(1);
            }
            lines = temp;
        }
    }

    fclose(file);
    return lines;
}



void freeLines(char **lines, int lineCount) {
    for (int i = 0; i < lineCount; i++) {
        free(lines[i]);
    }
    free(lines);
}

void bruteForce(const char *image, const char *passwordList) {
    int lineCount;
    char **lines = getLines(passwordList, &lineCount);
    for (int i = 0; i < lineCount; i++) {
        if (decode(image, lines[i])) {
            break;
        }
        printf("%d / %d\n", i+1, lineCount);
    }

    freeLines(lines, lineCount);
}


int main(int argc, char *argv[]) {
    printf("stegbreaker\n");

    if (argc != 3) {
        printf("Usage: %s <steg.jpg> <wordlist>\n", argv[0]);
        return 1;
    }

    const char *image = argv[1];
    const char *passwordList = argv[2];
    bruteForce(image, passwordList);

    return 0;
}
