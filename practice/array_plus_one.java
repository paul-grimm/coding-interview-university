// Given a non-negative number represented as an array of digits, add 1 to the number ( increment the number represented by the digits ). The digits are stored such that the most significant digit is the first element of the array.

class Solution {
    static ArrayList<Integer> increment(ArrayList<Integer> arr , int N) {
        
        arr.set(N-1, arr.get(N-1) + 1);
        int carry = arr.get(N-1) / 10;
        arr.set(N-1, arr.get(N-1) % 10);
        
        for (int i = N - 2; i >= 0; i--) {
            if (carry == 1) {
                arr.set(i, arr.get(i) + 1);
                carry = arr.get(i) / 10;
                arr.set(i, arr.get(i) % 10);
            }
        }
        
        if (carry == 1) {
            arr.add(0, 1);
        }
        
        return arr;
    }
};