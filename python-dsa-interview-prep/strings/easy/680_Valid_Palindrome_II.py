
# LeetCode 680 - Valid Palindrome II
# Difficulty: Easy
#
# Recommended Approach:
# Two Pointers + Skip One Character
#
# Recommended Current-Level Approach:
# Two Pointers + List Deletion + Palindrome Checking
#
# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: List + Two Pointers + Reverse Checking
# Your Approach
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Time Explanation:
# First, original string palindrome aa kaada ani check chestham.
#
# s[::-1] string ni reverse chestundi.
# Reverse string tho original string compare chestham.
#
# Already palindrome ayite True return chestham.
#
# Otherwise, string ni list ga convert chestham.
#
# Two pointers use chesi first mismatch find chestham.
#
# First, left character ni remove chesi,
# remaining string palindrome aa kaada check chestham.
#
# Palindrome ayite True return chestham.
#
# Otherwise, original list ni restore chesi,
# right character ni remove chesi check chestham.
#
# Either deletion successful ayite True.
# Both fail ayite False.
#
# Reverse, list conversion, pop, join, and comparison
# operations each worst case lo O(n) time teesukuntayi.
#
# Constant number of O(n) operations kabatti:
# Total time complexity = O(n).
#
# Space Explanation:
# result list lo n characters store chestham.
# Joined strings and reversed strings kuda temporary ga create avuthayi.
#
# Auxiliary space:
# O(n).

class Solution1:
    def validPalindrome(self, s: str) -> bool:
        if s[::-1] == s:
            return True

        result = list(s)
        left = 0
        right = len(result) - 1

        while left < right:
            if result[left] == result[right]:
                left += 1
                right -= 1
            else:
                # Try deleting the left character
                result.pop(left)
                string = "".join(result)

                if string == string[::-1]:
                    return True

                # Restore the original list
                result = list(s)

                # Try deleting the right character
                result.pop(right)
                string = "".join(result)

                if string == string[::-1]:
                    return True

                return False

        return True


# ============================================================
# Approach 2: Two Pointers + Helper Function
# Recommended Optimal Approach
# Time Complexity: O(n)
# Auxiliary Space Complexity: O(1)
# ============================================================
#
# Time Explanation:
# Two pointers use chesi string ni both ends nunchi compare chestham.
#
# Characters equal ayite:
# left += 1
# right -= 1
#
# First mismatch vachinappudu,
# two possibilities check chestham:
#
# 1. Skip left character.
# 2. Skip right character.
#
# Helper function remaining substring ni indices use chesi
# palindrome aa kaada check chestundi.
#
# Slicing or list creation cheyyatledu.
#
# Each candidate substring ni at most once traverse chestham.
#
# Total time complexity:
# O(n).
#
# Space Explanation:
# Only pointers and a few variables use chestham.
# No extra list or substring copies create cheyyatledu.
#
# Auxiliary space:
# O(1).

class Solution2:
    def validPalindrome(self, s: str) -> bool:

        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False

                left += 1
                right -= 1

            return True

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return (
                    is_palindrome(left + 1, right)
                    or is_palindrome(left, right - 1)
                )

            left += 1
            right -= 1

        return True


# ============================================================
# Approach 3: Two Pointers Without Helper Function
# Optimal Time and Auxiliary Space
# Time Complexity: O(n)
# Auxiliary Space Complexity: O(1)
# ============================================================
#
# Time Explanation:
# First, outer two pointers string ni compare chestayi.
#
# Characters match ayite pointers inward move avuthayi.
#
# Mismatch vachinappudu:
# First candidate:
# left character ni skip chesi remaining characters compare chestham.
#
# Second candidate:
# right character ni skip chesi remaining characters compare chestham.
#
# Either candidate palindrome ayite True return chestham.
#
# Both candidates fail ayite False return chestham.
#
# Each candidate check O(n) time lo complete avuthundi.
#
# Total time complexity:
# O(n).
#
# Space Explanation:
# Only a few pointer variables use chestham.
# Extra list, dictionary, or substring create cheyyatledu.
#
# Auxiliary space:
# O(1).
#
# Note:
# This approach avoids creating another function and
# also achieves optimal auxiliary space.

class Solution3:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:

                # Option 1: Skip the left character
                i = left + 1
                j = right

                while i < j and s[i] == s[j]:
                    i += 1
                    j -= 1

                if i >= j:
                    return True

                # Option 2: Skip the right character
                i = left
                j = right - 1

                while i < j and s[i] == s[j]:
                    i += 1
                    j -= 1

                return i >= j

            left += 1
            right -= 1

        return True


# ============================================================
# DRY RUN
# ============================================================
#
# Input:
# s = "abca"
#
# Initial:
# left = 0
# right = 3
#
# Step 1:
# s[left] = 'a'
# s[right] = 'a'
#
# Characters match.
# Move pointers inward.
#
# left = 1
# right = 2
#
# Step 2:
# s[left] = 'b'
# s[right] = 'c'
#
# Mismatch found.
#
# Option 1: Skip 'b'
# Remaining characters: "aca"
# "aca" is a palindrome.
#
# Return True.
#
# Output: True
#
#
# Example 2:
# s = "abc"
#
# First mismatch: 'a' and 'c'
#
# Skip 'a' -> "bc" -> Not a palindrome
# Skip 'c' -> "ab" -> Not a palindrome
#
# Both options fail.
#
# Output: False


# ============================================================
# IMPORTANT TEST CASES
# ============================================================
#
# "aba"      -> True
# "abca"     -> True
# "abc"      -> False
# "deeee"    -> True
# "raceacar" -> True
# "abecbea"  -> False
# "a"        -> True
# ""         -> True
