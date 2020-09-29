import os
import csv
import numpy as np

budget_csv_path = os.path.join('Resources', 'budget_data.csv')

total_months = []
profit_loss = []
monthly_change = []
monthly_change_list = []

with open(budget_csv_path) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader)
    
    
    for lines in csvreader:
        total_months.append(lines[0])
        profit_loss.append(int(lines[1]))

    monthly_change.append(np.diff(profit_loss))

    # Converting the array into a list
    monthly_change_list = sum(monthly_change)

    # Summing the monthly change
    total = sum(monthly_change_list)

    average_change = total / (len(total_months)-1)
    formated_avg_change = "{:.2f}".format(average_change)

    max_num = np.argmax(monthly_change_list, axis=0)
    min_num = np.argmin(monthly_change_list, axis=0)

    print ("Financial Analysis")
    print ("-------------------------")
    print (f"Total Months: {len(total_months)}")
    print (f"Total: ${sum(profit_loss)}")
    print (f"Average Change: ${formated_avg_change}")
    print (f"Greatest Increase in Profits: {total_months[max_num + 1]} $({monthly_change_list[max_num]})")
    print (f"Greatest Decrease in Profits: {total_months[min_num + 1]} $({monthly_change_list[min_num]})")

output_file = os.path.join('Analysis', 'financial_analysis.txt')

with open(output_file, 'w') as txtfile:

    # Initialize csv.writer
    print("Financial Analysis", file=txtfile)
    print("-------------------------", file=txtfile)
    print(f"Total Months: {len(total_months)}", file=txtfile)
    print(f"Total: ${sum(profit_loss)}", file=txtfile)
    print(f"Average Change: ${formated_avg_change}", file=txtfile)
    print(f"Greatest Increase in Profits: {total_months[max_num + 1]} $({monthly_change_list[max_num]})", file=txtfile)
    print(f"Greatest Decrease in Profits: {total_months[min_num + 1]} $({monthly_change_list[min_num]})", file=txtfile)

