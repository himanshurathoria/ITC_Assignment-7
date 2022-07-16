print("\nWelcome to my Program")
items = [n for n in input("Enter the elements : ").split(',')]
items.sort()
print("\nSorted elements : ")
print(','.join(items))