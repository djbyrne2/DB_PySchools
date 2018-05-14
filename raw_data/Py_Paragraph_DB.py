import os
import csv
import re

file_name = os.path.join("raw_data", "paragraph_2.txt")
print(os.path.exists(file_name))

with open (file_name, newline ="") as file_object:
    contents = file_object.read()

cleaned_contents = contents.replace('\n', ' ')

#print(cleaned_contents)

words = cleaned_contents.split()

number_words = len(words)
print(number_words)

sentences = re.split("(?<=[.!?]) +", cleaned_contents)
number_sentences = len(sentences)
print(number_sentences)

total_characters = 0
for words in words:
    total_characters += len(words)
print(total_characters)

avg_letter_count = total_characters/number_words
print(avg_letter_count)

avg_sentence_count = number_words/number_sentences
print(avg_sentence_count)

print("In this document there are approximately "+ str(number_words)+ " words.")
print("In this document there are approximately "+ str(number_sentences)+ " sentences.")
print("In this document the average letter count per word is "+ str(avg_letter_count)+ " letters.")
print("In this document the average sentence contains approximately "+ str(avg_sentence_count)+ " words.")
