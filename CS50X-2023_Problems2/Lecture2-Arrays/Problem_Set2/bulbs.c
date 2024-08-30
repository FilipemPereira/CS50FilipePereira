#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

// Convert one ASCII value to binary and store each bit in a cell of an array of type char. Then print the corresponding bulb for a bit
void convert(int value, char*bits);

// Print one emoji to represent one bulb on or off
void print_bulb(int bit);

void convert(int value, char* bits){
    for (int i = BITS_IN_BYTE - 1; i >= 0; i--) {
        *(bits + i) = value % 2;
        value /= 2;
    }
}

void print_bulb(int bit){
    if (bit == 0){
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1){
        // Light emoji
        printf("\U0001F7E1");
    }
}

int main(void){
    char message[1024], *bits = malloc(BITS_IN_BYTE * sizeof(char));
    printf("Message: ");
    fgets(message, sizeof(message), stdin);
    // Remove the newline character from the end of the input
    message[strcspn(message, "\n")] = '\0';
    for (int i = 0, n = strlen(message); i < n; i++) {
        convert(message[i], bits);
        for (int j = 0; j < BITS_IN_BYTE; j++){
            print_bulb(bits[j]);
        }
        printf("\n");
    }
    free(bits);
}