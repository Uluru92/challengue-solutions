'''
Write a script that sorts a list of tuples based on the number value in the tuple.
For example:

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]

'''
#My solution... enjoy:

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
print("unsorted_list", unsorted_list)

#Fisrt, I am going to create a new list just to keep the numbers in position [1], then sort it.

numbers_list =[]
for x in unsorted_list:
    numbers_list.append(x[1])
    numbers_list_sorted = sorted(numbers_list)

#Second, I am going to create a new list, I am going to analyze each element from the original list, and
#take every element if my sorted number list matches the element using the index!

sorted_list = []
for x in numbers_list_sorted:
    for y in unsorted_list:
        if x == y[1]:
            sorted_list.append(y)
            unsorted_list.remove(y)

print("sorted_list:",sorted_list)
