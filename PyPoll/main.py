# This is main.py in PyPoll
import os
import csv

electiondata_csv = os.path.join("election_data.csv")

# Open and read csv
with open(electiondata_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# Skip header row
    csv_header = next(csvreader)

# declare variables and starting values
    votes = 0
    candidate_count = 0
    candidates = []
    candidate_vote = []

    winning_candidate = ""
    winning_candidate_votes = 0

    for row in csvreader:
        votes += 1
        if row[2] not in candidates:
            candidates.append(row[2])
            candidate_vote.append(1)
        id = 0
        for candidate in candidates:
            if row[2] == candidate:
                candidate_vote[id] += 1
            id += 1

    print("Election Results")
    print("-----------------------------")
    print(f"Total Votes: {int(votes)}")
    print("-----------------------------")
    id = 0
    for candidate in candidates: 
        print(f"{(candidate)}",f"{(candidate_vote[id]/votes) * 100 :.3f}%",f"({(candidate_vote[id])})")
        if winning_candidate == "": 
            winning_candidate = candidate  
        if candidate_vote[id] > winning_candidate_votes: 
            winning_candidate = candidate  
            winning_candidate_votes = candidate_vote[id]
        id += 1
    print("-----------------------------")
    print(f"Winner: {winning_candidate}")
    print("-----------------------------")


# save the output file path
output_file = os.path.join("output.csv")

# open the output file, create a header row, and then write the 
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Election Results"])
    writer.writerow(["-----------------------------"])
    writer.writerow([f"Total Votes: {int(votes)}"])
    writer.writerow(["-----------------------------"])
    id = 0
    for candidate in candidates: 
        writer.writerow([f"{(candidate)}",f"{(candidate_vote[id]/votes) * 100}%",f"{(candidate_vote[id])}"])
        if winning_candidate == "": 
            winning_candidate = candidate  
        if candidate_vote[id] > winning_candidate_votes: 
            winning_candidate = candidate  
            winning_candidate_votes = candidate_vote[id]
        id += 1
    writer.writerow(["-----------------------------"])
    writer.writerow([f"Winner: {winning_candidate}"])
    writer.writerow(["-----------------------------"])

datafile.close()

# The total number of votes cast
    # Add number of rows (minus header row - done above) to Calculate the total number of votes cast

# A complete list of candidates who received votes
    # Loop through list and each time a new candidate name is found add it to the list of candidates to print

# A complete list of candidates who received votes
    # done - Loop through list and each time a new candidate name is found  
    # add it to the list of candidates to print

# The total number of votes each candidate won
    # Loop through list and each time a candidate is listed, add 1 to their vote total (The total number of votes each candidate won)

# The percentage of votes each candidate won
    # Divide the number of votes that a candidate won by the number of total votes and create a percentage * 100

# The winner of the election based on popular vote.
    # Loop through list of candidates and find the candidate with the lagest number of votes