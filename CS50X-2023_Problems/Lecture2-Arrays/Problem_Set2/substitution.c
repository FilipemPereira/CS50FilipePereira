#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Check if the argument is valid
bool isValid(char* arg);

// Check if the arg have only letters
bool allLetters(char* arg);

// Check if the arg have unique letters
bool uniqueLetters(char* arg);

// Replace a certain letter in plainText by the correspondent letter in newAlphabet
char* replace(char* plainText, char* newAlphabet);

bool isValid(char* arg){
    return strlen(arg) == 26 && allLetters(arg) && uniqueLetters(arg);
}

bool allLetters(char* arg){
    for (int i = 0; arg[i] != '\0'; i++){
        if (!isalpha(arg[i]))
            return false;
    }
    return true;
}

bool uniqueLetters(char* arg){
    char arr[26] = {0};

    for (int i = 0; arg[i] != '\0'; i++){
        char c = arg[i];
        if (isupper(c))
            arr[c - 'A']++;
        else if (islower(c))
            arr[c - 'a']++;
    }

    for (int i = 0; arg[i] != '\0'; i++){
        if (arr[i] > 1)
            return false;
    }

    return true;
}

char* replace(char* plainText, char* newAlphabet){
    int n;
    for (int i = 0; plainText[i] != '\0'; i++){
        if (isalpha(plainText[i])){
            if (islower(plainText[i])){
                n = (int) plainText[i] - 'a';
                plainText[i] = tolower(newAlphabet[n]);
            }
            else if (isupper(plainText[i])){
                n = (int) plainText[i] - 'A';
                plainText[i] = toupper(newAlphabet[n]);
            }
        }
    }
    return plainText;
}

int main(int argc, char* argv[]){
    if (argc == 1 || argc > 2 || !isValid(argv[1])){
        printf("Usage: ./substitution key (26 letters)\n");
        return 1;
    }
    char* newAlphabet = malloc(sizeof(char) * 26);
    newAlphabet = argv[1];

    char plainText[1024];
    printf("plainText: ");
    scanf("%s", plainText);
    char* ciphertext = replace(plainText, newAlphabet);
    printf("ciphertext: %s\n", ciphertext);
    free(newAlphabet);
}
