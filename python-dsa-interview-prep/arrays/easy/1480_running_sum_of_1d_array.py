# LeetCode 1480 - Running Sum of 1d Array
# Difficulty: Easy


# Approach 1: Slicing + sum()
# Your Solution
# Time Complexity: O(n^2)
# Space Complexity: O(n)
def running_sum_slice(nums):
    result = []

    for i in range(len(nums)):
        result.append(sum(nums[:i + 1]))

    return result


# Approach 2: Running Total / Prefix Sum
# Recommended Interview Solution
# Time Complexity: O(n)
# Space Complexity: O(n)
def running_sum_prefix(nums):
    result = []
    total = 0

    for num in nums:
        total += num
        result.append(total)

    return result


# Approach 3: Use Previous Result
# Time Complexity: O(n)
# Space Complexity: O(n)
def running_sum_previous(nums):
    result = [nums[0]]

    for i in range(1, len(nums)):
        result.append(result[i - 1] + nums[i])

    return result


# Approach 4: In-place Prefix Sum
# Time Complexity: O(n)
# Auxiliary Space Complexity: O(1)
# Note: Modifies the original input list.
def running_sum_inplace(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]

    return nums


# Approach 5: itertools.accumulate()
# Time Complexity: O(n)
# Space Complexity: O(n)
from itertools import accumulate


def running_sum_accumulate(nums):
    return list(accumulate(nums))
