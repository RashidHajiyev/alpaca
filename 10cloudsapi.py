import requests


# Replace these with your ALPACA API Key and Secret
API_KEY = 'PKQRBC27FFE1WFOPK7SK'
API_SECRET = '86bAYSOeq0BCELPGCtMcCjjbcdnGNiFdeVDABvwf' 

# ALPACA API URL for authentication (using the paper trading URL as an example)
API_URL = 'https://paper-api.alpaca.markets'

# Headers for authentication
headers = {
    'APCA-API-KEY-ID': API_KEY,
    'APCA-API-SECRET-KEY': API_SECRET
}

# Example request to retrieve account information to test authentication
response = requests.get(f'{API_URL}/v2/account', headers=headers)

# Check if the request was successful
if response.status_code == 200:
    print('Authentication successful! Account details:', response.json())
else:
    print('Authentication failed. Status code:', response.status_code)


