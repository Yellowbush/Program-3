# Jason Sy
# CSS 340: Applied Computing
# April 28 2022
#
# four find functions

import copy

# unsorted list is searched linearly
def find1(list, val):
    for i in range(len(list)):
        if (list[i] == val):
            return True
    return False

# deep copy is made and sorted, then binary search performed
def find2(list, val):
    temp = copy.deepcopy(list)
    temp.sort()
    start = 0
    end = len(temp) - 1
    while (start <= end):
        mid = (start + end) // 2
        if (temp[mid] < val):
            start = mid + 1
        elif (temp[mid] > val):
            end = mid - 1
        else:
            return True
    return False

# built-in used to determine if val is in the unsorted list
def find3(list, val):
    if(val in list):
        return True
    else:
        return False

# requires list to be sorted before call
# binary search performed on pre-sorted list to find val
def find4(list, val):
    start = 0
    end = len(list) - 1
    while(start <= end):
        mid = (start + end) // 2
        if(list[mid] > val):
            end = mid - 1
        elif(list[mid] < val):
            start = mid + 1
        else:
            return True
    return False