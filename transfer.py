def transfer(account, target, amount):
    # BUG: no check that account has sufficient balance
    account.balance -= amount
    target.balance += amount
