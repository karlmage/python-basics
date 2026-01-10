numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#i_numbers = numbers.__iter__()
i_numbers = iter(numbers) # iterator object

print(i_numbers)

print(next(i_numbers))
print(next(i_numbers))
print(next(i_numbers))
next(i_numbers)
print(next(i_numbers))

while True:
    try:
        print(next(i_numbers))
    except StopIteration:
        break