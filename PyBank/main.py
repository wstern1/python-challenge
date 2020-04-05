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

    total = int(previous[1])
    average_diff = []
    min = 0
    max = 0
    best_month = ''
    worst_month = ''
    for row in csvreader:

        total = total + int(row[1])
        month_diff = int(row[1])-int(previous[1])
        average_diff.append(month_diff)
        if month_diff >= max:
            max = month_diff
            best_month = row[0]
        elif month_diff <= min:
            min = month_diff
            worst_month = row[0]
          


        previous[1] = int(row[1])
    
    print('Total: ' + str('${:,.2f}'.format(total)))

    def average(argument):
            length = len(argument)
            running_total = 0
            for number in argument:
                running_total += number
            return running_total / length
    
    print('Average Change: ' + str('${:,.2f}'.format(round(average(average_diff), 2))))
    print('Greatest Increase in Profits: ' + str(best_month) + " " + '${:,.2f}'.format(max))
    print(('Greates Decrease in Profits: ' + str(worst_month) + " " + '${:,.2f}'.format(min)))

with open (csvpath) as csvfile:   
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        txt = open("analysis/report.txt","w+")
        H = ["Financial Analysis \n", "----------------------- \n"]
        txt.writelines(H)
        txt.write("Total Months: " + str(len(list(csvreader))) + "\n")
        txt.write('Total: ' + str('${:,.2f}'.format(total)) + "\n")
        txt.write('Average Change : ' + str('${:,.2f}'.format(round(average(average_diff), 2))) + "\n")
        txt.write('Greatest Increase in Profits: ' + str(best_month) + " " + '${:,.2f}'.format(max) + "\n")
        txt.write('Greatest Decrease in Profits: ' + str(worst_month) + " " + '${:,.2f}'.format(min) + "\n")