# LeetCode 409 - Longest Palindrome
# Difficulty: Easy

# Recommended Approach:
# Frequency Map + Pair Counting
#
# Recommended Current-Level Approach:
# Frequency Map + Even/Odd Frequency Logic


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: Frequency Map + Even/Odd Frequency Logic
# Your Approach
# Recommended Current-Level Approach
# Time Complexity: O(n)
# Space Complexity: O(k)
#
# Time Explanation:
# First string ni once traverse chesi,
# prati character frequency ni hashmap lo store chestunnam.
#
# Tarvata frequency values ni traverse chestunnam.
#
# Frequency even ayite:
# complete count ni palindrome lo use chestham.
#
# Frequency odd ayite:
# count - 1 characters ni pairs ga use chestham.
#
# At least oka odd frequency unte,
# one leftover character ni center lo use chestham.
#
# String traversal O(n).
# Frequency traversal O(k).
#
# k <= n kabatti total time:
# O(n).
#
# Space Explanation:
# k unique characters frequencies ni
# hashmap lo store chestunnam.
#
# Kabatti auxiliary space:
# O(k).

class Solution1:
    def longestPalindrome(self, s: str) -> int:
        longestPalindromeLength = 0
        freq = {}

        for char in s:
            freq[char] = freq.get(char, 0) + 1

        odd = False

        for count in freq.values():
            if count % 2 == 0:
                longestPalindromeLength += count
            else:
                longestPalindromeLength += count - 1
                odd = True

        if odd:
            return longestPalindromeLength + 1

        return longestPalindromeLength


# ============================================================


# Approach 2: Count Completed Pairs
# Recommended Optimal Approach
# Time Complexity: O(n)
# Space Complexity: O(k)
#
# Time Explanation:
# Prati character frequency ni increment chestham.
#
# Frequency even ayina prati sari,
# oka complete pair form avutundi.
#
# Example:
#
# freq = 1 -> no pair
# freq = 2 -> +2
# freq = 3 -> no new pair
# freq = 4 -> +2
#
# Kabatti completed pair ki:
# length += 2
#
# Last lo edaina odd frequency unte,
# one character ni center lo use chestham.
#
# Total time complexity:
# O(n).
#
# Space Explanation:
# Character frequencies hashmap lo store chestunnam.
#
# Kabatti auxiliary space:
# O(k).

class Solution2:
    def longestPalindrome(self, s: str) -> int:
        freq = {}
        length = 0

        for char in s:
            freq[char] = freq.get(char, 0) + 1

            if freq[char] % 2 == 0:
                length += 2

        for count in freq.values():
            if count % 2 == 1:
                length += 1
                break

        return length


# ============================================================


# Approach 3: Set Pair Tracking
# Time Complexity: O(n)
# Space Complexity: O(k)
#
# Time Explanation:
# Character first time vasthe,
# set lo add chestham.
#
# Same character malli vasthe,
# pair complete avutundi.
#
# Appudu set nunchi remove chesi:
# length += 2
#
# Final ga set empty kaakapothe,
# at least oka unmatched character undi.
#
# Danni center lo use chestham.
#
# String ni once traverse chestunnam.
#
# Kabatti total time:
# O(n).
#
# Space Explanation:
# Unmatched characters set lo store chestunnam.
#
# Worst case lo k unique characters untayi.
#
# Kabatti auxiliary space:
# O(k).

class Solution3:
    def longestPalindrome(self, s: str) -> int:
        unmatched = set()
        length = 0

        for char in s:
            if char in unmatched:
                unmatched.remove(char)
                length += 2
            else:
                unmatched.add(char)

        if unmatched:
            length += 1

        return length


# ============================================================
# OTHER POSSIBLE SOLUTIONS
# ============================================================


# Approach 4: collections.Counter
# Time Complexity: O(n)
# Space Complexity: O(k)
#
# Time Explanation:
# Counter character frequencies ni calculate chestundi.
#
# Prati frequency nunchi usable even count:
#
# (count // 2) * 2
#
# Odd frequency edaina unte,
# center kosam final ga +1 chestham.
#
# Counter build O(n).
# Frequency traversal O(k).
#
# Total time:
# O(n).
#
# Space Explanation:
# Counter lo k unique characters store chestunnam.
#
# Kabatti auxiliary space:
# O(k).

from collections import Counter


class Solution4:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)

        length = 0
        odd = False

        for count in freq.values():
            length += (count // 2) * 2

            if count % 2 == 1:
                odd = True

        if odd:
            length += 1

        return length
