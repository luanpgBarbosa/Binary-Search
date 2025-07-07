from binary_search import binary_search

ordered_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = int(input('What is the target number?\n'))

target_index = binary_search(ordered_list, target)

if target_index == None:
    print("The target doesn't exist in the list")
else:
    print(f"Here is the target index: {target_index}")