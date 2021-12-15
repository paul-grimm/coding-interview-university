# Data Structures

## Arrays
 
 A single chunk of memory broken down into equal size elements where each element is indexed by sequential integers.

 Constant time access to read AND write O(1)
 
constant time to add or remove to the *end* of the array O(1)

O(n) to add or remove to the *beginning* of the array

O(n) to add or remove to the *middle* of the array

take away = great for adding or removing from end, expensive otherwise but still have constant time read access

### Java

String[] s = new String[4];

## Multi-Dimensional Arrays

 Similar to table (1,1) row 1, column 1

 row-major ordering = laying out all elements in row, column sequence where each column is enumerated first (1,1), (1,2), (2,1), (2,) which is how elements are accessed under the hood for most languages

 column-major ordering = laying out all elements in row, column sequence where each row is enumerated first (1,1), (2,1), (1,2), (2,2)
 some languages use this ordering

## Dynamic Arrays

for when you don't know the size of the array upfront

rather than storing a reference to an array in memory, stores a pointer and updates the pointer as needed if an array of a new size needs to be allocated

get and set are always O(1)

implementation tracks max capacity and current total size to know if a new array needs to be allocated, copies current elements over, and then deletes the old array

### Java

ArrayList

## Jagged Array

Array of arrays

Useful for when a multi dimensional array is needed but data is not uniform

## Linked List

Main advantage is constant time adding value to front of list compared to linear time adding to array?
However, accessing an element is linear time because you have to traverse the nodes.

Apparently, there are not many great use cases for using a linked list given the memory compactness advantage of arrays and access.

One good use case that I found was a web browser history. Pressing forward/back in browser would efficiently move through linked list.

## Stacks

Collection of values where the interactions happen at the top. Like a stack of books, you can add (push) to the top, retrieve from the top (top), or remove from the top (pop).

Cannot retrieve from middle or bottom.

Can be implemented using an array (fixed size) or a linked list (dynamic).

Use case: find if parenths or brackets have closing pair.

