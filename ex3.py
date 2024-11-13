# write a factorial function, given n, you return n!
def factorial_recursive(n):
    if n < 0:
        raise ("Factorial is defined")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

