#You are given a stream of numbers, and at each step, you need to compute the median of all numbers seen so far.
def running_median(stream):
    medians = []
    # Fill your code here
    for i in range(len(stream)):
        if i % 2!=0:
            value = (stream[i//2] + stream[i//2+1])/2
        else:
            value = stream[int(i//2)+1]
        medians.append(value)
    return medians

stream = [5, 2, 1, 7, 3]
print(running_median(stream))  # Output: [5, 3.5, 2, 3.5, 3]
