# LeetCode 28 - Find the Index of the First Occurrence in a String
# Difficulty: Easy
# Recommended Approach: KMP Algorithm
# Recommended Current-Level Approach: Nested Loops


# Approach 1: KMP Algorithm - Optimal Solution
# Time Complexity: O(n + m)
# Needle kosam LPS array build cheyadaniki O(m), haystack lo search
# cheyadaniki O(n) time paduthundi.
# Space Complexity: O(m)
# Needle length prakaram LPS array create chesthunnam.
class Solution1:
    def strStr(self, haystack: str, needle: str) -> int:
        lps = [0] * len(needle)

        previous = 0
        current = 1

        while current < len(needle):
            if needle[current] == needle[previous]:
                previous += 1
                lps[current] = previous
                current += 1
            elif previous > 0:
                previous = lps[previous - 1]
            else:
                current += 1

        i = 0
        j = 0

        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1

                if j == len(needle):
                    return i - j

            elif j > 0:
                j = lps[j - 1]

            else:
                i += 1

        return -1


# Approach 2: Your Approach - Manual Character Comparison
# Time Complexity: O(n * m)
# Prathi starting position nunchi worst case lo m characters ni
# compare chestham.
# Space Complexity: O(1)
# start, i, j ane konni index variables mathrame use chesthunnam.
class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:
        start = 0
        i = 0
        j = 0

        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1

                if j == len(needle):
                    return start

            else:
                start += 1
                i = start
                j = 0

        return -1


# Approach 3: Nested Loops
# Time Complexity: O(n * m)
# Prathi valid starting position daggara needle lo unna m
# characters ni compare chestham.
# Space Complexity: O(1)
# Additional list, string leda data structure create cheyadam ledu.
class Solution3:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        for start in range(n - m + 1):
            for j in range(m):
                if haystack[start + j] != needle[j]:
                    break
            else:
                return start

        return -1


# Approach 4: Your Approach - Sliding Window with Slicing
# Time Complexity: O(n * m)
# Prathi window lo m characters ni slice chesi needle tho
# compare chesthunnam.
# Space Complexity: O(m)
# Python slicing prathi iteration lo maximum m characters unna
# kottha substring ni create chesthundi.
class Solution4:
    def strStr(self, haystack: str, needle: str) -> int:
        read = 0
        write = len(needle)

        while write <= len(haystack):
            if haystack[read:write] == needle:
                return read

            read += 1
            write += 1

        return -1


# Approach 5: Rabin-Karp Rolling Hash
# Time Complexity: O(n + m) Average, O(n * m) Worst Case
# Average case lo hashes ni linear time lo calculate chesi compare
# chestham. Ekkuva hash collisions vasthe worst case O(n * m).
# Space Complexity: O(1)
# Konni hash values mariyu index variables mathrame use chesthunnam.
class Solution5:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        if m > n:
            return -1

        base = 256
        modulus = 1_000_000_007
        highest_power = pow(base, m - 1, modulus)

        needle_hash = 0
        window_hash = 0

        for i in range(m):
            needle_hash = (
                needle_hash * base + ord(needle[i])
            ) % modulus

            window_hash = (
                window_hash * base + ord(haystack[i])
            ) % modulus

        for start in range(n - m + 1):
            if (
                needle_hash == window_hash
                and haystack[start:start + m] == needle
            ):
                return start

            if start < n - m:
                outgoing = ord(haystack[start])
                incoming = ord(haystack[start + m])

                window_hash = (
                    window_hash
                    - outgoing * highest_power
                ) % modulus

                window_hash = (
                    window_hash * base + incoming
                ) % modulus

        return -1


# Approach 6: Z Algorithm
# Time Complexity: O(n + m)
# Combined string lo unna prathi character ni linear ga process
# chestham. Kabatti total time complexity O(n + m).
# Space Complexity: O(n + m)
# Combined string length prakaram Z array create chesthunnam.
class Solution6:
    def strStr(self, haystack: str, needle: str) -> int:
        combined = needle + "#" + haystack
        z = [0] * len(combined)

        left = 0
        right = 0

        for i in range(1, len(combined)):
            if i <= right:
                z[i] = min(right - i + 1, z[i - left])

            while (
                i + z[i] < len(combined)
                and combined[z[i]] == combined[i + z[i]]
            ):
                z[i] += 1

            if i + z[i] - 1 > right:
                left = i
                right = i + z[i] - 1

            if z[i] == len(needle):
                return i - len(needle) - 1

        return -1


# Approach 7: Python Built-in find()
# Time Complexity: Implementation-Dependent
# Exact time complexity Python internal string-search implementation
# meeda depend avuthundi.
# Space Complexity: O(1) Auxiliary
# Mana code lo additional data structure create cheyadam ledu.
class Solution7:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
