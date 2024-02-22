from alpaca_trade_api.rest import REST, TimeFrame

api = REST('PKQRBC27FFE1WFOPK7SK', '86bAYSOeq0BCELPGCtMcCjjbcdnGNiFdeVDABvwf', base_url='https://paper-api.alpaca.markets')


order = api.submit_order(
    symbol='AAPL',
    qty=1,
    side='buy',
    type='market',
    time_in_force='gtc'
)


order_details = api.get_order(order.id)

print("Order details:")
print(f"ID: {order_details.id}")
print(f"Status: {order_details.status}")
print(f"Submitted At: {order_details.submitted_at}")
print(f"Filled At: {order_details.filled_at}")
print(f"Filled Qty: {order_details.filled_qty}")
print(f"Average Fill Price: {order_details.filled_avg_price}")

