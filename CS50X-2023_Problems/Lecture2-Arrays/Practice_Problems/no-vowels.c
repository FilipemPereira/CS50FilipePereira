#include <stdio.h>

// Replace any vowels in the text by a corresponding number (a is 6, e is 3, i is 1 and o is 0)
char* replace(char* input);

char* replace(char* input){
    for (int i = 0; input[i] != '\0'; i++){
        switch (input[i]){
            case 'a':
                input[i] = '6';
                break;
            case 'e':
                input[i] = '3';
                break;
            case 'i':
                input[i] = '1';
                break;
            case 'o':
                input[i] = '0';
                break;
            default:
                break;
        }
    }
    return input;
}


int main(int argc, char* argv[]){
    if (argc == 1 || argc > 2){
        printf("Usage: ./no-vowels word\n");
        return 1;
    }

    printf("%s\n", replace(argv[1]));
}
