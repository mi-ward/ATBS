def collatz(number):
    if number % 2 == 0:
        return (number // 2)
    else:
        return (3 * number + 1)

print("Enter number:")

i = None
while True:
    try:
        if i == None:
            i = int(input())

        print(i)
        if i == 1:
            break
        i = collatz(i)

    except ValueError:
        print("You must enter an integer.")





