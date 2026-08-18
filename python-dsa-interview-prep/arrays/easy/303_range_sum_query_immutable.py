# LeetCode 303 - Range Sum Query - Immutable
# Difficulty: Easy


# Approach 1: Slicing + sum()
# Your Approach
# __init__ Time Complexity: O(1)
# sumRange Time Complexity: O(n) worst case
# Space Complexity: O(n) for stored nums + O(k) temporary slice
class NumArraySlicing:

    def __init__(self, nums):
        self.nums = nums

    def sumRange(self, left, right):
        return sum(self.nums[left:right + 1])


# Approach 2: sum() Without Slicing
# Avoids creating a temporary sliced list
# __init__ Time Complexity: O(1)
# sumRange Time Complexity: O(n) worst case
# Extra Space Complexity per query: O(1)
class NumArrayDirectSum:

    def __init__(self, nums):
        self.nums = nums

    def sumRange(self, left, right):
        total = 0

        for i in range(left, right + 1):
            total += self.nums[i]

        return total


# Approach 3: Prefix Sum
# Recommended / Optimal
# __init__ Time Complexity: O(n)
# sumRange Time Complexity: O(1)
# Space Complexity: O(n)
class NumArrayPrefixSum:

    def __init__(self, nums):
        self.prefix = [0]

        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, left, right):
        return self.prefix[right + 1] - self.prefix[left]


# Approach 4: Prefix Sum In Same-Length Array
# __init__ Time Complexity: O(n)
# sumRange Time Complexity: O(1)
# Space Complexity: O(n)
class NumArrayPrefixSameLength:

    def __init__(self, nums):
        self.prefix = nums[:]

        for i in range(1, len(self.prefix)):
            self.prefix[i] += self.prefix[i - 1]

    def sumRange(self, left, right):
        if left == 0:
            return self.prefix[right]

        return self.prefix[right] - self.prefix[left - 1]
