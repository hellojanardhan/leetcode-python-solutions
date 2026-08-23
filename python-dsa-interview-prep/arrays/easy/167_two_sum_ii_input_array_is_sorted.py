# LeetCode 167 - Two Sum II - Input Array Is Sorted
# Difficulty: Medium


# Approach 1: Two Pointers
# Your Approach - Recommended / Optimal
# Time Complexity: O(n)
# Space Complexity: O(1)
def two_sum_two_pointers(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum > target:
            right -= 1
        elif current_sum < target:
            left += 1
        else:
            return [left + 1, right + 1]


# Approach 2: Binary Search
# Time Complexity: O(n log n)
# Space Complexity: O(1)
def two_sum_binary_search(numbers, target):
    for i in range(len(numbers)):
        required = target - numbers[i]

        left = i + 1
        right = len(numbers) - 1

        while left <= right:
            mid = (left + right) // 2

            if numbers[mid] == required:
                return [i + 1, mid + 1]

            elif numbers[mid] < required:
                left = mid + 1

            else:
                right = mid - 1


# Approach 3: Hash Map
# Time Complexity: O(n)
# Space Complexity: O(n)
def two_sum_hashmap(numbers, target):
    seen = {}

    for i, num in enumerate(numbers):
        required = target - num

        if required in seen:
            return [seen[required] + 1, i + 1]

        seen[num] = i


# Approach 4: Brute Force
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def two_sum_bruteforce(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
