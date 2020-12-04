#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: You might need to do some research in Google to figure out how to do this.

print("Welcome to tip calculator")
bill = float(input("What was the total bill ?$"))
tip = int(input("What percentage tip would you like to give ? 10,12 or 15?"))
split = int(input("How many people to split the bill?"))


tip_per = ((bill)/100)*(tip)
# print(tip_per)

Total_bill = round(((bill)+(tip_per))/int(split),2)
# print(Total_bill)
print(f"Each person should pay ${Total_bill}")
  