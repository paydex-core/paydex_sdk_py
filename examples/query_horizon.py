from paydex_base_sdk.server import Server

server = Server(horizon_url="https://testhorizon.paydex.io//")

# get a list of transactions that occurred in ledger 1400
transactions = server.transactions().for_ledger(1400).call()
print(transactions)

# get a list of transactions submitted by a particular account
transactions = server.transactions() \
    .for_account(account_id="GASOCNHNNLYFNMDJYQ3XFMI7BYHIOCFW3GJEOWRPEGK2TDPGTG2E5EDW") \
    .call()
print(transactions)
