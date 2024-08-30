import sys
import requests

"""
Implement a program that convert the current cost of Bitcoins in USD.
The program should:
expects the user to specify as a command-line argument the number of Bitcoins, that they would like to buy. If that 
argument cannot be converted to a float, the program should exit via sys.exit with an error message;
Queries the API for the CoinDesk Bitcoin Price Index  which returns a JSON object, among whose nested keys is the current 
price of Bitcoin as a float;
Outputs the current cost of Bitcoins in USD to four decimal places, using a ',' as thousands separator.
"""

# Program logic
def main():
    # Verify if the arguments exists.
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument!")

    try:
        n_bitcoins = float(sys.argv[1])
        # Request to the API
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response_obj = response.json()
        obj = response_obj["bpi"]
        obj_usd = obj["USD"]
        # retrieve from API the conversion rate
        conversion_rate = obj_usd["rate_float"]
        # Print the desired output
        print(f"${conversion_rate * n_bitcoins:,.4f}")
    except ValueError:
        # if was catch an ValueError
        sys.exit("Argument is not a number!")
    except requests.RequestException:
        # if was catch an RequestException
        sys.exit("Error in the request!")

main()
