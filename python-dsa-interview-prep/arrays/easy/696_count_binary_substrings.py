# LeetCode 696 - Count Binary Substrings
# Difficulty: Easy


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: Nested While + Consecutive Group Counting
# Your Approach
# Recommended / Optimal Approach
# Time Complexity: O(n)
# Space Complexity: O(1)
def count_binary_substrings_group_counting(s):
    read = 0
    answer = 0
    previous_group_count = 0

    while read < len(s):
        count = 0
        current_char = s[read]

        while read < len(s) and s[read] == current_char:
            read += 1
            count += 1

        current_group_count = count

        answer += min(
            previous_group_count,
            current_group_count
        )

        previous_group_count = current_group_count

    return answer


# ============================================================


# Approach 2: Single Pass + Previous Run / Current Run
# No nested while
# Time Complexity: O(n)
# Space Complexity: O(1)
def count_binary_substrings_single_pass(s):
    previous_count = 0
    current_count = 1
    answer = 0

    for i in range(1, len(s)):

        if s[i] == s[i - 1]:
            current_count += 1

        else:
            answer += min(previous_count, current_count)

            previous_count = current_count
            current_count = 1

    answer += min(previous_count, current_count)

    return answer


# ============================================================


# Approach 3: Count While Scanning
# Add a valid substring whenever current group size
# does not exceed previous group size
# Time Complexity: O(n)
# Space Complexity: O(1)
def count_binary_substrings_running(s):
    previous_count = 0
    current_count = 1
    answer = 0

    for i in range(1, len(s)):

        if s[i] == s[i - 1]:
            current_count += 1

        else:
            previous_count = current_count
            current_count = 1

        if current_count <= previous_count:
            answer += 1

    return answer


# ============================================================
# REMAINING SOLUTIONS
# ============================================================


# Approach 4: Store All Group Sizes
# Easy to visualize
# Time Complexity: O(n)
# Space Complexity: O(n)
def count_binary_substrings_group_list(s):
    groups = []

    read = 0

    while read < len(s):
        current_char = s[read]
        count = 0

        while read < len(s) and s[read] == current_char:
            count += 1
            read += 1

        groups.append(count)

    answer = 0

    for i in range(1, len(groups)):
        answer += min(groups[i - 1], groups[i])

    return answer


# ============================================================


# Approach 5: itertools.groupby
# Pythonic Approach
# Time Complexity: O(n)
# Space Complexity: O(n)
def count_binary_substrings_groupby(s):
    from itertools import groupby

    groups = [
        sum(1 for _ in group)
        for _, group in groupby(s)
    ]

    answer = 0

    for i in range(1, len(groups)):
        answer += min(groups[i - 1], groups[i])

    return answer
