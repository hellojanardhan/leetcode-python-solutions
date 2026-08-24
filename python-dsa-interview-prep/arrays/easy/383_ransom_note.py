# LeetCode 383 - Ransom Note
# Difficulty: Easy


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: Frequency HashMap + Consume
# Your Approach
# Recommended HashMap Approach
# Time Complexity: O(n + m)
# Space Complexity: O(k)
class Solution1:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        if len(ransomNote) > len(magazine):
            return False

        freq = {}

        for char in magazine:
            freq[char] = freq.get(char, 0) + 1

        for char in ransomNote:
            if char not in freq:
                return False

            freq[char] -= 1

            if freq[char] < 0:
                return False

        return True


# ============================================================


# Approach 2: Count Ransom Note First
# Then consume using Magazine
# Time Complexity: O(n + m)
# Space Complexity: O(k)
class Solution2:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        freq = {}

        for char in ransomNote:
            freq[char] = freq.get(char, 0) + 1

        for char in magazine:
            if char in freq:
                freq[char] -= 1

                if freq[char] == 0:
                    del freq[char]

        return len(freq) == 0


# ============================================================


# Approach 3: Fixed Frequency Array
# Optimal when only lowercase English letters are allowed
# Time Complexity: O(n + m)
# Space Complexity: O(1)
class Solution3:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        freq = [0] * 26

        for char in magazine:
            index = ord(char) - ord('a')
            freq[index] += 1

        for char in ransomNote:
            index = ord(char) - ord('a')
            freq[index] -= 1

            if freq[index] < 0:
                return False

        return True


# ============================================================
# REMAINING SOLUTIONS
# ============================================================


# Approach 4: collections.Counter
# Pythonic
# Time Complexity: O(n + m)
# Space Complexity: O(k)
from collections import Counter

class Solution4:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        ransom_count = Counter(ransomNote)
        magazine_count = Counter(magazine)

        return not (ransom_count - magazine_count)


# ============================================================


# Approach 5: String Search + Removal
# Simple but inefficient
# Time Complexity: O(n * m)
# Space Complexity: O(m)
class Solution5:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        for char in ransomNote:

            if char not in magazine:
                return False

            magazine = magazine.replace(char, "", 1)

        return True
