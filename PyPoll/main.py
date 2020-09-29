import os
import csv

election_csv_path = os.path.join('Resources', 'election_data.csv')

total_votes = 0
candidate_name_count = {}
candidate_percent = {}
formated_candidate_percent = {}
winner_count = 0


with open(election_csv_path) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader)

    for lines in csvreader:
        total_votes += 1
        if lines[2] in candidate_name_count.keys():
            candidate_name_count[lines[2]] += 1
        else:
            candidate_name_count[lines[2]] = 1

        for key, count in candidate_name_count.items():
            candidate_percent[key] = (count/total_votes)
            formated_candidate_percent[key] = "{:.3%}".format(candidate_percent[key])

        for key in candidate_name_count.keys():
            if candidate_name_count[key] > winner_count:
                winner = key
                winner_count = candidate_name_count[key]


print ("Election Results")
print ("-------------------------")
print (f"Total Votes: {total_votes}")
print ("-------------------------")
for key in candidate_name_count:
    print(f"{key} : {formated_candidate_percent[key]} ({candidate_name_count[key]})")
print ("-------------------------")
print (f"Winner: {winner}")
print ("-------------------------")

output_file = os.path.join('Analysis', 'election_analysis.txt')

with open(output_file, 'w') as txtfile:

    # Initialize csv.writer
    print("Election Results", file=txtfile)
    print("-------------------------", file=txtfile)
    print(f"Total Votes: {total_votes}", file=txtfile)
    print("-------------------------", file=txtfile)
    for key in candidate_name_count:
        print(f"{key} : {formated_candidate_percent[key]} ({candidate_name_count[key]})",file=txtfile)
    print("-------------------------", file=txtfile)
    print(f"Winner: {winner}", file=txtfile)
    print("-------------------------", file=txtfile)

