import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if (toss == 1 and guess == 'heads') or (toss == 0 and guess == 'tails'):
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if (toss == 1 and guess == 'heads') or (toss == 0 and guess == 'tails'):
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')

# VVV code that was fixed VVV
# import random
# guess = ''
# while guess not in ('heads', 'tails'):
#     print('Guess the coin toss! Enter heads or tails:')
#     guess = input()
# toss = random.randint(0, 1) # 0 is tails, 1 is heads
# if toss == guess:
#     print('You got it!')
# else:
#     print('Nope! Guess again!')
#     guesss = input()
#     if toss == guess:
#         print('You got it!')
#     else:
#         print('Nope. You are really bad at this game.')