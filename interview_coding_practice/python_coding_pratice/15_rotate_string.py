# 15. Rotate Array– Rotate a list by `k` steps.
# Input: [1,2,3,4,5,6,7], k=3` → Output: `[5,6,7,1,2,3,4]`
# Input: [-1,-100,3,99], k=2` → Output: `[3,99,-1,-100]`
# Input: [1,2], k=1` → Output: `[2,1]`
# Logic: Reverse entire array, then reverse first `k`, then reverse rest.

def prob15_rotate_string(s, k):
    n = len(s)
    k = k % n  # handle k > n
    return s[-k:] + s[:-k]

print(prob15_rotate_string([1,2,3,4,5,6,7], k=3))
assert prob15_rotate_string([1,2,3,4,5,6,7], k=3) ==[5,6,7,1,2,3,4]
assert prob15_rotate_string([-1,-100,3,99], k=2) ==[3,99,-1,-100]
assert prob15_rotate_string([1,2], k=1) ==[2,1]

print("All assert successful!")

