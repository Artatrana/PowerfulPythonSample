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