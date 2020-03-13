
import asyncio

from paydex_base_sdk.client.aiohttp_client import AiohttpClient
from paydex_base_sdk.keypair import Keypair
from paydex_base_sdk.network import Network
from paydex_base_sdk.server import Server
from paydex_base_sdk.transaction_builder import TransactionBuilder

source_secret_key = "SBFZCHU5645DOKRWYBXVOXY2ELGJKFRX6VGGPRYUWHQ7PMXXJNDZFMKD"

# Derive Keypair object and public key (that starts with a G) from the secret
source_keypair = Keypair.from_secret(source_secret_key)
source_public_key = source_keypair.public_key

receiver_public_key = "GA7YNBW5CBTJZ3ZZOWX3ZNBKD6OE7A7IHUQVWMY62W2ZBG2SGZVOOPVH"


async def main():
    # Configure paydexSdk to talk to the horizon instance hosted by paydex.org
    # When we use the `with` syntax, it automatically releases the resources it occupies.
    async with Server(
            horizon_url="https://testhorizon.paydex.io//", client=AiohttpClient()
    ) as server:
        # Transactions require a valid sequence number that is specific to this account.
        # We can fetch the current sequence number for the source account from Horizon.
        source_account = await server.load_account(source_public_key)

        base_fee = await server.fetch_base_fee()
        # we are going to submit the transaction to the test network,
        # so network_passphrase is `Network.TESTNET_NETWORK_PASSPHRASE`,
        # if you want to submit to the public network, please use `Network.PUBLIC_NETWORK_PASSPHRASE`.
        transaction = (
            TransactionBuilder(
                source_account=source_account,
                network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
                base_fee=base_fee,
            )
                .add_text_memo("Hello, paydex!")  # Add a memo
                # Add a payment operation to the transaction
                # Send 350.1234567 PAYDEX to receiver
                # Specify 350.1234567 lumens. Lumens are divisible to seven digits past the decimal.
                .append_payment_op(receiver_public_key, "350.1234567", "PAYDEX")
                .set_timeout(30)  # Make this transaction valid for the next 30 seconds only
                .build()
        )

        # Sign this transaction with the secret key
        # NOTE: signing is transaction is network specific. Test network transactions
        # won't work in the public network. To switch networks, use the Network object
        # as explained above (look for paydex_base_sdk.network.Network).
        transaction.sign(source_keypair)

        # Let's see the XDR (encoded in base64) of the transaction we just built
        print(transaction.to_xdr())

        # Submit the transaction to the Horizon server.
        # The Horizon server will then submit the transaction into the network for us.
        response = await server.submit_transaction(transaction)
        print(response)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
    # asyncio.run(main())  # Python 3.7+
