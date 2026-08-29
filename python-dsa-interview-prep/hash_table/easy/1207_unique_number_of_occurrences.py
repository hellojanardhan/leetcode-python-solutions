# LeetCode 1207 - Unique Number of Occurrences
# Difficulty: Easy

# Recommended Approach: Frequency HashMap + Seen HashSet
# Recommended Current-Level Approach: Frequency HashMap + Seen HashSet


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: Frequency HashMap + Seen HashSet
# Your Approach
# Recommended Optimal Approach
# Time Complexity: O(n)
# Space Complexity: O(k)
#
# Time Explanation:
# Array lo prati number ni okasari traverse chesi frequency calculate chestunnam.
# Tarvata k frequency values ni okasari traverse chestunnam.
# Dictionary mariyu set operations average-ga O(1).
# Kabatti total time complexity O(n + k), simplified-ga O(n).
#
# Space Explanation:
# k unique numbers frequencies ni dictionary lo store chestunnam.
# Frequency values ni seen set lo store chestunnam.
# Kabatti auxiliary space complexity O(k).
class Solution1:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        frequency = {}

        for num in arr:
            frequency[num] = frequency.get(num, 0) + 1

        seen_frequencies = set()

        for count in frequency.values():
            if count in seen_frequencies:
                return False

            seen_frequencies.add(count)

        return True


# ============================================================


# Approach 2: Compare Number of Frequencies with Unique Frequencies
# Short Optimal Approach
# Time Complexity: O(n)
# Space Complexity: O(k)
#
# Time Explanation:
# Array frequencies build cheyadaniki O(n).
# Frequency values ni set ga convert cheyadaniki O(k).
# Length comparison O(1).
# Kabatti total time complexity O(n + k), simplified-ga O(n).
#
# Space Explanation:
# Frequency dictionary mariyu frequency set lo maximum k values untayi.
# Kabatti auxiliary space complexity O(k).
class Solution2:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        frequency = {}

        for num in arr:
            frequency[num] = frequency.get(num, 0) + 1

        return len(frequency) == len(set(frequency.values()))


# ============================================================


# Approach 3: Counter + HashSet
# Time Complexity: O(n)
# Space Complexity: O(k)
#
# Time Explanation:
# Counter array elements frequencies ni O(n) time lo calculate chestundi.
# Frequency values ni set ga convert cheyadaniki O(k).
# Kabatti total time complexity O(n).
#
# Space Explanation:
# Counter mariyu set lo maximum k entries store avutayi.
# Kabatti auxiliary space complexity O(k).
class Solution3:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import Counter

        frequency = Counter(arr)

        return len(frequency) == len(set(frequency.values()))


# ============================================================
# OTHER POSSIBLE SOLUTIONS
# ============================================================


# Approach 4: Sorting + Group Counting
# Time Complexity: O(n log n)
# Space Complexity: O(n)
#
# Time Explanation:
# Array ni sort cheyadaniki O(n log n) time padutundi.
# Sorted array lo equal numbers groups ni count cheyadaniki O(n).
# Prati group count ni set lo check cheyadaniki average-ga O(1).
# Kabatti total time complexity O(n log n).
#
# Space Explanation:
# sorted() kotta list create chestundi.
# Group frequencies kosam set use chestunnam.
# Kabatti auxiliary space complexity O(n).
class Solution4:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        sorted_arr = sorted(arr)
        seen_frequencies = set()
        index = 0

        while index < len(sorted_arr):
            current_number = sorted_arr[index]
            count = 0

            while (
                index < len(sorted_arr)
                and sorted_arr[index] == current_number
            ):
                count += 1
                index += 1

            if count in seen_frequencies:
                return False

            seen_frequencies.add(count)

        return True


# ============================================================


# Approach 5: Brute Force Using count()
# Time Complexity: O(n^2)
# Space Complexity: O(k)
#
# Time Explanation:
# Prati unique number kosam arr.count() complete array ni scan chestundi.
# Worst case lo k nearly n unique values undavachu.
# Kabatti worst-case time complexity O(n^2).
#
# Space Explanation:
# Unique numbers mariyu frequencies sets lo store chestunnam.
# Kabatti auxiliary space complexity O(k).
class Solution5:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        unique_numbers = set(arr)
        seen_frequencies = set()

        for num in unique_numbers:
            count = arr.count(num)

            if count in seen_frequencies:
                return False

            seen_frequencies.add(count)

        return True
