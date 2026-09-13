# LeetCode 2269 - Find the K-Beauty of a Number
# Difficulty: Easy

# Recommended Approach: Fixed Sliding Window Using String
# Recommended Current-Level Approach: Fixed Sliding Window Using String


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: Fixed Sliding Window Using String
# Your Approach
# Recommended Current-Level Approach
# Time Complexity: O(d * k)
# Space Complexity: O(d)
#
# Time Explanation:
# Number ni string ga convert chestunnam.
# d = number of digits in num.
#
# Prati k-length substring ni left-to-right check chestunnam.
# Total approximately d-k+1 windows untayi.
#
# s[i:j] slice create cheyadaniki O(k),
# int() conversion k characters meeda O(k).
#
# Kabatti overall time complexity O((d-k+1) * k),
# simplified-ga O(d * k).
#
# Space Explanation:
# str(num) d characters unna string create chestundi.
# Prati slice temporary-ga maximum k characters store chestundi.
# Overall auxiliary space O(d).
class Solution1:
    def divisorSubstrings(self, num: int, k: int) -> int:
        string_num = str(num)

        i = 0
        j = k
        count = 0

        while j <= len(string_num):
            current = int(string_num[i:j])

            if current != 0 and num % current == 0:
                count += 1

            i += 1
            j += 1

        return count


# ============================================================


# Approach 2: For Loop + String Slicing
# Short Recommended Approach
# Time Complexity: O(d * k)
# Space Complexity: O(d)
#
# Time Explanation:
# Number ni string ga convert chestunnam.
# Prati valid starting index nunchi exactly k characters slice chestunnam.
#
# Slice + int conversion O(k).
# Approximately d-k+1 windows untayi.
#
# Kabatti total time complexity O(d * k).
#
# Space Explanation:
# String representation O(d).
# Temporary substring O(k).
# Overall O(d).
class Solution2:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_str = str(num)
        count = 0

        for i in range(len(num_str) - k + 1):
            current = int(num_str[i:i + k])

            if current != 0 and num % current == 0:
                count += 1

        return count


# ============================================================


# Approach 3: Integer Arithmetic Using Modulo and Division
# No String Conversion
# Time Complexity: O(d)
# Space Complexity: O(1)
#
# Time Explanation:
# String ga convert cheyyakunda last k digits ni modulo tho extract chestunnam.
#
# divisor = 10^k
#
# current % divisor
# -> current number lo last k digits istundi.
#
# Tarvata current //= 10
# chesi window ni one digit left side ki move chestunnam.
#
# Prati digit position ni okasari process chestunnam.
# Kabatti time complexity O(d).
#
# Space Explanation:
# Few integer variables maatrame use chestunnam.
# Input size batti additional data structure create cheyyatledu.
# Kabatti auxiliary space O(1).
class Solution3:
    def divisorSubstrings(self, num: int, k: int) -> int:
        original = num
        divisor = 10 ** k
        count = 0

        digits = len(str(num))

        for _ in range(digits - k + 1):
            current = num % divisor

            if current != 0 and original % current == 0:
                count += 1

            num //= 10

        return count


# ============================================================
# OTHER POSSIBLE SOLUTIONS
# ============================================================


# Approach 4: List of All K-Length Substrings
# Time Complexity: O(d * k)
# Space Complexity: O(d * k)
#
# Time Explanation:
# First all k-length substrings ni list comprehension tho create chestunnam.
# Tarvata each substring ni integer ga convert chesi divisor condition check chestunnam.
#
# Prati substring size k.
# Approximately d-k+1 substrings.
# Kabatti total time complexity O(d * k).
#
# Space Explanation:
# All substrings ni simultaneously list lo store chestunnam.
# Approximate space O((d-k+1) * k).
# Kabatti idi unnecessary extra memory use chestundi.
class Solution4:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_str = str(num)

        windows = [
            num_str[i:i + k]
            for i in range(len(num_str) - k + 1)
        ]

        count = 0

        for window in windows:
            current = int(window)

            if current != 0 and num % current == 0:
                count += 1

        return count
