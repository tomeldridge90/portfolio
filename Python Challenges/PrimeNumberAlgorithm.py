'''
<<<<<Question>>>>>
Primes that have only odd digits are pure odd digits primes, obvious but necessary definition.
Examples of pure odd digit primes are: 11, 13, 17, 19, 31... If a prime has only one even digit does not belong
to pure odd digits prime, no matter the amount of odd digits that may have.

Create a function, only_oddDigPrimes(), that receive any positive integer n, and output a list like the one below:

[number pure odd digit primes below n, largest pure odd digit prime smaller than n, smallest pure odd digit prime higher than n]

Let's see some cases:

only_oddDigPrimes(20) ----> [7, 19, 31]
7, beacause we have seven pure odd digit primes below 20 and are 3, 5, 7, 11, 13, 17, 19
19, because is the nearest prime of this type to 20
31, is the first pure odd digit that we encounter after 20///

only_oddDigPrimes(40) ----> [9, 37, 53]
In the case that n, the given value, is a pure odd prime, n should be counted with the found primes and
search for the immediately below and the immediately after.
'''

'''
<<<<<Answer>>>>>
'''

import math
def only_oddDigPrimes (n):
    numPurePrime = 0
    lastPurePrime = 0
    nearestPurePrime=0
    for i in range (3,n,2):
        isPrime = 0
        numberOfFactors = 0
        for e in range(1,int(math.sqrt(i))+1):
            if i%e ==0:
                numberOfFactors+=1
        if numberOfFactors <2:
            isPrime = 1
        lst = list(str(i))
        for num in lst:
            if int(num) %2 ==0:
                isPrime =0
                break
        if isPrime ==1:
            numPurePrime+=1
            lastPurePrime=i
    for i in range(n,99999999):
        if i %2 ==0:
            continue
        isPrime = 0
        numberOfFactors = 0
        for e in range(1,int(math.sqrt(i))+1):
            if i%e ==0:
                numberOfFactors+=1
        if numberOfFactors <2:
            isPrime = 1
        lst = list(str(i))
        for num in lst:
            if int(num) %2 ==0:
                isPrime =0
                break
        if isPrime ==1:
            nearestPurePrime = i
            break
    return [numPurePrime,lastPurePrime,nearestPurePrime]

'''
<<<<<Test Cases>>>>>

test.assert_equals(only_oddDigPrimes(20), [7, 19, 31])
test.assert_equals(only_oddDigPrimes(40), [9, 37, 53])
test.assert_equals(only_oddDigPrimes(55), [10, 53, 59])
test.assert_equals(only_oddDigPrimes(60), [11, 59, 71])
'''
