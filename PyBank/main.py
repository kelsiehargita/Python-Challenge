import os
import csv

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)

    number_of_months = 0
    net_total = 0
    previous_profit = 0
    total_profit_change = 0
    greatest_profit_increase = 0
    greatest_profit_decrease = 0
    GPI_month = ""
    GPD_month = ""

    print("Financial Analysis")
    print("----------------------------")

    for row in csvreader:

        number_of_months += 1
        net_total += int(row[1])
        total_profit_change += int(row[1])-previous_profit
        profit_difference = int(row[1])- previous_profit
        previous_profit = int(row[1])

    

        if profit_difference > greatest_profit_increase:
            GPI_month = row[0]
            greatest_profit_increase = profit_difference
        
        if profit_difference < greatest_profit_decrease:
            GPD_month = row[0]
            greatest_profit_decrease = profit_difference



    print("Total Months: " + str(number_of_months))
    print("Total: " + str(net_total))
    
    average_profit_change = total_profit_change/number_of_months
    print("Average Change: " + str(average_profit_change))
    print("Greatest Increase in Profits: " + GPI_month + " " + str(greatest_profit_increase))
    print("Greatest Decrease in Profits: " + GPD_month + " " + str(greatest_profit_decrease))

    output_path = os.path.join(".", "Analysis", "PyBankReport.txt")


with open(output_path, 'w') as txtfile:

    txtfile.write("Financial Analysis"+"\n")
    txtfile.write("----------------------------"+"\n")
    txtfile.write("Total Months: " + str(number_of_months)+"\n")
    txtfile.write("Total: " + str(net_total)+"\n")
    txtfile.write("Average Change: " + str(average_profit_change)+"\n")
    txtfile.write("Greatest Increase in Profits: " + GPI_month + " " + str(greatest_profit_increase)+"\n")
    txtfile.write("Greatest Decrease in Profits: " + GPD_month + " " + str(greatest_profit_decrease)+"\n")

txtfile.close()






  







