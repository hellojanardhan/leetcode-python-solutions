# LeetCode 409 - Longest Palindrome
# Difficulty: Easy
# Recommended Approach: Frequency HashMap + Pair Counting
# Recommended Current-Level Approach: Frequency HashMap + Pair Counting


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: Frequency HashMap + Pair Counting
# Your Approach
# Recommended Approach
# Time Complexity: O(n)
# Space Complexity: O(k)
#
# Time Explanation:
# String characters ni traverse chesi frequencies calculate chestunnam.
# Frequency even ayina ప్రతిసారి complete pair dorikindi kabatti
# palindrome length ki 2 add chestunnam.
#
# Tarvata frequency values lo odd count undaa ani check chestunnam.
# Odd frequency unte center kosam 1 add chestunnam.
#
# O(n + k), simplified-ga O(n).
#
# Space Explanation:
# k unique characters frequencies dictionary lo store avutayi.
# Kabatti auxiliary space complexity O(k).
class Solution1:
    def longestPalindrome(self, s: str) -> int:
        length = 0
        frequency = {}

        for character in s:
            frequency[character] = (
                frequency.get(character, 0) + 1
            )

            if frequency[character] % 2 == 0:
                length += 2

        for count in frequency.values():
            if count % 2 != 0:
                length += 1
                break

        return length


# ============================================================


# Approach 2: Build Complete Frequency Map
# Then Use Maximum Even Counts
# Time Complexity: O(n)
# Space Complexity: O(k)
#
# Time Explanation:
# First loop lo character frequencies calculate chestunnam.
# Second loop lo prati frequency nunchi maximum even count
# palindrome length ki add chestunnam.
#
# Odd frequency unte center_available True chestunnam.
# Chivarilo center kosam 1 add chestunnam.
#
# Space Explanation:
# k unique character frequencies store chestunnam.
# Kabatti auxiliary space complexity O(k).
class Solution2:
    def longestPalindrome(self, s: str) -> int:
        frequency = {}

        for character in s:
            frequency[character] = (
                frequency.get(character, 0) + 1
            )

        length = 0
        center_available = False

        for count in frequency.values():
            if count % 2 == 0:
                length += count
            else:
                length += count - 1
                center_available = True

        if center_available:
            length += 1

        return length


# ============================================================


# Approach 3: HashSet Pair Tracking
# Recommended Space-Clean Alternative
# Time Complexity: O(n)
# Space Complexity: O(k)
#
# Time Explanation:
# Character set lo lekapothe add chestunnam.
# Same character malli vasthe pair complete avutundi.
# Appudu set nunchi remove chesi length ki 2 add chestunnam.
#
# Complete traversal tarvata set empty kakapothe,
# at least one unpaired character undi.
# Danini palindrome center lo use cheyavachu.
#
# Space Explanation:
# Unpaired characters maatrame set lo store chestunnam.
# Worst case lo k unique characters undavachu.
class Solution3:
    def longestPalindrome(self, s: str) -> int:
        unpaired = set()
        length = 0

        for character in s:
            if character in unpaired:
                unpaired.remove(character)
                length += 2
            else:
                unpaired.add(character)

        if unpaired:
            length += 1

        return length


# ============================================================
# OTHER POSSIBLE SOLUTIONS
# ============================================================


# Approach 4: Counter + Mathematical Formula
# Short Python Approach
# Time Complexity: O(n)
# Space Complexity: O(k)
#
# Time Explanation:
# Counter character frequencies calculate chestundi.
# Prati frequency nunchi maximum even portion add chestunnam.
#
# count // 2 * 2:
# count = 4 → 4
# count = 3 → 2
# count = 1 → 0
#
# Palindrome length original string length kante thakkuva ayite,
# at least one odd character unused-ga undi.
# Danini center kosam add chestunnam.
class Solution4:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter

        frequency = Counter(s)

        length = sum(
            count // 2 * 2
            for count in frequency.values()
        )

        if length < len(s):
            length += 1

        return length
