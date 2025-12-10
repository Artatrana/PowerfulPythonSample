# Problem: Write a function that takes a list of strings and groups the anagrams together.
#
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
def group_anagrams(lst : list) -> list:
    result = []
    ana_map = {}
    for item in lst:
        sorted_item = "".join (sorted(item))
        if ana_map.get(sorted_item,"") != "":
            ana_map[sorted_item].append(item)
        else:
            ana_map[sorted_item]= [item]
    for key, value in ana_map.items():
        result.append(value)
    return result

#print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

def test_group_anagrams():
    result1 = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    expected1 = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

    # Use sets for order-insensitive comparison
    assert {frozenset(group) for group in result1} == {frozenset(group) for group in expected1}

    result2 = group_anagrams([""])
    expected2 = [[""]]
    assert {frozenset(group) for group in result2} == {frozenset(group) for group in expected2}

    result3 = group_anagrams(["a"])
    expected3 = [["a"]]
    assert {frozenset(group) for group in result3} == {frozenset(group) for group in expected3}

    result4 = group_anagrams(["abc", "bca", "cab", "xyz", "zyx"])
    expected4 = [["abc", "bca", "cab"], ["xyz", "zyx"]]
    assert {frozenset(group) for group in result4} == {frozenset(group) for group in expected4}

    print("All tests passed!")

# Run the test
test_group_anagrams()