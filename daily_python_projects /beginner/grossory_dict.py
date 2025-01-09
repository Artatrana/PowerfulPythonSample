def grocery_list_main():
# Initial grocery list
    grocery_list = ["apples", "bread", "milk", "eggs", "bananas"]

    # Step 1: Add a new item
    grocery_list.append("beans")

    # Step 2: Remove an item
    grocery_list.remove("bread")

    # Step 3: Sort the list alphabetically
    grocery_list.sort()

    # Step 4: Print the updated grocery list
    print("Updated Grocery List:")
    for item in grocery_list:
        print(item)

if __name__ == "__main__":
    grocery_list_main()