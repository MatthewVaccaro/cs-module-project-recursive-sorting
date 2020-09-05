ascending = [2, 4, 12, 14, 17, 30, 46, 47, 51, 54, 61]
descending = [101, 98, 57, 49, 45, 13, -3, -17, -61]
# TO-DO: Implement a recursive implementation of binary search


def binary_search(arr, target, start, end):

    if len(arr) == 0:
        return -1

    middle = (start + end) // 2

    if start == end:
        return -1

    if target == arr[middle]:
        return middle

    if target > arr[middle]:
        start = middle
        return binary_search(arr, target, start, end)

    if target < arr[middle]:
        end = middle
        return binary_search(arr, target, start, end)


# print(binary_search(testArray, 0, 0, len(testArray)))

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively

# def agnostic_binary_search(arr, target, start, end):
#     if len(arr) == 0:
#         return -1

#     middle = (start + end) // 2
#     findDirection = None

#     if arr[0] < arr[1]:
#         findDirection = "+"
#     else:
#         findDirection = "-"

#     if start == end:
#         return -1

#     if target == arr[middle]:
#         return middle

#     if target > arr[middle]:
#         if findDirection == "+":
#             start = middle
#             return agnostic_binary_search(arr, target, start, end)
#         else:
#             end = middle
#             return agnostic_binary_search(arr, target, start, end)

#     if target < arr[middle]:
#         if findDirection == "+":
#             end = middle
#             return agnostic_binary_search(arr, target, start, end)
#         else:
#             start = middle
#             return agnostic_binary_search(arr, target, start, end)
