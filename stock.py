# --------------------------------------------
# TASK 2: Stock Investment Summary Program
# --------------------------------------------
# Goal: Calculate total investment, profit/loss, and save results in a text file.

# Step 1: Take user input
stock_name = input("Enter stock name: ")
num_shares = int(input("Enter number of shares: "))
buy_price = float(input("Enter buying price per share: "))
current_price = float(input("Enter current price per share: "))

# Step 2: Perform calculations
investment_value = num_shares * buy_price
current_value = num_shares * current_price
profit_or_loss = current_value - investment_value

# Step 3: Display summary on console
print("\n----- Investment Summary -----")
print(f"Stock Name: {stock_name}")
print(f"Number of Shares: {num_shares}")
print(f"Buying Price per Share: ₹{buy_price}")
print(f"Current Price per Share: ₹{current_price}")
print(f"Total Investment: ₹{investment_value}")
print(f"Current Value: ₹{current_value}")

if profit_or_loss > 0:
    print(f"Profit: ₹{profit_or_loss}")
else:
    print(f"Loss: ₹{abs(profit_or_loss)}")

# Step 4: Save summary in a text file
file_name = f"{stock_name}_investment_summary.txt"

with open(file_name, "w") as file:
    file.write("----- Investment Summary -----\n")
    file.write(f"Stock Name: {stock_name}\n")
    file.write(f"Number of Shares: {num_shares}\n")
    file.write(f"Buying Price per Share: ₹{buy_price}\n")
    file.write(f"Current Price per Share: ₹{current_price}\n")
    file.write(f"Total Investment: ₹{investment_value}\n")
    file.write(f"Current Value: ₹{current_value}\n")

    if profit_or_loss > 0:
        file.write(f"Profit: ₹{profit_or_loss}\n")
    else:
        file.write(f"Loss: ₹{abs(profit_or_loss)}\n")

# Step 5: Confirm save
print(f"\n✅ Summary saved successfully as '{file_name}' in this folder.")
