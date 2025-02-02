import yfinance as yf
import pandas as pd

# Fetch historical data (1 year, daily)
ticker = "NVDA"


data = yf.download(ticker, period="1y", interval="1d")
data = data[['Close']]
data.reset_index(inplace=True)
data.columns = ['Date', 'Price']

data.to_csv("stock_data.csv", index=False)

# Initialize game parameters
balance = 200.0
shares = 0
day = 0

def get_price(day):
    return data.iloc[day]['Price']

def trade_game():
    global balance, shares, day
    transactions = []
    
    while day < len(data):
        act = False
        price = get_price(day)
        total_money = (price * shares) + balance
        print("")
        print(f"Day {day + 1}: S${price:.2f}, #S{round(shares, 2): }, B${balance:.2f}, T${total_money:.2f}")
        
        if shares == 0:
            action = input("Enter 'buy', '_ all', or 'hold': ").strip().lower()
        elif balance < price:
            action = input("Enter 'sell', '_ all', or 'hold': ").strip().lower()
        else:
            action = input("Enter 'buy', 'sell', '_ all', or 'hold': ").strip().lower()
        
        if action == "buy":
                amount = float(input("Enter amount to invest: "))
                if amount > balance:
                    print("Not enough funds! Try again.")
                    continue
                else:
                    shares += amount / price
                    balance -= amount
                    act = True
        elif action == "buy all":
                shares += balance / price
                balance = 0
                act = True
        elif action == "sell":
              amount = float(input("Enter number of shares to sell: "))
              if amount > shares:
                  print("Not enough shares! Try again.")
                  continue
              else:
                  balance += amount * price
                  shares -= amount
                  act = True
        elif action == "sell all":
                balance += shares * price
                shares = 0
                act = True
        elif action == "hold":
            act = True
            pass
        else:
            print("Invalid input, try again.")
            continue
          
        if act == True:
          transactions.append([day + 1, balance, shares, balance + (shares * price)])
          day += 1
    
    df = pd.DataFrame(transactions, columns=["Day", "Balance", "Shares", "Total Value"])
    df.to_csv("trade_history.csv", index=False)
    print("Game Over! Results saved to trade_history.csv.")

trade_game()
