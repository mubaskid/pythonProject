print(int(input('Enter a number: ')))
def checkEven(i):
    for i in range(1, 1000):
        for x in range(1, i):
            numbers = []
            if x % i == 0:
                numbers.append(x)
                return numbers


checkEven(6)
print(checkEven)