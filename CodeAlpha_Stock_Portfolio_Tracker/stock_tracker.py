# Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 200,
    "MSFT": 300
}

portfolio = {}
total_portfolio_value = 0

print("📈 Stock Portfolio Tracker")
print("\nAvailable Stocks:")

for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")

while True:
    stock_name = input("\nEnter Stock Name (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("❌ Stock not found!")
        continue

    try:
        quantity = int(input("Enter Quantity: "))

        portfolio[stock_name] = quantity
        total_portfolio_value += stock_prices[stock_name] * quantity

    except ValueError:
        print("❌ Please enter a valid number!")

print("\n📊 ----- Portfolio Summary -----")

for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity

    print(f"\nStock: {stock}")
    print(f"Price per Share: ${stock_prices[stock]}")
    print(f"Quantity: {quantity}")
    print(f"Investment Value: ${value}")

print("\n💰 Total Portfolio Value: $", total_portfolio_value)

print("\n✅ Thank you for using Stock Portfolio Tracker!")