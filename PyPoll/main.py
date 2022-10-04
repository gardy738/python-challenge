# Dependencies:
import os
import csv

# Access file directory
csvpath = os.path.join('Resources', 'election_data.csv')

# Initialize counter for votes
counter = 0
my_dict = {}
# Open the csv file to read through it
with open(csvpath, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)

# Loop through the files to count the total votes
    for row in csvreader:
        counter = counter + 1
        candidate = row[2]
        if candidate in my_dict:
            my_dict[candidate]["votes"] += 1
        else:
            my_dict[candidate] = {"votes":1}
        # Print the first part of the results
    print("```text\n Election Results\n-------------------------")
    print(f"Total Votes: {counter} \n-------------------------")

    winner = 0

    for i in my_dict:
        votes = my_dict[i]
        for j in votes:
            number_votes = votes[j]
            percent = round((number_votes / counter) * 100,3)
            if number_votes > winner:
                winner = number_votes
                name = i
        print(f"{i}: {percent}% ({number_votes})")
    print("------------------------")
    print(f"The winner is: {name}")
    print("```")

output_path = os.path.join('Analysis','output_file.csv')

with open(output_path, 'w') as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["```Text"])
    writer.writerow(["Election Results"]) 
    writer.writerow(["----------------------------"])
    writer.writerow(["```"])
    