def withdraw(account, amount):
    # BUG: no balance/overdraft check
    account.balance -= amount
    return account.balance

# burst 1

# burst 2
