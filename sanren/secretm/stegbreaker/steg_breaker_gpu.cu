#include <cuda_runtime.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define INITIAL_LINE_CAPACITY 100
#define LINE_INCREMENT 100

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

char **getLines(const char *passwordList, int *lineCount) {
    FILE *file = fopen(passwordList, "r");
    if (file == NULL) {
        printf("File not found!\n");
        exit(1);
    }

    int capacity = INITIAL_LINE_CAPACITY;
    char **lines = (char **)malloc(capacity * sizeof(char *));
    if (lines == NULL) {
        printf("Memory allocation failed!\n");
        exit(1);
    }

    *lineCount = 0;
    char buffer[200];
    while (fgets(buffer, sizeof(buffer), file) != NULL) {
        // Remove newline character if present
        buffer[strcspn(buffer, "\n")] = '\0';

        // Allocate memory for the line and copy the string
        lines[*lineCount] = (char *)malloc(strlen(buffer) + 1);
        if (lines[*lineCount] == NULL) {
            printf("Memory allocation failed!\n");
            exit(1);
        }
        strcpy(lines[*lineCount], buffer);

        (*lineCount)++;

        // Check if we need to resize the lines array
        if (*lineCount >= capacity) {
            capacity += LINE_INCREMENT;
            char **temp = (char **)realloc(lines, capacity * sizeof(char *));
            if (temp == NULL) {
                printf("Memory allocation failed!\n");
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
