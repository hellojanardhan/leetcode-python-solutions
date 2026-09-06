# LeetCode 1796 - Second Largest Digit in a String
# Difficulty: Easy
#
# Recommended Optimal Approach: One Pass + Two Variables
# Recommended Current-Level Approach: HashSet + Two Variables


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: HashSet + Two Maximum Variables
# Your Approach
#
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Set lo maximum 10 digits మాత్రమే ఉంటాయి: 0–9.
# Input size పెరిగినా set size 10 కంటే పెరగదు.

class Solution1:
    def secondHighest(self, s: str) -> int:
        digits = set()

        for character in s:
            if character.isdigit():
                digits.add(int(character))

        first_maximum = -1
        second_maximum = -1

        for digit in digits:
            if digit > first_maximum:
                second_maximum = first_maximum
                first_maximum = digit

            elif digit > second_maximum:
                second_maximum = digit

        return second_maximum


# ============================================================
# Approach 2: One Pass + Two Maximum Variables
# Recommended Optimal Approach
#
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Set create చేయకుండా string traverse చేస్తున్నాం.
# first > digit check వల్ల distinct digit మాత్రమే
# second maximum అవుతుంది.

class Solution2:
    def secondHighest(self, s: str) -> int:
        first_maximum = -1
        second_maximum = -1

        for character in s:
            if not character.isdigit():
                continue

            digit = int(character)

            if digit > first_maximum:
                second_maximum = first_maximum
                first_maximum = digit

            elif first_maximum > digit > second_maximum:
                second_maximum = digit

        return second_maximum


# ============================================================
# Approach 3: Fixed-Size Frequency Array
#
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Digits 0–9 frequencies fixed arrayలో store చేస్తున్నాం.
# 9 నుంచి 0 వరకు scan చేసి second present digit return చేస్తున్నాం.

class Solution3:
    def secondHighest(self, s: str) -> int:
        frequency = [0] * 10

        for character in s:
            if character.isdigit():
                digit = int(character)
                frequency[digit] += 1

        distinct_count = 0

        for digit in range(9, -1, -1):
            if frequency[digit] > 0:
                distinct_count += 1

                if distinct_count == 2:
                    return digit

        return -1


# ============================================================
# OTHER USEFUL SOLUTIONS
# ============================================================


# Approach 4: Sort Unique Digits
#
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# General form O(n + d log d).
# Here d <= 10, so d is constant.

class Solution4:
    def secondHighest(self, s: str) -> int:
        digits = {
            int(character)
            for character in s
            if character.isdigit()
        }

        sorted_digits = sorted(
            digits,
            reverse=True
        )

        if len(sorted_digits) < 2:
            return -1

        return sorted_digits[1]


# ============================================================
# Approach 5: Check Digits From 9 to 0
#
# Time Complexity: O(10n), simplified to O(n)
# Space Complexity: O(1)
#
# Prati digit stringలో ఉందా అని check చేస్తున్నాం.

class Solution5:
    def secondHighest(self, s: str) -> int:
        found_count = 0

        for digit in range(9, -1, -1):
            if str(digit) in s:
                found_count += 1

                if found_count == 2:
                    return digit

        return -1
