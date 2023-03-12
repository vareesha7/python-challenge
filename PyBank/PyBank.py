import os
import csv

# File path
PyBank_file = os.path.join("Resources", "budget_data.csv")
# Set variables
net_total = 0
months_count = 0
change = 0
greatest_increase = 0
greatest_decrease = 0
greatest_increase_month = ("")
greatest_decrease_month = ("")
data = []

# open the budget data file
with open(PyBank_file,"r",newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ",")
    file_header = next(csvreader)

    for row in csvreader:
        #the total number of months included in the dataset
        months_count = months_count + 1

        #The net total amount of "Profit/Losses" over the entire period
        net_total = int(net_total) + int(row[1])

        #Put data into a list to calculate monthly change
        data.append(row)
        
        #Loop through the whole list and get the monthly change (next month - current month)
        #len -1 is for the avoiding inaccurate calculation for the last data
        for i in range(len(data)-1):
            monthly_change = int((data)[i + 1][1]) - int((data)[i][1])

            #The greatest increase in profits (date and amount) over the entire period
            if greatest_increase < monthly_change:
                greatest_increase = monthly_change
                greatest_increase_month = data[i + 1][0]                

            #The greatest decrease in losses (date and amount) over the entire period
            if  greatest_decrease > monthly_change:
                    greatest_decrease = monthly_change
                    greatest_decrease_month = data[i + 1][0]

            #The average change in losses (date and amount) over the entire period
            average_change = round((int((data)[-1][1]) - int((data)[0][1])) / (len(data)-1),2)

# Create an output file
output_file = os.path.join("Analysis", "pybank_ result.csv")
with open(output_file,"w",newline="") as datafile:
    writer = csv.writer(datafile)

    # Write output to the file
    writer.writerow(["Financial Analysis"])
    writer.writerow(["----------------------------"])
    writer.writerow([f'Total Months: {months_count}'])
    writer.writerow([f'Total: ${net_total}'])
    writer.writerow([f'Average Change : ${average_change}'])
    writer.writerow([f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})'])
    writer.writerow([f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})'])

# Show the output in terminal
print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {months_count}')
print(f'Total: ${net_total}')
print(f'Average Change : ${average_change}')
print(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})')