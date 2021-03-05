import os
import csv

csvpath = os.path.join('Resources', '02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv')

with open(csvpath, "r", encoding='utf8') as csvfile: #open entire file and call it csvfile
    csvreader = csv.reader(csvfile,delimiter=",")   # csvreader here is to grab data and breaks into pieces based on delimiter
    # print(csvreader)
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader) # pop one row
    
    voter = 0
    candidate_list = []
    unique_candidate_list = []
    votes_per_candidate_list = []
    percent_per_candidate_list = []


    for row in csvreader:
        # print(row)
        voter = voter + 1
        candidate_list.append(row[2]) # append to column extractions
    
    # define a function here to use it for iterating candidate_list, iterator here is x which is a unique candidate name
    def unique(list1):
        for x in list1: 
            if x not in unique_candidate_list:
                unique_candidate_list.append(x)
                votes_per_candidate = candidate_list.count(x)
                votes_per_candidate_list.append(votes_per_candidate)
                percent_per_candidate = round((votes_per_candidate / voter)*100,2)
                percent_per_candidate_list.append(percent_per_candidate)
        # for x in unique_candidate_list:
            # print (x)

    list1 = candidate_list
    
    unique(list1)

    winner_vote = max(votes_per_candidate_list)
    winner = unique_candidate_list[votes_per_candidate_list.index(winner_vote)] # .index gives me the position of the winner in the list like [0][1][2][3]
    
    # print (unique_candidate_list)
    # print (votes_per_candidate_list)
    # print (percent_per_candidate_list)

    # print (voter)
    # print (candidate_list)
    # print (winner_vote)
    # print (winner)
    
print ("Election Results")
print ("-------------------------")      
print ("Total Votes :" + str(voter))
print ("-------------------------") 
for i in range(len(unique_candidate_list)):
    print(unique_candidate_list[i] + ": " + str(percent_per_candidate_list[i]) + "00% (" + str(votes_per_candidate_list[i]) + ")")
print ("-------------------------")
print ("Winner: " + winner)
print ("-------------------------")


output_file = os.path.join('analysis', 'analysis_result.txt') #Set variable for putput file. save the output path.
with open(output_file, "w", newline='', encoding='utf8') as datafile: # open the output file
    datafile.write("Election Results\n")
    datafile.write("-------------------------\n")
    datafile.write("Total Votes: " + str(voter) + "\n")
    datafile.write("-------------------------\n")
    for i in range(len(unique_candidate_list)):
        datafile.write(unique_candidate_list[i] + ": " + str(percent_per_candidate_list[i]) + "00% (" + str(votes_per_candidate_list[i]) + ")" + "\n")
    datafile.write("-------------------------\n")
    datafile.write("Winner: " + winner +"\n")
    datafile.write("-------------------------\n")
