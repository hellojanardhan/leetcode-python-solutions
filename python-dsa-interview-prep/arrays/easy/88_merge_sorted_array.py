# LeetCode 88 - Merge Sorted Array
# Difficulty: Easy


# Approach 1: Copy + Manual Sorting
# Your Approach
# Time Complexity: O((m + n)^2)
# Space Complexity: O(1)
def merge_manual_sort(nums1, m, nums2, n):
    for i in range(n):
        nums1[m + i] = nums2[i]

    for i in range(len(nums1)):
        for j in range(i + 1, len(nums1)):
            if nums1[i] > nums1[j]:
                nums1[i], nums1[j] = nums1[j], nums1[i]


# Approach 2: Copy + Built-in sort()
# Time Complexity: O((m + n) log(m + n))
# Space Complexity: O(m + n) in Python's sorting implementation
def merge_sort(nums1, m, nums2, n):
    for i in range(n):
        nums1[m + i] = nums2[i]

    nums1.sort()


# Approach 3: Extra Array + Two Pointers
# Time Complexity: O(m + n)
# Space Complexity: O(m + n)
def merge_extra_array(nums1, m, nums2, n):
    result = []

    i = 0
    j = 0

    while i < m and j < n:
        if nums1[i] <= nums2[j]:
            result.append(nums1[i])
            i += 1
        else:
            result.append(nums2[j])
            j += 1

    while i < m:
        result.append(nums1[i])
        i += 1

    while j < n:
        result.append(nums2[j])
        j += 1

    nums1[:] = result


# Approach 4: Three Pointers From the End
# Recommended / Optimal Interview Solution
# Time Complexity: O(m + n)
# Space Complexity: O(1)
def merge_three_pointers(nums1, m, nums2, n):
    i = m - 1
    j = n - 1
    k = m + n - 1

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1

        k -= 1

    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1
