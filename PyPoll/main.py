import os
import csv

csvpath = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    total_votes = len(list(csvreader))

    print('Total Votes ' + str((total_votes))) 
    print('Election Results')
    print('-----------------------')  
    

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    # Used candidate_list to identify all candidates who received votes.
    candidate_list = []
    candidate = {}
    khan_count = 0
    correy_count = 0
    li_count = 0
    otooley_count = 0

    for row in csvreader:
        # Iterated through 'Candidate' column to identify and append candidates to list.
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
        if row[2] == 'Khan':
            khan_count += 1
        elif row[2] == 'Correy':
            correy_count += 1
        elif row[2] == "Li":
            li_count += 1
        elif row[2] == "O'Tooley":
            otooley_count += 1
    # Printed candidate_list to terminal, used this info to populate keys of candidate dictionary below.
    #print(candidate_list)
    candidate = {'Khan ' : "{0:.0%}".format((khan_count)/(total_votes)) + " " + "(" + str(khan_count) +  ")", 
                'Correy ' : "{0:.0%}".format((correy_count)/(total_votes)) + " " + "(" + str(correy_count) + ")", 
                'Li ' : "{0:.0%}".format((li_count)/(total_votes)) + " " + "(" + str(li_count) + ")", 
                "O'Tooley " : "{0:.0%}".format((otooley_count)/(total_votes)) + " " + "(" + str(otooley_count)}

    
    print(candidate)
    print('-----------------------')

    vote_list = [khan_count, correy_count, li_count, otooley_count]
        
    if khan_count == max(vote_list):
            print("Winner: Khan")
            winner = "Khan"
    elif correy_count == max(vote_list):
            print("Winner: Correy")
            winner = "Correy"
    elif li_count == max(vote_list):
            print("Winner: Li")
            winner = "Li"
    elif otooley_count == max(vote_list):
            print("Winner: O'Tooley")
            winner = "O'Tooley"
    

 
       
with open (csvpath) as csvfile:   
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        txt = open("Analysis/report.txt","w+")
        H = ["Election Results \n", "----------------------- \n", "Total Votes: " + str(total_votes) + "\n", "----------------------- \n"]
        txt.writelines(H)
        txt.write(str(candidate) + "\n") 
        txt.write('-----------------------' + "\n")
        txt.write("Winner: " + str(winner))
       
        
