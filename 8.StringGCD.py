# Leetcode 1071 Greatest Common Divisor of Strings Easy
"""
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
"""


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Length of both strings
        len1, len2 = len(str1), len(str2)

        # Helper Func
        def isDivisor(l):
            # Check if len1 & len2 is divsible by l if not, its obviously not GCD
            if len1 % l or len2 % l:
                # Remainder isn't 0, thus not divisible and
                # we cant divide strs with substr of length l
                return False
            # Quotients after dividing
            f1, f2 = len1 // l, len2 // l
            # If we get str1 & str2 after multiplying substring f1 & f2 times
            # respectively, we have found GCD
            return str1[:l] * f1 == str1 and str1[:l] * f2 == str2

        # Loop over smaller string going from largest substring to single character
        for l in range(min(len1, len2), 0, -1):
            # Check if substring is GCD
            if isDivisor(l):
                return str1[:l]
        return ""
