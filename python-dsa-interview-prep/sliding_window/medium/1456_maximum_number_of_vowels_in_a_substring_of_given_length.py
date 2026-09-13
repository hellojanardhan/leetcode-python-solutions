# LeetCode 1456 - Maximum Number of Vowels in a Substring of Given Length
# Difficulty: Medium

# Recommended Approach: Optimized Fixed Sliding Window
# Recommended Current-Level Approach: Fixed Sliding Window + Count Vowels


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: Fixed Sliding Window + Count Vowels in Every Window
# Your Approach
# Recommended Current-Level Approach
# Time Complexity: O((n-k+1) * k)
# Space Complexity: O(k)
#
# Time Explanation:
# Exactly k length unna prati substring ni left-to-right check chestunnam.
#
# Prati window kosam:
# s[i:j] slice create chestunnam.
# Tarvata aa substring lo vowels enni unnayo loop tho count chestunnam.
#
# Oka window process cheyadaniki O(k).
# Total n-k+1 windows untayi.
#
# Kabatti total time complexity:
# O((n-k+1) * k)
#
# Worst-case lo approximately O(n * k).
#
# Space Explanation:
# s[i:j] slicing valla temporary k-length string create avutundi.
# Kabatti auxiliary space complexity O(k).
class Solution1:
    def maxVowels(self, s: str, k: int) -> int:
        i = 0
        j = k

        vowels = "aeiou"
        count = 0

        while j <= len(s):
            current_string = s[i:j]
            current_count = 0

            for char in current_string:
                if char in vowels:
                    current_count += 1

            count = max(count, current_count)

            i += 1
            j += 1

        return count


# ============================================================


# Approach 2: Optimized Fixed Sliding Window
# Recommended Optimal Approach
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Time Explanation:
# First k characters lo vowels count ni okasari calculate chestunnam.
#
# Tarvata window one position move ayye prati sari:
#
# outgoing character vowel ayite:
#     current_count -= 1
#
# incoming character vowel ayite:
#     current_count += 1
#
# Prati window ni scratch nunchi malli count cheyyatledu.
#
# First window O(k).
# Remaining characters O(n-k).
#
# Total:
# O(k + n-k) = O(n).
#
# Space Explanation:
# current_count, maximum mariyu few variables maatrame use chestunnam.
# Extra substring/list create cheyyatledu.
# Vowels string constant size 5.
# Kabatti auxiliary space complexity O(1).
class Solution2:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"

        current_count = 0

        for i in range(k):
            if s[i] in vowels:
                current_count += 1

        maximum = current_count

        for right in range(k, len(s)):
            outgoing = s[right - k]
            incoming = s[right]

            if outgoing in vowels:
                current_count -= 1

            if incoming in vowels:
                current_count += 1

            maximum = max(
                maximum,
                current_count
            )

        return maximum


# ============================================================


# Approach 3: Prefix Sum
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Time Explanation:
# Prati character vowel ayite 1,
# consonant ayite 0 ani prefix sum build chestunnam.
#
# Example:
#
# l -> 0
# e -> 1
# e -> 1
#
# Prati k-length substring lo vowel count ni:
#
# prefix[right] - prefix[left]
#
# tho O(1) lo calculate cheyochu.
#
# Prefix array build cheyadaniki O(n).
# All windows check cheyadaniki O(n).
#
# Kabatti total time complexity O(n).
#
# Space Explanation:
# n+1 prefix values store chestunnam.
# Kabatti auxiliary space complexity O(n).
class Solution3:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        n = len(s)

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = (
                prefix[i]
                + (1 if s[i] in vowels else 0)
            )

        maximum = 0

        for left in range(n - k + 1):
            right = left + k

            current_count = (
                prefix[right]
                - prefix[left]
            )

            maximum = max(
                maximum,
                current_count
            )

        return maximum


# ============================================================
# OTHER POSSIBLE SOLUTIONS
# ============================================================


# Approach 4: For Loop + Built-in sum()
# Time Complexity: O((n-k+1) * k)
# Space Complexity: O(k)
#
# Time Explanation:
# Prati k-length substring ni check chestunnam.
# Generator expression lo prati character vowel aa kaadaa ani verify chestunnam.
#
# Prati window ki O(k).
# Total n-k+1 windows.
#
# Kabatti total time:
# O((n-k+1) * k).
#
# Space Explanation:
# s[i:i+k] slice create cheste temporary k-length string vastundi.
# Kabatti auxiliary space O(k).
class Solution4:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        maximum = 0

        for i in range(len(s) - k + 1):
            current_count = sum(
                1
                for char in s[i:i + k]
                if char in vowels
            )

            maximum = max(
                maximum,
                current_count
            )

        return maximum
