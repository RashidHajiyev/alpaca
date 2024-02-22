from alpaca.trading.client import TradingClient

trading_client = TradingClient('PKQRBC27FFE1WFOPK7SK', '86bAYSOeq0BCELPGCtMcCjjbcdnGNiFdeVDABvwf')

print(trading_client.get_account().account_number)
print(trading_client.get_account().buying_power)
