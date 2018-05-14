import os
import csv
import re

file_name = os.path.join("raw_data", "paragraph_1.txt")
print(os.path.exists(file_name))

with open (file_name, newline="") as file_object:
    contents = file_object.read()

words = contents.split()

number_words = len(words)

sentences = re.split("(?<=[.!?]) +", contents)

number_sentences = len(sentences)

average_word = sum(len(words) for word in words / len(words)

# sum(len(sentences) for sentence in contents) / len(sentences)

print(contents + "\n")
print("This is the number of words "+ str(number_words))
print("This is the number of sentences "+ str(number_sentences))
print("This is the average word length " +str(average))
print("This is the average sentence length "+str(avg_sentence_len))

# >>> sentence = "Hi my name is Bob"
# >>> words = sentence.split()
# >>> average = sum(len(word) for word in words) / len(words)
# >>> average
# 2.6