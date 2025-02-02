import yfinance as yf
import pandas as pd

# Fetch historical data (1 year, daily) for multiple stocks
tickers = ["NVDA", "COST", "WMT", "TSLA", "GOOGL", "GOOG", "AMZN", "MSFT", "AAPL"]

stock_data = {}

for ticker in tickers:
    data = yf.download(ticker, period="1y", interval="1d")
    data = data[['Close']]
    data.reset_index(inplace=True)
    data.columns = ['Date', 'Price']
    
    stock_data[ticker] = data  # Store data in dictionary

# Initialize game parameters
balance = 200.0
shares = {ticker: 0 for ticker in tickers}  # Dictionary for shares per stock
day = 0
current_ticker = tickers[0]  # Default to first stock

def get_price(ticker, day):
    return stock_data[ticker].iloc[day]['Price']

def trade_game():
    global balance, shares, day, current_ticker
    transactions = []

    while day < len(stock_data[current_ticker]):
        act = False
        price = get_price(current_ticker, day)
        total_money = (price * shares[current_ticker]) + balance
        
        print("\n--- Trading", current_ticker, "---")
        print(f"Day {day + 1}: S${price:.2f}, #S{round(shares[current_ticker], 2)}, B${balance:.2f}, T${total_money:.2f}")
        
        print("\nAvailable stocks:", ", ".join(tickers))
        chosen_ticker = input("Enter a stock ticker to trade or press Enter to keep using the current one: ").strip().upper()
        if chosen_ticker in stock_data:
            current_ticker = chosen_ticker
        
        price = get_price(current_ticker, day)  # Update price based on new stock

        if shares[current_ticker] == 0:
            action = input("Enter 'buy', 'buy all', or 'hold': ").strip().lower()
        elif balance < price:
            action = input("Enter 'sell', 'sell all', or 'hold': ").strip().lower()
        else:
            action = input("Enter 'buy', 'buy all', 'sell', 'sell all', or 'hold': ").strip().lower()
        
        if action == "buy":
            amount = float(input("Enter amount to invest: "))
            if amount > balance:
                print("Not enough funds! Try again.")
                continue
            else:
                shares[current_ticker] += amount / price
                balance -= amount
                act = True
        elif action == "buy all":
            shares[current_ticker] += balance / price
            balance = 0
            act = True
        elif action == "sell":
            amount = float(input("Enter number of shares to sell: "))
            if amount > shares[current_ticker]:
                print("Not enough shares! Try again.")
                continue
            else:
                balance += amount * price
                shares[current_ticker] -= amount
                act = True
        elif action == "sell all":
            balance += shares[current_ticker] * price
            shares[current_ticker] = 0
            act = True
        elif action == "hold":
            act = True
        else:
            print("Invalid input, try again.")
            continue

        if act:
            transactions.append([day + 1, balance, shares[current_ticker], balance + (shares[current_ticker] * price)])
            day += 1

    df = pd.DataFrame(transactions, columns=["Day", "Balance", "Shares", "Total Value"])
    df.to_csv("trade_history.csv", index=False)
    print("Game Over! Results saved to trade_history.csv.")

trade_game()
