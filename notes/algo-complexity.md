# Algorithm Complexity

## Big-O

How well does an algorithm scale as the amount of data increases such as given and array of 10 vs an array of 10000

Asymptotic Notation = more formal definition of mathematical concept of Big-O

O(1)
order of one or "constant time"

executes the same amount of time regardless of number of scale of data set

O(n)
order of n or "linear time"

algo time to complete grows in direct proportion to the data
takes longer as more data is included

O(n^2)
order of n squared

example is bubble sort
nested iterations
**this one is not ideal or something to strive for because it's inefficient**

will this complexity always run slower than O(n)? no, but given increasing data sets it will

O(log n)
order of log n

example is binary search algo
data being used is being decreased by roughly 50% each iteration
**this one is good because it's efficient**

O(n log n)
order of n log n


## Other Related Concepts

best case scenario = lower bounds (Omega notation)
worst case scenario = upper bounds (Big O notation)
best and worst case scenario are the same = theta notation
