# LeetCode 414 - Third Maximum Number
# Difficulty: Easy


# Approach 1: Set + Sorting
# Your Approach
# Time Complexity: O(n log n)
# Space Complexity: O(n)
def third_max_sort(nums):
    unique = sorted(set(nums), reverse=True)

    if len(unique) < 3:
        return unique[0]

    return unique[2]


# Approach 2: Remove Maximum Three Times
# Time Complexity: O(n)
# Space Complexity: O(n)
def third_max_remove(nums):
    unique = set(nums)

    if len(unique) < 3:
        return max(unique)

    first = max(unique)
    unique.remove(first)

    second = max(unique)
    unique.remove(second)

    return max(unique)


# Approach 3: Track Top Three Distinct Values
# Recommended Interview Solution
# Time Complexity: O(n)
# Space Complexity: O(1)
def third_max_tracking(nums):
    first = None
    second = None
    third = None

    for num in nums:
        if num == first or num == second or num == third:
            continue

        if first is None or num > first:
            third = second
            second = first
            first = num

        elif second is None or num > second:
            third = second
            second = num

        elif third is None or num > third:
            third = num

    if third is None:
        return first

    return third
