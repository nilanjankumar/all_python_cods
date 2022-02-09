the_index = 0
lst = []


def bubble_sort(lts):

    for i in range(len(lst)-1, 0, -1):
        for j in range(i):

            if lst[j] > lst[j+1]:
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp


def binary_search(lts, n):
    low = 0
    upr = len(lts) - 1
    while low <= upr:

        mid = (low + upr) // 2

        if lts[mid] == n:
            globals()['the_index'] = mid
            return True
        else:
            if n > lts[mid]:
                low = mid + 1
            else:
                upr = mid - 1
    return False


a = int(input("Enter the length of the List: "))
for j in range(a):
    x = int(input("Enter the next value: "))
    lst.append(x)

bubble_sort(lst)


searching_value = int(input("Enter the Searching value: "))

if binary_search(lst, searching_value):
    print("Found at", the_index)
else:
    print("Not Found")
