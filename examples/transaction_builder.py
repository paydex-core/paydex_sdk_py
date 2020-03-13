from paydex_base_sdk.account import Account
from paydex_base_sdk.keypair import Keypair
from paydex_base_sdk.network import Network
from paydex_base_sdk.transaction_builder import TransactionBuilder

root_keypair = Keypair.from_secret("SA6XHAH4GNLRWWWF6TEVEWNS44CBNFAJWHWOPZCVZOUXSQA7BOYN7XHC")
# Create an Account object from an address and sequence number.
root_account = Account(account_id=root_keypair.public_key, sequence=1)

transaction = TransactionBuilder(
    source_account=root_account,
    network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
    base_fee=100) \
    .append_payment_op(  # add a payment operation to the transaction
    destination="GASOCNHNNLYFNMDJYQ3XFMI7BYHIOCFW3GJEOWRPEGK2TDPGTG2E5EDW",
    asset_code="PAYDEX",
    amount="125.5") \
    .append_set_options_op(  # add a set options operation to the transaction
    home_domain="overcat.me") \
    .set_timeout(30) \
    .build()  # mark this transaction as valid only for the next 30 seconds
