#GET PRIME NUMBERS BETWEEN THE GIVEN RANGE
#SIEVE OF ERATOSTHENES

def getPrimeNumbers(low,high):
    primes=[True for j in range(high+1)]
    currentPrime=2
    while currentPrime*currentPrime<=high:
        if primes[currentPrime]==True:
            for i in range(currentPrime*currentPrime,high+1,currentPrime):
                primes[i]=False
        currentPrime+=1
    for i in range(low,high+1):
        if primes[i]:
            print(i)

if __name__ == '__main__':
    low=6
    high=24
    getPrimeNumbers(low,high)
