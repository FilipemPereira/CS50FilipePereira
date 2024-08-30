#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>

// Check if one password is valid, i.e., if is secure
bool valid(char* password);

bool valid(char* password){
    bool upper = false, lower = false, number = false, symbol = false;
    for (int i = 0; password[i] != '\0'; i++){
        if (isdigit(password[i]))
            number = true;
        else if (islower(password[i]))
            lower = true;
            else if (isupper(password[i]))
                upper = true;
                else if (ispunct(password[i]))
                    symbol = true;
    }
    return upper && lower && number && symbol;
}


int main(void) {
    char password[102];
    printf("Enter your password: ");
    scanf("%s", password);
    if (valid(password)) {
        printf("Your password is valid!\n");
    }
    else {
        printf("Your password needs at least one uppercase letter, lowercase letter, number and symbol\n");
    }
}
