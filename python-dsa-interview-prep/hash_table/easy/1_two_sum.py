# LeetCode 1 - Two Sum
# Difficulty: Easy
# Recommended Approach: One-Pass HashMap
# Recommended Current-Level Approach: One-Pass HashMap


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: One-Pass HashMap
# Your Approach
# Recommended Optimal Approach
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Time Explanation:
# Array lo prati number ni maximum okasari traverse chestunnam.
# Dictionary lookup mariyu insertion average-ga O(1).
# Kabatti total time complexity O(n).
#
# Space Explanation:
# Worst case lo n numbers and indices dictionary lo store avvachu.
# Kabatti auxiliary space complexity O(n).
#
# Logic:
# Current number ki required complement calculate chestunnam.
#
# complement = target - current_number
#
# Complement already dictionary lo unte,
# previous complement index mariyu current index return chestunnam.
#
# Dictionary structure:
# number -> index
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index in range(len(nums)):
            complement = target - nums[index]

            if complement in seen:
                return [seen[complement], index]

            seen[nums[index]] = index


# ============================================================


# Approach 2: Brute Force - Nested Loops
# Basic Approach
# Time Complexity: O(n^2)
# Space Complexity: O(1)
#
# Time Explanation:
# Prati number ni dani tarvata unna prati number tho compare chestunnam.
# Outer loop O(n), inner loop worst case O(n).
# Kabatti total time complexity O(n^2).
#
# Space Explanation:
# Additional dictionary, set ledaa list create cheyadam ledu.
# Loop variables maatrame use chestunnam.
# Kabatti auxiliary space complexity O(1).
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for first_index in range(len(nums)):
            for second_index in range(
                first_index + 1,
                len(nums)
            ):
                if (
                    nums[first_index] + nums[second_index]
                    == target
                ):
                    return [first_index, second_index]


# ============================================================


# Approach 3: Two-Pass HashMap
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Time Explanation:
# First loop lo numbers and indices dictionary lo store chestunnam.
# Second loop lo prati number complement ni check chestunnam.
# O(n) + O(n) = O(2n), simplified-ga O(n).
#
# Space Explanation:
# Worst case lo n numbers and indices dictionary lo store avvachu.
# Kabatti auxiliary space complexity O(n).
#
# Important:
# Complement index current index tho equal kakunda check cheyali.
# Endukante same array element ni rendu saarlu use cheyakudadu.
class Solution3:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for index, number in enumerate(nums):
            indices[number] = index

        for index, number in enumerate(nums):
            complement = target - number

            if (
                complement in indices
                and indices[complement] != index
            ):
                return [index, indices[complement]]


# ============================================================
# OTHER POSSIBLE SOLUTIONS
# ============================================================


# Approach 4: Sorting + Two Pointers
# Time Complexity: O(n log n)
# Space Complexity: O(n)
#
# Time Explanation:
# Number and original index pairs create cheyadaniki O(n).
# Pairs ni sort cheyadaniki O(n log n).
# Two pointers tho array ni traverse cheyadaniki O(n).
# Kabatti total time complexity O(n log n).
#
# Space Explanation:
# Original indices preserve cheyadaniki n pairs create chestunnam.
# Kabatti auxiliary space complexity O(n).
#
# Logic:
# Current sum target kante thakkuva ayite left pointer move chestam.
# Current sum target kante ekkuva ayite right pointer move chestam.
# Target ki equal ayite original indices return chestam.
class Solution4:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexed_numbers = [
            (number, index)
            for index, number in enumerate(nums)
        ]

        indexed_numbers.sort()

        left = 0
        right = len(indexed_numbers) - 1

        while left < right:
            left_number = indexed_numbers[left][0]
            right_number = indexed_numbers[right][0]

            current_sum = left_number + right_number

            if current_sum == target:
                left_index = indexed_numbers[left][1]
                right_index = indexed_numbers[right][1]

                return [left_index, right_index]

            if current_sum < target:
                left += 1
            else:
                right -= 1


# ============================================================


# Approach 5: One-Pass HashMap Using enumerate()
# Short Recommended Version
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Time Explanation:
# enumerate() current index mariyu number direct-ga istundi.
# Array lo prati number ni maximum okasari process chestunnam.
# Dictionary operations average-ga O(1).
# Kabatti total time complexity O(n).
#
# Space Explanation:
# Worst case lo n number-index pairs dictionary lo store avutayi.
# Kabatti auxiliary space complexity O(n).
#
# Note:
# Idi Approach 1 ki same logic.
# enumerate() use cheyadam valla nums[index] repeatedly access cheyalsina
# avasaram undadu.
class Solution5:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for current_index, current_number in enumerate(nums):
            complement = target - current_number

            if complement in seen:
                return [seen[complement], current_index]

            seen[current_number] = current_index
