# LeetCode 217 - Contains Duplicate
# Difficulty: Easy


# Approach 1: Sorting + Adjacent Comparison
# Your Approach - Simplified
# Time Complexity: O(n log n)
# Space Complexity: O(n) worst case in Python
def contains_duplicate_sort(nums):
    nums.sort()

    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True

    return False


# Approach 2: Hash Set
# Recommended Interview Solution
# Time Complexity: O(n) average
# Space Complexity: O(n)
def contains_duplicate_set(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True

        seen.add(num)

    return False


# Approach 3: Set Length Comparison
# Pythonic Solution
# Time Complexity: O(n) average
# Space Complexity: O(n)
def contains_duplicate_set_length(nums):
    return len(nums) != len(set(nums))


# Approach 4: Dictionary / Frequency Tracking
# Time Complexity: O(n) average
# Space Complexity: O(n)
def contains_duplicate_dictionary(nums):
    frequency = {}

    for num in nums:
        if num in frequency:
            return True

        frequency[num] = 1

    return False


# Approach 5: Brute Force
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def contains_duplicate_bruteforce(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True

    return False
