
# 1. Two Sum
def two_sum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        if target - num in hashmap:
            return [hashmap[target - num], i]
        hashmap[num] = i


# 2. Longest Substring Without Repeating Characters
def length_of_longest_substring(s):
    char_set = set()
    left = 0
    max_len = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len


# 3. Valid Parentheses
def is_valid_parentheses(s):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in mapping:
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else:
            stack.append(char)
    return not stack


# 4. Merge Two Sorted Lists
def mergeTwoLists(l1, l2):
    dummy = curr = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 or l2
    return dummy.next


# 5. Remove Nth Node From End of List
def removeNthFromEnd(head, n):
    dummy = ListNode(0, head)
    fast = slow = dummy
    for _ in range(n):
        fast = fast.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy.next


# 6. Merge Intervals
def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged


# 7. Insert Interval
def insert(intervals, newInterval):
    res = []
    for i in intervals:
        if i[1] < newInterval[0]:
            res.append(i)
        elif i[0] > newInterval[1]:
            res.append(newInterval)
            newInterval = i
        else:
            newInterval[0] = min(newInterval[0], i[0])
            newInterval[1] = max(newInterval[1], i[1])
    res.append(newInterval)
    return res


# 8. Valid Palindrome
def isPalindrome(s):
    filtered = [c.lower() for c in s if c.isalnum()]
    return filtered == filtered[::-1]


# 9. Longest Palindrome
def longestPalindrome(s):
    res = ""
    for i in range(len(s)):
        tmp = expand(s, i, i)
        if len(tmp) > len(res):
            res = tmp
        tmp = expand(s, i, i + 1)
        if len(tmp) > len(res):
            res = tmp
    return res


def expand(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1:right]


# 10. Longest Common Prefix
def longestCommonPrefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
    return prefix


# 11. Climbing Stairs
def climbStairs(n):
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b


# 12. Maximum Subarray
def maxSubArray(nums):
    curr_sum = max_sum = nums[0]
    for num in nums[1:]:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
    return max_sum


# 13. Best Time to Buy and Sell Stock
def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit


# 14. Linked List Cycle
def hasCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


# 15. Intersection of Two Linked Lists
def getIntersectionNode(headA, headB):
    a, b = headA, headB
    while a != b:
        a = a.next if a else headB
        b = b.next if b else headA
    return a


# 16. Reverse Linked List
def reverseList(head):
    prev = None
    curr = head
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    return prev


# 17. Maximum Depth of Binary Tree
def maxDepth(root):
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))


# 18. Same Tree
def isSameTree(p, q):
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


# 19. Symmetric Tree
def isSymmetric(root):
    def isMirror(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2 or t1.val != t2.val:
            return False
        return isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)

    return isMirror(root, root)


# 20. Binary Tree Level Order Traversal
def levelOrder(root):
    res = []
    if not root:
        return res
    queue = [root]
    while queue:
        res.append([node.val for node in queue])
        queue = [child for node in queue for child in (node.left, node.right) if child]
    return res


# 21. Validate Binary Search Tree
def isValidBST(root):
    def helper(node, low, high):
        if not node:
            return True
        if node.val <= low or node.val >= high:
            return False
        return helper(node.left, low, node.val) and helper(node.right, node.val, high)

    return helper(root, float('-inf'), float('inf'))


# 22. Minimum Depth of Binary Tree
def minDepth(root):
    if not root:
        return 0
    if not root.left:
        return 1 + minDepth(root.right)
    if not root.right:
        return 1 + minDepth(root.left)
    return 1 + min(minDepth(root.left), minDepth(root.right))


# 23. Convert Sorted Array to BST
def sortedArrayToBST(nums):
    if not nums:
        return None
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid + 1:])
    return root


# 24. Path Sum
def hasPathSum(root, targetSum):
    if not root:
        return False
    if not root.left and not root.right and root.val == targetSum:
        return True
    return hasPathSum(root.left, targetSum - root.val) or hasPathSum(root.right, targetSum - root.val)


# 25. Invert Binary Tree
def invertTree(root):
    if root:
        root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root


# 26. Maximum Path Sum
def maxPathSum(root):
    max_sum = float('-inf')

    def dfs(node):
        nonlocal max_sum
        if not node:
            return 0
        left = max(dfs(node.left), 0)
        right = max(dfs(node.right), 0)
        max_sum = max(max_sum, left + right + node.val)
        return max(left, right) + node.val

    dfs(root)
    return max_sum


# 27. Binary Tree Zigzag Level Order Traversal
def zigzagLevelOrder(root):
    res = []
    if not root:
        return res
    queue, level = [root], 0
    while queue:
        level_nodes = [node.val for node in queue]
        if level % 2:
            level_nodes.reverse()
        res.append(level_nodes)
        queue = [child for node in queue for child in (node.left, node.right) if child]
        level += 1
    return res


# 28. Subtree of Another Tree
def isSubtree(s, t):
    if not s:
        return False
    if isSameTree(s, t):
        return True
    return isSubtree(s.left, t) or isSubtree(s.right, t)


# Helper for isSubtree
def isSameTree(p, q):
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


# 29. Lowest Common Ancestor of a Binary Tree
def lowestCommonAncestor(root, p, q):
    if not root or root == p or root == q:
        return root
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    if left and right:
        return root
    return left or right


# 30. Number of Islands
def numIslands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
            return
        grid[r][c] = '0'
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                dfs(r, c)
    return count


# 31. Word Search
def exist(board, word):
    rows, cols = len(board), len(board[0])

    def dfs(r, c, i):
        if i == len(word):
            return True
        if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i]:
            return False
        tmp, board[r][c] = board[r][c], '#'
        found = (dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1))
        board[r][c] = tmp
        return found

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    return False


# 32. Combination Sum
def combinationSum(candidates, target):
    res = []

    def backtrack(start, path, target):
        if target == 0:
            res.append(path[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] <= target:
                path.append(candidates[i])
                backtrack(i, path, target - candidates[i])
                path.pop()

    backtrack(0, [], target)
    return res


# 33. Permutations
def permute(nums):
    res = []

    def backtrack(path, remaining):
        if not remaining:
            res.append(path[:])
            return
        for i in range(len(remaining)):
            backtrack(path + [remaining[i]], remaining[:i] + remaining[i + 1:])

    backtrack([], nums)
    return res


# 34. Subsets
def subsets(nums):
    res = []

    def backtrack(start, path):
        res.append(path[:])
        for i in range(start, len(nums)):
            backtrack(i + 1, path + [nums[i]])

    backtrack(0, [])
    return res


# 35. Unique Paths
def uniquePaths(m, n):
    dp = [[1] * n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[-1][-1]


# 36. Longest Increasing Subsequence
def lengthOfLIS(nums):
    dp = []
    for num in nums:
        left, right = 0, len(dp)
        while left < right:
            mid = (left + right) // 2
            if dp[mid] < num:
                left = mid + 1
            else:
                right = mid
        if left == len(dp):
            dp.append(num)
        else:
            dp[left] = num
    return len(dp)


# 37. Coin Change
def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1


# 38. House Robber
def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    prev1, prev2 = 0, 0
    for num in nums:
        tmp = prev1
        prev1 = max(prev2 + num, prev1)
        prev2 = tmp
    return prev1


# 39. Maximum Product Subarray
def maxProduct(nums):
    res = curr_max = curr_min = nums[0]
    for num in nums[1:]:
        temp_max = max(num, curr_max * num, curr_min * num)
        curr_min = min(num, curr_max * num, curr_min * num)
        curr_max = temp_max
        res = max(res, curr_max)
    return res


# 40. Find Minimum in Rotated Sorted Array
def findMin(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]


# 41. Find All Duplicates in an Array
def findDuplicates(nums):
    res = []
    for num in nums:
        index = abs(num) - 1
        if nums[index] < 0:
            res.append(abs(num))
        else:
            nums[index] = -nums[index]
    return res


# 41. Find All Duplicates in an Array
assert findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]) == [2, 3]
assert findDuplicates([1, 1, 2]) == [1]
assert findDuplicates([1]) == []


# 42. Missing Number
def missingNumber(nums):
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)


# 43. Missing Ranges
def findMissingRanges(nums, lower, upper):
    res = []
    prev = lower - 1
    nums.append(upper + 1)
    for num in nums:
        if num - prev == 2:
            res.append(str(prev + 1))
        elif num - prev > 2:
            res.append(f"{prev + 1}->{num - 1}")
        prev = num
    return res


# 44. Binary Tree Right Side View
from collections import deque


def rightSideView(root):
    if not root:
        return []
    res, queue = [], deque([root])
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            if i == level_size - 1:
                res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return res


# 45. Sum Root to Leaf Numbers
def sumNumbers(root):
    def dfs(node, curr_sum):
        if not node:
            return 0
        curr_sum = curr_sum * 10 + node.val
        if not node.left and not node.right:
            return curr_sum
        return dfs(node.left, curr_sum) + dfs(node.right, curr_sum)

    return dfs(root, 0)


# 46. Reorder List
def reorderList(head):
    if not head:
        return
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    second = slow.next
    slow.next = None
    prev = None
    while second:
        tmp = second.next
        second.next = prev
        prev = second
        second = tmp
    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2


# 47. Odd Even Linked List
def oddEvenList(head):
    if not head:
        return head
    odd, even = head, head.next
    even_head = even
    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
    odd.next = even_head
    return head


# 48. Count Primes
def countPrimes(n):
    if n < 2:
        return 0
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n, i):
                is_prime[j] = False
    return sum(is_prime)


# 49. Reverse Bits
def reverseBits(n):
    res = 0
    for i in range(32):
        res = (res << 1) | (n & 1)
        n >>= 1
    return res


# 50. Hamming Distance
def hammingDistance(x, y):
    xor = x ^ y
    count = 0
    while xor:
        count += xor & 1
        xor >>= 1
    return count

# End of full Python Interview Guide: 50 Problems
