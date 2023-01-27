# Leetcode 472 Concatenated Words Hard
"""
Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.

A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
"dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
"""


class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        # Create a Hashset for faster access to any word
        wordSet = set(words)

        # Memoization
        dp = {}

        # Dfs
        def dfs(word):
            # Memoization Case
            if word in dp:
                return dp[word]

            # Split word into substrings
            for i in range(1, len(word)):
                # Substrig upto i
                prefix = word[:i]
                # Substring from i
                suffix = word[i:]
                # Check if prefix & suffix both r in set or prefix is in set and
                # suffix itself is comprised of 2/more words from set
                if (prefix in wordSet and suffix in wordSet) or (prefix in wordSet and dfs(suffix)):
                    # Store in memory for future reference
                    dp[word] = True
                    return dp[word]

            # No concatenation found
            dp[word] = False
            return False

        # Output
        res = []
        for word in words:
            if dfs(word):
                res.append(word)

        return res
