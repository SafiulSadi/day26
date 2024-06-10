# numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)
#
# new_list = [n + 1 for n in numbers]
# print(new_list)
# name = "Angela"
# new_list = [letter for letter in name ]
# print(new_list)
# # python sequences
# # list range string tuple
# new_list = [i*2 for i in range(1,5)]
# print(new_list)

# conditional list comprehension
# new_list = [new_item for item in list if test]
# new_list = [new_item for item in list if test]
# new_list = [new_item for item in list if test]
# new_list = [new_item for item in list if test]
# new_list = [new_item for item in list if test]
# # squared_numbers = [new_item for item in list]
# squared_numbers = [n**2 for n in numbers]
# print(squared_numbers)
# result = [int(n) for n in numbers if n % 2 == 0]
# print(result)

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
#
# numbers2 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# with open("file1.txt", "a") as f1:
#     for i in numbers:
#         f1.write(f"{i}\n")
#
# with open("file2.txt", "a") as f2:
#     for i in numbers:
#         f2.write(f"{i}\n")

# with open("file1.txt", "r") as f1:
#     nums = f1.read()
#
# num1 = [n.splitlines() for n in nums]
# print(nums)
# print(num1)
# num1 = nums.split()
# dictionary comprehension
# new_dict = {new_key: new_value for item in list}
# new_dict = {new_key: new_value for (key, value) in dict.items()}
# new_dict = {new_key: new_value for (key, value) in dict.items() if test}
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

# students_score = {new_key: new_value for item in list}
# import random
# students_score = {name: random.randint(1,100) for name in names}
# print(students_score)
#
# passed_students = {student: score for (student, score) in students_score.items() if score >= 60}
# print(passed_students)

# sentence = 'What is the Airspeed Velocity of an Unladen Swallow?'
# words = sentence.split()
# print(words)
# # result = {new_key: new_value for item in list}
# result = {word: len(word) for word in words}
# print(result)
# import pandas
#
# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# # Looping through dictionaries:
# for (key, value) in student_dict.items():
#     # print(key)
#     pass
#
# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# Loop through a data frame
# for (key, value) in student_data_frame.items():
#     print(value)

# Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     if row.student == "Angela":
#         print(row.score)
import pandas

# new_dict = {new_key: new_value for (key, value) in dict.items()}

# new_dict = {new_key: new_value for (index, row) in df.iterrows()}
# new_dict = {new_key: new_value for (key, value) in df.iterrows()}
# new_dict = {new_key: new_value for (key, value) in df.iterrows()}
# new_dict = {new_key: new_value for (key, value) in df.iterrows()}
# new_dict = {new_key: new_value for (key, value) in df.itterrows()}
df = pandas.read_csv("nato_phonetic_alphabet.csv")
print(df)
data_dict = {row.letter: row.code for (index, row) in df.iterrows()}
print(data_dict)

x = input("Enter a word").upper()

list_comp = [data_dict[letter] for letter in x]

print(list_comp)




