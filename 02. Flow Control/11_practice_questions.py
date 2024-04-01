# 1. What are the two values of the Boolean data type? How do you write them?
    # True | False - written with the first letter capitalized
# 2. What are the three Boolean operators?
    # and | or | not
# 3. Write out the truth tables of each Boolean operator 
#   (that is, every possible combination of Boolean values for the operator and what they evaluate to).
    # and
        # True and True   == True
        # True and False  == False
        # False and True  == False
        # False and False == False
    # or
        # True or True   == True
        # True or False  == True
        # False or True  == True
        # False or False == False
    # not
        # not True  == False
        # not False == True

# 4. What do the following expressions evaluate to?
    # (5 > 4) and (3 == 5)                == False
    # not (5 > 4)                         == False
    # (5 > 4) or (3 == 5)                 == True
    # not ((5 > 4) or (3 == 5))           == False
    # (True and True) and (True == False) == False
    # (not False) or (not True)           == True

# 5. What are the six comparison operators?
    # == equals
    # != not equals
    # >  greater than
    # <  less than
    # >= greater than or equal to
    # <= less than or equal to

# 6. What is the difference between the equal to operator and the assignment operator?
    # equal operater is two equal signs (==), assignment operator is one (=)

# 7. Explain what a condition is and where you would use one.
    # a condition is a block of code that only occurs if the condition is met
    # you would use it if you want something to happen for a specific event
    # evaluates to a Boolean

# 8. Identify the three blocks in this code:
    #    spam = 0                    
    #    if spam == 10:             Block 1
    #        print('eggs')               Block 2               
    #        if spam > 5:
    #            print('bacon')             Block 3
    #        else:
    #            print('ham')
    #        print('spam')          End Block 1
    #    print('spam')              

# 9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is
#    stored in spam, and prints Greetings! if anything else is stored in spam.
    # if spam == 1:
    #     print('Hello')
    # elif spam == 2:
    #     print('Howdy')
    # else:
    #     print('Greetings!')

# 10. What can you press if your program is stuck in an infinite loop?
    #ctrl + c

# 11. What is the difference between break and continue?
    # break will exit the loop, continue will move to the start of the loop

# 12. What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?
    # there is no difference, they all do the same thing, they just go into more detail of what's happening in each call

# 13. Write a short program that prints the numbers 1 to 10 using a for loop. 
#     Then write an equivalent program that prints the numbers 1 to 10 using a while loop.
    # for i in range(1, 11):
    #     print(i)

    # x = 0
    # while x < 10:
    #     x = x + 1
    #     print(x)

# 14. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
    #spam.bacon()

#Extra credit: Look up the round() and abs() functions on the Internet, and find out what they do. 
#              Experiment with them in the interactive shell.
