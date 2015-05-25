# Fibonacci generator
def fib():
    a,b = 0,1
    while True:
        yield a
        a, b = b, a+b

# num = fib()
# for x in range(100):
#     print(num.next())

# Returns nth digit of Fibonacci
def fib2(num):
    a,b = 0,1
    for _ in range(num-1):
        a, b = b, a+b
    return a

#print(fib2(100))
