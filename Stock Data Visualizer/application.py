# This is a test commit
import requests

print("This is another test")

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

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error fetching data:", response.status_code)
        return None
    
def get_stock_symbol():
    print("\nStock Data Visualizer\n----------------------\n")
    symbol = input("Enter the stock symbol you are looking for: ")

    return symbol


def get_chart_type():
    print("\nChart Types\n-----------\n")
    print("1. Bar")
    print("2. Line")

    chart_type = input("\nEnter the chart type you want (1, 2): ")

    return chart_type

def get_time_series():
    print("\nSelect the Time Series of the Chart You Want to Generate\n---------------------------------------------------------\n")
    print("1. Intraday")
    print("2. Daily")
    print("3. Weekly")
    print("4. Monthly")
    time_series = input("\nEnter the option (1, 2, 3, 4): ")

    return time_series

def main():
    get_stock_symbol()
    get_chart_type()
    get_time_series()


main()
