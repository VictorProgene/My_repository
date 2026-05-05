student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

nato = pandas.read_csv("nato_phonetic_alphabet.csv")
# letter = nato["letter"].tolist()
# code = nato["code"].tolist()
#
# nato_dict = {key:value for (key, value) in zip(letter, code)}
# print(nato_dict)

# Professor's solution:
phonetic_dic = {row.letter: row.code for (i, row) in nato.iterrows()}
print(phonetic_dic)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# name = input("What's your name?\n").upper()
# print(list(name))
#
# nato_name = [nato_dict[letter_name] for letter_name in name if letter_name != " "]
# print(nato_name)

# professor's solution:
name = input("What's your name?\n").upper()
output_list = [phonetic_dic[letter] for letter in name if letter !=" "]
print(output_list)