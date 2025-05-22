n = 7

fact = 1

while n > 0:
    fact = fact * n
    n = n - 1

print(fact)

def factorial (n):
    if n < 1:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial (7))

def fib (n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
print(fib(5))
    