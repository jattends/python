#mapping
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, nums))
print(squares)
#filter
nums = [1, 2, 3, 4, 5]
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)
#reduce
