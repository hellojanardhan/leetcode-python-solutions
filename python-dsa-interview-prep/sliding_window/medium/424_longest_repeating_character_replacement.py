# LeetCode 424 - Longest Repeating Character Replacement
# Difficulty: Medium

# Recommended Approach: Variable Sliding Window + Frequency HashMap
# Recommended Current-Level Approach: Variable Sliding Window + Frequency HashMap


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: Variable Sliding Window + Frequency HashMap
# Your Approach
# Recommended Optimal Approach
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Time Explanation:
# right pointer string ni once left-to-right traverse chestundi.
#
# Prati incoming character frequency ni update chestunnam.
#
# max_freq = current window lo most frequent character yokka
# highest useful frequency.
#
# replacements required:
#
# window_size - max_freq
#
# Ee value k kanna ekkuva ayithe window invalid.
#
# Appudu left side nunchi characters remove chestu
# window ni shrink chestam.
#
# right pointer maximum n times move avutundi.
# left pointer kuda maximum n times move avutundi.
#
# Kabatti:
#
# O(n + n)
# = O(n)
#
# Space Explanation:
# Problem uppercase English letters maatrame contain chestundi.
#
# Frequency map lo maximum 26 keys untayi.
#
# O(26)
# = O(1)
class Solution1:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)

        max_freq = 0
        freq = {}
        left = 0
        longest = 0

        for right in range(n):
            current_char = s[right]

            if current_char in freq:
                freq[current_char] += 1
            else:
                freq[current_char] = 1

            if freq[current_char] > max_freq:
                max_freq = freq[current_char]

            window_size = right - left + 1

            while window_size - max_freq > k:
                left_char = s[left]

                freq[left_char] -= 1
                left += 1

                window_size = right - left + 1

            if window_size > longest:
                longest = window_size

        return longest


# ============================================================


# Approach 2: Variable Sliding Window + Recalculate max_freq
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Time Explanation:
# Same sliding-window logic.
#
# Difference:
# Window shrink ayina prati sari actual current max frequency ni
# malli calculate chestam.
#
# max(freq.values()) maximum 26 uppercase letters meeda run avutundi.
#
# O(26) = O(1)
#
# Kabatti total:
#
# O(26 * n)
# = O(n)
#
# Ee version conceptually easy,
# because max_freq current window ni exact-ga represent chestundi.
#
# Space Explanation:
# Maximum 26 character frequencies.
#
# O(1)
class Solution2:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        left = 0
        longest = 0

        for right in range(len(s)):
            char = s[right]

            freq[char] = freq.get(char, 0) + 1

            max_freq = max(freq.values())

            while (right - left + 1) - max_freq > k:
                outgoing = s[left]

                freq[outgoing] -= 1

                if freq[outgoing] == 0:
                    del freq[outgoing]

                left += 1

                max_freq = max(freq.values())

            longest = max(
                longest,
                right - left + 1
            )

        return longest


# ============================================================


# Approach 3: Brute Force
# Time Complexity: O(n^2)
# Space Complexity: O(1)
#
# Time Explanation:
# Prati starting index nunchi
# possible substrings ni extend chestam.
#
# Current substring lo frequency maintain chestam.
#
# For each substring:
#
# replacements =
# substring_length - most_frequent_character_count
#
# replacements <= k ayithe valid.
#
# Worst-case all start/end combinations check chestam.
#
# Total:
# O(n^2)
#
# Space Explanation:
# Uppercase English letters maximum 26.
#
# O(26)
# = O(1)
class Solution3:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0

        for left in range(len(s)):
            freq = {}
            max_freq = 0

            for right in range(left, len(s)):
                char = s[right]

                freq[char] = freq.get(char, 0) + 1

                max_freq = max(
                    max_freq,
                    freq[char]
                )

                window_size = right - left + 1

                if window_size - max_freq <= k:
                    longest = max(
                        longest,
                        window_size
                    )

        return longest


# ============================================================
# OTHER POSSIBLE SOLUTIONS
# ============================================================


# Approach 4: Binary Search on Answer Length
# Time Complexity: O(n log n)
# Space Complexity: O(1)
#
# Possible answer length ni binary search chestam.
#
# Oka particular length valid aa kaadaa ani
# fixed sliding window tho check chestam.
#
# Each validation O(n).
# Binary search O(log n).
#
# Total:
# O(n log n)
