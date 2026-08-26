# LeetCode 202 - Happy Number
# Difficulty: Easy
# Recommended Approach: Floyd's Cycle Detection
# Recommended Current-Level Approach: Iterative HashSet


# Approach 1: Floyd's Cycle Detection - Optimal Solution
# Time Complexity: O(log n)
# Number lo unna digits ni process cheyadaniki O(log n) time paduthundi.
# slow and fast pointers cycle vachhe varaku limited sequence ni process chesthayi.
# Space Complexity: O(1)
# slow, fast, total ane konni variables mathrame use chesthunnam.
class Solution1:
    def isHappy(self, n: int) -> bool:
        def get_next(number):
            total = 0

            while number > 0:
                digit = number % 10
                total += digit ** 2
                number //= 10

            return total

        slow = n
        fast = get_next(n)

        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))

        return fast == 1


# Approach 2: Iterative HashSet
# Time Complexity: O(log n)
# Prathi number lo unna digits ni process chestham.
# Number 1 ki reach avuthundi leda cycle lo enter avuthundi.
# Space Complexity: O(log n)
# Already process chesina numbers ni seen set lo store chesthunnam.
class Solution2:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)

            total = 0

            while n > 0:
                digit = n % 10
                total += digit ** 2
                n //= 10

            n = total

        return n == 1


# Approach 3: Your Approach - Recursive HashSet
# Time Complexity: O(log n)
# Prathi recursive call lo number digits squares total ni calculate chestham.
# Number 1 ki reach avuthundi leda repeated number ni find chestham.
# Space Complexity: O(log n)
# Visited numbers seen set lo mariyu recursive calls call stack lo
# store avuthayi.
class Solution3:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def check(number):
            if number == 1:
                return True

            if number in seen:
                return False

            seen.add(number)

            total = 0

            for digit in str(number):
                total += int(digit) ** 2

            return check(total)

        return check(n)


# Approach 4: Detect the Known Cycle at 4
# Time Complexity: O(log n)
# Prathi number digits squares total ni calculate chestham.
# Sequence 1 ki reach ayithe happy number, 4 ki reach ayithe cycle start avuthundi.
# Space Complexity: O(1)
# Set leda additional data structure create cheyadam ledu.
class Solution4:
    def isHappy(self, n: int) -> bool:
        while n != 1 and n != 4:
            total = 0

            while n > 0:
                digit = n % 10
                total += digit ** 2
                n //= 10

            n = total

        return n == 1


# Approach 5: Iterative HashSet Using String Conversion
# Time Complexity: O(log n)
# Number ni string ga convert chesi prathi digit square ni calculate chestham.
# Cycle detect ayye varaku process continue avuthundi.
# Space Complexity: O(log n)
# Process chesina numbers ni seen set lo store chesthunnam.
class Solution5:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False

            seen.add(n)

            n = sum(int(digit) ** 2 for digit in str(n))

        return True
