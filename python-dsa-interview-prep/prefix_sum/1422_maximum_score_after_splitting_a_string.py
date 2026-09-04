# LeetCode 1422 - Maximum Score After Splitting a String
# Difficulty: Easy
#
# Recommended Optimal Approach: Left Zeros + Right Ones
# Recommended Current-Level Approach: Left Zeros + Right Ones


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: Running Left Zeros and Right Ones
# Your Approach — Cleaned
# Recommended Optimal Approach
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Time Explanation:
# s.count("1") complete string ni okasari scan chestundi: O(n).
# Loop first n - 1 characters ni traverse chestundi: O(n).
# Total O(n) + O(n) = O(n).
#
# Space Explanation:
# Konni integer variables maatrame use chestunnam.
# Input size periginaa additional space peragadu.
# Kabatti space complexity O(1).
#
# Logic:
# Initially right side lo complete string ones untayi.
# Oka character ni right nunchi left ki move chestunnam.
#
# Character "0" ayite:
# left_zeros += 1
#
# Character "1" ayite:
# right_ones -= 1
#
# Current score:
# left_zeros + right_ones

class Solution1:
    def maxScore(self, s: str) -> int:
        left_zeros = 0
        right_ones = s.count("1")
        max_score = 0

        for index in range(len(s) - 1):
            if s[index] == "0":
                left_zeros += 1
            else:
                right_ones -= 1

            current_score = left_zeros + right_ones
            max_score = max(max_score, current_score)

        return max_score


# ============================================================


# Approach 2: Prefix Difference
# Optimal Mathematical Approach
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Formula:
# score = left_zeros + right_ones
#
# right_ones = total_ones - left_ones
#
# score:
# total_ones + left_zeros - left_ones
#
# Prati valid prefix kosam:
# left_zeros - left_ones maximum value calculate chestunnam.
# Chivarilo total ones add chestunnam.

class Solution2:
OAOAOA    def maxScore(self, s: str) -> int:
        left_zeros = 0
        left_ones = 0
        best_difference = -len(s)

        for index, char in enumerate(s):
            if char == "0":
                left_zeros += 1
            else:
                left_ones += 1

            if index < len(s) - 1:
                difference = left_zeros - left_ones
                best_difference = max(
                    best_difference,
                    difference
                )

        total_ones = left_ones

        return total_ones + best_difference


# ============================================================


# Approach 3: Prefix Zeros + Suffix Ones Arrays
# Time Complexity: O(n)
OAOAOA# Space Complexity: O(n)
#
# Logic:
# prefix_zeros[i] lo index i mundu unna zeros count store chestunnam.
# suffix_ones[i] lo index i nunchi unna ones count store chestunnam.
#
# Prati valid split kosam:
# prefix_zeros[split] + suffix_ones[split]
#
# Arrays build cheyadaniki O(n).
# Valid splits check cheyadaniki O(n).
# Total time O(n).

class Solution3:
    def maxScore(self, s: str) -> int:
        n = len(s)

        prefix_zeros = [0] * (n + 1)
        suffix_ones = [0] * (n + 1)

        for index in range(n):
            prefix_zeros[index + 1] = (
                prefix_zeros[index]
                + (1 if s[index] == "0" else 0)
            )

        for index in range(n - 1, -1, -1):
            suffix_ones[index] = (
                suffix_ones[index + 1]
                + (1 if s[index] == "1" else 0)
            )

        max_score = 0

        for split in range(1, n):
            current_score = (
                prefix_zeros[split]
                + suffix_ones[split]
            )

            max_score = max(max_score, current_score)

        return max_score


# ============================================================
# OTHER USEFUL SOLUTIONS
# ============================================================


# Approach 4: Slicing + count()
# Brute-Force Approach
# Time Complexity: O(n^2)
# Space Complexity: O(n)
#
# Prati valid split kosam left and right slices create chestunnam.
# count() rendu substrings ni scan chestundi.
# n splits × O(n) work = O(n^2).
#
# Slicing temporary strings create chestundi.
# Kabatti temporary space O(n).

class Solution4:
    def maxScore(self, s: str) -> int:
        max_score = 0

        for split in range(1, len(s)):
            left = s[:split]
            right = s[split:]

            current_score = (
                left.count("0")
                + right.count("1")
            )

            max_score = max(max_score, current_score)

        return max_score


# ============================================================


# Approach 5: Manual Brute Force Without Slicing
# Time Complexity: O(n^2)
# Space Complexity: O(1)
#
# Prati split kosam left zeros mariyu right ones
# separate loops tho count chestunnam.
#
# Slices create cheyadam ledu kabatti space O(1).
# Kaani repeated scanning valla time O(n^2).

class Solution5:
    def maxScore(self, s: str) -> int:
        n = len(s)
        max_score = 0

        for split in range(1, n):
            left_zeros = 0
            right_ones = 0

            for index in range(split):
                if s[index] == "0":
                    left_zeros += 1

            for index in range(split, n):
                if s[index] == "1":
                    right_ones += 1

            current_score = left_zeros + right_ones
            max_score = max(max_score, current_score)

        return max_score
