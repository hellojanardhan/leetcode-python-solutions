# LeetCode 136 - Single Number
# Difficulty: Easy


# Approach 1: count()
# Your Approach
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def single_number_count(nums):
    for num in nums:
        if nums.count(num) == 1:
            return num


# Approach 2: Sorting + Adjacent Comparison
# Time Complexity: O(n log n)
# Space Complexity: O(n) worst case in Python sorting
def single_number_sort(nums):
    nums.sort()

    for i in range(0, len(nums) - 1, 2):
        if nums[i] != nums[i + 1]:
            return nums[i]

    return nums[-1]


# Approach 3: Hash Set
# Time Complexity: O(n) average
# Space Complexity: O(n)
def single_number_set(nums):
    seen = set()

    for num in nums:
        if num in seen:
            seen.remove(num)
        else:
            seen.add(num)

    return seen.pop()


# Approach 4: Mathematical Set Formula
# Time Complexity: O(n)
# Space Complexity: O(n)
def single_number_math(nums):
    return 2 * sum(set(nums)) - sum(nums)


# Approach 5: Dictionary / Frequency Count
# Time Complexity: O(n)
# Space Complexity: O(n)
def single_number_dictionary(nums):
    frequency = {}

    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1

    for num, count in frequency.items():
        if count == 1:
            return num


# Approach 6: XOR
# Recommended / Optimal Interview Solution
# Time Complexity: O(n)
# Space Complexity: O(1)
def single_number_xor(nums):
    result = 0

    for num in nums:
        result ^= num

    return result
