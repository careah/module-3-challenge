import os
import csv

# specify the csv file path
csvpath = "Resources/budget_data.csv"
print(csvpath)

# create empty lists to store data from each column
dates = []
profits_losses = []

# initializing variables
total_months = 0
net_total = 0
previous_profit_loss = 0
total_changes = 0
greatest_increase_profit = 0
greatest_increase_date = ""
greatest_decrease_profit = 0
greatest_decrease_date = ""

# open the csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader) # skip the header row

    # loop through each row and add the data to respective lists
    for row in csvreader:
        dates.append(row[0])
        profits_losses.append(int(row[1]))

        # calculate the total number of months and net total profit/loss
        total_months += 1
        net_total += int(row[1])

        # calculate changes in profit/loss and store the values
        if total_months > 1:
            current_profit_loss = int(row[1])
            change = current_profit_loss - previous_profit_loss
            total_changes += change

            # check for greatest increase and decrease in profit/loss
            if change > greatest_increase_profit:
                greatest_increase_profit = change
                greatest_increase_date = row[0]
            elif change < greatest_decrease_profit:
                greatest_decrease_profit = change
                greatest_decrease_date = row[0]

        previous_profit_loss = int(row[1])

# calculate the average change in profit/loss
average_changes = round(total_changes / (total_months - 1), 2)

# print the analysis to the terminal
print("Financial Analysis\n---------------------------")
print(f"Total Months: {total_months}")
print(f"Total Profit/Loss: ${net_total}")
print(f"Average Change: ${average_changes}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_profit})")
print(f"Greatest Decrease in Losses: {greatest_decrease_date} (${greatest_decrease_profit})")

# specify the output file path
output_path = os.path.join("./Analysis/budget_analysis.txt")

# write the analysis to a text file
with open(output_path, "w") as txtfile:
    txtfile.write("Financial Analysis\n---------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total Profit/Loss: ${net_total}\n")
    txtfile.write(f"Average Change: ${average_changes}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_profit})\n")
    txtfile.write(f"Greatest Decrease in Losses: {greatest_decrease_date} (${greatest_decrease_profit})\n")



###ELECTION DATA###


import csv

# Path to election data CSV file
election_path = os.path.join("Resources", "election_data.csv")

# Initialize variables
total_votes = 0
candidates = []
candidate_votes = {}

# Read the CSV file
with open(election_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    # Skip header row
    next(csv_reader)

    # Loop through each row
    for row in csv_reader:
        # Count the total number of votes
        total_votes += 1
        
        # Add the candidate to the list if they haven't been added before
        if row[2] not in candidates:
            candidates.append(row[2])
            
            # Initialize the candidate's vote count to 0
            candidate_votes[row[2]] = 0
        
        # Add a vote to the candidate's count
        candidate_votes[row[2]] += 1

# Initialize variables for tracking the winning candidate    
winner = ""
winning_votes = 0

# Calculate the percentage of votes each candidate won and determine the winner
for candidate in candidates:
    votes = candidate_votes[candidate]
    percentage = round((votes / total_votes) * 100, 3)
    
    # Check if this candidate won the election
    if votes > winning_votes:
        winner = candidate
        winning_votes = votes
    
    # Print the candidate's results
    print(f"{candidate}: {percentage}% ({votes})")
    
# Print the winner
print(f"Winner: {winner}")

# Save the analysis to a text file
output_path = os.path.join("./Analysis/election_results.txt")

with open(output_path, "w") as file:
    # Print the analysis to the file
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    
    for candidate in candidates:
        votes = candidate_votes[candidate]
        percentage = round((votes / total_votes) * 100, 3)
        file.write(f"{candidate}: {percentage}% ({votes})\n")
        
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")        