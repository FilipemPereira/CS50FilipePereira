# Lecture 2 -  Arrays

## List of Contents

1. Preprocessing
2. Compiling
3. Assembling
4. Linking
5. Debugging
6. Arrays
7. Strings
8. Command-Line Arguments
9. Cryptography.

## Practice problems

1. Hours
2. NoVowels
3. Password

## Lab 2

1. Scrabble
   
## Problem set 2

1. Readability
2. Bulbs
3. Caesar
4. Substitution
5. Wordle50

To compile the C programs you can use the `gcc` compiler or `make` using the follow structure in your command line (note: it is for linux operative systems - e.g., Ubuntu):

~~~
// Install the gcc compiler
sudo apt install gcc -y

// Compile the source code written on the C language (the default executable name is a.out)
gcc <source_name>.c 

// To run the executable
./a.out

// Compile the source code written on the C language and give a name to the executable file
gcc <source_name>.c -o <executable_name>

// To run the executable
./<executable_name>
~~~

Or

~~~
// Making the c program (the <executable_name> should correspond to the source code file name)
make <executable_name>

// To run the executable
./<executable_name>
~~~

For more information about the problems' instructions see [here](https://cs50.harvard.edu/c/2023/weeks/1)

Note: I'm not using the CS50's library.