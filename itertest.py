import itertools

def generate_strings():
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    for combo in itertools.product(characters, repeat=8):
        yield ''.join(combo)

# Usage example:
for string in generate_strings():
    if string == "QrSTAjGm":
        print(string)
        break