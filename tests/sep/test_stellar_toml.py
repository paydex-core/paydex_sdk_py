import pytest

from paydex_base_sdk.client.aiohttp_client import AiohttpClient
from paydex_base_sdk.sep.exceptions import PaydexTomlNotFoundError
from paydex_base_sdk.sep.paydex_toml import fetch_paydex_toml


class TestPaydexToml:
    def test_get_success_sync(self):
        toml = fetch_paydex_toml("overcat.me", None)
        assert toml.get("FEDERATION_SERVER") == "https://federation.overcat.workers.dev"

    @pytest.mark.asyncio
    async def test_get_success_async(self):
        client = AiohttpClient()
        toml = await fetch_paydex_toml("overcat.me", client)
        assert toml.get("FEDERATION_SERVER") == "https://federation.overcat.workers.dev"

    def test_get_success_http(self):
        toml = fetch_paydex_toml("overcat.me", None, True)
        assert toml.get("FEDERATION_SERVER") == "https://federation.overcat.workers.dev"

    def test_get_not_found(self):
        with pytest.raises(PaydexTomlNotFoundError):
            fetch_paydex_toml("httpbin.org")

    def test_invalid_client(self):
        client = "BAD TYPE"
        with pytest.raises(
            TypeError,
            match="This `client` class should be an instance "
            "of `paydex_base_sdk.client.base_async_client.BaseAsyncClient` "
            "or `paydex_base_sdk.client.base_sync_client.BaseSyncClient`.",
        ):
            fetch_paydex_toml("httpbin.org", client)
