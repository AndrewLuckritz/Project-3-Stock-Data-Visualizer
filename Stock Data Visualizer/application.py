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

    #error checking for valid input
    while True:
        symbol = input("Enter the stock symbol you are looking for: ")
        data = fetch_stock_data(symbol, "GLOBAL_QUOTE")

        if data:
            return symbol
        else:
            print("Please enter a valid stock symbol.\n")



def get_chart_type():
    print("\nChart Types\n-----------\n")
    print("1. Bar")
    print("2. Line")

    #error checking for valid input
    while True:
        chart_type = input("\nEnter the chart type you want (1, 2): ")

        if chart_type == "1":
            return "Bar"
        elif chart_type == "2":
            return "Line"
        else:
            print("Invalid choice. Please enter 1 for Bar or 2 for Line.\n")

    

def get_time_series():
    print("\nSelect the Time Series of the Chart You Want to Generate\n---------------------------------------------------------\n")
    print("1. Intraday")
    print("2. Daily")
    print("3. Weekly")
    print("4. Monthly")


    while True:
        time_series = input("\nEnter the option (1, 2, 3, 4): ")

        if time_series == "1":
            return "Intraday"
        elif time_series =="2":
            return "Daily"
        elif time_series =="3":
            return "Weekly"
        elif time_series =="4":
            return "Montly"
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4.\n")



def main():
    get_stock_symbol()
    get_chart_type()
    get_time_series()


main()
