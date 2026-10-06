students = ["kaisamba", "foday","sharon"]
print(students)

#accessing items in a list by their index
print(f"my best friend is {students[0]}")
print(f"my second friend is {students[1]}")
print(f"my third friend is {students[2]}")

#get the index of an items in a list
print(students.index("kaisamba"))
print(students.index("foday"))
print(students.index("sharon"))

#know the nuber of items stored in a list
print(f"the total items in the list is: {len(students)}")

#add items to a lists
students.append("mohamed")
print(students)
students += ["joseph", "musa","john"]
print(students)
students.insert(4, "clifford")
print(students)

#extend a list with another list
fruits =["apple", "banana", "orange"]
students.extend(fruits)
print(students)

#removing items  from list
fruits.remove("mango")
print(fruits)

#it remove or pos something out of the list and also return it for you to used it
students.pop()
print(students)
thirditem = students.pop()
print(students)
print(thirditem)
