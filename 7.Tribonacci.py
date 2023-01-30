# Leetcode N-th Tribonacci Number 1137 Easy
"""
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
"""


class Solution:
    def tribonacci(self, n: int) -> int:
        # Base Cases
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        # Base Values
        t1 = 0
        t2 = 1
        t3 = 1

        # Iterate n+1 times
        for i in range(3, n+1):
            res = t1 + t2 + t3
            # Shift up variables
            t1 = t2
            t2 = t3
            t3 = res

        return res
