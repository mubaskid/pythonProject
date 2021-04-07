from models.Account import Account
class Loan:
    def __init__(self, account: Account, date_obtained, pay_date, interest_rate, amount):
        self.account = account
        self.date_obtained = date_obtained
        self.pay_date = pay_date
        self.amount = amount
        self.interest = interest_rate