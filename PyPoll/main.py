# import the packages
import os
import csv

# the path to the csv
path = "C:\\Users\\zombi\\python-challenge\\PyPoll\\Resources"

# name of the file
csv_name = "election_data.csv"

# using the os packages to pull file
csv_path = os.path.join(path, csv_name)
file_to_save = os.path.join("Analysis","analysis.txt")

# open files
with open(csv_path) as file: 
 
    # reading the file
    csvreader = csv.reader(file, delimiter=',')
    print(csvreader)
    
    # pull headers from csv file
    csv_header = next(csvreader)
    
    
        # print column names and headers
    print("column names:")
    print(csv_header)
    
    Ballot_ID = []
    County = []
    Candidate = []
    Candidates_List = []
    #set up vote counter and trackers
    all_votes = 0
    candidateoption = []
    candidatevote= {}
    winner = ""
    winner_count = 0
    winner_percentage = 0
    # declare an empty dictionary
    vote = {}
            
# add data
    for row in csvreader:
        Ballot_ID.append(row[0]) 
        County.append(row[1])
        Candidate = row[2]
        
       


# set up results
#for row in csv_path:
        all_votes +=1
        #Candidate = []
       
        # set up conditionals
        if Candidate not in Candidates_List:
            # track voting
            Candidates_List.append(Candidate)
            print(Candidates_List)
            print(Candidate)
            vote[Candidate] = 0
            print("hi")
            print(vote[Candidate])
            
        print(vote[Candidate])
        vote[Candidate] = vote[Candidate] + 1
        
    

    
# print the election results
    all_results = (f"Election Results\n------\n" f"Total Votes: {all_votes:,}\n" f"-----\n")
    print(all_results, end="")


     
#finish saving
     

output_results = ""

#go through candidate list
for Candidate in vote:
        votes = vote[Candidate]
        percentage = float(votes) / float(all_votes) * 100
        results = (f"{Candidate}: {percentage:.1f}% ({votes:,})\n")
        output_results= output_results + results
        print(output_results)
        
        
     
       
    
        if (votes > winner_count) and (percentage > winner_percentage):
          winner_count = votes
          winner = Candidate
          winner_percentage = percentage
winner_summary = (
                 f"----------------\n" 
                 f"Winner: {winner}\n" 
                 f"Votes: {winner_count:,}\n" 
                 f"Percentage: {winner_percentage:.1f}%\n"
                 f"-----------------\n"
                 )
print(winner_summary)

#save work to txt file

with open(file_to_save, "w") as txt_file:   
    txt_file.write(all_results)
    txt_file.write(output_results)
    txt_file.write(winner_summary)
    
    
# 
    
    



 
        