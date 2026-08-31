# LeetCode 1365 - How Many Numbers Are Smaller Than the Current Number
# Difficulty: Easy
# Recommended Approach: Frequency Array + Prefix Count
# Recommended Current-Level Approach: Sorting + HashMap


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: Nested Loops
# Your Approach
# Time Complexity: O(n^2)
# Space Complexity: O(n)
#
# Time Explanation:
# Prati nums[i] kosam complete nums array ni traverse chestunnam.
# Outer loop n times run avutundi.
# Inner loop kuda n times run avutundi.
# Kabatti total comparisons roughly n * n.
# Total time complexity O(n^2).
#
# Space Explanation:
# result list lo n answers store chestunnam.
# Kabatti output space O(n).
# Output ni exclude chesthe auxiliary space O(1).
class Solution1:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(len(nums)):
            count = 0

            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    count += 1

            result.append(count)

        return result


# ============================================================


# Approach 2: Sorting + HashMap
# Recommended Current-Level Approach
# Time Complexity: O(n log n)
# Space Complexity: O(n)
#
# Time Explanation:
# nums ni sort cheyadaniki O(n log n).
# Sorted array ni traverse chesi each number first index ni
# dictionary lo store chestunnam - O(n).
#
# Sorted array lo oka number first occurrence index ante
# danikante smaller numbers count.
#
# Final nums traversal O(n).
# Kabatti total time complexity O(n log n).
#
# Space Explanation:
# sorted_nums list O(n).
# rank dictionary maximum O(n).
# result list O(n).
# Kabatti auxiliary space O(n).
class Solution2:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)

        rank = {}

        for index, num in enumerate(sorted_nums):
            if num not in rank:
                rank[num] = index

        result = []

        for num in nums:
            result.append(rank[num])

        return result


# ============================================================


# Approach 3: Frequency Array + Prefix Count
# Recommended Optimal Approach
# Time Complexity: O(n + R)
# Space Complexity: O(R)
#
# R = allowed value range.
# LeetCode constraints lo nums[i] 0 to 100.
#
# Time Explanation:
# First each number frequency calculate chestunnam - O(n).
#
# Tarvata frequency array meeda prefix count build chestunnam.
# Range fixed 0..100 kabatti R = 101.
#
# Final-ga each num ki danikante smaller values count
# direct-ga prefix information nundi retrieve chestunnam.
#
# Total:
# O(n + R)
#
# R fixed kabatti practical-ga O(n).
#
# Space Explanation:
# Frequency array fixed size 101.
# Kabatti constraint perspective lo auxiliary space O(1).
# General range perspective lo O(R).
class Solution3:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        frequency = [0] * 101

        for num in nums:
            frequency[num] += 1

        smaller = [0] * 101
        running_count = 0

        for value in range(101):
            smaller[value] = running_count
            running_count += frequency[value]

        result = []

        for num in nums:
            result.append(smaller[num])

        return result


# ============================================================
# OTHER POSSIBLE SOLUTIONS
# ============================================================


# Approach 4: Sorting + Binary Search
# Time Complexity: O(n log n)
# Space Complexity: O(n)
#
# Time Explanation:
# nums ni sort cheyadaniki O(n log n).
#
# Prati original number kosam bisect_left() use chesi
# sorted array lo first occurrence index find chestunnam.
# Oka binary search O(log n).
# n numbers kosam O(n log n).
#
# Kabatti total time complexity O(n log n).
#
# Space Explanation:
# sorted_nums copy O(n).
# result O(n).
# Kabatti auxiliary space O(n).
class Solution4:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        from bisect import bisect_left

        sorted_nums = sorted(nums)

        result = []

        for num in nums:
            result.append(bisect_left(sorted_nums, num))

        return result


# ============================================================


# Approach 5: Frequency HashMap + Sorted Unique Values
# Time Complexity: O(n + k log k)
# Space Complexity: O(k)
#
# Time Explanation:
# First frequency HashMap build cheyadaniki O(n).
#
# k unique numbers ni sort cheyadaniki O(k log k).
#
# Sorted unique values meeda running count maintain chesi,
# each value ki smaller numbers count store chestunnam.
#
# Final nums traversal O(n).
#
# Kabatti total time:
# O(n + k log k)
#
# Space Explanation:
# frequency dictionary O(k).
# smaller_count dictionary O(k).
# Kabatti auxiliary space O(k).
class Solution5:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        frequency = {}

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        smaller_count = {}
        running_count = 0

        for num in sorted(frequency):
            smaller_count[num] = running_count
            running_count += frequency[num]

        return [smaller_count[num] for num in nums]
