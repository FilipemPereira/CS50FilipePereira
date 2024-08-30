#include <stdio.h>

// Calculate your half of a restaurant bill
float half(float bill, float tax, int tip);


float half(float bill, float tax, int tip){
    float billAmount = bill + (bill * (tax / 100));
    billAmount += (billAmount * ((float) tip / 100));

    return billAmount / 2;
}

int main(void){
    float bill_amount, tax_percent; 
    int tip_percent;
    printf("Bill before tax and tip: ");
    scanf("%f", &bill_amount);
    printf("Sale Tax Percent: ");
    scanf("%f", &tax_percent);
    printf("Tip percent: ");
    scanf("%d", &tip_percent);

    printf("You will owe $%.2f each!\n", half(bill_amount, tax_percent, tip_percent));
}
