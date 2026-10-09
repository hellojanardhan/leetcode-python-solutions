# LeetCode 917 - Reverse Only Letters
# Difficulty: Easy

# Recommended Optimal Approach: Two Pointers
# Recommended Current-Level Approach: Two Pointers
#
# n = length of the string
#
# We use two pointers:
# left  -> starts from the beginning
# right -> starts from the end
#
# Only letters are reversed.
# Non-letter characters remain in their original positions.
#
# LeetCode Topics:
# String
# Two Pointers


# ============================================================
# TOP APPROACHES
# ============================================================


# Approach 1: Two Pointers
# Your Approach
# Recommended Optimal and Current-Level Approach
#
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Time Explanation:
# left pointer left nundi right side ki move avutundi.
# right pointer right nundi left side ki move avutundi.
#
# Each character ni maximum constant number of times check chestham.
# Therefore, two-pointer traversal O(n).
#
# Final "".join(s) kuda O(n).
#
# Overall Time Complexity = O(n).
#
# Space Explanation:
# Python strings immutable kabatti:
#
# s = list(s)
#
# ani convert chestham.
#
# Character list lo n characters store avutayi.
# Therefore, extra space O(n).
#
# left and right variables O(1) space use chestayi.
#
# Overall Space Complexity = O(n).
#
# Logic:
# 1. Both left and right are letters:
#       Swap them.
#       Move both pointers.
#
# 2. Left is not a letter:
#       Left character ni touch cheyyamu.
#       Only left pointer ni move chestham.
#
# 3. Right is not a letter:
#       Right character ni touch cheyyamu.
#       Only right pointer ni move chestham.
#
# This way non-letter characters original positions lo remain avutayi.


class Solution1:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)

        left = 0
        right = len(s) - 1

        while left <= right:

            if s[left].isalpha() and s[right].isalpha():
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

            elif not s[left].isalpha():
                left += 1

            elif not s[right].isalpha():
                right -= 1

        return "".join(s)


# ============================================================
# APPROACH 1 - DETAILED EXPLANATION
# ============================================================

# Example:
#
# s = "a-bC-dEf-ghIj"
#
# We need to reverse only the letters.
#
# Original:
#
# a - b C - d E f - g h I j
# ↑                           ↑
# left                       right
#
# Both 'a' and 'j' are letters.
# So swap:
#
# j - b C - d E f - g h I a
#
# Then:
# left += 1
# right -= 1
#
#
# If left points to a non-letter:
#
# Example:
#
# a - b
#   ↑
#   -
#
# '-' should not move.
# Therefore:
#
# left += 1
#
#
# If right points to a non-letter:
#
# a - b
#   ↑
#   -
#       ↑
#       right
#
# '-' should not move.
# Therefore:
#
# right -= 1
#
#
# Continue until left > right.


# ============================================================
# WHY WE USE list(s)
# ============================================================

# Python strings are immutable.
#
# We cannot directly modify:
#
# s[left] = ...
#
# when s is a string.
#
# Therefore:
#
# s = list(s)
#
# converts:
#
# "a-bC-d"
#
# into:
#
# ['a', '-', 'b', 'C', '-', 'd']
#
# Now characters can be swapped in-place.


# ============================================================
# WHY NON-LETTERS STAY IN THEIR POSITIONS
# ============================================================

# Example:
#
# Input:
# "a-b"
#
# left  -> 'a'
# right -> 'b'
#
# Both are letters, so swap:
#
# "b-a"
#
# '-' remains at index 1.
#
#
# Example:
#
# Input:
# "a-!b"
#
# Letters:
# a, b
#
# Non-letters:
# -, !
#
# Only a and b are swapped.
#
# Output:
# "b-!a"
#
# '-' and '!' remain in the same positions.


# ============================================================
# DRY RUN
# ============================================================

# Input:
# "a-bC-dEf-ghIj"
#
# left = 0
# right = len(s) - 1
#
# Step 1:
# left  -> 'a'
# right -> 'j'
#
# Both are letters:
# swap
#
# Step 2:
# Move both pointers.
#
# If left or right points to '-':
# skip that character by moving only the corresponding pointer.
#
# Continue until:
#
# left > right
#
# Final:
# "j-Ih-gfE-dCba"


# ============================================================
# IMPORTANT EDGE CASES
# ============================================================

# 1. All letters
#
# Input:
# "abcd"
#
# Output:
# "dcba"
#
#
# 2. No letters
#
# Input:
# "123-!"
#
# Output:
# "123-!"
#
#
# 3. One character
#
# Input:
# "a"
#
# Output:
# "a"
#
#
# 4. Letters with one non-letter
OBOBOBOBOBOB#
# Input:
# "a-b"
#
# Output:
OBOBOB# "b-a"
#
#
# 5. Multiple non-letters
#
OBOBOB# Input:
# "a-!b"
#
OBOBOB# Output:
# "b-!a"
#
#
# 6. Non-letters on both sides
OBOBOB#
# Input:
# "-a-b-"
#
# Output:
# "-b-a-"


# ============================================================
# OTHER POSSIBLE SOLUTIONS
# ============================================================


# Approach 2: Extract Letters + Reverse
# Alternative Approach
#
# Logic:
# 1. Extract all letters from the string.
# 2. Reverse the letters.
# 3. Traverse the original string.
OBOBOB# 4. Replace only letter positions with reversed letters.
#
OBOBOB# Example:
#
# Input:
# "a-bC-d"
OBOBOB#
# Extracted letters:
# ['a', 'b', 'C', 'd']
OBOBOB#
# Reverse:
# ['d', 'C', 'b', 'a']
#
OBOBOB# Put them back only at letter positions.
OBOBOB#
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# This works correctly, but Two Pointers is better because
# it directly processes the letters from both ends without
# maintaining a separate collection of letters.


class Solution2:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)

        letters = []

OBOBOB        for char in s:
OBOBOBOBOBOB            if char.isalpha():
                letters.append(char)
OBOBOB
        letters.reverse()

OBOBOB        index = 0

        for i in range(len(s)):
            if s[i].isalpha():
                s[i] = letters[index]
                index += 1

        return "".join(s)


# ============================================================
# APPROACH COMPARISON
# ============================================================

OBOBOB# Approach 1: Two Pointers
OBOBOB#
OBOBOBOBOBOBOBOBOB# Time:  O(n)
# Space: O(n)
#
# Advantages:
# - Directly solves the problem.
# - Simple interview pattern.
# - No separate collection of letters.
# - Uses opposite-direction two pointers.
#
# Recommended for interview:
# YES
#
#
# Approach 2: Extract + Reverse
#
# Time:  O(n)
# Space: O(n)
#
# Advantages:
# - Easy to understand.
# - Separates letter extraction and replacement.
#
# Disadvantages:
# - Requires an additional letters list.
# - More operations than the two-pointer approach.
#
# Recommended for interview:
# Good alternative, but Approach 1 is preferable.


# ============================================================
# PATTERN SUMMARY
# ============================================================

# Pattern:
# Two Pointers - Opposite Direction
#
#
# Recognition:
#
# Use this pattern when:
# - We need to process elements from both ends.
# - We need to reverse selected elements.
# - Some elements should be skipped.
# - Some elements must remain in their original positions.
#
#
# General Mental Template:
#
# left = 0
# right = len(arr) - 1
#
# while left <= right:
#
#     if both elements are valid:
#         process / swap
#         left += 1
#         right -= 1
#
#     elif left element is invalid:
#         left += 1
#
#     elif right element is invalid:
#         right -= 1
#
#
# Core Mental Model:
#
# Both valid:
#     -> process both
#
# Left invalid:
#     -> skip left
#
# Right invalid:
#     -> skip right
#
#
# Key Takeaway:
#
# If an element should remain in its original position,
# don't move the element.
# Move the pointer instead.


# ============================================================
# INTERVIEW ANSWER
# ============================================================

# "I use two pointers, one from the beginning and one from the end.
# If both pointers point to letters, I swap them and move both
# pointers. If either pointer points to a non-letter, I move only
# that pointer. This ensures that non-letter characters remain in
# their original positions. The time complexity is O(n), and the
# space complexity is O(n) because I convert the string into a list."
