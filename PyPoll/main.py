import os
import csv

csvpath = os.path.join('.', 'Resources', 'election_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)

    Total_votes = 0
    result_string = ""

    Candidate_votes = {}

    print("Election Results")

    for row in csvreader:
  
        Total_votes += 1

        if row[2] in Candidate_votes:
            Candidate_votes[row[2]] += 1

        else:
            Candidate_votes[row[2]] = 1

    print("-------------------------")

    print("Total Votes: " + str(Total_votes))

    print("-------------------------")

    for candidate, vote_count in Candidate_votes.items():
        percentage_vote = vote_count * 100 / Total_votes
        result_string = result_string + (candidate + ": " + str(round(percentage_vote, 3)) + "% (" + str(Total_votes) + ")\n")
    winner = max(Candidate_votes, key = Candidate_votes.get)

    print(result_string.rstrip("\n"))

    print("-------------------------")

    print("Winner: " + winner)
    

    print("-------------------------")

    output_path = os.path.join(".", "Analysis", "PyPollReport.txt")


    with open(output_path, 'w') as txtfile:

        txtfile.write("Election Results"+"\n")
        txtfile.write("-------------------------"+"\n")
        txtfile.write("Total Votes: " + str(Total_votes) +"\n")
        txtfile.write("-------------------------"+"\n")
        txtfile.write(result_string)
        txtfile.write("-------------------------"+"\n")
        txtfile.write("Winner: " + winner +"\n")
        txtfile.write("-------------------------"+"\n")

    txtfile.close()






