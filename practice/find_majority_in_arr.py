# Given an array A of N elements. Find the majority element in the array. A majority element in an array A of size N is an element that appears more than N/2 times in the array.
# https://practice.geeksforgeeks.org/problems/majority-element-1587115620/1

class Solution:
    def majorityElement(self, A, N):
        A.sort()
        #print(A)
        majority = -1
        currentMaxCount = 1
        if N == 1:
            return A[0]
        else:
            for i in range(N):
                #print("curr = ", A[i])
                if i == 0:
                    current = A[i]
                    #print("skipping count")
                else:
                    if A[i] == A[i-1]:
                       currentMaxCount += 1
                       #print("currentMaxCount", currentMaxCount)
                       if currentMaxCount > (N/2):
                           majority = A[i]
                           #print("majority is currently", majority)
                    else:
                        currentMaxCount = 1
        
        return majority