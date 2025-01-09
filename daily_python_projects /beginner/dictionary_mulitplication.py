# Given a dictionary define a fuction that will return the dictionary with new value multiplied by 10
def main():
    grocery_list = {
        "apples": 5,
        "bananas": 2,
        "milk": 1,
        "bread": 1
    }

    for item in grocery_list:
        grocery_list[item] = grocery_list.get(item) * 10

    print(grocery_list)

if __name__ == "__main__":
    main()