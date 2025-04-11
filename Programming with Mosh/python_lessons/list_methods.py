numbers = [5, 2, 1, 7, 4, 7]
numbers.append(20)      # adds item i.e '20' in the list 
print(numbers)

numbers.insert(0, 10)       # inserts item in the list. here 0 represents the place where to add the item & 10 represents the item we need to add.
print(numbers)

numbers.remove(5)       # removes the item from the list. here it removes the digit 5 from the list
print(numbers)

numbers.pop()       # removes last item in the list 
print(numbers)

print(numbers.index(7))       # shows the index of the item 

print(50 in numbers)    # we get a boolean value 

print(numbers.count(7))

numbers.sort()      # It'll sort the items form the list in asc. order
print(numbers)

numbers.reverse()   # It'll sort the items from the list in desc. order
print(numbers)

numbers2 = numbers.copy()
numbers.append(50)
print(numbers2)

numbers.clear()     # It clears all the list. i.e removes/deletes all the items from the list.
print(numbers)
