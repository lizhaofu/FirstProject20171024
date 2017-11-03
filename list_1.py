numbers = list(range(2,11,2))
print(numbers)
print(min(numbers))
print(max(numbers))
print(sum(numbers))

squares = [value**2 for value in range(1,11)]
print(squares)

ser = squares
print(ser)

dimensions = (29,30,45)
for dimension in dimensions:
    print(dimension)
dimensions = (23,45,90)
for dimension in dimensions:
    print(dimension)
