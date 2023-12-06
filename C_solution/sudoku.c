#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
// to compile, do gcc hello.c -o name-of-output.exe
// otherwise, gcc hello.c will produce a.exe

void printSudoku(int sudoku[9][9]);
bool contradiction(int num, int row, int col, int sudoku[9][9]);
bool recurse(int sudoku[9][9], int depth, int nodelist[][3], int maxdepth);
int compare(const void* a, const void* b);
int score(int row, int col, int sudoku[9][9]);


// the main function in this libray
int solveSudoku(int sudoku[9][9]){
    int nodelist[81][3];
    int length = 0;

    //create array of unknown points and their
    //assosiated "score", how many numbers are in their row/column/box
    for(int i = 0; i < 9; i++){
        for(int j = 0; j < 9; j++){
            if(sudoku[i][j] == 0){
                nodelist[length][0] = i;
                nodelist[length][1] = j;
                nodelist[length][2] = score(i, j, sudoku);
                length++;
            }
        }
    }
    //sort the array based on score -- this improves the
    //recursive algorithms performance
    qsort(nodelist, length, 3*sizeof(int), compare);
    return recurse(sudoku, 0, nodelist, length);
}

void printSudoku(int sudoku[9][9]) {
    for(int i = 0; i < 9; i++){
        for(int j = 0; j < 9; j++){
            printf("%d  ", sudoku[i][j]);
        }
        printf("\n");
    }
}

// everything beyond here is not intended to be used outside of library

// for testing the C code
void main(){
    int sudoku[9][9] = {{1,0,0,4,8,9,0,0,6}, 
                      {7,3,0,0,0,0,0,4,0}, 
                      {0,0,0,0,0,1,2,9,5}, 
                      {0,0,7,1,2,0,6,0,0},
                      {5,0,0,7,0,3,0,0,8},
                      {0,0,6,0,9,5,7,0,0},
                      {9,1,4,6,0,0,0,0,0},
                      {0,2,0,0,0,0,0,3,7}, 
                      {8,0,0,5,1,2,0,0,4}};
    int success = solveSudoku(sudoku);
    printf("\nSuccess: %d\n", success);
    printSudoku(sudoku);
}
// return whether an element in a given position causes a contradition
bool contradiction(int num, int row, int col, int sudoku[9][9]){
    for(int i = 0; i < 9; i++){
        if(sudoku[row][i] == num)
            return true;
        if(sudoku[i][col] == num)
            return true;
        if(num == sudoku[3*(row/3) + i/3][3*(col/3) + i%3])
            return true;
    }
    return false;
}

//recursive back-tracking algorithm to solve the sudoku. 
bool recurse(int sudoku[9][9], int depth, int nodelist[][3], int maxdepth){
    int px = nodelist[depth][0];
    int py = nodelist[depth][1];

    for(int i = 1; i <= 9; i++){
        if(contradiction(i, px, py, sudoku)){
            continue;
        } else if(depth == maxdepth - 1){
            sudoku[px][py] = i;
            return true;
        } else {
            sudoku[px][py] = i;
            if(recurse(sudoku, depth + 1, nodelist, maxdepth)){
                return true;
            } else {
                sudoku[px][py] = 0;
            }
        }
    }
    return false;
}

// optimize the order of elements guessed by the 
// recursive algorithm
int compare(const void* a, const void* b){
    
    //alongside the nodes in nodelist, we store the "score" assosiated with them
    //nodelist[i] = (x, y, score)
    //we can sort each point (x, y) based on score

    int a_score = *((int*)a +2);
    int b_score = *((int*)a +2);

    if(a_score < b_score){
        return 1;
    } else if (a_score > b_score){
        return -1;
    }
    return 0;
}

// Return a score for a given box in a sudoku. 
// The score is higher if there are more numbers in
// the same row, column and box as the point (row, col).
int score(int row, int col, int sudoku[9][9]){
    int score = 0;

    for(int i = 0; i < 9; i++){
        if(sudoku[row][i] != 0)
            score++;
        if(sudoku[i][col] != 0)
            score++;
        if(sudoku[3*(row/3) + i/3][3*(col/3) + i%3] != 0)
            score++;
    }
    return score;
}

