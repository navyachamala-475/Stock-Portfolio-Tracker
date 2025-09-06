# Stock Portfolio Tracker

# Hardcoded stock prices (dictionary)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 300
}

portfolio = {}

# Ask user how many stocks
n = int(input("How many different stocks do you want to add? "))

for i in range(n):
    stock = input(f"Enter stock name {i+1}: ").upper()
    qty = int(input(f"Enter quantity of {stock}: "))

    if stock in stock_prices:
        portfolio[stock] = qty
    else:
        print(f"{stock} not found in stock list!")

# Calculate total value
total_value = 0
print("\nYour Portfolio:")
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total_value += value
    print(f"{stock} - {qty} shares → ${value}")

print(f"\nTotal Portfolio Value: ${total_value}")