# Find min number of primes to sum to target.
# Eg. For 100 - 97 and 3
# Eg. For 25 - 23 and 2

# Cases - 
# 1. If the target is prime we need only 1 number
# 2. If the target is even then min numbber of primes would be 2 
# 3. If the target is odd and target - 2 is even then 2 primes, else 3 primes

# We will use a helper function to check if a number is prime or not

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**(1/2) + 1)):
        if (n % i == 0):
            return False
    return True

def minPrime(target):
    
    # Edgecase resolution
    if target < 2:
        return 0 
    
    minCount = 0
    # Case 1
    if isPrime(target):
        minCount = 1
    
    # Case 2 
    
    elif target%2 == 0:
        minCount = 2 
    
    # Case 3 
    else: 
        if isPrime(target - 2):
            minCount = 2
        else:
            minCount = 3 
    
    return minCount


print(minPrime(100))
print(minPrime(17))
print(minPrime(27))
print(minPrime(101))
print(minPrime(104))
print(minPrime(15))