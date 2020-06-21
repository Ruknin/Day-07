#Introducing List
motorcycle = ['honda','yamaha','suzuki']
print(motorcycle)

#Accessing Elements in a list
print(motorcycle[1])

#Updating Elements in a list
motorcycle[0] = 'hero'
print(motorcycle)

#Adding new element to the end of list
motorcycle.append('Mahim')
print(motorcycle)

fruits = []
print(fruits)
fruits.append('Orange')
fruits.append('Mango')
fruits.append('Banana')
print(fruits)

#Adding new element to the exact position of the list.
fruits.insert(1,'Apple')
print(fruits)

#Shorting alphabetically
print('After Sort :')
fruits.sort()
print(fruits)

#Reverse shorting
print('After Reverse:')
fruits.reverse()
print(fruits)

#Removing elements from the list
print('After Remove')
fruits.remove('Apple')
print(fruits)

#Deleting elements
print ('After Delete')
del fruits[0]
print(fruits)

cars = ['bmw','audi','toyota','audi','subaru','audi','cortina']
print('Count Number of Occurence:')
#counting total number of a element
print(cars.count('audi'))
#locating the the first occurence of a element
print(cars.index('audi'))
print("\nHere is the Sorted list")
print(sorted(cars))

print("\nHere is the Original list")
print(cars)

print("\nTotal Number of car: ",end="")
print(len(cars))

print(cars[0:2]) #ekhane 0 mane 0 theke suru hobe and 2 mane 0 theke count kore 1 eikhane duita element hocche so 1 er element dekhabe
print(cars[:2])
print(cars[2:4])
print(cars[-1])

'''print(dir('cars'))'''

print(30*'=')
print(help(fruits.index))


print('\n')
for x in cars:
    print(x,end="\t")