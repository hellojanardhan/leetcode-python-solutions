# LeetCode 35 - Search Insert Position
# Difficulty: Easy
# Recommended Approach: Iterative Binary Search
# Recommended Current-Level Approach: Iterative Binary Search

from typing import List


# Approach 1: Your Approach - Iterative Binary Search
# Time Complexity: O(log n)
# Prathi iteration lo search space ni half chesthunnam.
# Anduvalla time complexity O(log n).
# Space Complexity: O(1)
# left, right, mid ane variables mathrame use chesthunnam.
class Solution1:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if target > nums[mid]:
                left = mid + 1

            elif target < nums[mid]:
                right = mid - 1

            else:
                return mid

        return left


# Approach 2: Half-Open Binary Search
# Time Complexity: O(log n)
# Prathi iteration lo search range ni half chesthunnam.
# Anduvalla time complexity O(log n).
# Space Complexity: O(1)
# Konni index variables mathrame use chesthunnam.
class Solution2:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)

        while left < right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        return left


# Approach 3: bisect_left()
# Time Complexity: O(log n)
# bisect_left binary search ni use chesi target position ni
# O(log n) time lo find chesthundi.
# Space Complexity: O(1)
# Additional list leda data structure create cheyadam ledu.
class Solution3:
    def searchInsert(self, nums: List[int], target: int) -> int:
        from bisect import bisect_left

        return bisect_left(nums, target)


# Approach 4: Linear Search
# Time Complexity: O(n)
# Worst case lo list lo unna anni n elements ni check chestham.
# Anduvalla time complexity O(n).
# Space Complexity: O(1)
# index variable mathrame use chesthunnam.
class Solution4:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for index in range(len(nums)):
            if nums[index] >= target:
                return index

        return len(nums)


# Approach 5: Recursive Binary Search
# Time Complexity: O(log n)
# Prathi recursive call lo search space ni half chesthunnam.
# Anduvalla time complexity O(log n).
# Space Complexity: O(log n)
# Recursive calls call stack lo store avuthayi.
# Anduvalla space complexity O(log n).
class Solution5:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def binary_search(left, right):
            if left > right:
                return left

            mid = (left + right) // 2

            if target > nums[mid]:
                return binary_search(mid + 1, right)

            elif target < nums[mid]:
                return binary_search(left, mid - 1)

            return mid

        return binary_search(0, len(nums) - 1)
