#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// Convert a string of digits in a number
int convert(char* input);

int convert(char* input){
    // TODO
    if (strlen(input) == 0)
        return 0;

    int lastDigit = input[strlen(input) - 1] - '0';
    char* shortnedString = malloc(sizeof(char) * strlen(input));
    strncpy(shortnedString, input, strlen(input) - 1);
    shortnedString[strlen(input) - 1] = '\0';
    
    return (10 * convert(shortnedString)) + lastDigit;
    free(shortnedString);
}

int main(void){
    char input[5];
    printf("Enter a positive integer: ");
    scanf("%s", input);

    for (int i = 0, n = strlen(input); i < n; i++)
    {
        if (!isdigit(input[i]))
        {
            printf("Invalid Input!\n");
            return 1;
        }
    }

    // Convert string to int
    printf("%i\n", convert(input));
}