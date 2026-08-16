# LeetCode 26 - Remove Duplicates from Sorted Array
# Difficulty: Easy


# Approach 1: Your Approach - Compare Current and Next Element
# Time Complexity: O(n)
# Space Complexity: O(1)
def remove_duplicates_next(nums):
    k = 1

    for i in range(len(nums) - 1):
        if nums[i + 1] != nums[i]:
            nums[k] = nums[i + 1]
            k += 1

    return k


# Approach 2: Two Pointers - Compare with Last Unique Element
# Recommended Interview Solution
# Time Complexity: O(n)
# Space Complexity: O(1)
def remove_duplicates_two_pointers(nums):
    k = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[k - 1]:
            nums[k] = nums[i]
            k += 1

    return k


# Approach 3: Read Pointer + Write Pointer
# Time Complexity: O(n)
# Space Complexity: O(1)
def remove_duplicates_read_write(nums):
    write = 1

    for read in range(1, len(nums)):
        if nums[read] != nums[read - 1]:
            nums[write] = nums[read]
            write += 1

    return write


# Approach 4: While Loop
# Time Complexity: O(n)
# Space Complexity: O(1)
def remove_duplicates_while(nums):
    k = 1
    i = 1

    while i < len(nums):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1

        i += 1

    return k


# Approach 5: Python List Slice Assignment
# Python-specific, not preferred for interviews
# Time Complexity: O(n)
# Space Complexity: O(n)
def remove_duplicates_pythonic(nums):
    unique = list(dict.fromkeys(nums))
    nums[:len(unique)] = unique

    return len(unique)
