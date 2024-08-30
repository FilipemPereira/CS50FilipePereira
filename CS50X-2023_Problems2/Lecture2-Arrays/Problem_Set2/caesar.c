#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

// Check is a the command-line argument is a digit
bool isDigit(char* arg);

// Check is a the command-line argument is positive integer
bool isPositive(char* arg);

// Turn a character in another according to the key
char rotate(char c, int key);

bool isDigit(char* arg){
    bool b = false;
    int i = 0;
    while (arg[i] != '\0'){
        if (isdigit(arg[i]))
            b = true;
        else
            b = false;
        i++;
    }
    return b;
}

bool isPositive(char* arg){
    int n = atoi(arg);
    return n > 0;
}

char rotate(char c, int key){
    // Only the letters are modified
    if (isalpha(c)){
        // Convert ASCII to alphabetical index (0 ... 25)
        // Shift using formula and convert back to ASCII
        if (isupper(c)){
            c = (int) (c - 'A');
            c = ((c + key) % 26) + 65;
        }
        else if (islower(c)){
            c = (int) (c - 'a');
            c = ((c + key) % 26) + 97;
        }
    }
    return c;
}

int main(int argc, char* argv[]){
    if (argc == 1 || argc > 2 || !(isDigit(argv[1])) || (isDigit(argv[1]) && !isPositive(argv[1]))){
        printf("Usage: ./caesar Key\n");
        return 1;
    }
    int n = atoi(argv[1]);
    char* plainText;
    printf("PlainText:  ");
    scanf("%s", plainText);
    printf("Ciphertext: ");
    for (int i = 0; plainText[i] != '\0'; i++)
    {
        printf("%c", rotate(plainText[i], n));
    }
    printf("\n");
}
