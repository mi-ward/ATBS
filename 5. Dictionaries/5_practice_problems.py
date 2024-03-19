# 1. What does the code for an empty dictionary look like?
    # {}

# 2. What does a dictionary value with a key 'foo' and a value 42 look like?
    # {'foo': 42}

# 3. What is the main difference between a dictionary and a list?
    # dictionaries are unordered and have reference value (key)

# 4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?
    # you recieve a KeyEerror

# 5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?
    # these will return the same thing which is True

# 6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?
    # these will return different things because 'cat' in spam looks across keys. so True for the first and false for the second (unless 'cat' is a value)

# 7. What is a shortcut for the following code?
#                  if 'color' not in spam:
#                      spam['color'] = 'black'
    # spam.setdefault('color', 'black')

# 8. What module and function can be used to “pretty print” dictionary values?
    # import pprint, the pprint module
    # pprint.pprint(dict), the function