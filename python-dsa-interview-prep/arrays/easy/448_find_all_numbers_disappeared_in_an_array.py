# LeetCode 448 - Find All Numbers Disappeared in an Array
# Difficulty: Easy
# Recommended Approach: Negative Marking
# Recommended Current-Level Approach: HashSet

from typing import List


# Approach 1: Negative Marking - Optimal Solution
# Time Complexity: O(n)
# Array ni rendu sarlu traverse chesthunnam. Kabatti total time O(n).
# Space Complexity: O(1) Auxiliary
# Input array ne marking kosam use chesthunnam. Additional set leda list create cheyadam ledu.
class Solution1:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(len(nums)):
            index = abs(nums[i]) - 1

            if nums[index] > 0:
                nums[index] = -nums[index]

        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)

        return result


# Approach 2: Your Approach - HashSet
# Time Complexity: O(n)
# Set create cheyadaniki O(n), 1 nunchi n varaku check cheyadaniki O(n) time paduthundi.
# Space Complexity: O(n)
# nums lo unna values ni seen set lo store chesthunnam.
class Solution2:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        seen = set(nums)

        for num in range(1, len(nums) + 1):
            if num not in seen:
                result.append(num)

        return result


# Approach 3: Boolean Array
# Time Complexity: O(n)
# nums values ni mark cheyadaniki O(n), missing values ni check cheyadaniki O(n) time paduthundi.
# Space Complexity: O(n)
# n positions unna boolean array ni additional ga create chesthunnam.
class Solution3:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        present = [False] * (len(nums) + 1)

        for i in range(len(nums)):
            present[nums[i]] = True

        for num in range(1, len(nums) + 1):
            if present[num] == False:
                result.append(num)

        return result


# Approach 4: Frequency HashMap
# Time Complexity: O(n)
# Frequency dictionary build cheyadaniki O(n), numbers check cheyadaniki O(n) time paduthundi.
# Space Complexity: O(n)
# Unique numbers mariyu vaati counts ni dictionary lo store chesthunnam.
class Solution4:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        frequency = {}

        for i in range(len(nums)):
            frequency[nums[i]] = frequency.get(nums[i], 0) + 1

        for num in range(1, len(nums) + 1):
            if frequency.get(num, 0) == 0:
                result.append(num)

        return result


# Approach 5: Cyclic Sort
# Time Complexity: O(n)
# Prathi number ni correct index ki move chesthunnam. Prathi value limited times mathrame move avuthundi.
# Space Complexity: O(1) Auxiliary
# Input array ni in-place ga modify chesthunnam. Additional data structure create cheyadam ledu.
class Solution5:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
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
                result.append(i + 1)

        return result
