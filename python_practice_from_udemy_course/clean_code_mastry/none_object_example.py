MISSING = object()
# print(dir(MISSING))
print(type(MISSING))
# We have created this object to represent missing values as if we are going to put None inplace of missing value, there
# is a chance that None could be a valid value. Or None could be intensional
# For example
dict_example = {"key1":"Value1", "key2":"Value2", "key3":None}
val = dict_example.get("key3","None") # here we will not get to know None came because the value of because of defulted

# now inplace of None we will do like this
val1 = dict_example.get("key3",MISSING) # Its clear MISSING is coming as the value is not there.
