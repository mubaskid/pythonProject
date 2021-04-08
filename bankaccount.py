print("Zenith Bank Transfer System")
real_user_id = "6664"
real_balance = 50000
valid_account_number = '99574'
user_id = input("enter user ID:")
maximum_overdraft_allowed = 0.5 * real_balance

if real_user_id != user_id:
    print("wrong account id")
    print('re-enter user ID: ')
    exit(1)


transfer_amount = float(input("enter the amount you wish to transfer: "))   
recipient_account_number = input("enter the recipient account number: ")

if transfer_amount <= 0:
    print("invalid transfer amount")
    exit(2)
    
charges = 0.05 * transfer_amount
total_deducted_charges = transfer_amount
overdraft = total_deducted_charges - real_balance

print("applicable charges:", charges)
print("transfer_amount:", transfer_amount)
print("total debit amount:", total_deducted_charges)
if real_balance < transfer_amount:
    print("overdraft:", overdraft)


if real_balance < transfer_amount and overdraft > maximum_overdraft_allowed:
    print("you can only withdraw 50% of your total balance")
    exit(3)

if recipient_account_number != valid_account_number:
    print("invalid account number:", recipient_account_number)
    exit(4)

print("transfer sucessful")
real_balance -= total_deducted_charges
print(f"current balance: {real_balance:2f}")
