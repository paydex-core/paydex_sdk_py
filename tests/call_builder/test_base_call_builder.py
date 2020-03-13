import pytest

from paydex_base_sdk.__version__ import __version__
from paydex_base_sdk.call_builder import BaseCallBuilder
from paydex_base_sdk.client.aiohttp_client import AiohttpClient
from paydex_base_sdk.client.requests_client import RequestsClient
from paydex_base_sdk.exceptions import BadRequestError, NotFoundError, NotPageableError


class TestBaseCallBuilder:
    @pytest.mark.asyncio
    async def test_get_data_async(self):
        url = "https://testhorizon.paydex.io/get"
        client = AiohttpClient()
        resp = (
            await BaseCallBuilder(url, client)
            .cursor(89777)
            .order(desc=False)
            .limit(25)
            .call()
        )

        assert resp["args"] == {"cursor": "89777", "limit": "25", "order": "asc"}
        assert resp["headers"][
            "User-Agent"
        ] == "py-paydex-sdk/{}/AiohttpClient".format(__version__)
        assert resp["headers"]["X-Client-Name"] == "py-paydex-sdk"
        assert resp["headers"]["X-Client-Version"] == __version__
        assert resp["url"] == "https://testhorizon.paydex.io/get?cursor=89777&order=asc&limit=25"

    def test_get_data_sync(self):
        url = "https://testhorizon.paydex.io/get"
        client = RequestsClient()
        resp = (
            BaseCallBuilder(url, client).limit(10).cursor(10086).order(desc=True).call()
        )
        assert resp["args"] == {"cursor": "10086", "limit": "10", "order": "desc"}
        assert resp["headers"][
            "User-Agent"
        ] == "py-paydex-sdk/{}/RequestsClient".format(__version__)
        assert resp["headers"]["X-Client-Name"] == "py-paydex-sdk"
        assert resp["headers"]["X-Client-Version"] == __version__
        assert resp["url"] == "https://testhorizon.paydex.io/get?limit=10&cursor=10086&order=desc"

    @pytest.mark.slow
    @pytest.mark.asyncio
    @pytest.mark.timeout(30)
    async def test_get_stream_data_async(self):
        url = "https://testhorizon.paydex.io/ledgers"
        client = AiohttpClient()
        resp = BaseCallBuilder(url, client).cursor("now").stream()
        messages = []
        async for msg in resp:
            assert isinstance(msg, dict)
            messages.append(msg)
            if len(messages) == 2:
                break

    @pytest.mark.slow
    @pytest.mark.timeout(30)
    def test_stream_data_sync(self):
        url = "https://testhorizon.paydex.io/ledgers"
        client = RequestsClient()
        resp = BaseCallBuilder(url, client).cursor("now").stream()
        messages = []
        for msg in resp:
            assert isinstance(msg, dict)
            messages.append(msg)
            if len(messages) == 2:
                break

    def test_status_400_raise_sync(self):
        url = "https://testhorizon.paydex.io/accounts/BADACCOUNTID"
        client = RequestsClient()
        with pytest.raises(BadRequestError) as err:
            BaseCallBuilder(url, client).call()

        exception = err.value
        assert exception.status == 400
        assert exception.type == "https://paydex.org/horizon-errors/bad_request"
        assert exception.title == "Bad Request"
        assert exception.detail == "The request you sent was invalid in some way."
        assert exception.extras == {
            "invalid_field": "account_id",
            "reason": "invalid address",
        }

    def test_status_404_raise_sync(self):
        url = "https://testhorizon.paydex.io/not_found"
        client = RequestsClient()
        with pytest.raises(NotFoundError) as err:
            BaseCallBuilder(url, client).call()

        exception = err.value
        assert exception.status == 404
        assert exception.type == "https://paydex.org/horizon-errors/not_found"
        assert exception.title == "Resource Missing"
        assert (
            exception.detail
            == "The resource at the url requested was not found.  This "
            "usually occurs for one of two reasons:  The url requested is not valid, "
            "or no data in our database could be found with the parameters provided."
        )
        assert exception.extras is None

    @pytest.mark.asyncio
    async def test_status_400_raise_async(self):
        url = "https://testhorizon.paydex.io/accounts/BADACCOUNTID"
        client = AiohttpClient()
        with pytest.raises(BadRequestError) as err:
            await BaseCallBuilder(url, client).call()

        exception = err.value
        assert exception.status == 400
        assert exception.type == "https://paydex.org/horizon-errors/bad_request"
        assert exception.title == "Bad Request"
        assert exception.detail == "The request you sent was invalid in some way."
        assert exception.extras == {
            "invalid_field": "account_id",
            "reason": "invalid address",
        }

    @pytest.mark.asyncio
    async def test_status_404_raise_async(self):
        url = "https://testhorizon.paydex.io/not_found"
        client = AiohttpClient()
        with pytest.raises(NotFoundError) as err:
            await BaseCallBuilder(url, client).call()

        exception = err.value
        assert exception.status == 404
        assert exception.type == "https://paydex.org/horizon-errors/not_found"
        assert exception.title == "Resource Missing"
        assert (
            exception.detail
            == "The resource at the url requested was not found.  This "
            "usually occurs for one of two reasons:  The url requested is not valid, "
            "or no data in our database could be found with the parameters provided."
        )
        assert exception.extras is None

    def test_get_data_no_link(self):
        url = "https://testhorizon.paydex.io/get"
        client = RequestsClient()
        call_builder = (
            BaseCallBuilder(url, client).limit(10).cursor(10086).order(desc=True)
        )
        call_builder.call()
        assert call_builder.next_href is None
        assert call_builder.prev_href is None

    def test_get_data_not_pageable_raise(self):
        url = "https://testhorizon.paydex.io/get"
        client = RequestsClient()
        call_builder = (
            BaseCallBuilder(url, client).limit(10).cursor(10086).order(desc=True)
        )
        call_builder.call()
        with pytest.raises(NotPageableError, match="The next page does not exist."):
            call_builder.next()

        with pytest.raises(NotPageableError, match="The prev page does not exist."):
            call_builder.prev()

    def test_get_data_page(self):
        url = "https://testhorizon.paydex.io/transactions"
        client = RequestsClient()
        call_builder = (
            BaseCallBuilder(url, client)
            .cursor(81058917781504)
            .limit(10)
            .order(desc=True)
        )
        first_resp = call_builder.call()
        assert first_resp["_links"] == {
            "self": {
                "href": "https://testhorizon.paydex.io/transactions?cursor=81058917781504&limit=10&order=desc"
            },
            "next": {
                "href": "https://testhorizon.paydex.io/transactions?cursor=12884905984&limit=10&order=desc"
            },
            "prev": {
                "href": "https://testhorizon.paydex.io/transactions?cursor=80607946215424&limit=10&order=asc"
            },
        }
        next_resp = call_builder.next()
        assert next_resp["_links"] == {
            "self": {
                "href": "https://testhorizon.paydex.io/transactions?cursor=12884905984&limit=10&order=desc"
            },
            "next": {
                "href": "https://testhorizon.paydex.io/transactions?cursor=12884905984&limit=10&order=desc"
            },
            "prev": {
                "href": "https://testhorizon.paydex.io/transactions?cursor=12884905984&limit=10&order=asc"
            },
        }
        prev_page = call_builder.prev()
        assert prev_page["_links"] == {
            "self": {
                "href": "https://testhorizon.paydex.io/transactions?cursor=12884905984&limit=10&order=asc"
            },
            "next": {
                "href": "https://testhorizon.paydex.io/transactions?cursor=81827716927488&limit=10&order=asc"
            },
            "prev": {
                "href": "https://testhorizon.paydex.io/transactions?cursor=33676838572032&limit=10&order=desc"
            },
        }
