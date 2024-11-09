import math

def PrimeFormula(n):
    return (math.factorial(n) % (n + 1) // n)*(n - 1) + 2

def PrimeNumbers(n):
    primes = [2]
    for i in range(1,n):
        primes.append(PrimeFormula(i))
        if PrimeFormula(i) == 2:
            primes.pop()
    return primes


def PrimeCheck(num):
    if num > 1 :
        for i in range(2, (num//2) +1 ):

            if num % i == 0:
                return False
        
        else :
            return True

    else:
        return False



def PrimeFactorization(n: int) :
    factors = []
    i = 2
    while i * i <= n:
        if n % i :
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors



def MainMenu():
    choice = int(float(input("What would you like to do? \n1)Create a list of prime numbers: \n2)Check if a number is a prime number: \n3)Find prime factors of a number: \n>>>")))
    if choice == 1:
        print("Generate a list of primes!")
        PrimeList()
    if choice == 2:
        print("Check if a number is a prime number!")
        PrimeChecker()
    if choice == 3:
        print("Find the prime factors of a number!")
        PrimeFactors()
    else:
        print("Invalid input! Returning to main menu")
        MainMenu()

def PrimeList():
    x = int(float(input("Until which prime number would you like to generate? \nChoose an integer above 0 to generate list, or 0 to return to main menu: ")))
    if x > 0 :
        print(PrimeNumbers(n=x))
        PrimeList()
    elif x == 0 :
        print("Returning to main menu!")
        MainMenu()
    else:
        print("Invalid input! Try again...")

def PrimeChecker():
    x = int(float(input("Input a number to check if it's prime or not, 0 to return to the main menu (0 is not a prime btw :p) : ")))
    if x > 0 :
        PrimeCheck(x)
        if PrimeCheck(x) == 0:
            print(str(x) + " is not a prime number!")
        elif PrimeCheck(x) == 1:
            print(str(x) + " is a prime number!")
        PrimeChecker()
    elif x < 0 :
        print("No negative number is prime!")
        PrimeChecker()
    elif x == 0:
        print("Returning to main menu!")
        MainMenu() 
    else:
        print("Invalid input! Try again...")

def PrimeFactors():
    x = int(float(input("Input a number to generate a list of its prime factors, or 0 to return to main menu: ")))
    if x > 0:
        print(PrimeFactorization(n=x))
        PrimeFactors()
    elif x < 0:
        print("Input the positive value, then just add -1 by yourself :p")
        PrimeFactors()
    elif x == 0:
        print("Returning to main menu!")
        MainMenu() 
    elif x == 1 :
        print("Is 1 a prime number? Well, a nice output here would be [1], so there you go :3c ")
        PrimeFactors()
    else:
        print("Invalid input! Try again...")

MainMenu()