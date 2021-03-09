import os
import csv


election_csv = os.path.join("..", "PyPoll", "Resource", "election_data.csv")

 #redefine what headers we want in our analysis
voter_id = 0
candidates_dict = {}
candidates_perc_dict = {}
total_votes = 0

with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile,)

    csv_header = next(csvreader) # becasue file already has headers and the data is in the row below the header

   
   #conditions for counting candidates and their votes   
    for row in csvreader:
        total_votes +=1
        candidates = row[2]
        if candidates in candidates_dict:
            candidates_dict[candidates] += 1
        else:
            candidates_dict[candidates] = 1
        candidates_perc_dict[candidates] = f"{candidates_dict[candidates] /total_votes * 100:.2f}%" 

print("ELECTION RESULTS")
print("-------------------------------------")
print(f"Total Votes: {total_votes}")
# coding to print results horizontally
for key, value in candidates_dict.items():
            print(key, ' : ', value)
print("-------------------------------------")
for key, value in candidates_perc_dict.items():
            print(key, ' : ', value)

max_key = max(candidates_dict, key=candidates_dict.get)
print("-------------------------------------")
print("Winner: " + max_key + " !!!!")
print("-------------------------------------")




#found cool trick to minimize typing when printing to text file at: https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txt-file
with open("poll_results.txt", "w") as f:

    print("ELECTION RESULTS", file=f)
    print("-------------------------------------", file=f)
    print(f"Total Votes: {total_votes}", file=f)
    # coding to print results horizontally
    for key, value in candidates_dict.items():
            print(key, ' : ', value, file=f)
    print("-------------------------------------", file=f)
    for key, value in candidates_perc_dict.items():
            print(key, ' : ', value, file=f)

    max_key = max(candidates_dict, key=candidates_dict.get)
    print("-------------------------------------", file=f)
    print("Winner: " + max_key + " !!!!", file=f)
    print("-------------------------------------", file=f)

