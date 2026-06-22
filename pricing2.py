def compute_discount(price, rate):
    return price * (1 - rate)


def apply_tax(total, tax_rate):
    return total + total * tax_rate
