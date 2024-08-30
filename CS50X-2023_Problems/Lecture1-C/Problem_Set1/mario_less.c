#include <stdio.h>

/**
 * Program that print a pattern to the output
*/

int main(void){
    int height;
    do {
        printf("Height: ");
        scanf("%d", &height);
    } while (height < 1 || height > 8);

    for (int i = 0; i < height; i++) {
        int l = height - i - 1;
        while (l != 0) {
            printf(" ");
            l--;
        }
        for (int j = 0; j < i + 1; j++) {
            printf("#");
        }
        printf("\n");
    }
}