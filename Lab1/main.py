import utilities

print("Hello world!\n")

print(utilities.make_math_operation(2, 4, "add"))

list_of_numbers = [1, 2, 3, 4, 5, 6, 11]
list_of_even_numbers = [x for x in list_of_numbers if x % 2 == 0]

print(list_of_even_numbers)
