#include <stdio.h>

// Return the max value
int max(int array[], int n);


int max(int array[], int n){
    int max = array[0];
    for (int i = 1; i < n; i++){
        if (array[i] > max)
            max = array[i];
    }
    return max;
}

int main(void){
    int n;
    do {
        printf("Number of elements: ");
        scanf("%d", &n);
    } while (n < 1);

    int arr[n];

    for (int i = 0; i < n; i++){
        arr[i] = get_int("Element %i: ", i);
    }

    printf("The max value is %i.\n", max(arr, n));
}