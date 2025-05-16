from icecream import ic

def calculate_area(length, width):
    ic(length, width)
    area = length * width
    ic(area)
    return area

length = 10
width = 5
area = calculate_area(length, width)
ic(area)