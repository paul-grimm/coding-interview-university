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

LIFO

## Queues


Collection of values where interactions happen at the bottom. Oldest added key gets removed first. Enqueue and dequeue. Like a line of customers: first come, first serve.

Can be implemented using a linked list by adding new elements to the tail. Dequeue would remove element where head pointer is referencing.

Can also be implemented with an array but could be less efficient because of fixed size and wasted space for buffer between read and write indexes.

All operations should be implemented using constant time. Otherwise, un-optimal approach has been taken such as using a linked list and enqueu at head and dequeue at tail which would be o(n).

FIFO

## Sets

Collection of **UNIQUE** values. Differ from arrays or other data structures in that they only allow non-repeated, unique values.

## Graphs

Non-linear (non-sequential) data structure consisting of nodes and edges. Nodes can also be referred to as vertices. Edge connects any two nodes in the graph.

Many practical use cases for using graphs: representing networks such as paths in a city, phone network, or social network (person would be a node/vertex). Each node is a structure and contains it's own internal data like name, gender, etc.

### Directed Graph

- Directed graphs contain an ordered pair of vertices (V1, V2)
- (initial node, terminal node)
- Edges represent direction of the vertices

Use case: path optimization, shortest path such as Google Maps, family tree

### Undirected Graph

- Undirected graphs contain unordered pair of vertices (V1, V3), (V3, V1)
- Edges do not represent the direction of the vertices

Use case: recommendation engines such as Yelp local recommendations where user location and business location are vertices and recommendation is the edge, computer network, social network

### Cyclic Graph

Possible to start from a node and follow a path where you arrive at the same node you began. Trivial in undirected graphs as edges can be bidirectional. 

### Acyclic Graph

Graphs that contain no pathways to get back to original node. Directed Acyclic Graph represents this concept. 

## Hashing

### Dictionary

Collection of items that contains unique key that identifies the item. An item is a key/value pair.

Search by key which returns the item associated with key or does not exist.

Example use case: databases, network router keeping ip/address, keep track of count of a specific word in a document, substring of string

Like arrays but can use things other than integers as a key

**prehash** = map keys to non-negative integers to use as index in table

**hash** = take all possible keys and reduce down to a small set which is called a hash table. idea is to create a hash table around the same size as the number of items that need to be stored. *this is a hashing function*

**chaining** = way of dealing with collisions in the hash table. you store items that happen to map to the same index using a linked list
