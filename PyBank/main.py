import os
import csv

budgetdata_csv = os.path.join("budget_data.csv")

# Open and read csv
with open(budgetdata_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# Skip header row
    csv_header = next(csvreader)

# Declare variables and starting value
    months = 0
    profitloss_total = 0
    profitloss_averagechange = 0
    profitloss_change = 0
    profitloss_change_num = 0
    month_greatest_inc = ""
    greatest_inc = 0
    month_greatest_dec = ""
    greatest_dec = 0

    previous_month = ""
    previous_month_amt = 0

    for row in csvreader:    
        months += 1
        profitloss_total += int(row[1])
        
        if previous_month != "":
            profitloss_change = profitloss_change + (int(row[1]) - previous_month_amt)
            profitloss_change_num += 1      
            if int(row[1]) - previous_month_amt > greatest_inc:
                month_greatest_inc = (row[0])
                greatest_inc = int(row[1]) - previous_month_amt
            if int(row[1]) - previous_month_amt < greatest_dec:
                month_greatest_dec = row[0]
                greatest_dec = int(row[1]) - previous_month_amt
        previous_month = row[0]
        previous_month_amt = int(row[1])
    
    profitloss_averagechange = profitloss_change / profitloss_change_num 

# Print budget_data information
    print("Financial Analysis")
    print("-----------------------------")
    print(f"Total Months: {int(months)}")
    print(f"Total: ${int(profitloss_total)}")
    print(f"Average Change: ${float(profitloss_averagechange):.2f}")
    print(f"Greatest Increase in Profits: {str(month_greatest_inc)} ${int(greatest_inc)}")
    print(f"Greatest Decrease in Profits: {str(month_greatest_dec)} (${int(greatest_dec)})")

# save the output file path
output_file = os.path.join("output.csv")

# open the output file, create a header row, and then write the 
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Financial Analysis"])
    writer.writerow(["-----------------------------"])
    writer.writerow([f"Total Months: {int(months)}"])
    writer.writerow([f"Total: ${int(profitloss_total)}"])
    writer.writerow([f"Average Change: ${float(profitloss_averagechange):.2f}"])
    writer.writerow([f"Greatest Increase in Profits: {str(month_greatest_inc)} ${int(greatest_inc)}"])
    writer.writerow([f"Greatest Decrease in Profits: {str(month_greatest_dec)} (${int(greatest_dec)})"])

datafile.close()