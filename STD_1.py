import numpy as np                                                          # Importing the numpy library for array manipulation
unsorted = np.array([11, 22, 14, 67, 2, 9])                                 # Define the unsorted array
'''Selection Sort
Input: unsorted list
Output: sorted list
implements selection sort algorithm due to the small dataset
'''
def Selection_Sort(unsorted):                                                # Define the selection sort function which takes the unsorted array as an argument
    for i in range(len(unsorted)):                                           # Iterate over each element in the array using its length as the max value
        minn = i                                                             # Initialize the minn to be the current minimum value
        for j in range(i + 1, len(unsorted)):                                # Iterate over the remaining elements to find if there is a value smaller then minn
            if unsorted[j] < unsorted[minn]:                                 # If the current element is smaller than the value stored in minn, update minn so that it stores the current smallest value found
                    unsorted[j], unsorted[minn] = unsorted[minn], unsorted[j]# swap the two values
    sorted = unsorted[0:j+1]                                                 # creates a sub array from the original array unsorted including elements from index 0 up to index j
    return sorted                                                            # returns sorted subarray
print(Selection_Sort(unsorted))                                              # function call for Select_Sort function taking the unsorted array as its input argument