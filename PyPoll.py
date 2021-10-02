# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who recieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate one
# 5. The winner of the election based on popular vote

# Add our dependencies
import csv
import os
# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources","election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis","election_analysis.txt")
# Initialize a vote counter
total_votes = 0
# Candidate Options and candidate votes
candidate_options = []
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file
with open(file_to_load) as election_data:
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)
    # Read the header row
    headers = next(file_reader)
    # Print each row in the CSV file
    for row in file_reader:
       # Add to the total vote count
       total_votes += 1
       # Get the candidate name from each row
       candidate_name = row[2]
       #If the candidate name does not match any existing candidate...
       if candidate_name not in candidate_options:
           # Add candidate name to the candidate list
           candidate_options.append(candidate_name)
           # Begin tracking that candidate's vote count
           candidate_votes[candidate_name] = 0
       # Add a vote to that candidate's count
       candidate_votes[candidate_name] += 1

    # Determine the percentage of votes for each candidate by looping through the counts
    # Iterate through the candidate list
    for candidate_name in candidate_votes:
        # Retrieve vote count  and percentage of a candidate
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        # print out each candidate's name, vote count, and percentage of votes
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Determine winning vote count and candidate
        # Determine if the votes are greater than the winning count
        if(votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
    # Print the winning canidates results to the terminal  
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    


# Print the canidate list
# print(candidate_votes)
    



