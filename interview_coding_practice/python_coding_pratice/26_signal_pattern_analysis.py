# Imagine Qualcomm is analyzing signal strength values in an array, and they want to detect
# peaks (values greater than their neighbors).


# signal = [1, 3, 2, 4, 1, 5, 3]
# print(find_peaks(signal))  # Expected output: [3, 4, 5]

# Logic :
#     - For 1st and last values they have only one neighbours rest all have two neighbours
#     - First element: compare with next element.
#     - Middle elements: compare with previous and next.
#     - Last element: compare with previous.
#     - List comprehension makes the middle-element check concise and Pythonic.

def find_peaks(signal):
    n = len(signal)
    if n == 0:
        return []
    peak = []
    for i in range(n):
        if i == 0 and signal[i] > signal[i+1]:
            peak.append(signal[i] )
        elif i == n-1 and signal[n-1] > signal[n-2] :
            peak.append(signal[i] )
        elif signal[i] > signal[i-1] and signal[i] > signal[i+1]:
            peak.append(signal[i] )
    return peak

signal = [1, 3, 2, 4, 1, 5, 3]
print(find_peaks(signal))

def find_peaks2(signal):
    n = len(signal)
    if n == 0:
        return []
    peak = []
    for i in range(n):
        if  ( i ==0 and signal[i] > signal[i+1])  or \
            ( i == n-1 and signal[i] > signal[i-1]) or \
                (  signal[i] > signal[i - 1] and signal[i] > signal[i + 1]):

            peak.append(signal[i] )
    return peak

signal = [1, 3, 2, 4, 1, 5, 3]
print(find_peaks2(signal))
