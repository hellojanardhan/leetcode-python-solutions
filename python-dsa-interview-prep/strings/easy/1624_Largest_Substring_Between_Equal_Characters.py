# LeetCode 1624 - Largest Substring Between Two Equal Characters
# Difficulty: Easy
#
# Recommended Optimal Approach: First Occurrence + Hash Map
# Recommended Current-Level Approach: First Occurrence + Hash Map
#
# Your solution is correct and optimal.
#
# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: First Occurrence + Hash Map
# Your Approach — Recommended Optimal Approach
# Time Complexity: O(n)
# Space Complexity: O(1) for the fixed lowercase English alphabet
#
# Time Explanation:
# String ni one time traverse chestunnam: O(n).
# Dictionary lookup and insertion average O(1).
# Kabatti total time complexity O(n).
#
# Space Explanation:
# freq dictionary lo each character first index store chestunnam.
# Lowercase English letters maximum 26 characters matrame.
# Kabatti auxiliary space O(1) for this problem.
#
# Logic:
# Character first time encounter ayithe index store chestham.
# Already dictionary lo unte:
# current index - first index - 1
# Ee formula matching characters ni exclude chestundi.
# Maximum length ni update chestham.

class Solution1:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        n = len(s)
        length = -1
        freq = {}

        for index in range(n):
            if s[index] in freq:
                length = max(
                    length,
                    index - freq[s[index]] - 1
                )
            else:
                freq[s[index]] = index

        return length


# ============================================================
# Approach 2: enumerate() + Hash Map
# Clean Pythonic Approach
# Time Complexity: O(n)
# Space Complexity: O(1) for the fixed lowercase English alphabet
#
# Time Explanation:
# enumerate() index and character ni direct ga istundi.
# String ni once traverse chestham.
# Average dictionary operations O(1).
# Total time O(n).
#
# Space Explanation:
# First occurrence index ni dictionary lo store chestham.
# Maximum 26 lowercase English letters kabatti O(1).
#
# Logic:
# Approach 1 lo range(len(s)) use chesam.
# Ikkada enumerate(s) use chestunnam.
# Algorithm logic same.

class Solution2:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first = {}
        max_length = -1

        for index, char in enumerate(s):
            if char in first:
                max_length = max(
                    max_length,
                    index - first[char] - 1
                )
            else:
                first[char] = index

        return max_length


# ============================================================
# Approach 3: First Occurrence + Last Occurrence
# Two Dictionaries Approach
# Time Complexity: O(n)
# Space Complexity: O(1) for the fixed lowercase English alphabet
#
# Time Explanation:
# First loop string ni traverse chesi first and last indices
# store chestundi: O(n).
# Second loop distinct characters ni traverse chestundi: O(k).
# Total O(n + k) = O(n), where k <= 26.
#
# Space Explanation:
# Two dictionaries use chestunnam.
# Each dictionary lo maximum 26 characters store avuthayi.
# Kabatti O(1) auxiliary space for this problem.
#
# Logic:
# first dictionary lo first occurrence store chestham.
# last dictionary lo every occurrence index update chestham.
# Final ga last_index - first_index - 1 calculate chestham.

class Solution3:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first = {}
        last = {}

        for index, char in enumerate(s):
            if char not in first:
                first[char] = index

            last[char] = index

        max_length = -1

        for char in first:
            current_length = last[char] - first[char] - 1
            max_length = max(max_length, current_length)

        return max_length


# ============================================================
# OTHER USEFUL SOLUTIONS
# ============================================================


# Approach 4: Brute Force - Two Loops
# Time Complexity: O(n^2)
# Space Complexity: O(1)
#
# Time Explanation:
# Prati character ki remaining characters tho compare chestham.
# Worst case lo nested loops O(n^2) time teesukuntayi.
#
# Space Explanation:
# Extra dictionary or array use cheyyamu.
# Constant variables matrame use chestham.
# Kabatti O(1) auxiliary space.
#
# Logic:
# Same characters dorikinappudu madhyalo unna substring length:
# j - i - 1
# Maximum length update chestham.

class Solution4:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        n = len(s)
        max_length = -1

        for i in range(n):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    max_length = max(
                        max_length,
                        j - i - 1
                    )

        return max_length


# ============================================================
# DRY RUN
# ============================================================

# Input:
# s = "abca"
#
# Initial:
# freq = {}
# length = -1
#
# Index 0, char = 'a':
# 'a' dictionary lo ledu.
# Store freq['a'] = 0
# length = -1
#
# Index 1, char = 'b':
# 'b' dictionary lo ledu.
# Store freq['b'] = 1
# length = -1
#
# Index 2, char = 'c':
# 'c' dictionary lo ledu.
# Store freq['c'] = 2
# length = -1
#
# Index 3, char = 'a':
# 'a' already dictionary lo undi.
# First index = 0
# Current length = 3 - 0 - 1 = 2
# length = max(-1, 2) = 2
#
# Output: 2
#
# Substring between equal characters = "bc"
# Length = 2


# ============================================================
# TEST CASES
# ============================================================

# Input: "aa"
# Output: 0
#
# Input: "abca"
# Output: 2
#
# Input: "cbzxy"
# Output: -1
#
# Input: "cabbac"
# Output: 4
#
# Input: "mgntdygtx"
# Output: 4
#
# Input: "aaaa"
# Output: 2


# ============================================================
# INTERVIEW-READY EXPLANATION
# ============================================================

# "I use a dictionary to store the first occurrence index of
# each character. When I encounter the same character again,
# I calculate the substring length using the current index
# minus the first occurrence index minus one, excluding both
# matching characters. I update the maximum length and return it.
# The solution takes O(n) time and O(1) auxiliary space for
# lowercase English letters."


# ============================================================
# FINAL RECOMMENDATION
# ============================================================

# Solution 1:
# Best choice — your original code is correct and optimal.
#
# Solution 2:
# Same algorithm using enumerate(); cleaner Python syntax.
#
# Solution 3:
# Useful for understanding first and last occurrence tracking,
# but uses two dictionaries instead of one.
#
# Solution 4:
# Brute force; useful for understanding the problem, but slower.
#
# Recommended for interviews: Solution 1 or Solution 2.
# Filename: LeetCode_1624_Largest_Substring_Between_Equal_Characters.py
