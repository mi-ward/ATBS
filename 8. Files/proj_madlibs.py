

empty_madlib_file = open('madlib_script.txt')
empty_madlib = empty_madlib_file.read()

#TODO -> Create the object that calculates the number of each word type
parts_of_speech = {}
parts_of_speech_count = {'ADJECTIVE': len(empty_madlib.split('ADJECTIVE')) - 1,
                         'NOUN': len(empty_madlib.split('NOUN')) - 1,
                         'VERB': len(empty_madlib.split('VERB')) - 1}

#Create the interface that collects input form the user
for part_of_speech in parts_of_speech_count:
    temp_list = []
    for idx in range(parts_of_speech_count[part_of_speech]):
        if part_of_speech.lower().startswith(('a', 'e','i', 'o','u')):
            user_input = input("Enter an " + part_of_speech.lower() + ':\n')
        else:
            user_input = input("Enter a " + part_of_speech.lower() + ':\n')
        temp_list.append(user_input)
    parts_of_speech[part_of_speech] = temp_list
    

#Split the string and replace with each input
partially_filled_madlib = empty_madlib
for part_of_speech in parts_of_speech:
    filled_madlib = ""
    phrases = partially_filled_madlib.split(part_of_speech)
    for pos_idx in range(len(parts_of_speech[part_of_speech])):
        filled_madlib += (phrases[pos_idx] + parts_of_speech[part_of_speech][pos_idx])
        
    filled_madlib += phrases[-1]
    partially_filled_madlib = filled_madlib

#create it as a new text file
filled_madlib_file = open('madlib_script_complete.txt', 'w')
filled_madlib_file.write(filled_madlib)

empty_madlib_file.close()
filled_madlib_file.close()