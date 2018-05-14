import os
import csv

csv_file_path = os.path.join('raw_data', 'election_data_2.csv')

poll = {}

total_votes = 0

with open(csv_file_path, 'r') as csvfile:
    csvread = csv.reader(csvfile)
    next(csvread, None)

    for row in csvread:
        total_votes += 1
        if row[2] in poll.keys():
            poll[row[2]] = poll[row[2]] + 1
        else:
            poll[row[2]] = 1
 
#######
candidate_name = []
number_votes = []

for key, value in poll.items():
    candidate_name.append(key)
    number_votes.append(value)

vote_percentage = []
for n in number_votes:
    vote_percentage.append(round(n/total_votes*100, 1))

# zips candidates, num_votes, vote_percent into tuples
clean_data = list(zip(candidate_name, number_votes, vote_percentage))

#creates winner_list to put winners (even if there is a tie)
winner_list = []

for name in clean_data:
    if max(number_votes) == name[1]:
        winner_list.append(name[0])

# makes winner_list a str with the first entry
winner = winner_list[0]

#only runs if there is a tie and puts additional winners into a string separated by commas
if len(winner_list) > 1:
    for w in range(1, len(winner_list)):
        winner = winner + ", " + winner_list[w]

# #prints to file
# output_file = os.path.join('Output', 'election_results_' + str(file_num) +'.txt')

# with open(output_file, 'w') as txtfile:
#     txtfile.writelines('Election Results \n------------------------- \nTotal Votes: ' + str(total_votes) + 
#       '\n-------------------------\n')
#     for entry in clean_data:
#         txtfile.writelines(entry[0] + ": " + str(entry[2]) +'%  (' + str(entry[1]) + ')\n')
#     txtfile.writelines('------------------------- \nWinner: ' + winner + '\n-------------------------')

# #prints file to terminal
# with open(output_file, 'r') as readfile:
#     print(readfile.read())