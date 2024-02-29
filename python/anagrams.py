# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        seen = {}
        for char in s:
            seen[char] = seen.get(char, 0) + 1

        for char in t:
            seen[char] = seen.get(char, 0) - 1

        for key, value in seen.items():
            if value != 0:
                return False
            
        return True
