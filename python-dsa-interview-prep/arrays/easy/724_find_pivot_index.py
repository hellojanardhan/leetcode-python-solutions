# LeetCode 724 - Find Pivot Index
# Difficulty: Easy


# Approach 1: Slicing + sum()
# Your Approach
# Time Complexity: O(n^2)
# Space Complexity: O(n)
def pivot_index_slicing(nums):
    for i in range(len(nums)):
        if sum(nums[:i]) == sum(nums[i + 1:]):
            return i

    return -1


# Approach 2: Total Sum + Left Sum
# Recommended / Optimal
# Time Complexity: O(n)
# Space Complexity: O(1)
def pivot_index_total_sum(nums):
    total = sum(nums)
    left_sum = 0

    for i, num in enumerate(nums):
        right_sum = total - left_sum - num

        if left_sum == right_sum:
            return i

        left_sum += num

    return -1


# Approach 3: Prefix Sum Array
# Time Complexity: O(n)
# Space Complexity: O(n)
def pivot_index_prefix(nums):
    prefix = [0]

    for num in nums:
        prefix.append(prefix[-1] + num)

    total = prefix[-1]

    for i in range(len(nums)):
        left_sum = prefix[i]
        right_sum = total - prefix[i + 1]

        if left_sum == right_sum:
            return i

    return -1


# Approach 4: Running Left Sum Using Formula
# Time Complexity: O(n)
# Space Complexity: O(1)
def pivot_index_formula(nums):
    total = sum(nums)
    left_sum = 0

    for i in range(len(nums)):
        if left_sum == total - left_sum - nums[i]:
            return i

        left_sum += nums[i]

    return -1
