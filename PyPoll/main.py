# import the packages
import os
import csv

# the path to the csv
path = "C:\\Users\\zombi\\python-challenge\\PyPoll\\Resources"

# name of the file
csv_name = "election_data.csv"
txt_name = "analysis.txt"
# using the os packages to pull file
csv_path = os.path.join(path, csv_name)
file_to_save = os.path.join(path, txt_name)
file = open('analysis.txt', 'r')

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
              
# add data
for row in csvreader:
    Ballot_ID.append(row[0]) 
    County.append(row[1])
    Candidate.append(row[2])
    Candidates_List.append(row[2])
        


    #print first column
print("Ballot_ID")
print(type(Ballot_ID[0]))
    
#list out your rows
print("length of my list")
print(len(Ballot_ID))
      
# print second column
print("County")
print(type(County[1])) 

#list out your rows
print("length of my list")
print(len(County))

# print third column
print("Candidate")
print(type(Candidate[2]))

#list out your rows
print("length of list")
print(len(Candidate))
 

# set up vote counter and trackers
all_votes = 0
winner = ""
percentage = 0
canadite_votes = 0
canadite_percentage = 0

# declare an empty dictionary
vote = {}

# set up results
for now in csv_path:
       all_votes +=1
       Candidate = row[2]
       
 # set up conditionals
if Candidate not in Candidates_List:

# track voting
    vote[Candidate] = 0
    vote[Candidate] += 1
    
#save your work
with open(file_to_save, "w") as txt_file:

# print the election results
    results = (f"\nresults\n" f"all_votes: {all_votes:,}\n" f"-----\n")
print(results, end="")

     
#finish saving
txt_file.write(results)  


#go through candidate list
for Candidate in vote:
    votes = vote[Candidate]
    percentage = float(votes) / float(all_votes) * 100
    results = (f"{Candidate}: {percentage:.1f}% ({votes:,})\n")
    print(results)
    
# save your work
txt_file.writer(txt_name)
  
# 
    
    



 
        