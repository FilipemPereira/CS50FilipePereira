# Lecture 1 -  c

## List of Contents

1. Pointers. 
2. Segmentation Faults. 
3. Dynamic Memory Allocation. 
4. Stack / Heap.
5. Buffer Overflow. 
6. File I/O. 
7. Images.

## Practice problems

1. Bottom Up
2. License

## Lab 4

1. Smiley
2. Volume
   
## Problem set 1

1. Filter1
2. Filter2
3. Recover
4. Reverse

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