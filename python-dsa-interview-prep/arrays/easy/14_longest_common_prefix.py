# LeetCode 14 - Longest Common Prefix
# Difficulty: Easy


# =========================================================
# Approach 1: Vertical Scanning
# Time Complexity: O(m * n)
# Space Complexity: O(1)
# =========================================================

def longest_common_prefix_vertical(strs):
    if not strs:
        return ""

    shortest = min(strs, key=len)
    result = ""

    for i in range(len(shortest)):

        for j in range(len(strs)):

            if shortest[i] != strs[j][i]:
                return result

        result += shortest[i]

    return result


# =========================================================
# Approach 2: Horizontal Scanning
# Time Complexity: O(total characters)
# Space Complexity: O(1)
# =========================================================

def longest_common_prefix_horizontal(strs):
    if not strs:
        return ""

    prefix = strs[0]

    for word in strs[1:]:

        while not word.startswith(prefix):

            prefix = prefix[:-1]

            if not prefix:
                return ""

    return prefix


# =========================================================
# Approach 3: Sorting + First and Last String
# Time Complexity: O(n log n * m)
# Space Complexity: Depends on sorting
# =========================================================

def longest_common_prefix_sorting(strs):
    if not strs:
        return ""

    strs.sort()

    first = strs[0]
    last = strs[-1]

    result = ""

    for i in range(min(len(first), len(last))):

        if first[i] != last[i]:
            break

        result += first[i]

    return result


# =========================================================
# Approach 4: zip() + set()
# Time Complexity: O(m * n)
# Space Complexity: O(m)
# =========================================================

def longest_common_prefix_zip(strs):
    if not strs:
        return ""

    result = ""

    for characters in zip(*strs):

        if len(set(characters)) == 1:
            result += characters[0]

        else:
            break

    return result


# =========================================================
# Approach 5: Divide and Conquer
# Time Complexity: O(total characters)
# Space Complexity: O(log n)
# =========================================================

def common_prefix(left, right):
    result = ""

    for i in range(min(len(left), len(right))):

        if left[i] != right[i]:
            break

        result += left[i]

    return result


def divide_and_conquer(strs, left, right):

    if left == right:
        return strs[left]

    mid = (left + right) // 2

    prefix1 = divide_and_conquer(strs, left, mid)
    prefix2 = divide_and_conquer(strs, mid + 1, right)

    return common_prefix(prefix1, prefix2)


def longest_common_prefix_divide(strs):
    if not strs:
        return ""

    return divide_and_conquer(strs, 0, len(strs) - 1)


# =========================================================
# Testing
# =========================================================

strs = ["flower", "flow", "flight"]

print(longest_common_prefix_vertical(strs.copy()))
print(longest_common_prefix_horizontal(strs.copy()))
print(longest_common_prefix_sorting(strs.copy()))
print(longest_common_prefix_zip(strs.copy()))
print(longest_common_prefix_divide(strs.copy()))
