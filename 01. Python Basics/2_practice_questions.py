# 1. Which of the following are operators, and which are values?
    # *       ->  Operator
    # 'hello' ->  Value 
    # -88.8   ->  Value
    # -       ->  Operator
    # /       ->  Operator
    # +       ->  Operator
    # 5       ->  Value

# 2. Which of the following is a variable, and which is a string?
    # spam    -> Variable
    # 'spam'  -> String

# 3. Name three data types.
    # Strings, Integers, Floats

# 4. What is an expression made up of? What do all expressions do?
    # An expression is made up of values and operators.
    # An expression will evaluate down to the singular value.

# 5. This chapter introduced assignment statements, like spam = 10. 
#   What is the difference between an expression and a statement?
    # An expression evaluates to a value
    # A statement does not

# 6. What does the variable bacon contain after the following code runs? 
#   bacon = 20
#   bacon + 1 
    #   bacon contains 20 still

# 7. What should the following two expressions evaluate to?
#    'spam' + 'spamspam' -> 'spamspamspam'
#    'spam' * 3 -> 'spamspamspam'

# 8. Why is eggs a valid variable name while 100 is invalid?
    #   Variables can't start with a number.

# 9. What three functions can be used to get the integer, floating-point
#    number, or string version of a value?
    #  int(), float(), str()

# 10. Why does this expression cause an error? How can you fix it?
#    'I have eaten ' + 99 + ' burritos.'
    # An error is caused because you're trying to add a string and an int and python can't do that.
    # You can fix it by running the following: 'I have eaten ' + str(99) + ' burritos.'

# Extra credit: Search online for the Python documentation for the len() function. 
# It will be on a web page titled “Built-in Functions.” 
# Skim the list of other functions Python has, look up what the round() function does, 
# and experiment with it in the interactive shell.
    # Example: round(123.12340912834012938412, 3) -> 123.123
