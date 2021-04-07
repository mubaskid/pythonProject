from models.Account import Account

class Overdraft:
    def __init__(self, account:Account,  status, amount, date, ):
        self.account = account
        self.account_status = status
        self.amount = amount
        self.date_obtained = date
