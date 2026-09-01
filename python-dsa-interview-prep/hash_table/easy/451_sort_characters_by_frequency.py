# LeetCode 451 - Sort Characters By Frequency
# Difficulty: Medium

# Recommended Approach: Frequency HashMap + Sort Unique Keys
# Recommended Current-Level Approach: Frequency HashMap + Sort Unique Keys

# n = string length
# k = number of unique characters
#
# Space complexities include temporary result-building storage.
# Dictionary operations use average-case complexity.


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: Frequency HashMap + Sort Unique Keys
# Your Approach
# Recommended Approach
# Time Complexity: O(n + k log k)
# Space Complexity: O(n + k), simplified to O(n)
#
# Time Explanation:
# Frequencies build cheyadaniki O(n).
# k unique keys sort cheyadaniki O(k log k).
# Characters repeat chesi final string build cheyadaniki O(n).
#
# Space Explanation:
# Frequency dictionary and sorted keys kosam O(k).
# Result construction kosam O(n).
class Solution1:
    def frequencySort(self, s: str) -> str:
        frequency = {}

        for character in s:
            frequency[character] = (
                frequency.get(character, 0) + 1
            )

        sorted_keys = sorted(
            frequency,
            key=frequency.get,
            reverse=True
        )

        return "".join(
            character * frequency[character]
            for character in sorted_keys
        )


# ============================================================


# Approach 2: Frequency HashMap + Bucket Sort
# Linear-Time Approach Without Comparison Sorting
# Time Complexity: O(n + k), simplified to O(n)
# Space Complexity: O(n + k), simplified to O(n)
#
# Time Explanation:
# Frequencies build cheyadaniki O(n).
# Prati unique character ni frequency bucket lo add chestunnam: O(k).
# Buckets ni largest frequency nunchi traverse chestunnam: O(n).
# Final string construction O(n).
#
# Space Explanation:
# n + 1 buckets create chestunnam.
# Dictionary and result-building storage kuda use chestunnam.
#
# Logic:
# buckets[frequency] lo aa frequency unna characters untayi.
#
# Example: s = "tree"
# buckets[1] = ["t", "r"]
# buckets[2] = ["e"]
#
# Largest frequency first → "ee" + "t" + "r"
class Solution2:
    def frequencySort(self, s: str) -> str:
        frequency = {}

        for character in s:
            frequency[character] = (
                frequency.get(character, 0) + 1
            )

        buckets = [[] for _ in range(len(s) + 1)]

        for character, count in frequency.items():
            buckets[count].append(character)

        result = []

        for count in range(len(s), 0, -1):
            for character in buckets[count]:
                result.append(character * count)

        return "".join(result)


# ============================================================


# Approach 3: Counter + most_common()
# Short Python Approach
# Time Complexity: O(n + k log k)
# Space Complexity: O(n)
#
# Time Explanation:
# Counter frequencies build cheyadaniki O(n).
# most_common() unique characters ni frequency descending order lo istundi.
# All k entries order cheyadaniki O(k log k).
# Final string build cheyadaniki O(n).
#
# Space Explanation:
# Counter and ordered pairs kosam O(k).
# Result construction kosam O(n).
class Solution3:
    def frequencySort(self, s: str) -> str:
        from collections import Counter

        frequency = Counter(s)

        return "".join(
            character * count
            for character, count in frequency.most_common()
        )


# ============================================================
# OTHER USEFUL SOLUTIONS
# ============================================================


# Approach 4: Frequency HashMap + Heap
# Time Complexity: O(n + k log k)
# Space Complexity: O(n)
#
# Time Explanation:
# Frequencies build cheyadaniki O(n).
# heapify() kosam O(k).
# k elements pop cheyadaniki O(k log k).
# Result construction O(n).
#
# Space Explanation:
# Frequency dictionary and heap kosam O(k).
# Result construction kosam O(n).
#
# Logic:
# Python min-heap kabatti negative counts use chestunnam.
# Most frequent character first pop avutundi.
class Solution4:
    def frequencySort(self, s: str) -> str:
        import heapq

        frequency = {}

        for character in s:
            frequency[character] = (
                frequency.get(character, 0) + 1
            )

        heap = [
            (-count, character)
            for character, count in frequency.items()
        ]

        heapq.heapify(heap)
        result = []

        while heap:
            negative_count, character = heapq.heappop(heap)
            result.append(character * (-negative_count))

        return "".join(result)


# ============================================================


# Approach 5: Sort Every Character
# Time Complexity: O(n log n)
# Space Complexity: O(n)
#
# Time Explanation:
# Frequencies build cheyadaniki O(n).
# Unique keys kaakunda complete string characters ni sort chestunnam.
# Kabatti sorting cost O(n log n).
#
# Space Explanation:
# sorted() n characters unna new list create chestundi.
# Sorting keys and output kuda O(n) space use chestayi.
#
# Important:
# Frequency equal ayite character ni tie-breaker ga use chestunnam.
# Idi same characters kalisi unde la chestundi.
#
# Frequency maatrame sort chesthe equal-frequency characters
# interleaved-ga undipovachu.
class Solution5:
    def frequencySort(self, s: str) -> str:
        from collections import Counter

        frequency = Counter(s)

        sorted_characters = sorted(
            s,
            key=lambda character: (
                -frequency[character],
                character
            )
        )

        return "".join(sorted_characters)
