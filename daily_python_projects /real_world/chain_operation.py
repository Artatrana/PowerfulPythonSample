# Example of python programming wiht chain functionalty

class NumberProcessor:
    def __init__(self, numbers):
        self.numbers = numbers

    def filter_even_number(self):
        """Filter even numbers from the list."""
        self.numbers = [x for x in self.numbers if x % 2 == 0]
        return self

    def square_numbers(self):
        """Compute the sum of the numbers in the list."""
        self.numbers = [x ** 2 for x in self.numbers]
        return self

    def double_sum(self):
        """Double the sum."""
        if isinstance(self.numbers, int):
            self.numbers *= 2
        return self

    def get_result(self):
        """Return the final result."""
        return self.numbers

if __name__ == "__main__":
    # Input data
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    #print (NumberProcessor(numbers).get_result())

    print(NumberProcessor(numbers).double_sum().get_result())

    print(NumberProcessor(numbers).filter_even_number().get_result())

    print(NumberProcessor(numbers).filter_even_number().square_numbers().get_result())
