# LeetCode 15 - 3Sum
# Difficulty: Medium


# Approach 1: Brute Force
# Time Complexity: O(n^3)
# Space Complexity: O(k)
# k = number of unique triplets stored
def three_sum_bruteforce(nums):
    nums.sort()
    result = []

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = [nums[i], nums[j], nums[k]]

                    if triplet not in result:
                        result.append(triplet)

    return result


# Approach 2: Sorting + Two Pointers
# Recommended / Optimal Interview Solution
# Time Complexity: O(n^2)
# Space Complexity: O(1) auxiliary
# Output space is not counted
def three_sum_two_pointers(nums):
    nums.sort()
    result = []

    for i in range(len(nums) - 2):

        # Skip duplicate fixed values
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum < 0:
                left += 1

            elif current_sum > 0:
                right -= 1

            else:
                result.append([
                    nums[i],
                    nums[left],
                    nums[right]
                ])

                left += 1
                right -= 1

                # Skip duplicate left values
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                # Skip duplicate right values
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

    return result


# Approach 3: Hash Set for Two Sum
# Fix one number, then solve remaining pair using a set
# Time Complexity: O(n^2)
# Space Complexity: O(n)
def three_sum_hashset(nums):
    nums.sort()
    result = set()

    for i in range(len(nums) - 2):
        seen = set()

        for j in range(i + 1, len(nums)):
            required = -(nums[i] + nums[j])

            if required in seen:
                result.add(
                    (nums[i], required, nums[j])
                )

            seen.add(nums[j])

    return [list(triplet) for triplet in result]
