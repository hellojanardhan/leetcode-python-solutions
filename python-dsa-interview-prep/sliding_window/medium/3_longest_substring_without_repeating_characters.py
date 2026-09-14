# LeetCode 3 - Longest Substring Without Repeating Characters
# Difficulty: Medium

# Recommended Approach: Variable Sliding Window + HashSet
# Recommended Current-Level Approach: Variable Sliding Window + HashSet


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: Variable Sliding Window + HashSet
# Your Approach
# Recommended Current-Level Approach
# Time Complexity: O(n)
# Space Complexity: O(min(n, charset))
#
# Time Explanation:
# right pointer prati character ni once visit chestundi.
#
# Duplicate vachinappudu:
# left/start pointer forward move chestundi.
#
# Important:
# start pointer backward velladu.
#
# Oka character maximum:
#   once seen set lo add avutundi
#   once seen set nunchi remove avutundi
#
# Kabatti nested while unna sare O(n^2) kaadu.
#
# Total:
# O(n)
#
# Space Explanation:
# seen set lo current unique window characters untayi.
#
# Worst-case all characters unique ayithe:
# O(n)
#
# Fixed character set consider cheste:
# O(min(n, charset))
class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()

        max_length = 0
        start = 0

        for char in range(len(s)):

            while s[char] in seen:
                seen.remove(s[start])
                start += 1

            seen.add(s[char])

            length = char - start + 1

            max_length = max(
                max_length,
                length
            )

        return max_length


# ============================================================


# Approach 2: HashMap + Last Seen Index
# Recommended Optimal Interview Approach
# Time Complexity: O(n)
# Space Complexity: O(min(n, charset))
#
# Time Explanation:
# Prati character last seen index ni HashMap lo store chestam.
#
# Duplicate vachinappudu left pointer ni
# one-by-one move cheyyakunda direct ga jump chestam.
#
# Example:
# last_seen[char] + 1
#
# Each character once process chestam.
#
# Total O(n).
#
# Space Explanation:
# Unique characters last indices store chestam.
#
# O(min(n, charset)).
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}

        start = 0
        max_length = 0

        for right in range(len(s)):
            char = s[right]

            if char in last_seen and last_seen[char] >= start:
                start = last_seen[char] + 1

            last_seen[char] = right

            length = right - start + 1

            max_length = max(
                max_length,
                length
            )

        return max_length


# ============================================================


# Approach 3: Variable Sliding Window + Frequency HashMap
# Time Complexity: O(n)
# Space Complexity: O(min(n, charset))
#
# Time Explanation:
# Current window characters frequencies maintain chestam.
#
# Incoming character frequency increase chestam.
#
# Aa character frequency > 1 ayithe:
# duplicate undi ani meaning.
#
# Duplicate disappear ayye varaku left side shrink chestam.
#
# Each character once enters and once leaves.
#
# Total O(n).
#
# Space Explanation:
# Current window character frequencies HashMap lo store chestam.
#
# O(min(n, charset)).
class Solution3:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = {}

        left = 0
        max_length = 0

        for right in range(len(s)):
            char = s[right]

            freq[char] = freq.get(char, 0) + 1

            while freq[char] > 1:
                outgoing = s[left]

                freq[outgoing] -= 1

                if freq[outgoing] == 0:
                    del freq[outgoing]

                left += 1

            max_length = max(
                max_length,
                right - left + 1
            )

        return max_length


# ============================================================
# OTHER POSSIBLE SOLUTIONS
# ============================================================


# Approach 4: Brute Force
# Time Complexity: O(n^3)
# Space Complexity: O(n)
#
# Every possible substring generate chestam.
#
# Each substring unique aa kaadaa set tho check chestam.
#
# O(n^2) substrings.
# Each substring check O(n).
#
# Total:
# O(n^3)
class Solution4:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                substring = s[i:j + 1]

                if len(set(substring)) == len(substring):
                    max_length = max(
                        max_length,
                        len(substring)
                    )

        return max_length
