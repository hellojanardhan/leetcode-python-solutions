# LeetCode 125 - Valid Palindrome
# Difficulty: Easy


# Approach 1: Clean String + Reverse Using Two Pointers
# Your Approach
# Time Complexity: O(n)
# Space Complexity: O(n)
def is_palindrome_reverse(s):
    converted_string = "".join(
        char for char in s.lower()
        if char.isalnum()
    )

    comp = list(converted_string)

    left = 0
    right = len(comp) - 1

    while left < right:
        comp[left], comp[right] = comp[right], comp[left]
        left += 1
        right -= 1

    reversed_string = "".join(comp)

    return reversed_string == converted_string


# Approach 2: Clean String + Slicing
# Simple Python Approach
# Time Complexity: O(n)
# Space Complexity: O(n)
def is_palindrome_slicing(s):
    converted_string = "".join(
        char for char in s.lower()
        if char.isalnum()
    )

    return converted_string == converted_string[::-1]


# Approach 3: Two Pointers Directly on Original String
# Recommended Interview Solution
# Time Complexity: O(n)
# Space Complexity: O(1)
def is_palindrome_two_pointers(s):
    left = 0
    right = len(s) - 1

    while left < right:

        while left < right and not s[left].isalnum():
            left += 1

        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


# Approach 4: Clean List + Two Pointer Comparison
# No Need to Reverse Entire List
# Time Complexity: O(n)
# Space Complexity: O(n)
def is_palindrome_clean_two_pointers(s):
    chars = [
        char.lower()
        for char in s
        if char.isalnum()
    ]

    left = 0
    right = len(chars) - 1

    while left < right:
        if chars[left] != chars[right]:
            return False

        left += 1
        right -= 1

    return True
