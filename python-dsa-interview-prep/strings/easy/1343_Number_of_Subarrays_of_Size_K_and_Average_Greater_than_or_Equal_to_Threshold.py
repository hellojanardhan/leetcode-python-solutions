# ============================================================
# LeetCode 1343 - Number of Sub-arrays of Size K and Average
# Greater than or Equal to Threshold
# Difficulty: Medium
#
# Recommended Optimal Approach: Fixed-Size Sliding Window
# Recommended Current-Level Approach: Your Approach
# ============================================================


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: Fixed-Size Sliding Window
# Your Approach — Recommended Optimal Approach
# Time Complexity: O(n)
# Auxiliary Space Complexity: O(1)
#
# Time Explanation:
# First k elements sum calculate cheyadaniki O(k).
# Remaining windows ni O(n-k) time lo process chestham.
# Total O(k) + O(n-k) = O(n).
#
# Space Explanation:
# total, count, j lanti few variables matrame use chestham.
# Input size perigina additional space peragadu.
# Kabatti auxiliary space O(1).
#
# Logic:
# First window sum calculate chestham.
# Sum >= k * threshold ayithe count increment chestham.
# Next window ki move ayyetappudu:
# Incoming element add chestham.
# Outgoing element subtract chestham.
# Prati window sum ni threshold tho compare chestham.

class Solution1:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        count = 0
        total = 0

        for num in range(k):
            total += arr[num]

        if total >= threshold * k:
            count += 1

        for j in range(k, len(arr)):
            total += arr[j] - arr[j - k]

            if total >= k * threshold:
                count += 1

        return count


# ============================================================
# Approach 2: Fixed-Size Sliding Window Using enumerate()
# Clean Pythonic Approach
# Time Complexity: O(n)
# Auxiliary Space Complexity: O(1)
#
# Time Explanation:
# String/array ni one pass lo traverse chestham.
# Every element constant-time work matrame chestundi.
# Total time O(n).
#
# Space Explanation:
# Window sum and count matrame maintain chestham.
# Extra array or dictionary create cheyyamu.
# Kabatti O(1) auxiliary space.
#
# Logic:
# First k elements sum calculate chestham.
# Tarvatha enumerate() tho remaining elements traverse chestham.
# Incoming element index i ayithe outgoing element index i-k.
# New window sum calculate chesi valid ayithe count increment chestham.

class Solution2:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        total = sum(arr[:k])
        target = k * threshold
        count = int(total >= target)

        for i, num in enumerate(arr[k:], start=k):
            total += num - arr[i - k]

            if total >= target:
                count += 1

        return count


# ============================================================
# Approach 3: Prefix Sum
# Alternative Optimal-Time Approach
# Time Complexity: O(n)
# Auxiliary Space Complexity: O(n)
#
# Time Explanation:
# Prefix sums array build cheyadaniki O(n).
# Prati valid window sum O(1) lo calculate cheyochu.
# Total time O(n).
#
# Space Explanation:
# Prefix sums store cheyadaniki extra array use chestham.
# Array size n+1 kabatti auxiliary space O(n).
#
# Logic:
# prefix[i] ante arr lo first i elements sum.
# Window [i-k, i) sum:
# prefix[i] - prefix[i-k]
# Ee sum >= k * threshold ayithe count increment chestham.

class Solution3:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        n = len(arr)
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + arr[i]

        target = k * threshold
        count = 0

        for end in range(k, n + 1):
            window_sum = prefix[end] - prefix[end - k]

            if window_sum >= target:
                count += 1

        return count


# ============================================================
# OTHER USEFUL SOLUTIONS
# ============================================================


# Approach 4: Brute Force
# Time Complexity: O(n * k)
# Auxiliary Space Complexity: O(1)
#
# Time Explanation:
# Prati window kosam k elements sum calculate chestham.
# Total n-k+1 windows untayi.
# Kabatti O((n-k+1) * k), simplified worst case O(n*k).
#
# Space Explanation:
# Extra array create cheyyamu.
# Few variables matrame use chestham.
# Kabatti O(1) auxiliary space.
#
# Logic:
# Every possible window start position ki,
# k elements sum calculate chestham.
# Sum threshold condition satisfy ayithe count increment chestham.
#
# Note:
# Idi learning kosam useful.
# Large inputs ki sliding window better.

class Solution4:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        count = 0
        target = k * threshold

        for start in range(len(arr) - k + 1):
            total = 0

            for i in range(start, start + k):
                total += arr[i]

            if total >= target:
                count += 1

        return count


# ============================================================
# DRY RUN
# ============================================================

# Input:
# arr = [2, 2, 2, 2, 5, 5, 5, 8]
# k = 3
# threshold = 4
#
# Target sum = k * threshold = 3 * 4 = 12
#
# First window:
# [2, 2, 2]
# total = 6
# 6 >= 12 -> False
# count = 0
#
# Slide 1:
# Remove arr[0] = 2
# Add arr[3] = 2
# Window = [2, 2, 2]
# total = 6
# 6 >= 12 -> False
# count = 0
#
# Slide 2:
# Remove arr[1] = 2
# Add arr[4] = 5
# Window = [2, 2, 5]
# total = 9
# 9 >= 12 -> False
# count = 0
#
# Slide 3:
# Remove arr[2] = 2
# Add arr[5] = 5
# Window = [2, 5, 5]
# total = 12
# 12 >= 12 -> True
# count = 1
#
# Slide 4:
# Remove arr[3] = 2
# Add arr[6] = 5
# Window = [5, 5, 5]
# total = 15
# 15 >= 12 -> True
# count = 2
#
# Slide 5:
# Remove arr[4] = 5
# Add arr[7] = 8
# Window = [5, 5, 8]
# total = 18
# 18 >= 12 -> True
# count = 3
#
# Output: 3


# ============================================================
# TEST CASES
# ============================================================

# Test Case 1:
# arr = [2, 2, 2, 2, 5, 5, 5, 8]
# k = 3
# threshold = 4
# Output: 3
#
# Test Case 2:
# arr = [11, 13, 17, 23, 29, 31, 7, 5, 2, 3]
# k = 3
# threshold = 5
# Output: 8
#
# Test Case 3:
# arr = [1, 1, 1, 1, 1]
# k = 1
# threshold = 1
# Output: 5
#
# Test Case 4:
# arr = [7, 7, 7, 7, 7, 7, 7]
# k = 3
# threshold = 7
# Output: 5
#
# Test Case 5:
# arr = [4, 4, 4, 4]
# k = 2
# threshold = 5
# Output: 0


# ============================================================
# INTERVIEW-READY EXPLANATION
# ============================================================

# "I use a fixed-size sliding window to solve this problem.
# First, I calculate the sum of the first k elements.
# Instead of calculating the average using division, I compare
# the window sum with k multiplied by the threshold.
# For every next window, I add the incoming element and subtract
# the outgoing element. If the sum is greater than or equal to
# the target sum, I increment the count.
# This approach takes O(n) time and O(1) auxiliary space."


# ============================================================
# FINAL RECOMMENDATION
# ============================================================

# Solution 1:
# Best choice — your original solution is correct and optimal.
#
# Solution 2:
# Same sliding-window logic with a different iteration style.
#
# Solution 3:
# Useful for understanding prefix sums, but requires O(n) space.
#
# Solution 4:
# Brute force; useful for understanding all possible windows,
# but slower than the sliding-window approach.
#
# Recommended for interviews: Solution 1.
#
# Filename:
# LeetCode_1343_Number_of_Subarrays_of_Size_K_and_Average_Greater_than_or_Equal_to_Threshold.py
