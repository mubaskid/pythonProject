first_side = int(input("enter the first side: "))
second_side = int(input("enter the second side: "))
third_side =  int(input("enter the  third side: "))

perimeter = first_side + second_side + third_side

if first_side + second_side < third_side:
    print("invalid number")
elif second_side + first_side < third_side:
    print("invalid number")
elif third_side + second_side < first_side: 
    print("invalid")
else:
    print(perimeter)