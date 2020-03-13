
from paydex_base_sdk.keypair import Keypair
from paydex_base_sdk.network import Network
from paydex_base_sdk.server import Server
from paydex_base_sdk.transaction_builder import TransactionBuilder

source_secret_key = "SBFZCHU5645DOKRWYBXVOXY2ELGJKFRX6VGGPRYUWHQ7PMXXJNDZFMKD"

# Derive Keypair object and public key (that starts with a G) from the secret
source_keypair = Keypair.from_secret(source_secret_key)
source_public_key = source_keypair.public_key

receiver_public_key = "GA7YNBW5CBTJZ3ZZOWX3ZNBKD6OE7A7IHUQVWMY62W2ZBG2SGZVOOPVH"


server = Server(horizon_url="https://testhorizon.paydex.io/")

# Transactions require a valid sequence number that is specific to this account.
source_account = server.load_account(source_public_key)

base_fee = server.fetch_base_fee()

transaction = (
    TransactionBuilder(
        source_account=source_account,
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee=base_fee,
    )
        .add_text_memo("Hello, Paydex!")  # Add a memo
        # Add a payment operation to the transaction
        # Send 350.1234567 PAYDEX to receiver
        # Specify 350.1234567 lumens. Lumens are divisible to seven digits past the decimal.
        .append_payment_op(receiver_public_key, "350.1234567", "PAYDEX")
        .set_timeout(30)  # Make this transaction valid for the next 30 seconds only
        .build()
)

# Sign this transaction with the secret key
transaction.sign(source_keypair)

# Let's see the XDR (encoded in base64) of the transaction we just built
print(transaction.to_xdr())


response = server.submit_transaction(transaction)
print(response)
