import sympy as sy

x = sy.Symbol('x')
n = int(input('chose n：'))

if n >= 0:

    sum_ = 0

    while n >= 0:

        numerator = (-1) ** n

        denominator = sy.factorial(2 * n)

        right_side = x ** (2 * n)

        result = (numerator/denominator) * right_side

        sum_ += result
    
        n -= 1

print(sum_)
