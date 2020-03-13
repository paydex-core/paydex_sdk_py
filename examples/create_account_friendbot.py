import requests

from paydex_base_sdk.keypair import Keypair

keypair = Keypair.random()

print("Public Key: " + keypair.public_key)
print("Secret Seed: " + keypair.secret)

url = 'https://testhorizon.paydex.io/'
response = requests.get(url, params={'addr': keypair.public_key})
print(response)
