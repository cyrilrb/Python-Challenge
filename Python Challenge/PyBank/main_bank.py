
### Data Import 

#create a file path across all operating systems
import os
#Define the module used to read csv file
import csv

#Filepath to get to target csv file. 2 paths with 'resource' folder so had to incorporate 
#additional file level to better direct where to pull data from.
csvpath = os.path.join('..', 'PyBank', 'Resource', 'budget_data.csv')


with open(csvpath) as csvfile: #define the data then note how to extrat and separate the data
    csvreader = csv.reader(csvfile, )  #no delimeter since all information is in designated cell
    
    # print(csvreader) #print=show data label

    #Need to make a new column designations (aside from csv header) 
    csv_header = next(csvreader)  #Since provided, we are designating the header of the dataset the actual data is the 'next' row. 
    
    #could not work up results with defined csv header so created new "dataframe"
    profits = []
    date = []
    diff = []
    #print(f" CSV Header: {csv_header}") #Print the Header separate from the dataset.
   
    for row in csvreader:    # (Check progress)print each row in the csv data set.
        profits.append(float(row[1]))
        date.append(row[0])

      
print("             ")
print("Financial Analysis")
print("---------------------------------")
print("Total Months: ", len(date))
print("Total Revenue: $", round(sum(profits)))

#found cool trick to minimize typing when printing to text file at: https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txt-file
with open("main_bank_py_statement.txt", "w") as f:
    print("             ", file=f)
    print("Financial Analysis", file=f)
    print("---------------------------------", file=f)
    print("Total Months: ", len(date), file=f)
    print("Total Revenue: $", round(sum(profits)), file=f)


        
#set the variable like in VBA. Define the range as the length of the data in col for profits
for i in range(1,len(profits)):
    diff.append(profits[i] - profits[i-1])
    #print(diff)
    avg_diff = sum(diff)/len(diff)
    #print(round(avg_diff,2)) #values need to be put throught "round" function while being printed. round functions done before are negated before printing. 
    max_diff = max(diff)
    # print(max_diff)
    min_diff = min(diff)
    # print(min_diff)

    max_diff_date = str(date[diff.index(max_diff)])
    min_diff_date = str(date[diff.index(min_diff)])

print()
print("-----------------------------------")
print("Average Change: $", round(avg_diff,2))
print("Greatest Increase in Profits: $", round(max_diff),"(", max_diff_date,")")
print("Greatest Decrease in Profits: $", round(min_diff),"(", min_diff_date,")")
print("-----------------------------------")


#found cool trick to minimize typing when printing to text file at: https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txt-file
with open("main_bank_py_statement.txt", "a") as f:

    print()
    print("-----------------------------------", file=f)
    print("Average Change: $", round(avg_diff,2), file=f)
    print("Greatest Increase in Profits: $", round(max_diff),"(", max_diff_date,")", file=f)
    print("Greatest Decrease in Profits: $", round(min_diff),"(", min_diff_date,")", file=f)
    print("-----------------------------------", file=f)

        

