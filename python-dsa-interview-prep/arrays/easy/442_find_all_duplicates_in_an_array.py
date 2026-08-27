# LeetCode 442 - Find All Duplicates in an Array
# Difficulty: Medium
# Recommended Approach: Negative Marking
# Recommended Current-Level Approach: Negative Marking

from typing import List


# Approach 1: Your Approach - Negative Marking
# Time Complexity: O(n)
# Array lo unna prathi element ni okkasari process chesthunnam.
# Space Complexity: O(1) Auxiliary
# result output ni exclude chesthe, additional data structure create cheyadam ledu.
class Solution1:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(len(nums)):
            index = abs(nums[i]) - 1

            if nums[index] < 0:
                result.append(index + 1)
            else:
                nums[index] = -nums[index]

        return result


# Approach 2: Cyclic Sort
# Time Complexity: O(n)
# Prathi number ni daani correct index ki move chesthunnam.
# Prathi element limited times mathrame swap avuthundi.
# Space Complexity: O(1) Auxiliary
# Input array ni in-place ga modify chesthunnam.
class Solution2:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        i = 0

        while i < len(nums):
            correct_index = nums[i] - 1

            if nums[i] != nums[correct_index]:
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
            else:
                i += 1

        for i in range(len(nums)):
            if nums[i] != i + 1:
                result.append(nums[i])

        return result


# Approach 3: HashSet
# Time Complexity: O(n)
# Prathi number ni set lo check chesi, taruvatha add chesthunnam.
# Space Complexity: O(n)
# Already vachina numbers ni seen set lo store chesthunnam.
class Solution3:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        seen = set()

        for i in range(len(nums)):
            if nums[i] in seen:
                result.append(nums[i])
            else:
                seen.add(nums[i])

        return result


# Approach 4: Frequency HashMap
# Time Complexity: O(n)
# Frequency dictionary create cheyadaniki mariyu counts check cheyadaniki O(n) time paduthundi.
# Space Complexity: O(n)
# Numbers mariyu vaati frequencies ni dictionary lo store chesthunnam.
class Solution4:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        frequency = {}

        for i in range(len(nums)):
            frequency[nums[i]] = frequency.get(nums[i], 0) + 1

        for number, count in frequency.items():
            if count == 2:
                result.append(number)

        return result


# Approach 5: Sorting and Adjacent Comparison
# Time Complexity: O(n log n)
# Sorting ki O(n log n), adjacent elements check cheyadaniki O(n) time paduthundi.
# Space Complexity: O(1) Auxiliary
# Python sort() input list ni in-place ga modify chesthundi.
# Internal sorting memory implementation meeda depend avuthundi.
class Solution5:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                result.append(nums[i])

        return result
