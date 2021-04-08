intrest = float(input("enter the yearly interest rate:"))
amount = int(input("enter the monthly interest rate:"))
no_of_month_paid = int(input("enter a number:"))
print('Month\tCD Value')
count = 0
Month = 1
while count < no_of_month_paid:
    cd_value = amount + amount * (intrest / 1200)
    amount = cd_value
    count += 1
    roundvalue = round(cd_value, 2)
    print(Month, '\t', roundvalue)    

