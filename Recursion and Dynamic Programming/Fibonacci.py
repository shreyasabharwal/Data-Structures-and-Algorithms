# fibonacci


def fibonacci(num):
    if num == 0:
        return 0
    a = 0
    b = 1
    print(a, '\t', b, end='\t')

    for i in range(2, num+1):
        c = a+b
        a = b
        b = c
        print(c, end='\t')


def fibonacci_rec(num, memo):
    if num == 0:
        return num
    if num == 1:
        return num
    if memo[num] == 0:
        memo[num] = fibonacci_rec(num-1, memo)+fibonacci_rec(num-2, memo)
    return memo[num]


def fib_rec(num):
    # memoization
    memo = [0]*(num+1)
    return fibonacci_rec(num, memo)


if __name__ == '__main__':
    fibonacci(6)
    print("################")
    print(fib_rec(6))
