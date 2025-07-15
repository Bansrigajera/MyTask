# # List Data Type Example Program
#
# def main():
#     # Creating a list
#     fruits = ["apple", "banana", "mango", "orange"]
#     print("Original List of Fruits:", fruits)
#
#     # Accessing list elements
#     print("First fruit:", fruits[0])
#     print("Last fruit:", fruits[-1])
#
#     # Modifying list elements
#     fruits[1] = "grape"
#     print("After replacing banana with grape:", fruits)
#
#     # Adding elements
#     fruits.append("pineapple")
#     print("After adding pineapple:", fruits)
#
#     # Inserting at a specific position
#     fruits.insert(2, "kiwi")
#     print("After inserting kiwi at position 2:", fruits)
#
#     # Removing elements
#     fruits.remove("apple")
#     print("After removing apple:", fruits)
#
#     # Removing by index
#     removed_item = fruits.pop(3)
#     print(f"Removed item at index 3: {removed_item}")
#     print("List after pop:", fruits)
#
#     # Sorting list
#     fruits.sort()
#     print("Sorted list:", fruits)
#
#     # Reversing list
#     fruits.reverse()
#     print("Reversed list:", fruits)
#
#     # Length of list
#     print("Number of fruits:", len(fruits))
#
#     # Iterating through the list
#     print("List of fruits:")
#     for fruit in fruits:
#         print(fruit)
#
#     # Check if an item exists in the list
#     if "mango" in fruits:
#         print("Mango is in the list.")
#     else:
#         print("Mango is not in the list.")
#
#     # Clearing the list
#     fruits.clear()
#     print("After clearing the list:", fruits)
#
#
# # Run the program
# if __name__ == "__main__":
#     main()

def divide(a, b):
    return a / b

result = divide(10, 0)
print("Result:", result)



