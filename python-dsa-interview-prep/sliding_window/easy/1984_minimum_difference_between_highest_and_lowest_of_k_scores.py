# LeetCode 1984 - Minimum Difference Between Highest and Lowest of K Scores
# Difficulty: Easy

# Recommended Approach: Sorting + Fixed Sliding Window
# Recommended Current-Level Approach: Sorting + Fixed Sliding Window


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: Sorting + Fixed Sliding Window
# Your Approach
# Recommended Optimal Approach
# Time Complexity: O(n log n)
# Space Complexity: O(n) worst-case for Python sorting
#
# Time Explanation:
# Munduga nums array ni sort chestunnam.
# Sorting time complexity O(n log n).
#
# Tarvata exactly k elements unna prati window ni check chestunnam.
#
# Sorted window lo:
# nums[i] = minimum score
# nums[j] = maximum score
#
# Kabatti difference:
# nums[j] - nums[i]
#
# Sliding window traversal O(n).
# Total:
# O(n log n + n) = O(n log n).
#
# Space Explanation:
# nums.sort() array ni in-place modify chestundi.
# Kaani Python Timsort worst-case lo extra temporary memory use cheyyachu.
# Kabatti worst-case auxiliary space O(n).
class Solution1:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        minimum = float("inf")

        i = 0
        j = k - 1

        while j < len(nums):
            minimum = min(
                nums[j] - nums[i],
                minimum
            )

            i += 1
            j += 1

        return minimum


# ============================================================


# Approach 2: Sorting + For Loop
# Short Optimal Approach
# Time Complexity: O(n log n)
# Space Complexity: O(n) worst-case for Python sorting
#
# Time Explanation:
# Array ni O(n log n) time lo sort chestunnam.
#
# Prati valid k-size sorted window kosam:
#
# first element = minimum
# last element = maximum
#
# Difference ni direct-ga calculate chestunnam.
# Window traversal O(n).
#
# Kabatti total time complexity O(n log n).
#
# Space Explanation:
# Extra data structure create cheyyatledu.
# Python sorting implementation worst-case temporary memory use cheyyachu.
# Kabatti worst-case auxiliary space O(n).
class Solution2:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        minimum = float("inf")

        for i in range(len(nums) - k + 1):
            j = i + k - 1

            minimum = min(
                minimum,
                nums[j] - nums[i]
            )

        return minimum


# ============================================================


# Approach 3: Brute Force - Generate All K Student Combinations
# Time Complexity: O(C(n, k) * k)
# Space Complexity: O(k)
#
# Time Explanation:
# Original problem "any k students" ani cheptundi.
#
# Brute force lo every possible k-student combination ni generate chestam.
# Prati combination lo maximum and minimum calculate cheyadaniki O(k).
#
# Number of combinations:
# C(n, k)
#
# Kabatti total time:
# O(C(n, k) * k)
#
# Large inputs ki idi chaala expensive.
#
# Space Explanation:
# Oka combination lo k values maintain chestam.
# Kabatti working space approximately O(k),
# combinations anni okesari store cheyakunda iterator use cheste.
class Solution3:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        from itertools import combinations

        minimum = float("inf")

        for group in combinations(nums, k):
            difference = max(group) - min(group)

            minimum = min(
                minimum,
                difference
            )

        return minimum


# ============================================================
# OTHER POSSIBLE SOLUTIONS
# ============================================================


# Approach 4: Sorting + Window Slicing + max()/min()
# Time Complexity: O(n log n + (n-k+1) * k)
# Space Complexity: O(k) + sorting memory
#
# Time Explanation:
# Array ni first O(n log n) lo sort chestunnam.
#
# Tarvata prati k-size window slice create chesi:
# max(window)
# min(window)
# calculate chestunnam.
#
# Prati window processing O(k).
# Approximately n-k+1 windows untayi.
#
# Kabatti:
# O(n log n + (n-k+1) * k)
#
# Idi correct kaani unnecessary work,
# because sorted window lo first and last values already min/max.
#
# Space Explanation:
# Slice create chesinappudu maximum k elements temporary-ga store avutayi.
# Kabatti O(k), plus Python sorting memory.
class Solution4:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        minimum = float("inf")

        for i in range(len(nums) - k + 1):
            window = nums[i:i + k]

            difference = max(window) - min(window)

            minimum = min(
                minimum,
                difference
            )

        return minimum
