# bubble sort

# def bubblesort(array):
#     for i in range(len(array)):
#         for j in range(0, len(array)-i -1):
#             if array[j]>array[j+1]:
#                 temp = array[j]
#                 array[j] = array[j+1]
#                 array[j+1] = temp
# data = [-2, 45, 0, 11, -9]
# bubblesort(data)
# print('Sorted Array in Ascending Order:')
# print(data)


# Selection Sort

# def selectionSort(array, size):
#    for step in range(size):
#         min_idx = step
#         for i in range(step + 1, size):
#             if array[i] < array[min_idx]:
#              min_idx = i
#         (array[step], array[min_idx]) = (array[min_idx], array[step])
# data = [-2, 45, 0, 11, -9]
# size = len(data)
# selectionSort(data, size)
# print('Sorted Array in Ascending Order:')
# print(data) 


# Insertion Sort

# def insertionSort(array):

#     for step in range(1, len(array)):
#         key = array[step]
#         j = step - 1
#         while j >= 0 and key < array[j]:
#             array[j + 1] = array[j]
#             j = j - 1
#         array[j + 1] = key
# data = [9, 5, 1, 4, 3]
# insertionSort(data)
# print('Sorted Array in Ascending Order:')
# print(data)