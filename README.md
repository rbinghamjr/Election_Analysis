# Election_Analysis

## Project Overview
A Colorado Board of Elections employee provided the following tasks to complete an election audit for a recent local congressional election. 

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calcualate the percentage of votes won for each candidate.
5. Determine the winner of the election based on popular vote.
6. Calculate the total number of votes per county and the percentage for that county
7. Determine the county with the largest voter turnout

Due to the large amount of data to analyze for this deliverable, Python scripting was created to provide a detail output in the Terminal as well as in a text file.

## Election-Audit Results
The final analysis of the election data showed the following:
- There were 369,711 votes cast
- There were three counties in the precinct with the total votes for each county as follows:
    - Jefferson: 10.5% (38,855)
    - Denver: 82.8% (306,055)
    - Arapahoe: 6.7% (24,801)
- The county with the largest number of votes was Denver.
- There were three candidates who received votes:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The individual results for the candidates were:
    -Charles Casper Stockham: 85,213 votes representing 23.0% of votes cast
    -Diana DeGette: 272,892 votes representing 73.8% of votes cast
    -Raymon Anthony Doane: 11,606 votes representing 3.1% of votes cast
- The winner of the election was:
    -Diana DeGette who received 272,892 votes out of the 369,711 votes cast whcih is 73.8% of the total votes
 
 ## Election-Audit Summary
 As you can see below, the output results of the script provide accurately detailed analysis of the election results in an easy to read format.
 
    Election Results
    -------------------------
    Total Votes: 369,711
    -------------------------

    County Votes:
    Jefferson: 10.5% (38,855)
    Denver: 82.8% (306,055)
    Arapahoe: 6.7% (24,801)
    -------------------------
    Largest County Turnout: Denver
    -------------------------
    Charles Casper Stockham: 23.0% (85,213)
    Diana DeGette: 73.8% (272,892)
    Raymon Anthony Doane: 3.1% (11,606)
    -------------------------
    Winner: Diana DeGette
    Winning Vote Count: 272,892
    Winning Percentage: 73.8%
    -------------------------
 
 The written code can be repurposed depending on the data provided. The variables, list, and created dictionaries can be used with most datasets pertaining to election resulst.
 
```
# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

Create a county list and county votes dictionary.
county_list = []
county_votes = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Track the largest county and county voter turnout.
largest_county = ""
largest_county_voter_turnout = 0
largest_county_percentage = 0
```

The use of the following for loop captures the county information from the created county dictionary. There is a similar for loop utilized for the candidate information as well. The code ends with the ability to write this information to the file for easier reading:

```    
    for county in county_list:
        # Retrieve the county vote count.
        county_vote = county_votes.get(county)
        # Calculate the percentage of votes for the county.
        county_vote_percentage = float(county_vote) / float(total_votes) * 100

        # Print the county results to the terminal.
        county_results = f"{county}: {county_vote_percentage:.1f}% ({county_vote:,})\n"
        print(county_results)
        # Save the county votes to a text file.
        txt_file.write(county_results)
        # Write an if statement to determine the winning county and get its vote count.
        if (county_vote > largest_county_voter_turnout) and (county_vote_percentage > largest_county_percentage):
            largest_county_voter_turnout = county_vote
            largest_county_percentage = county_vote_percentage
            largest_county = county

    # Print the county with the largest turnout to the terminal.
    winning_county = (
        f"-------------------------\n"
        f"Largest County Turnout: {largest_county}\n"
        f"-------------------------\n")
    print(winning_county)

    # Save the county with the largest turnout to a text file.
    txt_file.write(winning_county)
```

All in all, I am satisfied with the outcomes of this project and feel that repurposing for any election analysis need would please whomever needed to utilize this.
 
 
