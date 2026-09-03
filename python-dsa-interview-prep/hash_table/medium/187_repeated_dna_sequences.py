# LeetCode 187 - Repeated DNA Sequences
# Difficulty: Medium
#
# Recommended Approach: HashSet + Sliding Window
# Recommended Current-Level Approach: HashSet + Sliding Window


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: HashSet + Fixed Sliding Window
# Your Approach — Cleaned
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Prati 10-character substring ni seen set lo check chestunnam.
# Already seen ayite repeated set lo add chestunnam.

class Solution1:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []

        seen = set()
        repeated = set()

        for i in range(len(s) - 9):
            sequence = s[i:i + 10]

            if sequence in seen:
                repeated.add(sequence)

            seen.add(sequence)

        return list(repeated)


# ============================================================


# Approach 2: Frequency HashMap
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Sequence count exactly 2 ayinappudu result lo add chestunnam.
# Kabatti same sequence output lo okkasare vastundi.

class Solution2:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
OAOAOA        frequency = {}
        result = []

        for i in range(len(s) - 9):
            sequence = s[i:i + 10]
            frequency[sequence] = frequency.get(sequence, 0) + 1

            if frequency[sequence] == 2:
                result.append(sequence)

        return result


# ============================================================


# Approach 3: Bitmask Rolling Encoding
# Advanced Optimal Approach
# Time Complexity: O(n)
# Space Complexity: O(n)
OAOAOA#
# A, C, G, T characters ni 2 bits tho represent chestunnam.
# 10 characters ante 20 bits.
# Complete substring badulu encoded integer ni set lo store chestunnam.

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

        code = 0
        mask = (1 << 20) - 1

        for i, char in enumerate(s):
            code = ((code << 2) | encoding[char]) & mask

            if i < 9:
                continue

            if code in seen and code not in repeated:
                result.append(s[i - 9:i + 1])
                repeated.add(code)

            seen.add(code)

        return result


# ============================================================
# OTHER USEFUL SOLUTIONS
# ============================================================


# Approach 4: Counter
# Time Complexity: O(n)
# Space Complexity: O(n)

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


# Approach 5: Sorting All Substrings
# Time Complexity: O(n log n)
# Space Complexity: O(n)
#
# Equal sequences sorting tarvata adjacent-ga vastayi.
# HashSet use cheyani alternative, kaani O(n) optimal kaadu.

class Solution5:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sequences = [
            s[i:i + 10]
            for i in range(len(s) - 9)
        ]

        sequences.sort()
        result = []

        for i in range(1, len(sequences)):
            if (
                sequences[i] == sequences[i - 1]
                and (
                    not result
                    or result[-1] != sequences[i]
                )
            ):
                result.append(sequences[i])

        return result
