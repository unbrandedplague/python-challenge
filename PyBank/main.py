# import the packages
import os
import csv

# the path to the csv
path = "C:\\Users\\zombi\\python-challenge\\PyBank\\Resources"

# name of the file
csv_name = "budget_data.csv"

# using the os packages to pull file
csv_path = os.path.join(path, csv_name)

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
 #print first column
print("Date")
print(type(Date[0]))
    
#list out your rows
print("length of my list")
print(len(Date))
      
# print second column
print("Profit/Losses")
print(type(Profit_Losses[1])) 

#list out your rows
print("length of my list")
print(len(Profit_Losses)) 

# Total of Profit_Losses

Total = sum(Profit_Losses)

print (Total)

Averagechange = sum(Net_Change_List)/len(Net_Change_List)
print(Averagechange)

# Greatest Increase

#Greatest Decrease
