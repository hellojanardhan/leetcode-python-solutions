# LeetCode 11 - Container With Most Water
# Difficulty: Medium


# Approach 1: Brute Force
# Check every possible pair of lines
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def max_area_brute_force(height):
    maximum = 0

    for left in range(len(height)):
        for right in range(left + 1, len(height)):

            width = right - left
            container_height = min(height[left], height[right])

            water = width * container_height

            maximum = max(maximum, water)

    return maximum


# Approach 2: Two Pointers
# Your Approach - Recommended / Optimal
# Time Complexity: O(n)
# Space Complexity: O(1)
def max_area_two_pointers(height):
    left = 0
    right = len(height) - 1
    maximum = 0

    while left < right:

        width = right - left
        container_height = min(height[left], height[right])

        water = width * container_height

        maximum = max(maximum, water)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return maximum


# Approach 3: Two Pointers - Compact Version
# Same algorithm as Approach 2
# Time Complexity: O(n)
# Space Complexity: O(1)
def max_area_two_pointers_compact(height):
    left = 0
    right = len(height) - 1
    maximum = 0

    while left < right:

        maximum = max(
            maximum,
            (right - left) * min(height[left], height[right])
        )

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return maximum


# Approach 4: Recursive Two Pointers
# Same two-pointer idea implemented recursively
# Time Complexity: O(n)
# Space Complexity: O(n) due to recursion stack
def max_area_recursive(height):

    def helper(left, right, maximum):

        if left >= right:
            return maximum

        water = (
            (right - left)
            * min(height[left], height[right])
        )

        maximum = max(maximum, water)

        if height[left] < height[right]:
            return helper(left + 1, right, maximum)

        return helper(left, right - 1, maximum)

    return helper(0, len(height) - 1, 0)
