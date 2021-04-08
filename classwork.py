def multiplicationTable(num, multiply_by):
    i = 0
    while i < multiply_by:
        i += 1
        print(f"{num} x {1} = {1 * num}")


number = int(input("enter your number:"))
no_of_times_multiplied = int(input("enter the number of times: "))

multiplicationTable(number, no_of_times_multiplied)