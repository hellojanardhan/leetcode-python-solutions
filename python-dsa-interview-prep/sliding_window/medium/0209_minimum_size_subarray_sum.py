# LeetCode 209 - Minimum Size Subarray Sum
# Difficulty: Medium

# Recommended Approach: Variable Sliding Window
# Recommended Current-Level Approach: Variable Sliding Window


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: Variable Sliding Window
# Your Approach
# Recommended Optimal Approach
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Time Explanation:
# right pointer nums array ni left-to-right once traverse chestundi.
#
# Prati number ni total ki add chestunnam.
#
# total >= target ayinappudu:
# current window valid.
#
# Appudu:
# current length calculate chestam
# minimum update chestam
# left side nunchi element remove chestam
# start pointer move chestam
#
# Important:
# while loop for loop lopala unna sare O(n^2) kaadu.
#
# end/right pointer maximum n times move avutundi.
# start/left pointer kuda maximum n times move avutundi.
#
# start pointer backward velladu.
#
# Kabatti total operations approximately:
# n right movements + n left movements
#
# O(n + n)
# = O(2n)
# = O(n)
#
# Space Explanation:
# total, minimal_length, start, length lanti
# few variables maatrame use chestunnam.
#
# Extra array / set / hashmap create cheyyatledu.
#
# Kabatti:
# O(1)
class Solution1:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        minimal_length = float("inf")

        start = 0

        for end in range(len(nums)):
            total += nums[end]

            while total >= target:
                length = end - start + 1

                minimal_length = min(
                    minimal_length,
                    length
                )

                total -= nums[start]
                start += 1

        if minimal_length == float("inf"):
            return 0

        return minimal_length


# ============================================================


# Approach 2: Prefix Sum + Binary Search
# Time Complexity: O(n log n)
# Space Complexity: O(n)
#
# Time Explanation:
# nums positive values kabatti prefix sums strictly increasing
# or non-decreasing ga untayi.
#
# First prefix sum array build chestam -> O(n).
#
# Prati start position kosam,
# target reach cheyyadaniki required prefix value ni
# binary search chestam -> O(log n).
#
# n starting positions untayi.
#
# Total:
# O(n log n)
#
# Space Explanation:
# Prefix sum array n+1 values store chestundi.
#
# O(n)
class Solution2:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        import bisect

        n = len(nums)

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        minimum = float("inf")

        for start in range(n):
            required = prefix[start] + target

            end = bisect.bisect_left(
                prefix,
                required
            )

            if end <= n:
                minimum = min(
                    minimum,
                    end - start
                )

        return 0 if minimum == float("inf") else minimum


# ============================================================


# Approach 3: Brute Force
# Time Complexity: O(n^2)
# Space Complexity: O(1)
#
# Time Explanation:
# Prati starting index nunchi
# right side elements ni add chestam.
#
# Sum target reach ayye varaku continue chestam.
#
# Worst-case:
# start=0 -> almost n elements
# start=1 -> almost n-1 elements
# start=2 -> almost n-2 elements
#
# Total approximately:
# n + (n-1) + (n-2) + ...
#
# = O(n^2)
#
# Space Explanation:
# Few variables maatrame.
#
# O(1)
class Solution3:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        minimum = float("inf")

        for i in range(n):
            total = 0

            for j in range(i, n):
                total += nums[j]

                if total >= target:
                    minimum = min(
                        minimum,
                        j - i + 1
                    )

                    break

        return 0 if minimum == float("inf") else minimum


# ============================================================
# OTHER POSSIBLE SOLUTIONS
# ============================================================


# Approach 4: Prefix Sum + Nested Search
# Time Complexity: O(n^2)
# Space Complexity: O(n)
#
# Prefix sum valla any subarray sum ni O(1) lo calculate cheyochu.
#
# Kaani every possible start/end pair check chestunnam.
#
# Kabatti total O(n^2).
#
# Prefix array kosam O(n) space.
class Solution4:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        minimum = float("inf")

        for start in range(n):
            for end in range(start + 1, n + 1):

                current_sum = (
                    prefix[end] - prefix[start]
                )

                if current_sum >= target:
                    minimum = min(
                        minimum,
                        end - start
                    )

                    break

        return 0 if minimum == float("inf") else minimum
