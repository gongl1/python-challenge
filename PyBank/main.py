import os
import csv
# csvpath = os.path.join('..', 'PyBank', 'Resources', '02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv') #main.py is in Pybank right now and  .. goes to PYTHON-CHALLENGE, then goes down to PyBank
csvpath = os.path.join('Resources', '02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv')
# csvpath = os.path.join('C:\\Users\\gongl\\Desktop\\DS_Bootcamp_2021class\\Homework\\python-challenge\\PyBank\\Resources\\02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv')
# csvpath = os.path.join('C:\\', 'Users', 'gongl', 'Desktop', 'DS_Bootcamp_2021class', 'Homework', 'python-challenge', 'PyBank', 'Resources', '02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv')


# def print_change(row):
    # for frist_row in 1 to row_month
        # frist_row[1]
        # for second_row in 2 to row_month
           # second_row[1]
           # neighbor_change = second_row[1] - frist_row[1]

with open(csvpath, "r", encoding='utf8') as csvfile: #open entire file and call it csvfile
    csvreader = csv.reader(csvfile,delimiter=",")   # csvreader here is to grab data and breaks into pieces based on delimiter
    # print(csvreader)
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader) # pop one row
    # Read each row of data after the header
    row_month = 0
    row_total_profit_losses = 0
    previous_row_profit_losses = 0
    neighbor_change_list = []
    total_neighbor_change = 0
    date_list = []


    for row in csvreader:
        
        # print(row)
        row_month = row_month + 1
        row_total_profit_losses = int(row[1]) + row_total_profit_losses
        
        date_list.append(row[0]) # append to column extractions

        current_row_profit_losses = int(row[1])
        neighbor_change = current_row_profit_losses - previous_row_profit_losses
        neighbor_change_list.append(neighbor_change) #!here the neighbor_change_list can not be named as neighbor_change

        if previous_row_profit_losses != 0: #!remember : sign here
           total_neighbor_change = total_neighbor_change + neighbor_change
        previous_row_profit_losses = current_row_profit_losses # !sequence here is very important, so at the end treat the current_row_profit_losses as previous_row_profit_losses, and then go to next row
    
    average_neighbor_change = total_neighbor_change / (row_month - 1)
    

    date_neighbor_change = dict(zip(neighbor_change_list, date_list)) # zip two lists into a disctionary so that I can find date by indexing neighbor_change
    

    # below are two loops to find greatest_increase_in_profit_losses and greatest_decrease_in_profit_losses
    greatest_increase_in_profit_losses = neighbor_change_list[1]
    for profit_losses in neighbor_change_list: 
        if  profit_losses > greatest_increase_in_profit_losses: 
            greatest_increase_in_profit_losses = profit_losses

    
    greatest_decrease_in_profit_losses = neighbor_change_list[1]
    for profit_losses in neighbor_change_list: 
        if  profit_losses < greatest_decrease_in_profit_losses: 
            greatest_decrease_in_profit_losses = profit_losses


    # print (row_month)
    # print (row_total_profit_losses)

    # print (neighbor_change)
    # print (total_neighbor_change)
    # print (average_neighbor_change)
    # print (neighbor_change_list)
    # print (date_list)
    
    # print (date_neighbor_change)
    # print (greatest_increase_in_profit_losses)
    # print (date_neighbor_change[greatest_increase_in_profit_losses])
    # print (greatest_decrease_in_profit_losses)
    # print (date_neighbor_change[greatest_decrease_in_profit_losses])
      

print ("Financial Analysis")   
print ("-------------------------") 
print ("Total Months: " + str(row_month))
print ("Total: " + "$" + str(row_total_profit_losses))
print ("Average Change: " + "$" + str(round(average_neighbor_change, 2)))
print ("Greatest Increase in Profits: " + str(date_neighbor_change[greatest_increase_in_profit_losses]) + " ($" + str(greatest_increase_in_profit_losses) + ")")
print ("Greatest Decrease in Profits: " + str(date_neighbor_change[greatest_decrease_in_profit_losses]) + " ($" + str(greatest_decrease_in_profit_losses) + ")")

output_file = os.path.join('analysis', 'analysis_result.txt') #Set variable for putput file. save the output path.
with open(output_file, "w", newline='', encoding='utf8') as datafile: # open the output file
    datafile.write("Financial Analysis\n")
    datafile.write("-------------------------\n")
    datafile.write("Total Months: " + str(row_month) + "\n")
    datafile.write("Total: " + "$" + str(row_total_profit_losses) + "\n")
    datafile.write("Average Change: " + "$" + str(round(average_neighbor_change, 2)) + "\n")
    datafile.write("Greatest Increase in Profits: " + str(date_neighbor_change[greatest_increase_in_profit_losses]) + " ($" + str(greatest_increase_in_profit_losses) + ")" + "\n")
    datafile.write("Greatest Decrease in Profits: " + str(date_neighbor_change[greatest_decrease_in_profit_losses]) + " ($" + str(greatest_decrease_in_profit_losses) + ")" + "\n")
    
