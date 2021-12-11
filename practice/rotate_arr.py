# Given an unsorted array arr[] of size N. Rotate the array to the left (counter-clockwise direction) by D steps, where D is a positive integer. 
# https://practice.geeksforgeeks.org/problems/rotate-array-by-n-elements-1587115621/1

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self,A,D,N):
        tempArr = A[0:D]
        # print("temp ", tempArr)
        del A[0:D]
        # print("sliced ", A)
        A.extend(tempArr)