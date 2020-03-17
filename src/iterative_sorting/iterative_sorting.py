# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Loop through elements on right-hand-side of current index
        for j in range(cur_index, len(arr)):
            # find the smallest element
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # set up a variable to check if the swap occurred
    swap_occurred = True
    # loops through over again as long as a swap occurred
    while swap_occurred:
        # sets false as a default so the while loop breaks if the condition below doesn't pass
        swap_occurred = False
        # Loop through the array
        for i in range(0, len(arr) - 1):
            # compare each element to its neighbor
            if arr[i] > arr[i + 1]:
                # if element is in wrong position(relative to neighbor), swap them
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swap_occurred = True

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
