// Practice using structs
// Practice writing a linear search function

/**
 * Beach Burger Shack has the following 10 items on their menu
 * Burger: $9.5
 * Vegan Burger: $11
 * Hot Dog: $5
 * Cheese Dog: $7
 * Fries: $5
 * Cheese Fries: $6
 * Cold Pressed Juice: $7
 * Cold Brew: $3
 * Water: $2
 * Soda: $2
 */

#include <ctype.h>
#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <strings.h>

// Number of menu items
// Adjust this value (10) to number of items input below
#define NUM_ITEMS 5

// Menu items have item name and price
typedef struct{
    char* item;
    float price;
} menu_item;

// Array of menu items
menu_item menu[NUM_ITEMS];

// Add items to menu
void add_items(void);

// Calculate total cost
float get_cost(char* item);


void add_items(void){
    menu[0].item = "Burger";
    menu[0].price = 9.5;

    menu[1].item = "Vegan Burger";
    menu[1].price = 11;

    menu[2].item = "Hot Dog";
    menu[2].price = 5;

    menu[3].item = "Cheese Dog";
    menu[3].price = 7;

    menu[4].item = "Fries";
    menu[4].price = 5;
}

// Search through the menu array to find an item's cost
float get_cost(char* item){
    for (int i = 0; i < NUM_ITEMS; i++){
        if (strcmp(menu[i].item, item) == 0)
            return menu[i].price;
    }
    return 0.0;
}

int main(void){
    add_items();

    printf("\nWelcome to Beach Burger Shack!\n");
    printf("Choose from the following menu to order. Press enter when done.\n\n");

    for (int i = 0; i < NUM_ITEMS; i++){
        printf("%s: $%.2f\n", menu[i].item, menu[i].price);
    }
    printf("\n");

    float total = 0;
    while (true){
        char item[1024];
        printf("Enter a food item: ");
        fgets(item, sizeof(item), stdin);
        printf("%s", item);
        if (strlen(item) == 0){
            printf("\n");
            break;
        }

        total += get_cost(item);
        printf("%f", total);
    }

    printf("Your total cost is: $%.2f\n", total);
}