# Bubble sort and selection sort are 2 basic sorting algorithms:
# Bubble Sort: Goes through a list multiple times, swapping elements that are in the wrong order until everything is sorted.
# Selection Sort: Finds the smallest (or largest) element in the list and moves it to its correct position, repeating this process for each element.

response = int(input("Enter a number(0 to stop): "))
num_list = []

# append all values into a list first
while response != 0:
    num_list.append(response)
    response = int(input("Enter a number(0 to stop): "))

# find length of num_list and assign it to varable n
n = len(num_list)

# outer loop manages multiple passes over the list to ensure the entire list is sorted.
# each pass through the list moves the unsorted element to its correct position.
for i in range(0, n-1):
    swapped = False

    # starts a nested loop to compare adjacent elements. The inner loop performs the actual comparisons and swaps of 
    # adjacent elements. The inner loop's range decreases by i after each outer loop iteration, because the largest elements 
    # are already sorted
    for j in range(0, n-i-1):
        if num_list[j] > num_list[j + 1]:
                swapped = True
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]

    # after the inner loop completes, checks if any swaps were made.
    if not swapped:
        break
    
print(num_list)
        