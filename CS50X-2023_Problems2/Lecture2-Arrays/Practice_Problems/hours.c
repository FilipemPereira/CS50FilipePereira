#include <ctype.h>
#include <stdio.h>

// Calculate the total number of hours spending on CS50 course or the average time spending on CS50 course according to the output
float calc_hours(int hours[], int weeks, char output);

float calc_hours(int hours[], int weeks, char output){
    float sum = 0.0, result;
    for (int i = 0; i < weeks; i++){
        sum += hours[i];
    }
    if (output == 'T')
        result = sum;
    else if (output == 'A')
        result = sum / weeks;
    return result;
}

int main(void){
    int weeks;
    char output;
    printf("Number of weeks taking CS50: ");
    scanf("%d", &weeks);
    int hours[weeks];

    for (int i = 0; i < weeks; i++){
        printf("Week %i HW Hours: ", i);
        scanf("%d", &hours[i]);
    }

    do {
        printf("Enter T for total hours, A for average hours per week: ");
        scanf("%c", &output);
        output = toupper(output);

    } while (output != 'T' && output != 'A');

    printf("%.1f hours\n", calc_hours(hours, weeks, output));
}
