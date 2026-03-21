# -------------------------------- Stock Market Risk Auditor--------------------------------------------
# Prepared by - Shaurya Bhatt
# Telling python which file to look at on my dekstop
myfile = "stocks.csv"
print("Script is starting...checking for file now.")
# Using 'with open' to grab the data and 'readlines' to put every line on the list
with open(myfile, "r") as x:
    all_lines = x.readlines()
#-------My Risk Calculation Section--------
# Making a function here to keep my main code clean
# It takes the High and Low prices and tell me if it's a risky day
def calculate_risk(high_price, low_price):
    # Using percentage because $5 gap is too huge for $100 stock but small for a $1000 stock
    difference= high_price - low_price
    percent_move = (difference/low_price)*100
    # If the stock moves more than 2% in one day, I'll call it 'High Risk'
    if percent_move > 2.0:
        return "High Risk", percent_move
    else:
        return "Normal", percent_move
    # Setting up the output file for my excel chart
result_file = open("audit_result.csv", "w")
result_file.write("Data, Ticker, Move_Percentage, Status\n")
#------The Main Auditor Section---------
riskyday_count = 0
# Starting the loop from 1 to skip the header names in the CSV
for row in all_lines[1:]:
    #Splitting the long string into a list so that I can pick specific columns
    parts= row.strip().split(",")
    # Safety Check: 1) If the row is empty or broken, just skip it and it prevents the 'Index out of range' error that I was getting
    if len(parts) < 5:
        continue

    ticker = parts[0]
    date = parts[1]
    # Safety Check 2) If the prices are missing in excel, skip this row too
    if parts[3] == "" or parts[4] == "":
        continue
    # Translating text from the file into decimal number for math
    h = float(parts[3])
    l = float(parts[4])
    # Using functions above to get the result and percentage move
    status, move = calculate_risk(h,l)
    # If the function says it's risky, I'll add it to my total counter
    if status == "High Risk":
        riskyday_count+=1
    # Saving the risky data in our new file
        result_file.write(f"{date}, {ticker}, {round(move,2)}, {status}\n")
    # Printing each row with round() so that it doesn't show 10 decimal
        print(ticker, "| Date:", date, "| Move:", round(move,2), "%| Result:", status)
    # Closing the result file
result_file.close()
    #-------My Final Summary Report---------
print("\n" + "*"*30)
print("Audit Completed By Shaurya")
print("Total number of High Risk Days found:", riskyday_count)
print("Note: I have used a 2% daily swing as my risk limit")
print("*"*30)
