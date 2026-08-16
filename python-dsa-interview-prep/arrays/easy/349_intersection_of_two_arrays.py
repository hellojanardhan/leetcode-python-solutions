# LeetCode 349 - Intersection of Two Arrays
# Difficulty: Easy


# Approach 1: Set Intersection
# Your Approach
# Time Complexity: O(n + m) average
# Space Complexity: O(n + m)
def intersection_set(nums1, nums2):
    result = set(nums1).intersection(set(nums2))
    return list(result)


# Approach 2: & Operator with Sets
# Time Complexity: O(n + m) average
# Space Complexity: O(n + m)
def intersection_set_operator(nums1, nums2):
    return list(set(nums1) & set(nums2))


# Approach 3: Hash Set + Loop
# Time Complexity: O(n + m) average
# Space Complexity: O(n + m)
def intersection_hashset(nums1, nums2):
    seen = set(nums1)
    result = set()

    for num in nums2:
        if num in seen:
            result.add(num)

    return list(result)


# Approach 4: Brute Force
# Time Complexity: O(n * m)
# Space Complexity: O(min(n, m))
def intersection_bruteforce(nums1, nums2):
    result = set()

    for num1 in nums1:
        for num2 in nums2:
            if num1 == num2:
                result.add(num1)

    return list(result)


# Approach 5: Sorting + Two Pointers
# Time Complexity: O(n log n + m log m)
# Space Complexity: O(n + m) worst case in Python sorting
def intersection_two_pointers(nums1, nums2):
    nums1.sort()
    nums2.sort()

    i = 0
    j = 0
    result = []

    while i < len(nums1) and j < len(nums2):

        if nums1[i] == nums2[j]:
            if not result or result[-1] != nums1[i]:
                result.append(nums1[i])

            i += 1
            j += 1

        elif nums1[i] < nums2[j]:
            i += 1

        else:
            j += 1

    return result
