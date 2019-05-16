'''8.1 Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
steps at a time. Implement a method to count how many possible ways the child can run up the
stairs.
'''


def countStepRec(n, memo):
    # base case
    if n == 0:
        return 1
    elif n < 0:
        return 0
    if memo[n] == 0:
        memo[n] = countStepRec(
            n-1, memo)+countStepRec(n-2, memo)+countStepRec(n-3, memo)
    return memo[n]


def tripleStep(n):
    memo = [0]*(n+1)
    return countStepRec(n, memo)


if __name__ == "__main__":
    print(tripleStep(7))
