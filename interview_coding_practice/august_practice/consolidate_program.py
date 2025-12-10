"""
Top 10 Python Interview Programs - Medium Complexity
====================================================
Each program includes logic explanation in simple English
"""

from typing import List, Dict, Optional, Tuple
from collections import defaultdict, deque
import heapq
from functools import lru_cache


# Program 1: Find All Anagrams in a String
# ========================================

def find_anagrams(s: str, pattern: str) -> List[int]:
    """
    PROBLEM STATEMENT:
    Given a string s and a pattern p, find all starting indices of p's anagrams in s.
    An anagram is a word formed by rearranging letters of another word.

    EXAMPLE:
    Input: s = "abab", pattern = "ab"
    Output: [0, 2]
    Explanation:
    - At index 0: "ab" is anagram of "ab" ✓
    - At index 1: "ba" is anagram of "ab" ✓
    - At index 2: "ab" is anagram of "ab" ✓
    So we return [0, 2] (index 1 would be [1] but "ba" at index 1-2 overlaps)

    LOGIC IN SIMPLE ENGLISH:
    1. An anagram means same letters in different order (like "abc" and "bca")
    2. Use sliding window technique - move a window of pattern length across string
    3. Count letters in pattern and current window
    4. If counts match, we found an anagram - save the starting position
    5. Slide window: remove first character, add next character
    """

    if len(pattern) > len(s):
        return []

    result = []
    pattern_count = {}
    window_count = {}

    # Count letters in pattern
    for char in pattern:
        pattern_count[char] = pattern_count.get(char, 0) + 1

    window_size = len(pattern)

    # Process first window
    for i in range(window_size):
        char = s[i]
        window_count[char] = window_count.get(char, 0) + 1

    # Check if first window is anagram
    if window_count == pattern_count:
        result.append(0)

    # Slide window through rest of string
    for i in range(window_size, len(s)):
        # Add new character
        new_char = s[i]
        window_count[new_char] = window_count.get(new_char, 0) + 1

        # Remove old character
        old_char = s[i - window_size]
        window_count[old_char] -= 1
        if window_count[old_char] == 0:
            del window_count[old_char]

        # Check if current window is anagram
        if window_count == pattern_count:
            result.append(i - window_size + 1)

    return result


# Program 2: Merge Overlapping Intervals
# ======================================

def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    """
    PROBLEM STATEMENT:
    Given a collection of intervals, merge all overlapping intervals.
    Return the merged intervals in any order.

    EXAMPLE:
    Input: [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation:
    - [1,3] and [2,6] overlap → merge to [1,6]
    - [8,10] stands alone
    - [15,18] stands alone

    Another Example:
    Input: [[1,4],[4,5]]
    Output: [[1,5]]
    Explanation: [1,4] and [4,5] touch at point 4, so they merge

    LOGIC IN SIMPLE ENGLISH:
    1. Sort intervals by their start time
    2. Take first interval as current merged interval
    3. For each next interval:
       - If it overlaps with current (next start <= current end), merge them
       - If no overlap, save current and start new merged interval
    4. Don't forget to add the last merged interval
    """

    if not intervals:
        return []

    # Sort by start time
    intervals.sort(key=lambda x: x[0])

    merged = []
    current_start, current_end = intervals[0]

    for start, end in intervals[1:]:
        if start <= current_end:  # Overlapping
            current_end = max(current_end, end)  # Extend the end
        else:  # No overlap
            merged.append([current_start, current_end])
            current_start, current_end = start, end

    # Add the last interval
    merged.append([current_start, current_end])

    return merged


# Program 3: Longest Substring Without Repeating Characters
# =========================================================

def longest_unique_substring(s: str) -> int:
    """
    PROBLEM STATEMENT:
    Given a string, find the length of the longest substring without repeating characters.

    EXAMPLE:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The longest substring without repeating characters is "abc", length = 3

    Input: s = "bbbbb"
    Output: 1
    Explanation: The longest substring is "b", length = 1

    Input: s = "pwwkew"
    Output: 3
    Explanation: The longest substring is "wke", length = 3

    LOGIC IN SIMPLE ENGLISH:
    1. Use sliding window with two pointers (left and right)
    2. Keep track of characters we've seen and their positions
    3. Expand right pointer and add characters to our seen set
    4. If we see a repeated character:
       - Move left pointer to just after the previous occurrence
       - Update the position of repeated character
    5. Keep track of maximum window size seen so far
    """

    if not s:
        return 0

    char_positions = {}
    left = 0
    max_length = 0

    for right in range(len(s)):
        char = s[right]

        # If character was seen and is in current window
        if char in char_positions and char_positions[char] >= left:
            left = char_positions[char] + 1

        char_positions[char] = right
        max_length = max(max_length, right - left + 1)

    return max_length


# Program 4: Group Anagrams
# =========================

def group_anagrams(words: List[str]) -> List[List[str]]:
    """
    PROBLEM STATEMENT:
    Given an array of strings, group the anagrams together in any order.
    An anagram is a word formed by rearranging letters of another word.

    EXAMPLE:
    Input: ["eat","tea","tan","ate","nat","bat"]
    Output: [["eat","tea","ate"],["tan","nat"],["bat"]]
    Explanation:
    - "eat", "tea", "ate" are anagrams (same letters: e,a,t)
    - "tan", "nat" are anagrams (same letters: t,a,n)
    - "bat" is alone (letters: b,a,t)

    Input: ["a"]
    Output: [["a"]]

    LOGIC IN SIMPLE ENGLISH:
    1. Anagrams have same letters, so when sorted they look identical
    2. Use sorted version of each word as a "key"
    3. Group all words that have the same key together
    4. Return all groups as separate lists
    """

    anagram_groups = defaultdict(list)

    for word in words:
        # Sort letters to create key (anagrams will have same key)
        key = ''.join(sorted(word))
        anagram_groups[key].append(word)

    return list(anagram_groups.values())


# Program 5: Validate Binary Search Tree
# ======================================

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    """
    PROBLEM STATEMENT:
    Given the root of a binary tree, determine if it is a valid binary search tree (BST).
    A valid BST is defined as follows:
    - Left subtree contains only nodes with keys less than the node's key
    - Right subtree contains only nodes with keys greater than the node's key
    - Both left and right subtrees must also be binary search trees

    EXAMPLE:
    Input: Tree [2,1,3]
        2
       / \
      1   3
    Output: True
    Explanation: Left child (1) < root (2) < right child (3) ✓

    Input: Tree [5,1,4,null,null,3,6]
        5
       / \
      1   4
         / \
        3   6
    Output: False
    Explanation: Right subtree has 3 < 5, violating BST property

    LOGIC IN SIMPLE ENGLISH:
    1. In a valid BST, each node has a valid range of values it can have
    2. Root can be any value (range: -infinity to +infinity)
    3. Left child must be less than parent (range: -infinity to parent_value)
    4. Right child must be greater than parent (range: parent_value to +infinity)
    5. Check each node recursively with its valid range
    """

    def validate(node, min_val, max_val):
        if not node:
            return True

        # Check if current node violates BST property
        if node.val <= min_val or node.val >= max_val:
            return False

        # Check left subtree (values must be < node.val)
        # Check right subtree (values must be > node.val)
        return (validate(node.left, min_val, node.val) and
                validate(node.right, node.val, max_val))

    return validate(root, float('-inf'), float('inf'))


# Program 6: Top K Frequent Elements
# ==================================

def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """
    PROBLEM STATEMENT:
    Given an integer array nums and an integer k, return the k most frequent elements.
    You may return the answer in any order.

    EXAMPLE:
    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]
    Explanation:
    - Number 1 appears 3 times
    - Number 2 appears 2 times
    - Number 3 appears 1 time
    Top 2 frequent are 1 and 2

    Input: nums = [1], k = 1
    Output: [1]

    LOGIC IN SIMPLE ENGLISH:
    1. Count how many times each number appears
    2. Use a min-heap to keep track of top K frequent elements
    3. For each number and its count:
       - If heap has less than k elements, add it
       - If heap is full and current count > smallest in heap, replace it
    4. Heap will contain k most frequent elements
    """

    # Count frequencies
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1

    # Use heap to find top k
    heap = []

    for num, freq in count.items():
        if len(heap) < k:
            heapq.heappush(heap, (freq, num))
        elif freq > heap[0][0]:
            heapq.heappushpop(heap, (freq, num))

    return [num for freq, num in heap]


# Program 7: Word Break Problem
# =============================

def word_break(s: str, word_dict: List[str]) -> bool:
    """
    PROBLEM STATEMENT:
    Given a string s and a dictionary of strings wordDict, return true if s
    can be segmented into a space-separated sequence of dictionary words.
    Note: The same word may be reused multiple times.

    EXAMPLE:
    Input: s = "leetcode", wordDict = ["leet","code"]
    Output: True
    Explanation: "leetcode" can be split as "leet code"

    Input: s = "applepenapple", wordDict = ["apple","pen"]
    Output: True
    Explanation: "applepenapple" can be split as "apple pen apple"

    Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
    Output: False
    Explanation: Cannot split into dictionary words

    LOGIC IN SIMPLE ENGLISH:
    1. Check if string can be split into words from dictionary
    2. Use dynamic programming: dp[i] = True if s[0:i] can be split
    3. For each position i, check all possible previous positions j:
       - If s[0:j] can be split (dp[j] is True)
       - AND s[j:i] is in dictionary
       - Then s[0:i] can also be split (dp[i] = True)
    4. Answer is dp[len(s)]
    """

    word_set = set(word_dict)  # For faster lookup
    dp = [False] * (len(s) + 1)
    dp[0] = True  # Empty string can always be "split"

    for i in range(1, len(s) + 1):
        for j in range(i):
            # If s[0:j] can be split and s[j:i] is in dictionary
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break

    return dp[len(s)]


# Program 8: Minimum Window Substring
# ===================================

def min_window_substring(s: str, t: str) -> str:
    """
    PROBLEM STATEMENT:
    Given two strings s and t, return the minimum window substring of s
    such that every character in t (including duplicates) is included in the window.
    If no such window exists, return empty string "".

    EXAMPLE:
    Input: s = "ADOBECODEBANC", t = "ABC"
    Output: "BANC"
    Explanation: The minimum window is "BANC" which contains A, B, C

    Input: s = "a", t = "a"
    Output: "a"

    Input: s = "a", t = "aa"
    Output: ""
    Explanation: Need 2 'a's but s only has 1

    LOGIC IN SIMPLE ENGLISH:
    1. Find smallest window in s that contains all characters of t
    2. Use sliding window with two pointers
    3. Expand right pointer until window contains all characters of t
    4. Once valid, try shrinking from left to find minimum window
    5. Keep track of the smallest valid window found
    """

    if not s or not t:
        return ""

    # Count characters needed
    need = {}
    for char in t:
        need[char] = need.get(char, 0) + 1

    required = len(need)  # Number of unique characters in t
    formed = 0  # Number of unique characters in current window with desired frequency

    window_counts = {}
    left = right = 0

    # Result: (window length, left, right)
    ans = float("inf"), None, None

    while right < len(s):
        # Add character from right to window
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1

        # If this character's frequency matches desired frequency, increment formed
        if char in need and window_counts[char] == need[char]:
            formed += 1

        # Try to shrink window from left
        while left <= right and formed == required:
            char = s[left]

            # Update result if this window is smaller
            if right - left + 1 < ans[0]:
                ans = (right - left + 1, left, right)

            # Remove leftmost character from window
            window_counts[char] -= 1
            if char in need and window_counts[char] < need[char]:
                formed -= 1

            left += 1

        right += 1

    return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]


# Program 9: Coin Change Problem
# ==============================

def coin_change(coins: List[int], amount: int) -> int:
    """
    PROBLEM STATEMENT:
    You are given an integer array coins representing coins of different denominations
    and an integer amount representing a total amount of money.
    Return the fewest number of coins needed to make up that amount.
    If impossible, return -1.

    EXAMPLE:
    Input: coins = [1,3,4], amount = 6
    Output: 2
    Explanation: 6 = 3 + 3 (2 coins)

    Input: coins = [2], amount = 3
    Output: -1
    Explanation: Cannot make amount 3 with only coin 2

    Input: coins = [1], amount = 0
    Output: 0
    Explanation: No coins needed for amount 0

    LOGIC IN SIMPLE ENGLISH:
    1. Find minimum number of coins needed to make the amount
    2. Use dynamic programming: dp[i] = minimum coins needed for amount i
    3. For each amount from 1 to target:
       - Try each coin that's <= current amount
       - If we can make (amount - coin) with dp[amount - coin] coins
       - Then we can make amount with dp[amount - coin] + 1 coins
       - Take minimum across all coin choices
    """

    # dp[i] represents minimum coins needed for amount i
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # 0 coins needed for amount 0

    for current_amount in range(1, amount + 1):
        for coin in coins:
            if coin <= current_amount:
                dp[current_amount] = min(dp[current_amount],
                                       dp[current_amount - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1


# Program 10: LRU Cache Implementation
# ===================================

class LRUCache:
    """
    PROBLEM STATEMENT:
    Design a data structure that follows Least Recently Used (LRU) cache constraints.
    Implement LRUCache class with:
    - LRUCache(capacity): Initialize with positive size capacity
    - get(key): Return value of key if exists, otherwise return -1
    - put(key, value): Update value if key exists, otherwise add key-value pair
      If adding causes cache to exceed capacity, remove least recently used key
    Both get and put must run in O(1) average time complexity.

    EXAMPLE:
    Input: ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
           [[2], [1,1], [2,2], [1], [3,3], [2], [4,4], [1], [3], [4]]
    Output: [null, null, null, 1, null, -1, null, -1, 3, 4]

    Explanation:
    LRUCache cache = new LRUCache(2);
    cache.put(1, 1);        // cache: {1=1}
    cache.put(2, 2);        // cache: {1=1, 2=2}
    cache.get(1);           // return 1, cache: {2=2, 1=1} (1 becomes most recent)
    cache.put(3, 3);        // evict 2, cache: {1=1, 3=3}
    cache.get(2);           // return -1 (not found)
    cache.put(4, 4);        // evict 1, cache: {3=3, 4=4}
    cache.get(1);           // return -1 (not found)
    cache.get(3);           // return 3
    cache.get(4);           // return 4

    LOGIC IN SIMPLE ENGLISH:
    1. LRU = Least Recently Used - remove items that haven't been used for longest time
    2. Need fast access (get/put in O(1)) - use hash map
    3. Need to track usage order - use doubly linked list
    4. Hash map points to nodes in linked list for fast access
    5. Move accessed items to front, remove from back when full
    """

    class Node:
        def __init__(self, key=0, value=0):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> node

        # Create dummy head and tail nodes
        self.head = self.Node()
        self.tail = self.Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node):
        """Add node right after head"""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        """Remove an existing node"""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _move_to_head(self, node):
        """Move node to head (mark as recently used)"""
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        """Remove last node (least recently used)"""
        last_node = self.tail.prev
        self._remove_node(last_node)
        return last_node

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if node:
            # Move to head (mark as recently used)
            self._move_to_head(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)

        if node:
            # Update existing node
            node.value = value
            self._move_to_head(node)
        else:
            # Add new node
            new_node = self.Node(key, value)

            if len(self.cache) >= self.capacity:
                # Remove least recently used
                tail = self._pop_tail()
                del self.cache[tail.key]

            self.cache[key] = new_node
            self._add_node(new_node)


# Demo and Test Functions
# =======================

def run_all_demos():
    """Test all interview programs with sample inputs"""

    print("🐍 Top 10 Python Interview Programs - Medium Complexity")
    print("=" * 60)

    # Test 1: Find Anagrams
    print("\n1. Find All Anagrams:")
    result = find_anagrams("abab", "ab")
    print(f"   Input: s='abab', pattern='ab' → Output: {result}")

    # Test 2: Merge Intervals
    print("\n2. Merge Overlapping Intervals:")
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    result = merge_intervals(intervals)
    print(f"   Input: {intervals} → Output: {result}")

    # Test 3: Longest Unique Substring
    print("\n3. Longest Substring Without Repeating Characters:")
    result = longest_unique_substring("abcabcbb")
    print(f"   Input: 'abcabcbb' → Output: {result}")

    # Test 4: Group Anagrams
    print("\n4. Group Anagrams:")
    words = ["eat","tea","tan","ate","nat","bat"]
    result = group_anagrams(words)
    print(f"   Input: {words} → Output: {result}")

    # Test 5: Validate BST (create simple tree)
    print("\n5. Validate Binary Search Tree:")
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    result = is_valid_bst(root)
    print(f"   Tree: [2,1,3] → Is Valid BST: {result}")

    # Test 6: Top K Frequent
    print("\n6. Top K Frequent Elements:")
    result = top_k_frequent([1,1,1,2,2,3], 2)
    print(f"   Input: [1,1,1,2,2,3], k=2 → Output: {result}")

    # Test 7: Word Break
    print("\n7. Word Break:")
    result = word_break("leetcode", ["leet","code"])
    print(f"   Input: 'leetcode', ['leet','code'] → Output: {result}")

    # Test 8: Minimum Window Substring
    print("\n8. Minimum Window Substring:")
    result = min_window_substring("ADOBECODEBANC", "ABC")
    print(f"   Input: 'ADOBECODEBANC', 'ABC' → Output: '{result}'")

    # Test 9: Coin Change
    print("\n9. Coin Change:")
    result = coin_change([1,3,4], 6)
    print(f"   Input: coins=[1,3,4], amount=6 → Output: {result}")

    # Test 10: LRU Cache
    print("\n10. LRU Cache:")
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    print(f"    get(1): {lru.get(1)}")  # returns 1
    lru.put(3, 3)  # evicts key 2
    print(f"    get(2): {lru.get(2)}")  # returns -1 (not found)

    print("\n🎉 All tests completed!")


if __name__ == "__main__":
    run_all_demos()