def resolve_digits(text):
    text = text.strip()
    if text.isdigit():
        return int(text)
    else:
        raise ValueError('Input must contain a numeric value')

def print_hop(value):
    if value % 15 == 0:
        return 'Hop'
    elif value % 5 == 0:
        return 'Hophop'
    elif value % 3 == 0:
        return 'Hoppity'
    else:
        return None

def loop(value):
    for i in xrange(1, value+1):
        result = print_hop(i)
        if result:
            print result
