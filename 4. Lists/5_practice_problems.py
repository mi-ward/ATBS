# 1. What is []?
    #this is an array, the first bracket is the start of an array, the closing bracket is the end
    
# 2. How would you assign the value 'hello' as the third value in a list stored
#    in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].) 
    #spam[2] = 'hello' or spam.insert(2, 'hello')

##For the following three questions, let’s say spam contains the list ['a', 'b', 'c', 'd'].

# 3. What does spam[int('3' * 2) / 11] evaluate to?
    # TypeError because list indices must be integers and not floats
    # 'd' if it were spam[int('3' * 2) // 11]
# 4. What does spam[-1] evaluate to?
    # 'd'
# 5. What does spam[:2] evaluate to?
    # ['a', 'b']

## For the following three questions, let’s say bacon contains the list [3.14, 'cat', 11, 'cat', True].

# 6. What does bacon.index('cat') evaluate to?
    # 1
# 7. What does bacon.append(99) make the list value in bacon look like?
    # [3.14, 'cat', 11, 'cat', True, 99]

# 8. What does bacon.remove('cat') make the list value in bacon look like?
    # [3.14, 11, 'cat', True]

# 9. What are the operators for list concatenation and list replication?
    # + and *

# 10. What is the difference between the append() and insert() list methods?
    # append adds to the end, insert adds to wherever you tell it to index

# 11. What are two ways to remove values from a list?
    #del which removes by index or remove() which removes based on the value

# 12. Name a few ways that list values are similar to string values.
    #they have a length, they can be indexed and sliced

# 13. What is the difference between lists and tuples?
    # lists are mutable, tuples are not

# 14. How do you type the tuple value that has just the integer value 42 in it?
    # (42, )

# 15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?
    # list((tuple)), tuple([list])

# 16. Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?
    # they contain a list reference

# 17. What is the difference between copy.copy() and copy.deepcopy()?
    # copy.copy() copies the list values at the top level, copy.deepcopy() copies all sublist values
