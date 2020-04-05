import os
import csv

csvpath = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    
    for row in csvreader:
        print('Financial Analysis')
        print('-----------------------------')
        print("Total Months: " + str(len(list(csvreader)))) 
        
       

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    previous = next(csvreader)

    count = 1
    total = int(previous[1])
    averagediff = []
    min = 0
    max = 0
    for row in csvreader:

        count += 1
        total = total + int(row[1])
        previous[1] = int(row[1])
    print('Total: ' + str(total))

with open (csvpath) as csvfile:   
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        txt = open("analysis/report.txt","w+")
        H = ["Financial Analysis \n", "----------------------- \n"]
        txt.writelines(H)
        txt.write(f"Total Months: {len(list(csvreader))} \n")
        txt.write(f"Total: {total} \n")
    
  