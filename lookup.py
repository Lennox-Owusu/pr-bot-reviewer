def get_item(items, index):
    return items[index]


def parse_ratio(text):
    a, b = text.split(":")
    return int(a) / int(b)
