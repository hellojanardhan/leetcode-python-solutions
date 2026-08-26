# LeetCode 228 - Summary Ranges
# Difficulty: Easy
# Recommended Approach: Single Pointer Linear Scan
# Recommended Current-Level Approach: Single Pointer Linear Scan

from typing import List


# Approach 1: Your Approach - Single Pointer Linear Scan
# Time Complexity: O(n)
# Prathi element ni maximum okkasari process chesthunnam.
# Space Complexity: O(1) Auxiliary
# result output ni exclude chesthe, konni variables mathrame use chesthunnam.
class Solution1:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        i = 0

        while i < len(nums):
            start = nums[i]

            while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
                i += 1

            if start == nums[i]:
                result.append(str(start))
            else:
                result.append(str(start) + "->" + str(nums[i]))

            i += 1

        return result


# Approach 2: Start and End Pointers
# Time Complexity: O(n)
# start mariyu end pointers forward direction lo mathrame move avuthayi.
# Space Complexity: O(1) Auxiliary
# start mariyu end ane pointer variables mathrame use chesthunnam.
class Solution2:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        start = 0

        while start < len(nums):
            end = start

            while end + 1 < len(nums) and nums[end + 1] == nums[end] + 1:
                end += 1

            if start == end:
                result.append(str(nums[start]))
            else:
                result.append(str(nums[start]) + "->" + str(nums[end]))

            start = end + 1

        return result


# Approach 3: For Loop with Range Start
# Time Complexity: O(n)
# For loop prathi element ni okkasari check chesthundi.
# Space Complexity: O(1) Auxiliary
# start mariyu i ane variables mathrame additional ga use chesthunnam.
class Solution3:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        result = []
        start = nums[0]

        for i in range(1, len(nums) + 1):
            if i == len(nums) or nums[i] != nums[i - 1] + 1:
                if start == nums[i - 1]:
                    result.append(str(start))
                else:
                    result.append(str(start) + "->" + str(nums[i - 1]))

                if i < len(nums):
                    start = nums[i]

        return result


# Approach 4: Using itertools.groupby()
# Time Complexity: O(n)
# groupby prathi number ni okkasari process chesthundi.
# Space Complexity: O(k)
# Largest consecutive group lo k elements ni list lo store chesthunnam.
class Solution4:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        from itertools import groupby

        result = []

        for _, group in groupby(enumerate(nums), lambda item: item[1] - item[0]):
            current_group = [value for _, value in group]
            start = current_group[0]
            end = current_group[-1]

            if start == end:
                result.append(str(start))
            else:
                result.append(str(start) + "->" + str(end))

        return result
