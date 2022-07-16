print("\nWelcome to my Program")
def Removedup(oglist) :
    finallist = []
    for num in oglist :
        if num not in finallist :
            finallist.append(num)
    return finallist

oglist = [4,5,2,4,5,6,5,4,5,5,6]
print(Removedup(oglist))
newlist = Removedup(oglist)

def selectionSort(array):
    n = len(array)
    for i in range(n):
        minimum = i
        for j in range(i+1, n):
            if (array[j] < array[minimum]):
                minimum = j

            if (minimum!=i):
                temp = array[i]
                array[i] = array[minimum]
                array[minimum] = temp
    return array

print(selectionSort(newlist))

def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - 1 - i):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

oglist = [4,5,2,4,5,6,5,4,5,5,6]
bubbleSort(newlist)
print('Sorted Array in Ascending Order:')
print(newlist)