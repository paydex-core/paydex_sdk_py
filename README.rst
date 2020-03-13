Paydex SDK Python
==================


paydex-sdk is a Python library for communicating with
a `Paydex server`_. It is used for building Paydex apps on Python. It supports **Python 3.6+** as
well as PyPy 3.6+.`Paydex server`_.

It provides:

- a networking layer API for Paydex endpoints.
- facilities for building and signing transactions, for communicating with a Paydex instance, and for submitting transactions or querying network history.

Documentation
==================

Documentation of the code's layout and abstractions, as well as for the functionality available, can be found in ./docs.


A Simple Example
----------------

* Generate Keypair

.. code-block:: python

    from paydex_base_sdk import Keypair

    keypair = Keypair.from_secret("SBK2VIYYSVG76E7VC3QHYARNFLY2EAQXDHRC7BMXBBGIFG74ARPRMNQM")
    public_key = keypair.public_key  # GDHMW6QZOL73SHKG2JA3YHXFDHM46SS5ZRWEYF5BCYHX2C5TVO6KZBYL
    can_sign = keypair.can_sign()  # True


* Create Account

.. code-block:: python

    import requests

    from paydex_base_sdk import Keypair

    keypair = Keypair.random()

    print("Public Key: " + keypair.public_key)
    print("Secret Seed: " + keypair.secret)

    url = 'https://testhorizon.paydex.io/'
    response = requests.get(url, params={'addr': keypair.public_key})
    print(response)



* Building transaction with synchronous server

.. code-block:: python

    # Alice pay 10.25 PAYDEX to Bob
    from paydex_base_sdk import Server, Keypair, TransactionBuilder, Network

    alice_keypair = Keypair.from_secret("SBFZCHU5645DOKRWYBXVOXY2ELGJKFRX6VGGPRYUWHQ7PMXXJNDZFMKD")
    bob_address = "GA7YNBW5CBTJZ3ZZOWX3ZNBKD6OE7A7IHUQVWMY62W2ZBG2SGZVOOPVH"

    server = Server("https://testhorizon.paydex.io/")
    alice_account = server.load_account(alice_keypair.public_key)
    base_fee = server.fetch_base_fee()
    transaction = (
        TransactionBuilder(
            source_account=alice_account,
            network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
            base_fee=base_fee,
        )
        .add_text_memo("Hello, Paydex!")
        .append_payment_op(bob_address, "10.25", "PAYDEX")
        .build()
    )
    transaction.sign(alice_keypair)
    response = server.submit_transaction(transaction)
    print(response)

* Building transaction with asynchronous server

.. code-block:: python

    # Alice pay 10.25 PAYDEX to Bob
    import asyncio

    from paydex_base_sdk import Server, Keypair, TransactionBuilder, Network
    from paydex_base_sdk.client.aiohttp_client import AiohttpClient

    alice_keypair = Keypair.from_secret("SBFZCHU5645DOKRWYBXVOXY2ELGJKFRX6VGGPRYUWHQ7PMXXJNDZFMKD")
    bob_address = "GA7YNBW5CBTJZ3ZZOWX3ZNBKD6OE7A7IHUQVWMY62W2ZBG2SGZVOOPVH"


    async def payment():
        async with Server(
            horizon_url="https://testhorizon.paydex.io/", client=AiohttpClient()
        ) as server:
            alice_account = await server.load_account(alice_keypair.public_key)
            base_fee = await server.fetch_base_fee()
            transaction = (
                TransactionBuilder(
                    source_account=alice_account,
                    network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
                    base_fee=base_fee,
                )
                .add_text_memo("Hello, Paydex!")
                .append_payment_op(bob_address, "10.25", "PAYDEX")
                .build()
            )

            transaction.sign(alice_keypair)
            response = await server.submit_transaction(transaction)
            print(response)


    if __name__ == "__main__":
        asyncio.run(payment())



