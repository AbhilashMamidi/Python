# 9. Generator Function with yield
# Problem: Write a generator function that yields even numbers up to a specified limit.

def even_generator(limit):
    for i in  range(2, limit+1, 2):
        yield i

for num in even_generator(10):
    print(num)


# limit = 10
# for i in range(2, limit+1, 2): 
#    print(i)
# 2
# 4
# 6
# 8
# 10



# limit = 10
# for i in range(1, limit+1, 2): 
#    print(i)
# 1
# 3
# 5
# 7
# 9


