# LeetCode 1089 - Duplicate Zeros
# Difficulty: Easy


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: Backward Two Pointers / Read-Write
# Your Approach
# Recommended / Optimal
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution1:
    def duplicateZeros(self, arr: List[int]) -> None:

        zeros = arr.count(0)

        read = len(arr) - 1
        write = len(arr) + zeros - 1

        while read >= 0:

            if arr[read] == 0:

                if write < len(arr):
                    arr[write] = 0

                write -= 1

                if write < len(arr):
                    arr[write] = 0

                write -= 1

            else:

                if write < len(arr):
                    arr[write] = arr[read]

                write -= 1

            read -= 1


# ============================================================


# Approach 2: Extra Array
# Simple and Easy to Understand
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution2:
    def duplicateZeros(self, arr: List[int]) -> None:

        result = []

        for num in arr:

            result.append(num)

            if num == 0:
                result.append(0)

        for i in range(len(arr)):
            arr[i] = result[i]


# ============================================================


# Approach 3: Boundary-Based Backward Two Pointers
# Optimal Alternative
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution3:
    def duplicateZeros(self, arr: List[int]) -> None:

        n = len(arr)

        possible_dups = 0
        last = n - 1

        read = 0

        while read <= last - possible_dups:

            if arr[read] == 0:

                if read == last - possible_dups:
                    arr[last] = 0
                    last -= 1
                    break

                possible_dups += 1

            read += 1

        read = last - possible_dups
        write = last

        while read >= 0:

            if arr[read] == 0:

                arr[write] = 0
                write -= 1

                arr[write] = 0
                write -= 1

            else:

                arr[write] = arr[read]
                write -= 1

            read -= 1


# ============================================================
# REMAINING SOLUTIONS
# ============================================================


# Approach 4: Insert + Pop
# Simple but Inefficient
# Time Complexity: O(n^2)
# Space Complexity: O(1)
class Solution4:
    def duplicateZeros(self, arr: List[int]) -> None:

        read = 0

        while read < len(arr):

            if arr[read] == 0:

                arr.insert(read, 0)
                arr.pop()

                read += 2

            else:

                read += 1


# ============================================================


# Approach 5: Extra Array with Size Limit
# Avoids Building More Than Required
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution5:
    def duplicateZeros(self, arr: List[int]) -> None:

        result = []

        for num in arr:

            if len(result) >= len(arr):
                break

            result.append(num)

            if num == 0 and len(result) < len(arr):
                result.append(0)

        for i in range(len(arr)):
            arr[i] = result[i]
