# LeetCode 80 - Remove Duplicates from Sorted Array II
# Difficulty: Medium

# Approach 1: Read / Write Pointer using write - 2
# Your Approach
# Recommended / Optimal Approach
# Time Complexity: O(n)
# Space Complexity: O(1)
def remove_duplicates_write_pointer(nums):
    if len(nums) <= 2:
        return len(nums)

    read = 2
    write = 2

    while read < len(nums):

        if nums[read] != nums[write - 2]:
            nums[write] = nums[read]
            write += 1

        read += 1

    return write


# Approach 2: Read / Write Pointer + Duplicate Count
# Time Complexity: O(n)
# Space Complexity: O(1)
def remove_duplicates_count(nums):
    if len(nums) <= 2:
        return len(nums)

    write = 1
    count = 1

    for read in range(1, len(nums)):

        if nums[read] == nums[read - 1]:
            count += 1
        else:
            count = 1

        if count <= 2:
            nums[write] = nums[read]
            write += 1

    return write


# Approach 3: Group Counting
# Count each consecutive group.
# Write at most 2 copies of every value.
# Time Complexity: O(n)
# Space Complexity: O(1)
def remove_duplicates_group_counting(nums):
    n = len(nums)

    read = 0
    write = 0

    while read < n:

        current = nums[read]
        count = 0

        while read < n and nums[read] == current:
            count += 1
            read += 1

        copies = min(count, 2)

        for _ in range(copies):
            nums[write] = current
            write += 1

    return write

# Approach 4: Extra List
# Easy to understand.
# Uses additional memory.
# Time Complexity: O(n)
# Space Complexity: O(n)
def remove_duplicates_extra_list(nums):
    result = []

    for num in nums:

        if len(result) < 2 or num != result[-2]:
            result.append(num)

    for i in range(len(result)):
        nums[i] = result[i]

    return len(result)


# Approach 5: Frequency Dictionary
# Count every number.
# Write each number at most twice.
# Time Complexity: O(n)
# Space Complexity: O(n)
def remove_duplicates_dictionary(nums):
    frequency = {}

    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1

    write = 0

    for num, count in frequency.items():

        copies = min(count, 2)

        for _ in range(copies):
            nums[write] = num
            write += 1

    return write


# Approach 6: Delete Extra Duplicates
# Python-specific brute-force approach.
# del shifts the remaining elements.
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def remove_duplicates_delete(nums):
    i = 2

    while i < len(nums):

        if nums[i] == nums[i - 1] == nums[i - 2]:
            del nums[i]

        else:
            i += 1

    return len(nums)
