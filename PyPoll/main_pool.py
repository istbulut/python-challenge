import os
import csv

election_path = os.path.join("Resources","election_data.csv")
total_vote_counter = 0

newlist1 = []
newlist2 = []
newlist3 = []

candidate_votes = {}

with open(election_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)
    print("Election Results")
    print("------------------------")

    for x in csv_reader:
        candidate_name = x[2]
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
        else:
            candidate_votes[candidate_name] = 1

        if "Charles Casper Stockham" in x:
            newlist1.append(x)

        if "Diana DeGette" in x:
            newlist2.append(x)

        if "Raymon Anthony Doane" in x:
            newlist3.append(x)

        total_vote_counter = total_vote_counter + 1

vote_c = len(newlist1)
vote_d = len(newlist2)
vote_r = len(newlist3)

percent_charles = len(newlist1) / total_vote_counter
percent_diana = len(newlist2) / total_vote_counter
percent_raymon = len(newlist3) / total_vote_counter

percent_c = "{:.3%}".format(percent_charles)
percent_d = "{:.3%}".format(percent_diana)
percent_r = "{:.3%}".format(percent_raymon)

print("Total Vote: ", total_vote_counter)
print("-------------------------")
print("Charles Casper Stockham: ", percent_c, "(", vote_c, ")")
print("Diana Degette: ", percent_d, "(", vote_d, ")")
print("Raymon Anthony Doane: ", percent_r, "(", (vote_r), ")")
print("-------------------------")

if vote_c > vote_d and vote_c > vote_r:
    print("Winner: Charles Casper Stockham")
elif vote_d > vote_c and vote_d > vote_r:
    print("Winner: Diana Degette")
elif vote_r > vote_d and vote_r > vote_c:
    print("Winner: Raymon Anthony Doane")
