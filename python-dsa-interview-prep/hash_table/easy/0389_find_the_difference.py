# LeetCode 389 - Find the Difference
# Difficulty: Easy

# Recommended Approach: XOR
# Recommended Current-Level Approach: Frequency HashMap + Consume

# n = length of s
# m = length of t
# u = number of unique characters in s


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: Frequency HashMap + Consume
# Your Approach — Cleaned
# Time Complexity: O(n + m)
# Space Complexity: O(u)
# Under lowercase English constraints: O(1), maximum 26 keys.
#
# Time Explanation:
# s frequencies build cheyadaniki O(n).
# t characters ni check cheyadaniki worst case O(m).
# Available count lekapothe extra character dorikinatte.
#
# Space Explanation:
# s lo unique characters frequencies store chestunnam.
class Solution1:
    def findTheDifference(self, s: str, t: str) -> str:
        frequency = {}

        for character in s:
            frequency[character] = (
                frequency.get(character, 0) + 1
            )

        for character in t:
            if frequency.get(character, 0) > 0:
                frequency[character] -= 1
            else:
                return character


# ============================================================


# Approach 2: XOR
# Recommended Constant-Space Approach
# Time Complexity: O(n + m)
# Space Complexity: O(1)
#
# Time Explanation:
# Rendu strings characters ni okkokkasari process chestunnam.
#
# Space Explanation:
# Oka XOR accumulator maatrame use chestunnam.
# Dictionary, array ledaa combined string create cheyadam ledu.
#
# Logic:
# x ^ x = 0
# 0 ^ x = x
#
# Rendu strings lo matching character codes cancel avutayi.
# Extra character code maatrame migulutundi.
class Solution2:
    def findTheDifference(self, s: str, t: str) -> str:
        difference = 0

        for character in s:
            difference ^= ord(character)

        for character in t:
            difference ^= ord(character)

        return chr(difference)


# ============================================================


# Approach 3: Fixed-Size Frequency Array
# Time Complexity: O(n + m)
# Space Complexity: O(1)
#
# Time Explanation:
# s characters frequencies array lo calculate chestunnam.
# t characters kosam available count check chestunnam.
#
# Space Explanation:
# Lowercase English letters kosam fixed 26-element array.
# Input size perigina array size maaradu.
class Solution3:
    def findTheDifference(self, s: str, t: str) -> str:
        frequency = [0] * 26

        for character in s:
            index = ord(character) - ord("a")
            frequency[index] += 1

        for character in t:
            index = ord(character) - ord("a")

            if frequency[index] == 0:
                return character

            frequency[index] -= 1


# ============================================================
# OTHER USEFUL SOLUTIONS
# ============================================================


# Approach 4: Character-Code Sum Difference
# Time Complexity: O(n + m)
# Space Complexity: O(1)
#
# Time Explanation:
# Rendu strings character codes sums calculate chestunnam.
# t total nunchi s total subtract chestunnam.
#
# Space Explanation:
# Generator expressions use chestunnam; character lists create cheyamu.
#
# Logic:
# Matching character codes subtraction lo cancel avutayi.
# Extra character code maatrame migulutundi.
class Solution4:
    def findTheDifference(self, s: str, t: str) -> str:
        first_sum = sum(ord(character) for character in s)
        second_sum = sum(ord(character) for character in t)

        return chr(second_sum - first_sum)


# ============================================================


# Approach 5: Counter Subtraction
# Short Python Approach
# Time Complexity: O(n + m)
# Space Complexity: O(u + 1)
# Under lowercase English constraints: O(1).
#
# Time Explanation:
# Rendu strings frequencies calculate chestunnam.
# t frequencies nunchi s frequencies subtract chestunnam.
# Positive count unna extra character maatrame migulutundi.
#
# Space Explanation:
# Rendu Counters and difference Counter store chestunnam.
class Solution5:
    def findTheDifference(self, s: str, t: str) -> str:
        from collections import Counter

        difference = Counter(t) - Counter(s)

        return next(iter(difference))


# ============================================================


# Approach 6: Sorting + Comparison
# Time Complexity: O(n log n + m log m)
# Space Complexity: O(n + m)
#
# Time Explanation:
# Rendu strings characters ni sort chestunnam.
# Tarvata corresponding positions compare chestunnam.
#
# Space Explanation:
# sorted() rendu new character lists create chestundi.
#
# Logic:
# First mismatch daggara t lo unna character extra character.
# Mismatch lekapothe sorted_t last character extra character.
class Solution6:
    def findTheDifference(self, s: str, t: str) -> str:
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        for index in range(len(sorted_s)):
            if sorted_s[index] != sorted_t[index]:
                return sorted_t[index]

        return sorted_t[-1]
