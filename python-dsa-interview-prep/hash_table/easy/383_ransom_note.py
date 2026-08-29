# LeetCode 383 - Ransom Note
# Difficulty: Easy
# Recommended Approach: Frequency HashMap + Consume
# Recommended Current-Level Approach: Frequency HashMap + Consume


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: Count Magazine + Consume Using Ransom Note
# Your Approach
# Recommended HashMap Approach
# Time Complexity: O(n + m)
# Space Complexity: O(k)
#
# Time Explanation:
# magazine lo prati character frequency ni calculate chestunnam.
# ransomNote lo prati character ni okasari process chestunnam.
# Dictionary lookup mariyu update average-ga O(1).
# Kabatti total time complexity O(n + m).
#
# Space Explanation:
# magazine lo unna unique characters ni dictionary lo store chestunnam.
# k unique characters unte auxiliary space complexity O(k).
class Solution1:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        frequency = {}

        for char in magazine:
            frequency[char] = frequency.get(char, 0) + 1

        for char in ransomNote:
            if char not in frequency:
                return False

            frequency[char] -= 1

            if frequency[char] < 0:
                return False

        return True


# ============================================================


# Approach 2: Count Ransom Note + Consume Using Magazine
# Time Complexity: O(n + m)
# Space Complexity: O(k)
#
# Time Explanation:
# ransomNote lo required characters frequencies ni calculate chestunnam.
# magazine characters tho required frequencies ni decrease chestunnam.
# Required characters anni dorikina ventane True return cheyavachu.
# Worst case lo total time complexity O(n + m).
#
# Space Explanation:
# ransomNote lo unique required characters maatrame store chestunnam.
# k unique characters unte auxiliary space complexity O(k).
class Solution2:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        required = {}

        for char in ransomNote:
            required[char] = required.get(char, 0) + 1

        remaining = len(ransomNote)

        for char in magazine:
            if char in required and required[char] > 0:
                required[char] -= 1
                remaining -= 1

                if remaining == 0:
                    return True

        return remaining == 0


# ============================================================


# Approach 3: Fixed-Size Frequency Array
# Recommended Optimal Space Approach
# Time Complexity: O(n + m)
# Space Complexity: O(1)
#
# Time Explanation:
# magazine characters frequencies ni fixed array lo calculate chestunnam.
# ransomNote characters vachinappudu frequencies ni decrease chestunnam.
# Rendu strings ni okkokkasaari process chestunnam.
# Kabatti total time complexity O(n + m).
#
# Space Explanation:
# Fixed size 26 array maatrame use chestunnam.
# Input size periginaa array size maaradu.
# Kabatti auxiliary space complexity O(1).
class Solution3:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        frequency = [0] * 26

        for char in magazine:
            index = ord(char) - ord("a")
            frequency[index] += 1

        for char in ransomNote:
            index = ord(char) - ord("a")
            frequency[index] -= 1

            if frequency[index] < 0:
                return False

        return True


# ============================================================
# OTHER POSSIBLE SOLUTIONS
# ============================================================


# Approach 4: collections.Counter
# Time Complexity: O(n + m)
# Space Complexity: O(k)
#
# Time Explanation:
# Counter rendu strings character frequencies ni calculate chestundi.
# Ransom Note frequency magazine frequency kante ekkuva undaa ani
# prati required character kosam check chestunnam.
# Kabatti total time complexity O(n + m).
#
# Space Explanation:
# Character frequencies Counter objects lo store avutayi.
# k unique characters unte auxiliary space complexity O(k).
class Solution4:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter

        ransom_frequency = Counter(ransomNote)
        magazine_frequency = Counter(magazine)

        for char, count in ransom_frequency.items():
            if magazine_frequency[char] < count:
                return False

        return True


# ============================================================


# Approach 5: count() for Every Character
# Time Complexity: O(k * (n + m))
# Space Complexity: O(k)
#
# Time Explanation:
# Ransom Note lo prati unique character kosam rendu strings meeda
# count() call chestunnam.
# count() complete string ni scan chestundi.
# Kabatti total time complexity O(k * (n + m)).
#
# Space Explanation:
# ransomNote unique characters ni set lo store chestunnam.
# Kabatti auxiliary space complexity O(k).
class Solution5:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        for char in set(ransomNote):
            if ransomNote.count(char) > magazine.count(char):
                return False

        return True


# ============================================================


# Approach 6: Remove Characters from a List
# Time Complexity: O(n * m)
# Space Complexity: O(m)
#
# Time Explanation:
# Magazine ni list ga convert chestunnam.
# Ransom Note lo prati character kosam list membership check chestunnam.
# List search mariyu remove O(m) time teesukovachu.
# Kabatti worst-case time complexity O(n * m).
#
# Space Explanation:
# Magazine characters kosam separate list create chestunnam.
# Kabatti auxiliary space complexity O(m).
class Solution6:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        available = list(magazine)

        for char in ransomNote:
            if char not in available:
                return False

            available.remove(char)

        return True
