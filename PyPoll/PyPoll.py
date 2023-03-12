import os, csv

# Set the file path
pypoll_file = os.path.join("Resources","election_data.csv")

# Set the first value 
total_vote = 0
candidate_votes = {}
candidate_list = []
votes_count = []
percentage_voted_list = []
winner = ""
winner_votes_count = 0
cleaned_output = []

# Read csv file
with open(pypoll_file,"r",newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter= ",")
    file_header = next(csvreader)

    # Loop through each row in csv file
    for row in csvreader:
        # Count toal number of votes (count rows without header)
        total_vote = total_vote + 1
        
        # Set row[2] as candidate name for readability
        candidate_name = row[2]
        
        # If candidate name is already in the list, then keep adding one to get the vote count
        if candidate_name in candidate_list:
            candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

        # If candidate name is not in the list, put the name in the list 
        else:
            candidate_list.append(candidate_name)
            candidate_votes[candidate_name] = 1

        # Loop through each candidate in vote summary and get he percentage of votes each candidate won
    for key, value in candidate_votes.items():
        votes_count.append(value)
        votes = candidate_votes[candidate_name]
        percentage_voted = round((int(value)/ total_vote * 100),2)
        percentage_voted_list.append(percentage_voted)

        # Determine the winner by comparing votes count for each candidate
        if (value > winner_votes_count):
            winner_votes_count = value
            winner= key
    
    # Combine 3 lists as 1 list to print
    cleaned_output = zip(candidate_list,percentage_voted_list, votes_count)
    cleaned_output = list(cleaned_output)

    # Show the result in terminal
    print("Election Results")
    print("-------------------------")
    print(f'Total Votes :  {total_vote}')
    print("-------------------------")
    for item in cleaned_output:
        print(f'{item[0]} : {item[1]}00% ({item[2]})')
    print("-------------------------")
    print(f'Winner : {winner}')
    print("-------------------------")



# Export the result as csv file
output_file = os.path.join("Analysis","pypoll_result.csv")
with open(output_file,"w",newline="") as datafile:
    csvwriter = csv.writer(datafile)

    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow([f'Total Votes :  {total_vote}'])
    csvwriter.writerow(["-------------------------"])
    for item in cleaned_output:
        csvwriter.writerow([f'{item[0]} : {item[1]}00% ({item[2]})'])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow([f'Winner : {winner}'])
    csvwriter.writerow(["-------------------------"])