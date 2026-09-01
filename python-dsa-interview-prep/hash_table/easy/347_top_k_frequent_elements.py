# LeetCode 347 - Top K Frequent Elements
# Difficulty: Medium

# Recommended Optimal Approach: Frequency HashMap + Bucket Sort
# Recommended Current-Level Approach: Frequency HashMap + Sorting

# n = total number of elements
# u = number of unique elements
# k = number of elements to return
#
# Dictionary operations use average-case complexity.
# Space complexities include result construction.


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: Frequency HashMap + Sort Unique Numbers
# Your Approach
# Time Complexity: O(n + u log u)
# Space Complexity: O(u)
#
# Time Explanation:
# Array frequencies build cheyadaniki O(n).
# u unique numbers ni frequency prakaram sort cheyadaniki O(u log u).
# First k elements slice cheyadaniki O(k).
# k <= u kabatti total O(n + u log u).
#
# Space Explanation:
# Frequency dictionary and sorted keys list kosam O(u).
# Returned slice kosam O(k).
# k <= u kabatti total O(u).
class Solution1:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for number in nums:
            frequency[number] = frequency.get(number, 0) + 1

        sorted_numbers = sorted(
            frequency,
            key=frequency.get,
            reverse=True
        )

        return sorted_numbers[:k]


# ============================================================


# Approach 2: Frequency HashMap + Bucket Sort
# Recommended Optimal Approach
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Time Explanation:
# Frequencies build cheyadaniki O(n).
# n + 1 buckets create cheyadaniki O(n).
# u unique numbers ni corresponding buckets lo add chestunnam.
# Highest frequency nunchi buckets traverse chestunnam.
# Total O(n + u), simplified-ga O(n).
#
# Space Explanation:
# n + 1 bucket lists and frequency dictionary use chestunnam.
# Kabatti total additional space O(n).
#
# Logic:
# Bucket index = frequency
# Bucket value = aa frequency unna numbers list
#
# Example:
# nums = [1, 1, 1, 2, 2, 3]
# k = 2
#
# buckets[3] = [1]
# buckets[2] = [2]
# buckets[1] = [3]
#
# Highest frequencies nunchi first 2 numbers:
# [1, 2]
class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for number in nums:
            frequency[number] = frequency.get(number, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for number, count in frequency.items():
            buckets[count].append(number)

        result = []

        for count in range(len(nums), 0, -1):
            for number in buckets[count]:
                result.append(number)

                if len(result) == k:
                    return result

        return result


# ============================================================


# Approach 3: Frequency HashMap + Size-k Min-Heap
# Useful When k Is Small Compared With u
# Time Complexity: O(n + u log(k + 1))
# Space Complexity: O(u + k), simplified to O(u)
#
# Time Explanation:
# Frequencies build cheyadaniki O(n).
# Prati unique number ni heap lo process chestunnam.
# Heap maximum k + 1 entries varaku untundi.
# Prati insertion/removal O(log(k + 1)).
#
# Space Explanation:
# Frequency dictionary O(u).
# Heap and result O(k).
# Frequency dictionary kuda count cheyali;
# total space O(k) maatrame kaadu.
#
# Logic:
# Heap lo top k candidates maintain chestunnam.
# k kante ekkuva candidates unte smallest frequency ni remove chestunnam.
#
# Note:
# Answer frequency order lo undalsina avasaram ledu.
# LeetCode any order accept chestundi.
class Solution3:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq

        frequency = {}

        for number in nums:
            frequency[number] = frequency.get(number, 0) + 1

        heap = []

        for number, count in frequency.items():
            heapq.heappush(heap, (count, number))

            if len(heap) > k:
                heapq.heappop(heap)

        return [
            number
            for count, number in heap
        ]


# ============================================================
# OTHER USEFUL SOLUTION
# ============================================================


# Approach 4: Counter + most_common(k)
# Short Python Approach
# Time Complexity: O(n + u log(k + 1))
# Space Complexity: O(u)
#
# Time Explanation:
# Counter frequencies calculate chestundi: O(n).
# most_common(k) top k frequent entries select chestundi.
# General bound O(u log(k + 1)).
#
# Space Explanation:
# Counter O(u).
# Selection and returned result kosam O(k).
# Total O(u), because k <= u.
class Solution4:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        frequency = Counter(nums)

        return [
            number
            for number, count in frequency.most_common(k)
        ]
