import pytest

from paydex_base_sdk.client.aiohttp_client import AiohttpClient
from paydex_base_sdk.sep.exceptions import (
    InvalidFederationAddress,
    FederationServerNotFoundError,
    BadFederationResponseError,
)
from paydex_base_sdk.sep.federation import (
    resolve_paydex_address,
    resolve_account_id,
    FederationRecord,
    split_paydex_address,
)
from paydex_base_sdk.exceptions import ValueError


class TestFederation:
    ACCOUNT_ID = "GAWCQ74PIJO2NH6F3KZ4AMX27UAKBXWC7KG3FLYJOFIMRQF3RSZHCOVN"
    PAYDEX_ADDRESS = "hello*overcat.me"
    DOMAIN = "overcat.me"
    FEDERATION_SERVER = "https://federation.overcat.workers.dev/"
    FEDERATION_RECORD = FederationRecord(
        paydex_address=PAYDEX_ADDRESS,
        account_id=ACCOUNT_ID,
        memo_type="text",
        memo="Nice to meet you :-)",
    )

    def test_resolve_by_PAYDEX_address_sync(self):
        record = resolve_paydex_address(self.PAYDEX_ADDRESS)
        assert record == self.FEDERATION_RECORD

    @pytest.mark.asyncio
    async def test_resolve_by_PAYDEX_address_async(self):
        record = await resolve_paydex_address(
            self.PAYDEX_ADDRESS, client=AiohttpClient()
        )
        assert record == self.FEDERATION_RECORD

    def test_resolve_by_PAYDEX_address_federation_not_found_sync(self):
        with pytest.raises(
            FederationServerNotFoundError,
            match="Unable to find federation server at sdk-test.overcat.me.",
        ):
            resolve_paydex_address("hello*sdk-test.overcat.me")

    @pytest.mark.asyncio
    async def test_resolve_by_PAYDEX_address_federation_not_found_async(self):
        with pytest.raises(
            FederationServerNotFoundError,
            match="Unable to find federation server at sdk-test.overcat.me.",
        ):
            await resolve_paydex_address(
                "hello*sdk-test.overcat.me", client=AiohttpClient()
            )

    def test_resolve_by_PAYDEX_address_with_federation_url_sync(self):
        record = resolve_paydex_address(
            "hello*example.com", federation_url=self.FEDERATION_SERVER
        )
        assert (
            record.account_id
            == "GAWCQ74PIJO2NH6F3KZ4AMX27UAKBXWC7KG3FLYJOFIMRQF3REXAMPLE"
        )

    @pytest.mark.asyncio
    async def test_resolve_by_PAYDEX_address_with_federation_url_async(self):
        record = await resolve_paydex_address(
            "hello*example.com",
            federation_url=self.FEDERATION_SERVER,
            client=AiohttpClient(),
        )
        assert (
            record.account_id
            == "GAWCQ74PIJO2NH6F3KZ4AMX27UAKBXWC7KG3FLYJOFIMRQF3REXAMPLE"
        )

    def test_resolve_by_account_id_with_domain_sync(self):
        record = resolve_account_id(self.ACCOUNT_ID, domain=self.DOMAIN)
        assert record == self.FEDERATION_RECORD

    @pytest.mark.asyncio
    async def test_resolve_by_account_id_with_domain_async(self):
        record = await resolve_account_id(
            self.ACCOUNT_ID, domain=self.DOMAIN, client=AiohttpClient()
        )
        assert record == self.FEDERATION_RECORD

    def test_resolve_by_account_id_without_domain_and_federation_url(self):
        with pytest.raises(
            ValueError, match="You should provide either `domain` or `federation_url`."
        ):
            resolve_account_id(self.ACCOUNT_ID)

    def test_resolve_by_account_id_federation_not_found_sync(self):
        with pytest.raises(
            FederationServerNotFoundError,
            match="Unable to find federation server at sdk-test.overcat.me.",
        ):
            resolve_account_id(self.ACCOUNT_ID, domain="sdk-test.overcat.me")

    @pytest.mark.asyncio
    async def test_resolve_by_account_id_federation_not_found_async(self):
        with pytest.raises(
            FederationServerNotFoundError,
            match="Unable to find federation server at sdk-test.overcat.me.",
        ):
            await resolve_account_id(
                self.ACCOUNT_ID, domain="sdk-test.overcat.me", client=AiohttpClient()
            )

    def test_not_found_record_at_federation(self):
        with pytest.raises(BadFederationResponseError) as err:
            resolve_paydex_address("not_found*overcat.me")
        assert err.value.status == 404

    def test_split_address(self):
        assert split_paydex_address(self.PAYDEX_ADDRESS) == {
            "name": "hello",
            "domain": "overcat.me",
        }

    @pytest.mark.parametrize("PAYDEX_address", ["", "hey", "hey*hello*overcat.me"])
    def test_split_invalid_address(self, PAYDEX_address):
        with pytest.raises(InvalidFederationAddress):
            split_paydex_address(PAYDEX_address)

    def test_invalid_client(self):
        client = "BAD TYPE"
        with pytest.raises(
            TypeError,
            match="This `client` class should be an instance "
            "of `paydex_base_sdk.client.base_async_client.BaseAsyncClient` "
            "or `paydex_base_sdk.client.base_sync_client.BaseSyncClient`.",
        ):
            resolve_account_id(self.ACCOUNT_ID, domain=self.DOMAIN, client=client)

        with pytest.raises(
            TypeError,
            match="This `client` class should be an instance "
            "of `paydex_base_sdk.client.base_async_client.BaseAsyncClient` "
            "or `paydex_base_sdk.client.base_sync_client.BaseSyncClient`.",
        ):
            resolve_paydex_address(self.PAYDEX_ADDRESS, client=client)
