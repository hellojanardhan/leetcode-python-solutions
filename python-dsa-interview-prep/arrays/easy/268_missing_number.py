# LeetCode 268 - Missing Number
# Difficulty: Easy


# Approach 1: Your Approach - Sorting + Membership Check
# Time Complexity: O(n^2)
# Space Complexity: O(n) worst case in Python sorting
def missing_number_membership(nums):
    nums.sort()

    for num in range(len(nums)):
        if num not in nums:
            return num

    return nums[-1] + 1


# Approach 2: Sorting + Index Comparison
# Time Complexity: O(n log n)
# Space Complexity: O(n) worst case in Python sorting
def missing_number_sort(nums):
    nums.sort()

    for i in range(len(nums)):
        if nums[i] != i:
            return i

    return len(nums)


# Approach 3: Hash Set
# Time Complexity: O(n) average
# Space Complexity: O(n)
def missing_number_set(nums):
    numbers = set(nums)

    for num in range(len(nums) + 1):
        if num not in numbers:
            return num


# Approach 4: Mathematical Sum Formula
# Recommended Simple Solution
# Time Complexity: O(n)
# Space Complexity: O(1)
def missing_number_sum(nums):
    n = len(nums)

    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)

    return expected_sum - actual_sum


# Approach 5: XOR
# Recommended Interview / DSA Solution
# Time Complexity: O(n)
# Space Complexity: O(1)
def missing_number_xor(nums):
    missing = len(nums)

    for i, num in enumerate(nums):
        missing ^= i
        missing ^= num

    return missing
