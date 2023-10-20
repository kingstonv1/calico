#include <stdio.h>
#include <stdlib.h>
#include <string.h>


// Assumes the size of the output buffer is 26.
// Converts inventory strings to 26-length arrays representing the count for each character
// In output, index 0 is A, 1 is B, and so on.
void parseInventory(char inputString[], int size, int output[]) {
    int ascii_offset = 65; //64 Chars before the alphabet in ascii + 1 to account for 0 indexing
    
    for (int i = 0; i < size; i += 2) {
        int ascii = (int) inputString[i];
        output[ascii - ascii_offset]++;
    }
}


// Takes two arrays fresh out of the above function, returns the solution string.
void stack(int inventory1[], int inventory2[], char output[]) {
    int idxPointer = 0;
    int total;


    for (int i = 0; i < 26; i++) {
        total = inventory1[i] + inventory2[i];

        // its like c++ guys get it!! hahaha
        for (int c = 0; c < total; c++) { 
            output[idxPointer] = i + 65;
            output[idxPointer + 1] = ' ';
            idxPointer += 2;
        }
    }
}


int main() {
    char casesBuf[5];
    char *ptr;

    // Take t, number of test cases
    fgets(casesBuf, sizeof(casesBuf), stdin);
    int cases = strtol(casesBuf, &ptr, 0);

    for (int i = 0; i < cases; i++) {
        // Take inventory size inputs
        char sizes[14];
        fgets(sizes, sizeof(sizes), stdin);
        
        // Split the input into player and chest inventory sizes
        char* start = sizes;
        char *ptr;
        long playerSize = strtol(start, &ptr, 0);
        
        // Set the start pointer to after the first int
        // (the ptr was modified by strtol)    
        start = ptr;
        long chestSize = strtol(start, &ptr, 0);   // hehe chest size

        // Take inventory content inputs
        char playerInventory[playerSize * 2];
        char chestInventory[chestSize * 2];

        // +1 To account for the newline
        fgets(playerInventory, sizeof(playerInventory) + 1, stdin);
        fgets(chestInventory, sizeof(chestInventory) + 1, stdin);

        // Remove trailing newlines from fgets input
        playerInventory[strcspn(playerInventory, "\n")] = 0;
        chestInventory[strcspn(chestInventory, "\n")] = 0;

        // The answer is our inventories added, and will need to be at least that big.
        int answerSize = sizeof(playerInventory) / sizeof(playerInventory[0]) + sizeof(chestInventory) / sizeof(chestInventory[0]);
        
        // +1 For trailing space (won't get printed)
        char answer[answerSize];
        
        int i1[26] = {0};
        parseInventory(playerInventory, sizeof(playerInventory) / sizeof(playerInventory[0]), i1);
        
        int i2[26] = {0};
        parseInventory(chestInventory, sizeof(chestInventory) / sizeof(chestInventory[0]), i1);

        stack(i1, i2, answer);
        
        // Stack function overwrites the null terminator at the end of the array.
        // We have to put it back or we get undefined behavior.
        answer[answerSize] = '\0';

        printf("%s\n", answer);
    }
}