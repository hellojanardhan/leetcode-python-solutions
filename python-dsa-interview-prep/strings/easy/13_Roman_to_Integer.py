# ============================================================
# LeetCode 13: Roman to Integer
# Difficulty: Easy
# ============================================================

# Recommended Approach:
# Solution 3 - Right-to-Left Traversal
#
# Recommended Current-Level Approach:
# Solution 1 - Two Pointers (My Original Approach)
#
# TOP 3 SOLUTIONS
# ============================================================


# ============================================================
# SOLUTION 1: TWO POINTERS (MY ORIGINAL APPROACH)
# ============================================================

class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            "I": 1, "V": 5, "X": 10,
            "L": 50, "C": 100, "D": 500, "M": 1000
        }

        result = 0
        start = 0
        right = 1

        while start < len(s) and right < len(s):
            if d[s[start]] < d[s[right]]:
                result += d[s[right]] - d[s[start]]
                start += 2
                right += 2
            else:
                result += d[s[start]]
                start += 1
                right += 1

        if start < len(s):
            result += d[s[start]]

        return result


# Explanation:
# 1. Dictionary lo Roman symbols ki values store chestham.
# 2. start current character ni point chestundi.
# 3. right next character ni point chestundi.
# 4. Current value < next value ayithe, subtractive pair.
#    Example: IV = 5 - 1 = 4.
# 5. Pair process chesaka, two positions skip chestham.
# 6. Otherwise, current value add chesi one position move chestham.
# 7. Loop ayyaka, last character process avvakapothe add chestham.
#
# Dry Run: s = "LVIII"
#
# Initial: start = 0, right = 1, result = 0
#
# L(50), V(5): 50 < 5 is False -> Add 50 -> result = 50
# V(5), I(1):  5 < 1 is False  -> Add 5  -> result = 55
# I(1), I(1):  1 < 1 is False  -> Add 1  -> result = 56
# I(1), I(1):  1 < 1 is False  -> Add 1  -> result = 57
# Loop ends. Last I = 1 is added -> result = 58
#
# Output: 58
#
# Time Complexity: O(n)
# Each character is processed at most once.
#
# Auxiliary Space: O(1)
# Dictionary size is fixed (7 symbols); only constant
# extra variables are used.


# ============================================================
# SOLUTION 2: FORWARD TRAVERSAL - SINGLE INDEX
# ============================================================

class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            "I": 1, "V": 5, "X": 10,
            "L": 50, "C": 100, "D": 500, "M": 1000
        }

        result = 0
        i = 0

        while i < len(s):
            if i + 1 < len(s) and d[s[i]] < d[s[i + 1]]:
                result += d[s[i + 1]] - d[s[i]]
                i += 2
            else:
                result += d[s[i]]
                i += 1

        return result


# Explanation:
# Idi Solution 1 ki similar, but two pointers badulu
# single index i use chestham.
#
# Current value < next value ayithe:
#   Difference add chesi, i ni 2 positions move chestham.
#
# Otherwise:
#   Current value add chesi, i ni 1 position move chestham.
#
# Separate last-character check avasaram ledu.
#
# Dry Run: s = "IV"
#
# i = 0: I = 1, V = 5
# 1 < 5 -> True
# result = 5 - 1 = 4
# i = 2 -> Loop ends
#
# Output: 4
#
# Time Complexity: O(n)
# Index forward move avuthundi; each character at most once
# process avuthundi.
#
# Auxiliary Space: O(1)
# Fixed dictionary and constant variables only.


# ============================================================
# SOLUTION 3: RIGHT-TO-LEFT TRAVERSAL (RECOMMENDED)
# ============================================================

class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            "I": 1, "V": 5, "X": 10,
            "L": 50, "C": 100, "D": 500, "M": 1000
        }

        result = 0
        prev = 0

        for char in reversed(s):
            value = d[char]

            if value < prev:
                result -= value
            else:
                result += value

            prev = value

        return result


# Explanation:
# String ni right to left traverse chestham.
#
# prev = right side lo previously process chesina character
# value = current character value
#
# Current value < prev ayithe subtract chestham.
# Otherwise, current value add chestham.
#
# Example: IV
# Right nunchi start chestham:
# V = 5 -> result = 5
# I = 1, 1 < 5 -> result = 5 - 1 = 4
#
# Dry Run: s = "MCMXCIV"
#
# Reversed order: V, I, C, X, M, C, M
#
# Initial: result = 0, prev = 0
#
# V = 5:
# 5 < 0 -> False
# Add 5 -> result = 5, prev = 5
#
# I = 1:
# 1 < 5 -> True
# Subtract 1 -> result = 4, prev = 1
#
# C = 100:
# 100 < 1 -> False
# Add 100 -> result = 104, prev = 100
#
# X = 10:
# 10 < 100 -> True
# Subtract 10 -> result = 94, prev = 10
#
# M = 1000:
# 1000 < 10 -> False
# Add 1000 -> result = 1094, prev = 1000
#
# C = 100:
# 100 < 1000 -> True
# Subtract 100 -> result = 994, prev = 100
#
# M = 1000:
# 1000 < 100 -> False
# Add 1000 -> result = 1994, prev = 1000
#
# Output: 1994
#
# Time Complexity: O(n)
# Each character is visited once.
#
# Auxiliary Space: O(1)
# Fixed dictionary and a constant number of variables.
# reversed(s) does not create a reversed string copy.


# ============================================================
# TEST CASES
# ============================================================

# "III"     -> 3
# "LVIII"   -> 58
# "IV"      -> 4
# "IX"      -> 9
# "CDXLIV"  -> 444
# "MCMXCIV" -> 1994
# "MMXXVI"  -> 2026


# ============================================================
# INTERVIEW-READY EXPLANATION
# ============================================================

# "I use a dictionary to map Roman numerals to integer values.
# I compare adjacent values to handle subtractive notation.
# If a smaller value appears before a larger value, I subtract
# it; otherwise, I add it.
# Each character is processed once, so time complexity is O(n)
# and auxiliary space complexity is O(1)."


