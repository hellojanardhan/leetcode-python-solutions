# LeetCode 128 - Longest Consecutive Sequence
# Difficulty: Medium
#
# Recommended Approach: HashSet + Sequence Starts
# Recommended Current-Level Approach: HashSet + Sequence Starts
#
# n = total input numbers
# u = unique numbers
# HashMap/HashSet operations average-ga O(1) ani assume chestunnam.


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: HashSet + Sequence Starts
# Your Approach — cleaned
# Recommended Optimal Approach
#
# Time Complexity: O(n) average
# Space Complexity: O(u), worst-case O(n)
#
# Time:
# Set build cheyadaniki O(n).
# Previous number lenappude sequence count chestunnam.
# Prati unique sequence okkasare traverse avutundi.
#
# Space:
# Set lo u unique numbers store chestunnam.

from typing import List


class Solution1:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        max_count = 0

        for num in seen:
            if num - 1 in seen:
                continue

            count = 1
            nxt = num + 1

            while nxt in seen:
                count += 1
                nxt += 1

            max_count = max(max_count, count)

        return max_count


# ============================================================


# Approach 2: Sorting + Scan
# Simple Alternative
#
# Time Complexity: O(n log n)
# Space Complexity: O(n)
#
# Time:
# Sorting O(n log n), tarvata single scan O(n).
# Duplicates vachinappudu skip cheyali.
#
# Space:
# sorted(nums) kotta list create chestundi.
#
# Note:
# Correct answer istundi, kaani problem O(n) target meet kaadu.

class Solution2:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        ordered = sorted(nums)
        count = 1
        max_count = 1

        for i in range(1, len(ordered)):
            if ordered[i] == ordered[i - 1]:
                continue

            if ordered[i] == ordered[i - 1] + 1:
                count += 1
            else:
                count = 1

            max_count = max(max_count, count)

        return max_count


# ============================================================


# Approach 3: HashMap + Sequence Boundary Lengths
# Advanced Alternative
#
# Time Complexity: O(n) average
# Space Complexity: O(u), worst-case O(n)
#
# Logic:
# Kotta number vachinappudu left/right sequences ni kaluputham.
# Combined sequence length ni rendu endpoints daggara update chestham.
# Already unna number ayite skip chestham.
#
# Time:
# Prati input number kosam constant number of dictionary operations.
#
# Space:
# Dictionary lo u unique numbers untayi.

class Solution3:
    def longestConsecutive(self, nums: List[int]) -> int:
        lengths = {}
        max_count = 0

        for num in nums:
            if num in lengths:
                continue

            left_length = lengths.get(num - 1, 0)
            right_length = lengths.get(num + 1, 0)

            total = left_length + 1 + right_length

            lengths[num] = total
            lengths[num - left_length] = total
            lengths[num + right_length] = total

            max_count = max(max_count, total)

        return max_count


# ============================================================
# OTHER USEFUL SOLUTIONS
# ============================================================


# Approach 4: HashSet + Expand Both Directions + Remove
#
# Time Complexity: O(n) average
# Space Complexity: O(u), worst-case O(n)
#
# Logic:
# Oka number teesukoni left/right directions lo expand chestham.
# Count chesina numbers ni set nunchi remove chestham.
#
# Time:
# Prati unique number set nunchi okkasare remove avutundi.
#
# Space:
# Separate set create chestunnam.
# Original nums list change kaadu.

class Solution4:
    def longestConsecutive(self, nums: List[int]) -> int:
        remaining = set(nums)
        max_count = 0

        while remaining:
            num = remaining.pop()
            count = 1

            left = num - 1
            right = num + 1

            while left in remaining:
                remaining.remove(left)
                count += 1
                left -= 1

            while right in remaining:
                remaining.remove(right)
                count += 1
                right += 1

            max_count = max(max_count, count)

        return max_count
