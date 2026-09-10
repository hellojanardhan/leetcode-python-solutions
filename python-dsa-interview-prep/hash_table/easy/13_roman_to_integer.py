# LeetCode 13 - Roman to Integer
# Difficulty: Easy
#
# Recommended Approach: Single Pass — Compare Current with Next
# Your Approach: Consume One Character or Subtraction Pair


# ============================================================
# Approach 1: Consume One Character or a Pair
# Your Approach — Cleaned
# Time Complexity: O(n)
# Space Complexity: O(1)
# ============================================================

class Solution1:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        result = 0
        current = 0
        next_index = 1

        while next_index < len(s):
            if values[s[current]] < values[s[next_index]]:
                result += (
                    values[s[next_index]]
                    - values[s[current]]
                )

                current += 2
                next_index += 2
            else:
                result += values[s[current]]

                current += 1
                next_index += 1

        if current < len(s):
            result += values[s[current]]

        return result


# ============================================================
# Approach 2: Compare Current Character with Next
# Recommended Approach
# Time Complexity: O(n)
# Space Complexity: O(1)
# ============================================================
#
# Current < Next ayithe current value subtract chestam.
# Otherwise current value add chestam.
# Final character ni loop tarvata add chestam.

class Solution2:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        result = 0

        for index in range(len(s) - 1):
            current = values[s[index]]
            next_value = values[s[index + 1]]

            if current < next_value:
                result -= current
            else:
                result += current

        result += values[s[-1]]

        return result


# ============================================================
# Approach 3: Traverse from Right to Left
# Time Complexity: O(n)
# Space Complexity: O(1)
# ============================================================
#
# Right-side character already process ayindi.
# Current value right-side value kante smaller ayithe subtract chestam.

class Solution3:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        result = values[s[-1]]

        for index in range(len(s) - 2, -1, -1):
            current = values[s[index]]
            right_value = values[s[index + 1]]

            if current < right_value:
                result -= current
            else:
                result += current

        return result
