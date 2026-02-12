def factorial(n):
    """ Calculate factorial of a non-negative number n. """
    if n <0 :
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n+1):
        result *= i

    return result 

    
