def isPrime(number):
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            return False
        divisor += 1
        return True

def PrintPrimeNumbers(PrimeNumbers):
    PRIME_NUMBERS = 50
    PRIME_NUMBERS_PER_LINE = 10
    count = 10
    number = 2

    while count < PrimeNumbers:
        if isPrime(number):
            count += 1

            print(number, end=  " ")
            if count % PRIME_NUMBERS_PER_LINE == 0:
                print()
        number += 1 

def main():

    print('the first prime numbers are')

    PrintPrimeNumbers
    main()           