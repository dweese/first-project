# first_project/main.py
import argparse
import requests
import sys

def get_ip_details(ip_address: str):
    """Fetches and prints geographic details for a given IP address."""

    # Use the ip-api.com endpoint
    url = f"http://ip-api.com/json/{ip_address}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes

        data = response.json()

        if data.get("status") == "success":
            print(f"Details for IP: {data.get('query')}")
            print(f"  Country: {data.get('country')}")
            print(f"  City:    {data.get('city')}")
            print(f"  ISP:     {data.get('isp')}")
        else:
            print(f"Could not retrieve details for {ip_address}. Message: {data.get('message')}")

    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    # 1. Set up the argument parser
    parser = argparse.ArgumentParser(description="Get geographic details for an IP address.")

    # 2. Add an argument for the IP address
    parser.add_argument("ip_address", help="The IP address to look up.")

    # 3. Parse the arguments provided by the user
    args = parser.parse_args()

    # 4. Call the main function with the user-provided IP
    get_ip_details(args.ip_address)
