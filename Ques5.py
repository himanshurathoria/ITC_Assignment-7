print("\nWelcome to my Program")

# creating an empty list
lst = []

# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
    ele = int(input())

    lst.append(ele)  # adding the element

print(lst)
print(lst.sort())


def binarySearch(lst, l, r, x):
    # Check base case
    if r >= l:

        mid = l + (r - l) // 2

        # If element is present at the middle itself
        if lst[mid] == x:
            return mid

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif lst[mid] > x:
            return binarySearch(lst, l, mid - 1, x)

        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(lst, mid + 1, r, x)

    else:
        # Element is not present in the array
        return -1


print("ENTER NUMBER TO SEARCH")
x = int(input(":"))
# Function call
result = binarySearch(lst, 0, len(lst) - 1, x)

if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")


def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count


x = int(input("Enter Number of occurnce to check:"))
print('{} has occurred {} times'.format(x, countX(lst, x)))