from alpaca_trade_api.rest import REST, TimeFrame
import pandas as pd


api = REST('PKQRBC27FFE1WFOPK7SK', '86bAYSOeq0BCELPGCtMcCjjbcdnGNiFdeVDABvwf', base_url='https://paper-api.alpaca.markets')

aapl_data = api.get_bars('AAPL', TimeFrame.Day, "2024-02-20", "2024-02-21", adjustment='raw').df

print(aapl_data)

aapl = pd.DataFrame(aapl_data)

print(aapl.head())