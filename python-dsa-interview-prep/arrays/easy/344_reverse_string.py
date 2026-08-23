# LeetCode 344 - Reverse String
# Difficulty: Easy


# Approach 1: Two Pointers
# Your Approach - Recommended / Optimal
# Time Complexity: O(n)
# Space Complexity: O(1)
def reverse_string_two_pointers(s):
    left = 0
    right = len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


# Approach 2: Two Pointers Using for Loop
# Time Complexity: O(n)
# Space Complexity: O(1)
def reverse_string_for_loop(s):
    n = len(s)

    for i in range(n // 2):
        j = n - 1 - i
        s[i], s[j] = s[j], s[i]


# Approach 3: Built-in reverse()
# Time Complexity: O(n)
# Space Complexity: O(1)
def reverse_string_builtin(s):
    s.reverse()


# Approach 4: Slice Assignment
# Time Complexity: O(n)
# Space Complexity: O(n)
def reverse_string_slicing(s):
    s[:] = s[::-1]


# Approach 5: Manual Copy + Reverse Write
# Time Complexity: O(n)
# Space Complexity: O(n)
def reverse_string_extra_space(s):
    copied = s[:]

    for i in range(len(s)):
        s[i] = copied[len(s) - 1 - i]
