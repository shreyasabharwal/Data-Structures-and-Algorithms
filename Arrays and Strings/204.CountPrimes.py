'''204. Count Primes

Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.'''


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 0
        isPrime = [True]*n
        isPrime[0] = isPrime[1] = False

        i = 2
        while i*i < n:
            if isPrime[i]:
                for j in range(i*i, n, i):
                    isPrime[j] = False
            i += 1

        return sum(isPrime)
