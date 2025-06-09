# Give a list of word, write a function to return list havig anagram ward together

def group_anagram(s: list[str]) -> list[str]:

    ana_dict = {}

    for word in s:
        sorted_word = "".join(sorted(word))
        if sorted_word in ana_dict:
            ana_dict[sorted_word].append(word)
        else:
            ana_dict[sorted_word] = [word]

    result = []
    for val in ana_dict.values():
        result.append(val)
    
    return result 

print(group_anagram(["eat", "tea","tan","ate","nat","bat"]))
            
