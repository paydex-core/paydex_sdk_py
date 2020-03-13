import asyncio

from paydex_base_sdk.client.aiohttp_client import AiohttpClient
from paydex_base_sdk.server import Server

HORIZON_URL = "https://testhorizon.paydex.io//"


async def payments():
    async with Server(HORIZON_URL, AiohttpClient()) as server:
        async for payment in server.payments().cursor(cursor="now").stream():
            print(f"Payment: {payment}")


async def effects():
    async with Server(HORIZON_URL, AiohttpClient()) as server:
        async for effect in server.effects().cursor(cursor="now").stream():
            print(f"Effect: {effect}")


async def operations():
    async with Server(HORIZON_URL, AiohttpClient()) as server:
        async for operation in server.operations().cursor(cursor="now").stream():
            print(f"Operation: {operation}")


async def transactions():
    async with Server(HORIZON_URL, AiohttpClient()) as server:
        async for transaction in server.transactions().cursor(cursor="now").stream():
            print(f"Transaction: {transaction}")


async def listen():
    await asyncio.gather(
        payments(),
        effects(),
        operations(),
        transactions()
    )


if __name__ == '__main__':
    asyncio.run(listen())
