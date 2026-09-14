# LeetCode 2461 - Maximum Sum of Distinct Subarrays With Length K
# Difficulty: Medium

# Recommended Approach: Fixed Sliding Window + Frequency HashMap + Running Sum
# Recommended Current-Level Approach: Fixed Sliding Window + Frequency HashMap


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: Fixed Sliding Window + Frequency HashMap + Running Sum
# Your Approach
# Recommended Optimal Approach
# Time Complexity: O(n)
# Space Complexity: O(k)
#
# Time Explanation:
# First k-size window ni build chestunnam.
#
# First window kosam:
# frequency map build -> O(k)
# sum calculate      -> O(k)
#
# Tarvata remaining n-k elements kosam window slide chestundi.
#
# Prati window movement lo:
#
# outgoing number ni sum nunchi remove
# outgoing frequency -= 1
# zero ayithe dictionary nunchi delete
#
# incoming frequency += 1
# incoming number ni sum ki add
#
# Dictionary get/update/delete average-ga O(1).
#
# Kabatti:
#
# O(k) + O(n-k)
# = O(n)
#
# Space Explanation:
# current_freq dictionary lo current window values maatrame maintain chestunnam.
#
# Maximum k distinct values undachu.
#
# Kabatti:
# O(k)
class Solution1:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        current_sum = 0
        current_freq = {}

        for i in range(k):
            current_freq[nums[i]] = current_freq.get(nums[i], 0) + 1
            current_sum += nums[i]

        maximum = 0

        if len(current_freq) == k:
            maximum = current_sum

        for j in range(k, len(nums)):
            outgoing_number = nums[j - k]
            incoming_number = nums[j]

            # Remove outgoing number from sum
            current_sum -= outgoing_number

            # Remove outgoing number from frequency
            current_freq[outgoing_number] -= 1

            if current_freq[outgoing_number] == 0:
                del current_freq[outgoing_number]

            # Add incoming number
            current_freq[incoming_number] = (
                current_freq.get(incoming_number, 0) + 1
            )

            current_sum += incoming_number

            # k distinct values unnappudu maatrame valid window
            if len(current_freq) == k:
                maximum = max(maximum, current_sum)

        return maximum


# ============================================================


# Approach 2: Sliding Window + HashMap + Duplicate Counter
# Time Complexity: O(n)
# Space Complexity: O(k)
#
# Time Explanation:
# Same sliding-window concept.
#
# But prati sari:
#
# len(freq) == k
#
# ani check cheyyadam badulu,
# current window lo duplicate values unnaya ani duplicate_count maintain chestam.
#
# Frequency 1 -> 2 ayithe:
# duplicate_count += 1
#
# Frequency 2 -> 1 ayithe:
# duplicate_count -= 1
#
# duplicate_count == 0 ante
# current window lo all elements distinct.
#
# Every number once enters and once leaves.
#
# Total O(n).
#
# Space Explanation:
# Frequency map maximum k current-window values store chestundi.
# So O(k).
class Solution2:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq = {}
        current_sum = 0
        maximum = 0
        duplicate_count = 0

        for i in range(k):
            num = nums[i]

            freq[num] = freq.get(num, 0) + 1

            if freq[num] == 2:
                duplicate_count += 1

            current_sum += num

        if duplicate_count == 0:
            maximum = current_sum

        for right in range(k, len(nums)):
            outgoing = nums[right - k]
            incoming = nums[right]

            current_sum -= outgoing

            if freq[outgoing] == 2:
                duplicate_count -= 1

            freq[outgoing] -= 1

            if freq[outgoing] == 0:
                del freq[outgoing]

            freq[incoming] = freq.get(incoming, 0) + 1

            if freq[incoming] == 2:
                duplicate_count += 1

            current_sum += incoming

            if duplicate_count == 0:
                maximum = max(maximum, current_sum)

        return maximum


# ============================================================


# Approach 3: Check Every k-Size Window Using Set
# Brute Force Approach
# Time Complexity: O((n-k+1) * k)
# Space Complexity: O(k)
#
# Time Explanation:
# Prati k-size window ni separately process chestunnam.
#
# Window ni set ga convert chestam.
#
# len(set(window)) == k ayithe
# all elements distinct.
#
# Tarvata sum calculate chestam.
#
# Each window:
# set creation -> O(k)
# sum          -> O(k)
#
# Total windows:
# n-k+1
#
# Total:
# O((n-k+1) * k)
#
# Simplified:
# O(n * k)
#
# Space Explanation:
# Window slice + set maximum k elements store chestayi.
# So O(k).
class Solution3:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        maximum = 0

        for i in range(len(nums) - k + 1):
            window = nums[i:i + k]

            if len(set(window)) == k:
                maximum = max(
                    maximum,
                    sum(window)
                )

        return maximum


# ============================================================
# OTHER POSSIBLE SOLUTIONS
# ============================================================


# Approach 4: Prefix Sum + Set Check
# Time Complexity: O((n-k+1) * k)
# Space Complexity: O(n + k)
#
# Prefix sum valla each window sum O(1) lo calculate cheyochu.
#
# Kaani distinct elements check cheyyadaniki
# every window ki set create chestunnam -> O(k).
#
# Kabatti total time still O(n * k).
class Solution4:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        maximum = 0

        for left in range(n - k + 1):
            right = left + k

            window = nums[left:right]

            if len(set(window)) == k:
                current_sum = prefix[right] - prefix[left]
                maximum = max(maximum, current_sum)

        return maximum
