#include <ctype.h>
#include <math.h>
#include <stdio.h>

// Count the number of letters in the text
int countLetters(char* text);

// Count the number of words in a text
int countWords(char* text);

// Count the number of sentences in the text
int countLetters(char* text);

int countLetters(char* text){
    int count = 0;
    for (int i = 0; text[i] != '\0'; i++){
        if (isalpha(text[i]))
            count++;
    }
    return count;
}

int countWords(char* text){
    int count = 0;
    for (int i = 0; text[i] != '\0'; i++){
        if (isspace(text[i]))
            count++;
    }
    return count + 1;
}

int countSentences(char* text){
    int count = 0;
    for (int i = 0; text[i] != '\0'; i++){
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
            count++;
    }
    return count;
}

int grade(int letters, int words, int sentences){
    float L = ((float) letters / words) * 100;
    float S = ((float) sentences / words) * 100;
    return round(0.0588 * L - 0.296 * S - 15.8);
}

int main(void){
    char text[1024];
    printf("Text: ");
    scanf("%s", text);
    int gr = grade(countLetters(text), countWords(text), countSentences(text));

    if (gr < 1)
        printf("Before Grade 1\n");
    else if (gr > 16)
        printf("Grade 16+\n");
    else
        printf("Grade %d\n", gr);
}