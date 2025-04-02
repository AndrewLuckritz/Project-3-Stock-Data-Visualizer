import requests
from flask import Flask
import webbrowser
import threading
import time
from datetime import datetime

# Your original unchanged functions
def fetch_stock_data(symbol, function):
    API_KEY = "9YF471K7UE0O3U9A"  
    BASE_URL = "https://www.alphavantage.co/query"
    params = {
        "function": function,
        "symbol": symbol,
        "apikey": API_KEY,
        "datatype": "json"
    }
    response = requests.get(BASE_URL, params=params)
    return response.json() if response.status_code == 200 else None

def get_stock_symbol():
    print("\nStock Data Visualizer\n----------------------\n")
    while True:
        symbol = input("Enter the stock symbol you are looking for: ")
        if fetch_stock_data(symbol, "GLOBAL_QUOTE"):
            return symbol
        print("Please enter a valid stock symbol.\n")

def get_chart_type():
    print("\nChart Types\n-----------\n1. Bar\n2. Line")
    while True:
        choice = input("\nEnter the chart type you want (1, 2): ")
        if choice == "1": return "Bar"
        if choice == "2": return "Line"
        print("Invalid choice. Please enter 1 for Bar or 2 for Line.\n")

def get_time_series():
    print("\nSelect the Time Series\n----------------------\n1. Intraday\n2. Daily\n3. Weekly\n4. Monthly")
    while True:
        choice = input("\nEnter the option (1, 2, 3, 4): ")
        if choice == "1": return "TIME_SERIES_INTRADAY"
        if choice == "2": return "TIME_SERIES_DAILY"
        if choice == "3": return "TIME_SERIES_WEEKLY"
        if choice == "4": return "TIME_SERIES_MONTHLY"
        print("Invalid choice. Please enter 1, 2, 3, or 4.\n")

def get_date(prompt):
    while True:
        date_str = input(prompt)
        try:
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

def get_date_range():
    while True:
        start = get_date("Enter the start date (YYYY-MM-DD): ")
        end = get_date("Enter the end date (YYYY-MM-DD): ")
        if start <= end:
            return start, end
        print("End date cannot be before start date.\n")

# Web interface setup
app = Flask(__name__)

# Global variables to store user inputs
user_data = {}

@app.route('/')
def show_results():
    return f"""
    <h1>Stock Visualizer</h1>
        <h3>Graph will go here</h3>
    </div>
    """

def run_flask():
    app.run(host='0.0.0.0', port=5050)

if __name__ == '__main__':
    # Collect all user input first
    symbol = get_stock_symbol()
    chart_type = get_chart_type()
    time_series = get_time_series()
    start_date, end_date = get_date_range()
    user_data.update({
    'start_date': start_date,
    'end_date': end_date
    })



    # Store the data for the web interface
    user_data.update({
        'symbol': symbol,
        'chart_type': chart_type,
        'time_series': time_series
    })
    
    # Start Flask in a separate thread
    threading.Thread(target=run_flask, daemon=True).start()
    
    # Open the browser after a brief delay
    webbrowser.open_new('http://127.0.0.1:5050')
    
    # Keep the program running
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nClosing the application...")