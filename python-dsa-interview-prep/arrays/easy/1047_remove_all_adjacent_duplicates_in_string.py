# LeetCode 1047 - Remove All Adjacent Duplicates In String
# Difficulty: Easy


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: Simple Stack
# Recommended / Optimal Approach
# Time Complexity: O(n)
# Space Complexity: O(n)
def remove_duplicates_stack(s):
    stack = []

    for char in s:

        if stack and stack[-1] == char:
            stack.pop()

        else:
            stack.append(char)

    return "".join(stack)


# ============================================================


# Approach 2: Stack + Character Count
# Your Approach
# Time Complexity: O(n)
# Space Complexity: O(n)
def remove_duplicates_stack_count(s):
    stack = []

    for char in s:

        if stack and stack[-1][0] == char:
            stack[-1][1] += 1

            if stack[-1][1] > 1:
                stack.pop()

        else:
            stack.append([char, 1])

    return "".join(char for char, count in stack)


# ============================================================


# Approach 3: Read / Write Pointer
# Use a list as a mutable character array
# Time Complexity: O(n)
# Space Complexity: O(n) because string is converted to list
def remove_duplicates_read_write(s):
    chars = list(s)

    write = 0

    for read in range(len(chars)):

        if write > 0 and chars[write - 1] == chars[read]:
            write -= 1

        else:
            chars[write] = chars[read]
            write += 1

    return "".join(chars[:write])


# ============================================================
# REMAINING SOLUTIONS
# ============================================================


# Approach 4: Repeated String Replacement
# Brute-force style
# Time Complexity: O(n^2) worst case
# Space Complexity: O(n)
def remove_duplicates_repeated(s):

    changed = True

    while changed:
        changed = False
        result = []

        i = 0

        while i < len(s):

            if i + 1 < len(s) and s[i] == s[i + 1]:
                i += 2
                changed = True

            else:
                result.append(s[i])
                i += 1

        s = "".join(result)

    return s


# ============================================================


# Approach 5: Recursive Removal
# Not recommended
# Time Complexity: O(n^2) worst case
# Space Complexity: O(n) or more because of recursion/string copies
def remove_duplicates_recursive(s):

    for i in range(len(s) - 1):

        if s[i] == s[i + 1]:
            new_s = s[:i] + s[i + 2:]

            return remove_duplicates_recursive(new_s)

    return s
