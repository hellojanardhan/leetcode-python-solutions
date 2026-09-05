# LeetCode 3005 - Count Elements With Maximum Frequency
# Difficulty: Easy
#
# Recommended Optimal Approach: One-Pass Frequency HashMap
# Recommended Current-Level Approach: Two-Pass Frequency HashMap


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: Two-Pass Frequency HashMap
# Your Approach — Cleaned
# Recommended Current-Level Approach
#
# Time Complexity: O(n)
# Space Complexity: O(u)
#
# Time Explanation:
# First loop lo n elements frequencies calculate chestunnam.
# Second loop lo u frequency values traverse chestunnam.
# O(n + u), u <= n kabatti O(n).
#
# Space Explanation:
# u unique numbers frequencies dictionary lo store avutayi.
# Kabatti auxiliary space O(u).

class Solution1:
    def maxFrequencyElements(
        self,
        nums: List[int]
    ) -> int:

        frequency = {}

        for number in nums:
            frequency[number] = (
                frequency.get(number, 0) + 1
            )

        maximum_frequency = max(frequency.values())
        result = 0

        for count in frequency.values():
            if count == maximum_frequency:
                result += count

        return result


# ============================================================


# Approach 2: One-Pass Frequency HashMap
# Recommended Optimal Approach
#
# Time Complexity: O(n)
# Space Complexity: O(u)
#
# Frequency update chestune maximum frequency
# mariyu result rendu maintain chestunnam.
#
# New maximum vasthe:
# Previous result invalid kabatti reset chestam.
#
# Same maximum vasthe:
# Current frequency ni result ki add chestam.

class Solution2:
    def maxFrequencyElements(
        self,
        nums: List[int]
    ) -> int:

        frequency = {}
        maximum_frequency = 0
        result = 0

        for number in nums:
            frequency[number] = (
                frequency.get(number, 0) + 1
            )

            current_frequency = frequency[number]

            if current_frequency > maximum_frequency:
                maximum_frequency = current_frequency
                result = current_frequency

            elif current_frequency == maximum_frequency:
                result += current_frequency

        return result


# ============================================================


# Approach 3: Fixed-Size Frequency Array
# Recommended Constraint-Specific Space Approach
#
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# nums[i] range 1 nunchi 100 varaku maatrame.
# Kabatti fixed 101-element array use cheyavachu.
#
# Input size perigina array size maaradu.
# Anduke space O(1).

class Solution3:
    def maxFrequencyElements(
        self,
        nums: List[int]
    ) -> int:

        frequency = [0] * 101

        for number in nums:
            frequency[number] += 1

        maximum_frequency = max(frequency)

        return sum(
            count
            for count in frequency
            if count == maximum_frequency
        )


# ============================================================
# OTHER USEFUL SOLUTIONS
# ============================================================


# Approach 4: collections.Counter
#
# Time Complexity: O(n)
# Space Complexity: O(u)
#
# Counter frequencies calculate chestundi.
# Tarvata maximum frequency unna counts ni sum chestunnam.

class Solution4:
    def maxFrequencyElements(
        self,
        nums: List[int]
    ) -> int:

        from collections import Counter

        frequency = Counter(nums)
        maximum_frequency = max(frequency.values())

        return sum(
            count
            for count in frequency.values()
            if count == maximum_frequency
        )


# ============================================================


# Approach 5: Sorting + Group Counting
#
# Time Complexity: O(n log n)
# Space Complexity: O(n)
#
# sorted() kotta sorted list create chestundi.
# Equal numbers adjacent positions lo untayi.
# Prati group frequency ni calculate chestunnam.

class Solution5:
    def maxFrequencyElements(
        self,
        nums: List[int]
    ) -> int:

        sorted_numbers = sorted(nums)

        maximum_frequency = 0
        result = 0
        index = 0

        while index < len(sorted_numbers):
            next_index = index

            while (
                next_index < len(sorted_numbers)
                and sorted_numbers[next_index]
                == sorted_numbers[index]
            ):
                next_index += 1

            current_frequency = next_index - index

            if current_frequency > maximum_frequency:
                maximum_frequency = current_frequency
                result = current_frequency

            elif current_frequency == maximum_frequency:
                result += current_frequency

            index = next_index

        return result
