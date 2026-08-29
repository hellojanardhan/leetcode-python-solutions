# LeetCode 217 - Contains Duplicate
# Difficulty: Easy
# Recommended Approach: HashSet
# Recommended Current-Level Approach: HashSet


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: HashSet - Seen Before
# Your Approach
# Recommended Optimal Approach
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Time Explanation:
# Array lo unna prati number ni okasari check chestunnam.
# Set lookup mariyu insertion average-ga O(1) untundi.
# Kabatti total time complexity O(n).
#
# Space Explanation:
# Duplicates lekapothe maximum n unique numbers set lo store avutayi.
# Kabatti auxiliary space complexity O(n).
class Solution1:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True

            seen.add(num)

        return False


# ============================================================


# Approach 2: Convert List to Set
# Recommended Shortest Approach
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Time Explanation:
# nums nunchi set create cheyadaniki anni n elements process chestundi.
# List length mariyu set length compare cheyadam O(1).
# Kabatti total time complexity O(n).
#
# Space Explanation:
# Set lo maximum n unique values store avutayi.
# Kabatti auxiliary space complexity O(n).
class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


# ============================================================


# Approach 3: Sorting + Adjacent Comparison
# Time Complexity: O(n log n)
# Space Complexity: O(n) in Python
#
# Time Explanation:
# Array ni sort cheyadaniki O(n log n) time padutundi.
# Tarvata adjacent elements check cheyadaniki O(n) time padutundi.
# Kabatti total time complexity O(n log n).
#
# Space Explanation:
# sorted(nums) kotta sorted list create chestundi.
# Andulo n elements store avutayi.
# Kabatti auxiliary space complexity O(n).
class Solution3:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sorted_nums = sorted(nums)

        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] == sorted_nums[i - 1]:
                return True

        return False


# ============================================================
# OTHER POSSIBLE SOLUTIONS
# ============================================================


# Approach 4: Frequency HashMap
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Time Explanation:
# Prati number frequency ni dictionary lo update chestunnam.
# Dictionary lookup mariyu update average-ga O(1).
# Kabatti total time complexity O(n).
#
# Space Explanation:
# Maximum n unique numbers dictionary lo store avvachu.
# Kabatti auxiliary space complexity O(n).
class Solution4:
    def containsDuplicate(self, nums: List[int]) -> bool:
        frequency = {}

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

            if frequency[num] > 1:
                return True

        return False


# ============================================================


# Approach 5: Brute Force
# Time Complexity: O(n^2)
# Space Complexity: O(1)
#
# Time Explanation:
# Prati number ni migilina numbers annitito compare chestunnam.
# Worst case lo nearly n * n comparisons jarugutayi.
# Kabatti time complexity O(n^2).
#
# Space Explanation:
# Additional data structure create cheyadam ledu.
# Konni variables maatrame use chestunnam.
# Kabatti auxiliary space complexity O(1).
class Solution5:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True

        return False
