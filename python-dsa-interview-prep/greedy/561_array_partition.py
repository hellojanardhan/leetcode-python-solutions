# LeetCode 561 - Array Partition
# Difficulty: Easy

# Recommended Approach:
# Sorting + Greedy
#
# Recommended Current-Level Approach:
# Sorting + Greedy
#
# Main Strategy:
# Greedy
#
# LeetCode Topics:
# Array
# Greedy
# Sorting
# Counting Sort


# ============================================================
# TOP APPROACHES
# ============================================================


# Approach 1: Sorting + Greedy
# Your Approach
# Recommended Current-Level Approach
# Recommended Interview Approach
#
# Pattern:
# Sorting + Greedy
#
# Time Complexity:
# O(n log n)
#
# Space Complexity:
# O(1) excluding sorting internals
#
# Time Explanation:
# First nums ni ascending order lo sort chestunnam.
#
# Example:
# nums = [1, 4, 3, 2]
#
# Sorted:
# [1, 2, 3, 4]
#
# Adjacent pairs:
# (1, 2)
# (3, 4)
#
# Prati pair lo minimum:
# first element.
#
# Sorted array lo pair starts:
# index 0, 2, 4, 6 ...
#
# Kabatti every even index value ni
# total ki add chestham.
#
# Sorting:
# O(n log n)
#
# Traversal:
# O(n)
#
# Total:
# O(n log n)
#
# Space Explanation:
# total and loop variable maatrame
# extra ga use chestunnam.
#
# Sorting internal memory ignore chesthe:
# O(1).

class Solution1:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort()

        total = 0
        n = len(nums)

        for i in range(0, n, 2):
            total += nums[i]

        return total


# ============================================================


# Approach 2: Counting Sort + Greedy
# Recommended Optimal for Bounded Value Range
#
# Pattern:
# Counting Sort + Greedy
#
# Time Complexity:
# O(n + K)
#
# Space Complexity:
# O(K)
#
# K = total possible value range
#
# Time Explanation:
# Constraint:
#
# -10000 <= nums[i] <= 10000
#
# So possible values count:
# 20001
#
# Normal sorting badulu
# frequency array create cheyochu.
#
# Prati value frequency ni count chestham.
#
# Tarvata smallest value nunchi
# increasing order lo process chestham.
#
# Sorted-order concept:
#
# 1st element -> pair minimum
# 2nd element -> pair maximum
# 3rd element -> pair minimum
# 4th element -> pair maximum
#
# Kabatti every alternate occurrence ni
# answer lo add chestham.
#
# Frequency build:
# O(n)
#
# Range traversal:
# O(K)
#
# Total:
# O(n + K)
#
# Space Explanation:
# Frequency array size K.
#
# Kabatti:
# O(K).

class Solution2:
    def arrayPairSum(self, nums: list[int]) -> int:
        offset = 10000
        freq = [0] * 20001

        for num in nums:
            freq[num + offset] += 1

        total = 0
        take = True

        for i in range(len(freq)):
            while freq[i] > 0:

                if take:
                    total += i - offset

                take = not take
                freq[i] -= 1

        return total


# ============================================================
# OTHER POSSIBLE SOLUTIONS
# ============================================================


# Approach 3: Array Brute Force
# Baseline Approach
# Not Recommended
#
# Pattern:
# Array + Simulation
#
# Time Complexity:
# O(n^2)
#
# Space Complexity:
# O(n)
#
# Time Explanation:
# Repeatedly smallest element ni find chestham.
#
# First smallest value ni
# pair minimum ga total ki add chestham.
#
# Next smallest value ni
# pair partner laga remove chestham.
#
# Ila array empty ayye varaku
# repeat chestham.
#
# min() and remove() operations
# repeated ga O(n) cost tisukuntayi.
#
# Kabatti:
# O(n^2)
#
# Space Explanation:
# nums copy create chestunnam.
#
# Kabatti:
# O(n).

class Solution3:
    def arrayPairSum(self, nums: list[int]) -> int:
        arr = nums[:]

        total = 0

        while arr:
            first = min(arr)
            total += first
            arr.remove(first)

            second = min(arr)
            arr.remove(second)

        return total


# ============================================================
# PATTERN SUMMARY
# ============================================================


# Array:
# Baseline brute-force / simulation approach.
#
# Greedy:
# Small values ni nearby values tho pair chestham.
#
# Enduku?
# Small value ni very large value tho pair chesthe,
# large value contribution waste avutundi.
#
# Sorting:
# Adjacent optimal pairing ni create chestundi.
#
# Counting Sort:
# Fixed bounded range ni use chesi
# comparison sorting ni avoid chestundi.
#
# Main optimal interview combination:
#
# Sorting
# +
# Greedy
#
# Best asymptotic approach for given constraints:
#
# Counting Sort
# +
# Greedy
