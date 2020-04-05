import os
import csv

csvpath = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    for date in csvreader:
        print('Financial Analysis')
        print('-----------------------------')
        print("Total Months: " + str(len(list(csvreader)))) 
        months = str(len(list(csvreader)))


with open (csvpath) as csvfile:   
    csvreader = csv.reader(csvfile, delimiter=',')
    for date in csvreader:
        txt = open("analysis/report.txt","w+")
        H = ["Financial Analysis \n", "----------------------- \n"]
        txt.writelines(H)
        txt.write(f"Total Months: {len(list(csvreader))}")
  