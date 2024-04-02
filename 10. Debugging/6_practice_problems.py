# Practice Questions
# 1. Write an assert statement that triggers an AssertionError if the variable spam is an integer less than 10.

    # spam = 0
    # assert spam >= 10, "spam can't be less than 10"

# 2. Write an assert statement that triggers an AssertionError if the variables eggs and bacon contain strings 
# that are the same as each other, even if their cases are different 
# (that is, 'hello' and 'hello' are considered the same, and 'goodbye' and 'GOODbye' are also considered the same).

    # eggs = 'EGGS'
    # bacon = 'eggs'
    # assert eggs.lower() != bacon.lower(), "eggs and bacon can't be the same"

# 3. Write an assert statement that always triggers an AssertionError.
    #assert False, "always trigger"

# 4. What are the two lines that your program must have in order to be able
# to call logging.debug()?
    
    # import logging
    # logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

# 5. What are the two lines that your program must have in order to have
# logging.debug() send a logging message to a file named programLog.txt?

    # import logging
    # logging.basicConfig(filename='programLog.txt', level=logging.DEBUG, 
    # format=' %(asctime)s - %(levelname)s - %(message)s')

# 6. What are the five logging levels?
    # DEBUG, INFO, WARNING, ERROR, CRITICAL

# 7. What line of code can you add to disable all logging messages in your program?
    # logging.disable(logging.CRITICAL)

# 8. Why is using logging messages better than using print() to display the same message?
    # you can control them all from one line, turn them off, and print them to a file

# 9. What are the differences between the Step, Over, and Out buttons in the Debug Control window?
    # Step takes you to the next function and will go into the function
    # Over will execute the function
    # Out will execute the rest of the function you're in

# 10. After you click Go in the Debug Control window, when will the debugger stop?
    # the first line if set, or it will run through the program unless a breakpoint is set

# 11. What is a breakpoint?
    # a point you select in the code to pause the program execution

# 12. How do you set a breakpoint on a line of code in IDLE?
    # in vscode you click on the line, in IDLE you right click and select Set Breakpoint