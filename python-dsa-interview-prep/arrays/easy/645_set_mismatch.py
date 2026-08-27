# LeetCode 645 - Set Mismatch
# Difficulty: Easy
# Recommended Approach: Negative Marking
# Recommended Current-Level Approach: Negative Marking

from typing import List


# Approach 1: Your Approach - Negative Marking
# Time Complexity: O(n)
# Array ni rendu sarlu traverse chesthunnam. Kabatti total time O(n).
# Space Complexity: O(1) Auxiliary
# result output ni exclude chesthe, additional data structure create cheyadam ledu.
class Solution1:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(len(nums)):
            index = abs(nums[i]) - 1

            if nums[index] > 0:
                nums[index] = -nums[index]
            else:
                result.append(index + 1)

        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)

        return result


# Approach 2: Mathematical Equations
# Time Complexity: O(n)
# Actual sum mariyu square sum calculate cheyadaniki array ni okkasari traverse chesthunnam.
# Space Complexity: O(1)
# Konni mathematical variables mathrame use chesthunnam.
class Solution2:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        expected_square_sum = n * (n + 1) * (2 * n + 1) // 6
        actual_sum = sum(nums)
        actual_square_sum = sum(num * num for num in nums)

        difference = actual_sum - expected_sum
        square_difference = actual_square_sum - expected_square_sum
        duplicate_plus_missing = square_difference // difference
        duplicate = (difference + duplicate_plus_missing) // 2
        missing = duplicate_plus_missing - duplicate

        return [duplicate, missing]


# Approach 3: XOR
# Time Complexity: O(n)
# nums values mariyu 1 nunchi n values ni XOR chesthunnam.
# Taruvatha duplicate ni identify cheyadaniki array ni marokasari check chesthunnam.
# Space Complexity: O(1)
# Konni XOR mariyu counter variables mathrame use chesthunnam.
class Solution3:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        xor_value = 0
        n = len(nums)

        for i in range(n):
            xor_value ^= nums[i]
            xor_value ^= i + 1

        rightmost_bit = xor_value & -xor_value
        first = 0
        second = 0

        for i in range(n):
            if nums[i] & rightmost_bit:
                first ^= nums[i]
            else:
                second ^= nums[i]

            if (i + 1) & rightmost_bit:
                first ^= i + 1
            else:
                second ^= i + 1

        count = 0

        for num in nums:
            if num == first:
                count += 1

        if count == 2:
            return [first, second]

        return [second, first]


# Approach 4: HashSet and Sum
# Time Complexity: O(n)
# Prathi number ni seen set lo check chesi duplicate ni find chesthunnam.
# Space Complexity: O(n)
# Unique numbers ni seen set lo store chesthunnam.
class Solution4:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set()
        duplicate = -1

        for num in nums:
            if num in seen:
                duplicate = num
            else:
                seen.add(num)

        expected_sum = len(nums) * (len(nums) + 1) // 2
        missing = expected_sum - sum(seen)

        return [duplicate, missing]


# Approach 5: Frequency Array
# Time Complexity: O(n)
# Frequency array build chesi, duplicate mariyu missing values ni check chesthunnam.
# Space Complexity: O(n)
# n + 1 positions unna frequency array ni create chesthunnam.
class Solution5:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        frequency = [0] * (len(nums) + 1)
        duplicate = -1
        missing = -1

        for num in nums:
            frequency[num] += 1

        for num in range(1, len(nums) + 1):
            if frequency[num] == 2:
                duplicate = num

            if frequency[num] == 0:
                missing = num

        return [duplicate, missing]


# Approach 6: Sorting and Linear Scan
# Time Complexity: O(n log n)
# Sorting ki O(n log n), array scan cheyadaniki O(n) time paduthundi.
# Space Complexity: O(1) Auxiliary
# Python sort input list ni modify chesthundi.
# Internal sorting memory Python implementation meeda depend avuthundi.
class Solution6:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        duplicate = -1
        missing = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                duplicate = nums[i]
            elif nums[i] > nums[i - 1] + 1:
                missing = nums[i - 1] + 1

        if nums[-1] != len(nums):
            missing = len(nums)

        return [duplicate, missing]
