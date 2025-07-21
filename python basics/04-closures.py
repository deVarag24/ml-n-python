def counter(intial):
    def add(val = 0):
        return intial + val
    return add


a = counter(10)

print(a(10))

# callbacks
def square(n):
    return n**2

def executeToN(func, n):
    for i in range(n):
        print(func(i))

executeToN(square, 10)