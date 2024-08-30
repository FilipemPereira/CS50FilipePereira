#include <stdio.h>
#include <stdbool.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// Candidates have name and vote count
typedef struct{
    char* name;
    int votes;
} candidate;

// Array of candidates
candidate candidates[MAX];

// Number of candidates
int candidate_count;

// Swap the positions in the array of two candidates (aux function to vote)
void swap(candidate *x, candidate *y);

// Updte vote totals given a new vote
bool vote(char* name);

// Print the winner (or winners) of the election
void print_winner(void);


bool vote(char* name){
    for (int i = 0; i < candidate_count; i++){
        if (strcmp(name, candidates[i].name) == 0){
            candidates[i].votes++;
            return true;
        }
    }
    return false;
}

void swap(candidate *x, candidate *y){
    candidate temp = *x;
    *x = *y;
    *y = temp;
}

void print_winner(void){
    // Selection sort
    int max;
    for (int i = 0; i < MAX - 1; i++){
        max = i;
        for (int j = i + 1; j < MAX; j++){
            if (candidates[j].votes > candidates[max].votes)
                max = j;
        }
        if (max != i)
            swap(&candidates[max], &candidates[i]);
    }

    // Print the name of the (first) winner
    int votes = candidates[0].votes;
    if (votes != 0)
        printf("%s\n", candidates[0].name);

    // Search for other winners
    for (int c = 1; c < candidate_count; c++){
        if (candidates[c].votes == votes && candidates[c].votes != 0)
            printf("%s\n", candidates[c].name);
        else
            break;
    }
}

int main(int argc, char* argv[]){
    // Check for invalid usage
    if (argc < 2){
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX){
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    // Set the array of candidates
    for (int i = 0; i < candidate_count; i++){
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    int voter_count = get_int("Number of voters: ");

    // Loop over all voters
    for (int i = 0; i < voter_count; i++){
        char name[20];
        printf("Vote: ");
        scanf("%s", name);

        // Check for invalid vote
        if (!vote(name))
            printf("Invalid vote.\n");
    }

    // Display winner of election
    print_winner();
}
