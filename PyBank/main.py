# Dependencies
import os
import csv

# Initialize variables
counter = 1
profit_loss = 0
profit_increase = 0
profit_decrease = 0

# Access the budget data directory
csvpath = os.path.join('Resources','budget_data.csv')

# Open the csv file to read and analyze the data
with open(csvpath, encoding='utf-8') as csvfile:
    
    # Access the CSV Reader 
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip the header
    csvheader = next(csvreader)
    # Get the first row of data out so we can have something to compare the rest of data to.
    first_row = next(csvreader)
    # Grab the profit/loss amount to compare the rest of the data
    first_profit = int(first_row[1])
    # Initialize the profit_loss amount to calculate the net amount
    profit_loss = int(first_row[1])
    
    # Loop through the csv file to access each data row
    for row in csvreader:
        # Update the counter to get the total months
        counter = counter + 1 
        # Get the profit to add to the profit loss amount
        profit = int(row[1]) 
        # Update profit loss after accessing the row each iteration
        profit_loss = profit_loss + profit 
        # Get the profit change 
        decrease = profit - first_profit
        # If statement to get the greatest increase/decrease 
        if decrease > profit_increase:
            # Greatest increase value after each iteration
            profit_increase = decrease
            # Get the date in the row with the greates increase
            date = row[0]
        # If statement to access the greatest decrease
        if decrease < profit_decrease:
            # Greatest decrease after each iteration
            profit_decrease = decrease
            # Access the date where the greatest decrease occur
            Dates = row[0]
        # Update/re-initialize the profit to compare with next row.
        first_profit = profit
    # Calculate the average change from the entire period
    average_change = round((profit - int(first_row[1]))/(counter-1),2)
    
# Unnecesary value assignments for the total months and profit loss
total_months = counter
Total = profit_loss
# Print ou the results
print("```Text\n Financial Analysis\n----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${Total}")
print(f"Average change: ${average_change}")
print(f"Greatest Increase in Profits: {date} (${profit_increase})")
print(f"Greatest Decrease in Profits: {Dates} (${profit_decrease})")
print("```")
# Access the directory to write the new csv file
output_path = os.path.join('Analysis','output.csv')
# Open the csv file to write
with open(output_path, 'w') as datafile:
    writer = csv.writer(datafile)
    # Write in the rows based on what the results should look like
    writer.writerow(["```Text"])
    writer.writerow(["Financial Analysis"]) 
    writer.writerow(["----------------------------"])
    writer.writerow([f"Total Months: {total_months}"])
    writer.writerow([f"Total:  ${Total}"])
    writer.writerow([f"Average change: ${average_change}"])
    writer.writerow([f"Greatest Increase in Profits:  {date} (${profit_increase})"])
    writer.writerow([f"Greatest Decrease in Profits:  {Dates} (${profit_decrease})"])
    writer.writerow(["```"])
# End of code.