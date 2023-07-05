# import the packages
import os
import csv

# the path to the csv
path = "C:\\Users\\zombi\\python-challenge\\PyBank\\Resources"

# name of the file
csv_name = "budget_data.csv"

# using the os packages to pull file
csv_path = os.path.join(path, csv_name)
# using path to save to txt
file_to_save = os.path.join("Analysis","analysis.txt")

# open files
with open(csv_path) as file:
    # reading the csv
    csvreader = csv.reader(file, delimiter=',')
    
    # pull headers from csv file
    csv_header = next(csvreader)
    
        # print column names and headers
    print("column names:")
    print(csv_header)
     
    #List Columns 
    Date = []
    Profit_Losses = []
    Net_Change_List = [] 
    First_Row = next(csvreader)
    Previous_Profit_Loss = int(First_Row[1])
    Date.append(First_Row[0]) 
    Profit_Losses.append (int(First_Row[1]))
    # add data
    for row in csvreader:
        Date.append(row[0]) 
        Profit_Losses.append (int(row[1]))
        Net_Change_List.append(int(row[1])-Previous_Profit_Loss)
        Previous_Profit_Loss =int(row[1])                                                             


# total months
print(f"Total Months: {len(Date)}")

# Total of Profit_Losses
print (f"Total: ${sum(Profit_Losses)}")

# average change
print(f"Average Change: {round(sum(Net_Change_List)/len(Net_Change_List),2)}")

# Greatest Increase and decrease
greatest = max(Net_Change_List)
worst = min(Net_Change_List)

# calculate min and max
greatest_month = Net_Change_List.index(max(Net_Change_List))+1
print(f"Greatest Increase: {Date[greatest_month]} (${(str(greatest))})")

worst_month = Net_Change_List.index(min(Net_Change_List))+1
print(f"Greatest Decrease: {Date[worst_month]} (${(str(worst))})")

with open(file_to_save, "w") as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("------------------\n")
    txt_file.write(f"Total Months: {len(Date)}\n")
    txt_file.write(f"Total: ${sum(Profit_Losses)}\n")
    txt_file.write(f"Average Change: {round(sum(Net_Change_List)/len(Net_Change_List),2)}\n")
    txt_file.write(f"Greatest Increase: {Date[greatest_month]} (${(str(greatest))})\n")
    txt_file.write(f"Greatest Decrease: {Date[worst_month]} (${(str(worst))})\n")