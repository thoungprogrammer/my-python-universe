motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati' # to change the element at index 0 to ducati.
print(motorcycles)

motorcycles.append('honda') # to add honda to the last element.
print(motorcycles)

motorcycles = [] # remove all the list to empty
motorcycles.append('honda') # start adding 'honda' to 1st element.
motorcycles.append('yamaha') # adding 'yamaha' to 2nd element.
motorcycles.append('suzuki') # adding 'suzuki' to 3rd element.
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0,'ducati') # the insert() function is used to add an item at a specific position in a list.
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0] # del is a Python keyword used to delete an item from a list by its position (index), or to delete an entire variable.
print(motorcycles)
