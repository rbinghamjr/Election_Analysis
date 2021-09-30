my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("I recieved " + str(percentage_votes) + "% of the total votes.")

#same code but with f string
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

#multiline f strings and the 2f is for precision decimal points
candidate_votes = int(input("How many votes did the candidate get in the election?"))
total_votes = int(input("What is the total number of votes in the election?"))
message_to_candidate = (
        f"You received {candidate_votes} number of votes. "
        f"The total number of votes in the election was {total_votes}. "
        f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes")

print(message_to_candidate)
