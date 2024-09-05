
username = "chaiaurcode"

def fun():
    username = "chai"
    print(username)

print(username)
fun()

x = 99

# def fun3():
#     global x
#     x=12
# fun3()
# print(x) 

# def f1():
#     def f2():
#         print(x)
#     return f2
# my_result = f1()
# my_result()

def chaicoder(num):
    def actual(x):
        return x ** num 
    return actual




f = chaicoder(2)
g = chaicoder(3)

# print(f)
# print(g)
print(f(2))
print(f(3))