# LeetCode 1209 - Remove All Adjacent Duplicates in String II
# Difficulty: Medium


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: Stack + Character Count
# Recommended / Optimal Approach
# Time Complexity: O(n)
# Space Complexity: O(n)
def remove_duplicates_stack(s, k):
    stack = []

    for char in s:

        # Same as previous surviving character
        if stack and stack[-1][0] == char:
            stack[-1][1] += 1

            # Remove group when count reaches k
            if stack[-1][1] == k:
                stack.pop()

        else:
            # Start a new group
            stack.append([char, 1])

    return "".join(char * count for char, count in stack)


# ============================================================


# Approach 2: Read / Write Pointer + Count Array
# Best Pointer-Based Approach
# Time Complexity: O(n)
# Space Complexity: O(n)
def remove_duplicates_read_write(s, k):
    chars = list(s)
    counts = [0] * len(chars)

    write = 0

    for read in range(len(chars)):

        # Place current character
        chars[write] = chars[read]

        # Calculate consecutive count
        if write > 0 and chars[write] == chars[write - 1]:
            counts[write] = counts[write - 1] + 1
        else:
            counts[write] = 1

        # Current write position is filled
        write += 1

        # Remove last k characters
        if counts[write - 1] == k:
            write -= k

    return "".join(chars[:write])


# ============================================================


# Approach 3: Consecutive Group Counting + Stack
# Similar to the group-counting pattern
# you used in LeetCode 696 / 1446 / 443
# Time Complexity: O(n)
# Space Complexity: O(n)
def remove_duplicates_group_stack(s, k):
    stack = []

    read = 0

    while read < len(s):
        current_char = s[read]
        count = 0

        # Count current consecutive group
        while read < len(s) and s[read] == current_char:
            count += 1
            read += 1

        # Remove complete groups of k
        count %= k

        if count == 0:
            continue

        # Merge with previous surviving group
        if stack and stack[-1][0] == current_char:
            new_count = stack[-1][1] + count

            new_count %= k

            if new_count == 0:
                stack.pop()
            else:
                stack[-1][1] = new_count

        else:
            stack.append([current_char, count])

    return "".join(char * count for char, count in stack)


# ============================================================
# REMAINING SOLUTIONS
# ============================================================


# Approach 4: Repeated Group Scan
# Scan all groups, remove groups of k,
# and repeat because removals may create new groups.
# Time Complexity: O(n^2) worst case
# Space Complexity: O(n)
def remove_duplicates_repeated_scan(s, k):

    while True:
        read = 0
        result = []
        changed = False

        while read < len(s):
            current_char = s[read]
            count = 0

            # Count current group
            while read < len(s) and s[read] == current_char:
                count += 1
                read += 1

            # Remove complete groups of k
            remaining = count % k

            if remaining != count:
                changed = True

            result.append(current_char * remaining)

        new_s = "".join(result)

        # No more removals
        if not changed:
            return new_s

        s = new_s


# ============================================================


# Approach 5: Regular Expression + Repeated Removal
# Python-specific approach
# Not recommended for interviews
# Time Complexity: O(n^2) worst case
# Space Complexity: O(n)
def remove_duplicates_regex(s, k):
    import re

    # Example for k = 3:
    # (.)\1{2}
    # means same character repeated 3 times
    pattern = re.compile(r"(.)\1{" + str(k - 1) + r"}")

    while True:
        new_s = pattern.sub("", s)

        if new_s == s:
            return s

        s = new_s


# ============================================================


# Approach 6: Recursive Brute Force
# Find a group with at least k characters,
# remove k characters, and restart.
# Time Complexity: O(n^2) worst case
# Space Complexity: O(n^2) worst case due to recursion/string copies
def remove_duplicates_recursive(s, k):
    read = 0

    while read < len(s):
        end = read

        while end < len(s) and s[end] == s[read]:
            end += 1

        count = end - read

        if count >= k:

            # Remove exactly k characters
            new_s = s[:read] + s[read + k:]

            return remove_duplicates_recursive(new_s, k)

        read = end

    return s
