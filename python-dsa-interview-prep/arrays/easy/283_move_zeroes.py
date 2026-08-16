# LeetCode 283 - Move Zeroes
# Difficulty: Easy


# Approach 1: Nested Loop + Swap
# Your Approach - Improved
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def move_zeroes_nested(nums):
    for i in range(len(nums)):
        if nums[i] == 0:
            for j in range(i + 1, len(nums)):
                if nums[j] != 0:
                    nums[i], nums[j] = nums[j], nums[i]
                    break


# Approach 2: Two Pointers + Swap
# Recommended Interview Solution
# Time Complexity: O(n)
# Space Complexity: O(1)
def move_zeroes_two_pointers(nums):
    k = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[k], nums[i] = nums[i], nums[k]
            k += 1


# Approach 3: Overwrite Non-Zero Elements + Fill Zeroes
# Time Complexity: O(n)
# Space Complexity: O(1)
def move_zeroes_overwrite(nums):
    k = 0

    for num in nums:
        if num != 0:
            nums[k] = num
            k += 1

    while k < len(nums):
        nums[k] = 0
        k += 1


# Approach 4: Python Slice Assignment
# Time Complexity: O(n)
# Space Complexity: O(n)
# Python-specific; not preferred for interviews
def move_zeroes_pythonic(nums):
    non_zero = [num for num in nums if num != 0]
    nums[:] = non_zero + [0] * (len(nums) - len(non_zero))
