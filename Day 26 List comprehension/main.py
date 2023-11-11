my_list = [1, 2, 3]
new_list = []
for n in my_list:
    add_1 = n + 1
    new_list.append(add_1)
print(new_list)

# List comprehension [new_item for item in list]
numbers = [1, 2, 3]
new_list1 = [n + 1 for n in numbers]
print(new_list1)

# List comprehension strings
name = "Arun"
letters_list = [letter for letter in name]
print(letters_list)
# Range
double = [n * 2 for n in range(1, 5)]
print(double)
# Conditional List comprehension [new_item for item in list if test]
names = ["alex", "beth", "caroline", "dave", "elanor", "freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

uppercase_names = [name.upper() for name in names if len(name) > 5]
print(uppercase_names)
# dict comprehension {new key:new value for item in list}
#
import random

body_count = {n: random.randint(1, 10) for n in names}
print(body_count)
rizz = {student: count for (student, count) in body_count.items() if count > 5}
print(rizz)
# Data frame comprehension
import pandas

student_hist = {
    "student": ["Arun", "Batman", "Monish", "Kamesh"],
    "Body_count": [7, 4, 8, 9]
}
student_df = pandas.DataFrame(student_hist)
print(student_df)

# for (key, value) in student_df.items():
#     print(key or value)

for (index, row) in student_df.iterrows():

    if row.student == "Arun":
        print(row.Body_count)

# NATO Phonetic alphabet exercise
data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


def generate():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry there can only be alphabet.")
        generate()
    else:
        print(output_list)


generate()
