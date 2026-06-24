def withdraw(account, amount):
    # BUG: no balance/overdraft check
    account.balance -= amount
    return account.balance
