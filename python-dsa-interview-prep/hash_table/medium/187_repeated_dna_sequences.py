# LeetCode 187 - Repeated DNA Sequences
# Difficulty: Medium

# Recommended Optimal Approach: HashSet + Fixed Sliding Window
# Recommended Current-Level Approach: HashSet + Fixed Sliding Window

# n = total number of characters
# u = number of unique 10-character substrings
# r = number of repeated sequences returned
#
# Total windows = max(0, n - 9).
# r <= u <= total windows.
#
# Substring length is fixed at 10.
# Slicing and hashing each substring take O(10), treated as O(1).
# Dictionary and set operations use average-case complexity.
# Space complexities include result construction.

from typing import List


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: HashSet + Fixed Sliding Window
# Your Approach
# Recommended Optimal and Current-Level Approach
# Time Complexity: O(n)
# Space Complexity: O(u), worst-case O(n)
#
# Time Explanation:
# n - 9 windows ni traverse chestunnam.
# Prati window lo exactly 10 characters slice chestunnam.
# Slicing and hashing O(10), fixed length kabatti O(1).
# Set lookup and insertion average-ga O(1).
# Repeated set ni list ga convert cheyadaniki O(r).
# Total O(n + r), simplified-ga O(n).
#
# Space Explanation:
# seen set lo u unique sequences untayi.
# repeated set and returned list lo r entries untayi.
# Prati sequence length fixed 10.
# Total O(u + r), simplified-ga O(u).
# Worst case lo u proportional to n kabatti O(n).
#
# Logic:
# First occurrence: seen lo store cheyali.
# Already seen: repeated lo store cheyali.
# repeated set valla output lo duplicates undavu.
#
# Example:
# s = "AAAAAAAAAAAA"
# Total 10-character windows = 3.
# Moodu windows kuda "AAAAAAAAAA".
# Result = ["AAAAAAAAAA"].
#
# Note:
# Output sequences any order lo undavachu.

class Solution1:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)

        if n < 10:
            return []

        seen = set()
        repeated = set()

        for i in range(n - 9):
            sequence = s[i:i + 10]

            if sequence in seen:
                repeated.add(sequence)
            else:
                seen.add(sequence)

        return list(repeated)


# ============================================================


# Approach 2: Frequency HashMap
# Useful Alternative Without a Separate Repeated Set
# Time Complexity: O(n)
# Space Complexity: O(u), worst-case O(n)
#
# Time Explanation:
# Prati 10-character window ni okasari process chestunnam.
# Substring creation fixed O(10), simplified-ga O(1).
# Frequency lookup/update average-ga O(1).
# Result append amortized-ga O(1).
# Total O(n).
#
# Space Explanation:
# Frequency dictionary lo u unique sequences store chestunnam.
# Result list lo r repeated sequences untayi.
# r <= u kabatti total O(u).
# Worst-case space O(n).
#
# Logic:
# Sequence frequency exactly 2 ayinappude result lo add chestunnam.
# Count 3, 4, 5 ayinappudu malli add cheyamu.
# Kabatti separate repeated set avasaram ledu.
#
# Example:
# "AAAAAAAAAA" counts:
# 1: result lo add cheyamu.
# 2: result lo add chestham.
# 3: malli add cheyamu.

class Solution2:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        frequency = {}
        result = []

        for i in range(len(s) - 9):
            sequence = s[i:i + 10]

            frequency[sequence] = frequency.get(sequence, 0) + 1

            if frequency[sequence] == 2:
                result.append(sequence)

        return result


# ============================================================


# Approach 3: Bitmask Rolling Encoding
# Advanced Optimal Alternative
# Time Complexity: O(n)
# Space Complexity: O(u), worst-case O(n)
#
# Time Explanation:
# Prati character ni okasari process chestunnam.
# Window code maximum 20 bits maatrame untundi.
# Bit shifting, OR, AND operations fixed-size kabatti O(1).
# Set operations average-ga O(1).
# Result lo add chesetappudu maatrame substring create chestunnam.
# Prati result substring length 10 kabatti O(1).
# Total O(n + r), simplified-ga O(n).
#
# Space Explanation:
# seen set lo u unique integer codes untayi.
# repeated set and result list lo r entries untayi.
# Encoding dictionary lo fixed 4 entries maatrame untayi.
# Total O(u + r), simplified-ga O(u).
# Worst-case space O(n).
#
# Logic:
# A = 00, C = 01, G = 10, T = 11.
# Prati DNA character ki 2 bits saripothayi.
# 10 characters represent cheyadaniki 20 bits saripothayi.
#
# New character vachinappudu:
# Existing code ni 2 bits left shift chestham.
# New character code ni OR chestham.
# Mask tho last 20 bits maatrame retain chestham.
#
# Note:
# Fixed-length 10-character DNA sequences ki idi exact encoding.
# Different sequences ki same encoded value raadu.
# String slicing approach laga idi kuda O(n);
# mainly stored representation and constant work maarutayi.

class Solution3:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []

        encoding = {
            "A": 0,
            "C": 1,
            "G": 2,
            "T": 3
        }

        seen = set()
        repeated = set()
        result = []

        window_code = 0
        mask = (1 << 20) - 1

        for i, char in enumerate(s):
            window_code = (
                (window_code << 2) | encoding[char]
            ) & mask

            if i < 9:
                continue

            if window_code in seen and window_code not in repeated:
                result.append(s[i - 9:i + 1])
                repeated.add(window_code)

            seen.add(window_code)

        return result


# ============================================================
# OTHER USEFUL SOLUTIONS
# ============================================================


# Approach 4: Counter + Filter Frequencies
# Short Python Approach
# Time Complexity: O(n)
# Space Complexity: O(u), worst-case O(n)
#
# Time Explanation:
# Generator n - 9 fixed-length substrings produce chestundi.
# Counter frequencies build cheyadaniki O(n).
# u frequency entries ni filter cheyadaniki O(u).
# Total O(n + u), simplified-ga O(n).
#
# Space Explanation:
# Counter lo u unique sequences store avutayi.
# Result list lo r entries untayi.
# Generator anni windows ni separate list lo store cheyadu.
# Total O(u + r), simplified-ga O(u).
# Worst-case space O(n).
#
# Logic:
# Counter tho frequencies calculate chestham.
# Frequency > 1 unna sequences return chestham.

class Solution4:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        from collections import Counter

        sequences = (
            s[i:i + 10]
            for i in range(len(s) - 9)
        )

        frequency = Counter(sequences)

        return [
            sequence
            for sequence, count in frequency.items()
            if count > 1
        ]


# ============================================================


# Approach 5: Sorting All Substrings + Adjacent Comparison
# Correct but Not Time-Optimal
# Time Complexity: O(n log n)
# Space Complexity: O(n)
#
# Time Explanation:
# All fixed-length substrings create cheyadaniki O(n).
# Approximately n substrings sort cheyadaniki O(n log n).
# Prati string comparison maximum 10 characters compare chestundi.
# Fixed length kabatti comparison cost O(1).
# Sorted list ni scan cheyadaniki O(n).
# Total O(n log n).
#
# Space Explanation:
# Substrings list lo approximately n entries untayi.
# Prati substring length fixed 10.
# Python sorting temporary memory worst-case O(n).
# Result list space O(r), where r <= n.
# Total additional space O(n).
#
# Logic:
# Sorting tarvata equal sequences adjacent-ga untayi.
# Adjacent sequences equal ayite repeated sequence dorikindi.
# Result last entry tho compare chesi duplicate output avoid chestham.

class Solution5:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sequences = [
            s[i:i + 10]
            for i in range(len(s) - 9)
        ]

        sequences.sort()
        result = []

        for i in range(1, len(sequences)):
            if sequences[i] == sequences[i - 1]:
                if not result or result[-1] != sequences[i]:
                    result.append(sequences[i])

        return result
