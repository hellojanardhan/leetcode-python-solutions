# LeetCode 242 - Valid Anagram
# Difficulty: Easy


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: Two Frequency Dictionaries
# Your Approach
# Clean and Easy to Understand
# Time Complexity: O(n + m)
# Space Complexity: O(k)
class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_freq = {}
        t_freq = {}

        for char in s:
            s_freq[char] = s_freq.get(char, 0) + 1

        for char in t:
            t_freq[char] = t_freq.get(char, 0) + 1

        return s_freq == t_freq


# ============================================================


# Approach 2: One Frequency Dictionary
# Recommended HashMap Approach
# Increment using s
# Decrement using t
# Time Complexity: O(n)
# Space Complexity: O(k)
class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        freq = {}

        for char in s:
            freq[char] = freq.get(char, 0) + 1

        for char in t:

            if char not in freq:
                return False

            freq[char] -= 1

            if freq[char] < 0:
                return False

        return True


# ============================================================


# Approach 3: Fixed Frequency Array
# Optimal when input contains only lowercase English letters
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution3:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        freq = [0] * 26

        for char in s:
            index = ord(char) - ord('a')
            freq[index] += 1

        for char in t:
            index = ord(char) - ord('a')
            freq[index] -= 1

        return all(count == 0 for count in freq)


# ============================================================
# REMAINING SOLUTIONS
# ============================================================


# Approach 4: collections.Counter
# Pythonic Approach
# Time Complexity: O(n)
# Space Complexity: O(k)
from collections import Counter

class Solution4:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


# ============================================================


# Approach 5: Sorting
# Simple but less optimal
# Time Complexity: O(n log n)
# Space Complexity: O(n)
class Solution5:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
