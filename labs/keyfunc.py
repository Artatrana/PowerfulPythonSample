'''
Use max, min, or sorted along with key functions to implement the
following functions and make the tests pass.

>>> most_spaces(["a", "a b", "a b c", "c", "abc"])
'a b c'

>>> one_line_poems = [
...      "The dogs are barking at the stillness, the stillness is still.",
...      "In the canopy of the night heaven the stars are tiptoeing.",
...      "A sunrise smiles wide into my expectant face.",
...      "The bees are awakening to the life in a yellow wonder!",
...      "The land runs astoundingly under my soles.",
...      "The dance of the flowers kissed by the butterflies.",
... ]

>>> for poem in sorted_by_word_count(one_line_poems):
...     print(poem)
The land runs astoundingly under my soles.
A sunrise smiles wide into my expectant face.
The dance of the flowers kissed by the butterflies.
The dogs are barking at the stillness, the stillness is still.
In the canopy of the night heaven the stars are tiptoeing.
The bees are awakening to the life in a yellow wonder!

'''

# Write your code here:



# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

# From Powerful Python. Copyright MigrateUp LLC. All rights reserved.
