#include <stdio.h>
#include <stdbool.h>

// Cheack if a number is prime
bool prime(int number);

bool prime(int number){
    bool b = true;
    
    if (number == 1)
        b = false;

    for (int i = 2; i < number - 1; i++) {
        if (number % i == 0)
            b = false;
    }
    return b;
}

int main(void){
    int min, max;
    do {
        printf("Minimum: ");
        scanf("%d", &min);
    } while (min < 1);

    do {
        printf("Maximum: ");
        scanf("%d", &max);
    } while (min >= max);

    for (int i = min; i <= max; i++) {
        if (prime(i))
            printf("%i\n", i);
    }
}