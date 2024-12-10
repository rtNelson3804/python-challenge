# Importing modules.
import csv
import os

# Loading file paths to read and write.
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize dictionary, list and variables required to track election data.
total_votes = 0
winning_votes = 0
vote_count = {}
output_summary = []

# Opening the CSV file and processing it.
with open(file_to_load) as election_data:
    reader = csv.reader(election_data, delimiter=',')

    # Skipping the header row.
    header = next(reader)

    # Looping through each row of the dataset.
    for row in reader:

        # Incrementing the total vote count for each row.
        total_votes += 1

        # Getting the candidate's name from the row.
        candidate_name = row[2]

        # If the candidate is not on the list, adding their first vote, else adding to their vote_count.
        if candidate_name not in vote_count:
            vote_count[candidate_name] = 1
        else:
            vote_count[candidate_name] += 1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Appending our output_summary list to organize the results.
    output_summary.append("Election Results")
    output_summary.append("-------------------------")
    output_summary.append(f"Total Votes: {total_votes}")
    output_summary.append("-------------------------")

    # Looping through the candidates.
    for candidate, votes in vote_count.items():

        # Taking the vote count to calculate the percentage votes.
        perc_votes = (votes / total_votes) * 100
        
        # Updating the winning candidate if this one has more votes.
        if votes > winning_votes:
            winning_votes = votes
            winner = candidate

        # Appending our output_summary list adding each candidate, their perc_votes, and total votes.
        output_summary.append(f"{candidate}: {perc_votes:.3f}% ({votes})")

    # Appending our output_summary list to display the winner.
    output_summary.append("-------------------------")
    output_summary.append(f"Winner: {winner}")
    output_summary.append("-------------------------")
    
    # Printing each line of the output_summary list to display final data in terminal.
    for line in output_summary:
        print(line)
    
    # Joining the output_summary list into a single string so we can write it to a text file.
    output_text = "\n".join(output_summary)
    
    # Writing the output_text in to a text file to display results.
    txt_file.write(output_text)