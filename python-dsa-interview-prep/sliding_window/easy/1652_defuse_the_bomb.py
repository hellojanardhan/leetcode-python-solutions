# LeetCode 1652 - Defuse the Bomb
# Difficulty: Easy

# Recommended Approach: Fixed Sliding Window + Circular Indexing
# Recommended Current-Level Approach: Brute Force + Circular Modulo Indexing


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: Brute Force + Circular Modulo Indexing
# Your Approach
# Recommended Current-Level Approach
# Time Complexity: O(n * |k|)
# Space Complexity: O(n)
#
# Time Explanation:
# Array lo prati index i kosam next k values ledaa previous |k| values
# separately traverse chestunnam.
#
# Outer loop n times run avutundi.
# Inner loop maximum |k| times run avutundi.
# Kabatti total time complexity O(n * |k|).
#
# Circular array ni handle cheyadaniki modulo (%) use chestunnam.
#
# k > 0:
#     (i + j) % n
#
# k < 0:
#     (i - j) % n
#
# Space Explanation:
# n elements unna result array create chestunnam.
# total, index, i, j laanti variables constant extra space.
# Kabatti output/result array include cheste O(n) space.
class Solution1:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        result = [0] * n

        for i in range(n):
            total = 0

            if k > 0:
                for j in range(1, k + 1):
                    index = (i + j) % n
                    total += code[index]

                result[i] = total

            elif k < 0:
                for j in range(1, -k + 1):
                    index = (i - j) % n
                    total += code[index]

                result[i] = total

            if k == 0:
                result[i] = 0

        return result


# ============================================================


# Approach 2: Fixed Sliding Window + Circular Indexing
# Recommended Optimal Approach
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Time Explanation:
# First |k|-size window sum ni okasari calculate chestunnam.
#
# Tarvata window ni circular-ga move chestunnam.
# Prati move lo:
#
#     old element remove
#     new element add
#
# Kabatti prati window sum ni scratch nunchi calculate cheyyatledu.
#
# Initial window build O(|k|).
# Remaining n windows process cheyadaniki O(n).
#
# LeetCode constraints lo |k| < n kabatti total simplified-ga O(n).
#
# Space Explanation:
# Result array lo n decrypted values store chestunnam.
# Sliding window kosam few variables maatrame extra-ga use chestunnam.
# Kabatti total result space O(n),
# auxiliary working space O(1).
class Solution2:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        result = [0] * n

        if k == 0:
            return result

        if k > 0:
            window_sum = 0

            for index in range(1, k + 1):
                window_sum += code[index % n]

            result[0] = window_sum

            for i in range(1, n):
                outgoing = code[i % n]
                incoming = code[(i + k) % n]

                window_sum = window_sum - outgoing + incoming
                result[i] = window_sum

        else:
            window_size = -k
            window_sum = 0

            for index in range(1, window_size + 1):
                window_sum += code[-index % n]

            result[0] = window_sum

            for i in range(1, n):
                outgoing = code[(i - window_size - 1) % n]
                incoming = code[(i - 1) % n]

                window_sum = window_sum - outgoing + incoming
                result[i] = window_sum

        return result


# ============================================================


# Approach 3: Doubled Array + Prefix Sum
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Time Explanation:
# Circular wrap-around problem ni simplify cheyadaniki:
#
# code + code
#
# create chestunnam.
#
# Example:
# [5, 7, 1, 4]
#
# becomes:
# [5, 7, 1, 4, 5, 7, 1, 4]
#
# Tarvata prefix sum build chestunnam.
# Prefix array build O(n).
#
# Prati |k|-size range sum ni O(1) lo calculate chestunnam.
# Total n positions process chestunnam.
# Kabatti total time complexity O(n).
#
# Space Explanation:
# Doubled array approximately 2n elements.
# Prefix array approximately 2n + 1 elements.
# Result array n elements.
# Constants ignore cheste total O(n) space.
class Solution3:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)

        if k == 0:
            return [0] * n

        doubled = code + code
        prefix = [0] * (len(doubled) + 1)

        for i in range(len(doubled)):
            prefix[i + 1] = prefix[i] + doubled[i]

        result = [0] * n

        if k > 0:
            for i in range(n):
                left = i + 1
                right = i + k + 1

                result[i] = prefix[right] - prefix[left]

        else:
            window_size = -k

            shifted = code + code + code
            prefix = [0] * (len(shifted) + 1)

            for i in range(len(shifted)):
                prefix[i + 1] = prefix[i] + shifted[i]

            offset = n

            for i in range(n):
                current = offset + i

                left = current - window_size
                right = current

                result[i] = prefix[right] - prefix[left]

        return result


# ============================================================
# OTHER POSSIBLE SOLUTIONS
# ============================================================


# Approach 4: Doubled Array + Direct Window Sum
# Time Complexity: O(n * |k|)
# Space Complexity: O(n)
#
# Time Explanation:
# Circular indexing ni avoid cheyadaniki code array ni duplicate chestunnam.
#
# k > 0 case lo next values doubled array nunchi direct slice/range ga access cheyochu.
#
# Kaani prati index kosam |k| elements malli sum chestunnam.
# Kabatti time complexity O(n * |k|).
#
# Space Explanation:
# Doubled array O(n).
# Result array O(n).
# Kabatti total O(n).
class Solution4:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)

        if k == 0:
            return [0] * n

        result = [0] * n
        doubled = code + code

        if k > 0:
            for i in range(n):
                result[i] = sum(doubled[i + 1:i + k + 1])

        else:
            window_size = -k
            tripled = code + code + code
            offset = n

            for i in range(n):
                current = offset + i
                result[i] = sum(
                    tripled[current - window_size:current]
                )

        return result


# ============================================================


# Approach 5: Brute Force with Manual Circular Reset
# Time Complexity: O(n * |k|)
# Space Complexity: O(n)
#
# Time Explanation:
# Modulo operator use cheyakunda index ni manually circular-ga reset chestunnam.
#
# k > 0:
# index n reach ayite index = 0
#
# k < 0:
# index -1 kante takkuva ayite index = n - 1
#
# Outer loop O(n).
# Inner traversal O(|k|).
# Kabatti total O(n * |k|).
#
# Space Explanation:
# Result array O(n).
# Remaining variables O(1).
# Kabatti total O(n).
class Solution5:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        result = [0] * n

        if k == 0:
            return result

        for i in range(n):
            total = 0

            if k > 0:
                index = i + 1

                for _ in range(k):
                    if index == n:
                        index = 0

                    total += code[index]
                    index += 1

            else:
                index = i - 1

                for _ in range(-k):
                    if index < 0:
                        index = n - 1

                    total += code[index]
                    index -= 1

            result[i] = total

        return result
