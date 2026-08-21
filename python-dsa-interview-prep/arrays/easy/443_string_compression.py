# LeetCode 443 - String Compression
# Difficulty: Medium


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: Read / Write Pointer + Group Counting
# Your Current Approach
# Recommended / Optimal Approach
# Time Complexity: O(n)
# Space Complexity: O(1) in-place
def compress_read_write(chars):
    read = 0
    write = 0

    while read < len(chars):

        current_char = chars[read]
        count = 0

        # Count the current group
        while read < len(chars) and chars[read] == current_char:
            count += 1
            read += 1

        # Write the character
        chars[write] = current_char
        write += 1

        # Write count only when count > 1
        if count > 1:
            for digit in str(count):
                chars[write] = digit
                write += 1

    return write


# ============================================================


# Approach 2: For Loop + Adjacent Comparison + Write Pointer
# Closest to your earlier nums[i] == nums[i + 1] thinking
# Time Complexity: O(n)
# Space Complexity: O(1) in-place
def compress_adjacent(chars):
    if not chars:
        return 0

    write = 0
    count = 1

    for read in range(1, len(chars) + 1):

        # Still inside the same group
        if read < len(chars) and chars[read] == chars[read - 1]:
            count += 1

        # Group finished
        else:
            chars[write] = chars[read - 1]
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

            count = 1

    return write


# ============================================================


# Approach 3: Start / End Group Pointers
# Find the complete group first.
# count = end - start
# Time Complexity: O(n)
# Space Complexity: O(1) in-place
def compress_start_end(chars):
    start = 0
    write = 0
    n = len(chars)

    while start < n:

        end = start

        # Move end until the group finishes
        while end < n and chars[end] == chars[start]:
            end += 1

        count = end - start

        # Write group character
        chars[write] = chars[start]
        write += 1

        # Write group count
        if count > 1:
            for digit in str(count):
                chars[write] = digit
                write += 1

        # Move to next group
        start = end

    return write


# ============================================================
# REMAINING SOLUTIONS
# ============================================================


# Approach 4: Extra Result List
# Easiest to understand
# Not optimal because it uses extra memory
# Time Complexity: O(n)
# Space Complexity: O(n)
def compress_extra_list(chars):
    result = []

    read = 0

    while read < len(chars):

        current_char = chars[read]
        count = 0

        while read < len(chars) and chars[read] == current_char:
            count += 1
            read += 1

        result.append(current_char)

        if count > 1:
            result.extend(str(count))

    # Copy compressed result back
    for i in range(len(result)):
        chars[i] = result[i]

    return len(result)


# ============================================================


# Approach 5: itertools.groupby
# Pythonic approach
# Easy to write, but not preferred for interviews
# Time Complexity: O(n)
# Space Complexity: O(n) for compressed result
def compress_groupby(chars):
    from itertools import groupby

    result = []

    for char, group in groupby(chars):

        count = sum(1 for _ in group)

        result.append(char)

        if count > 1:
            result.extend(str(count))

    for i in range(len(result)):
        chars[i] = result[i]

    return len(result)


# ============================================================


# Approach 6: pop() / insert() Modification
# Brute-force Python approach
# Not recommended because pop/insert shift elements
# Time Complexity: O(n^2)
# Space Complexity: O(1) auxiliary
def compress_pop_insert(chars):
    i = 0

    while i < len(chars):

        j = i

        while j < len(chars) and chars[j] == chars[i]:
            j += 1

        count = j - i

        if count > 1:

            # Delete duplicate characters
            for _ in range(count - 1):
                chars.pop(i + 1)

            # Insert count digits
            digits = str(count)

            for offset, digit in enumerate(digits):
                chars.insert(i + 1 + offset, digit)

            i += 1 + len(digits)

        else:
            i += 1

    return len(chars)
