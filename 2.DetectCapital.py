# 2/1
# 520. Detect Capital Leetcode Easy
"""
We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.

Input: word = "USA"
Output: true

Input: word = "FlaG"
Output: false
"""


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # Count for num of capitals in word
        count = 0
        # Parse word
        for char in word:
            # Char is in uppercase
            if char.isupper():
                # Updated Count
                count += 1

        # Count is 0 -> no capitals in string OR..
        # Count is length of word -> all letters are capital
        if count == len(word) or not count:
            return True

        # Count is 1 and 1st character is capital
        if count == 1 and word[0].isupper():
            return True

        return False
