"""
SEP: 0002
Title: Federation protocol
Author: paydex.org
Status: Final
Created: 2020-1-3
Updated: 2020-3-12
Version 0.1.0
"""
from typing import Optional, Union, Coroutine, Any

from ..exceptions import ValueError
from .exceptions import (
    InvalidFederationAddress,
    FederationServerNotFoundError,
    BadFederationResponseError,
)
from .paydex_toml import fetch_paydex_toml
from ..client.base_async_client import BaseAsyncClient
from ..client.base_sync_client import BaseSyncClient
from ..client.requests_client import RequestsClient
from ..client.response import Response

SEPARATOR = "*"
FEDERATION_SERVER_KEY = "FEDERATION_SERVER"


class FederationRecord:
    def __init__(self, account_id, paydex_address, memo_type, memo):
        """The :class:`FederationRecord`, which represents record in federation server.

        :param account_id: Paydex public key / account ID
        :param paydex_address: Paydex address
        :param memo_type: Type of memo to attach to transaction, one of *text*, *id* or *hash*
        :param memo: value of memo to attach to transaction, for *hash* this should be base64-encoded.
            This field should always be of type *string* (even when ``memo_type`` is equal *id*) to support parsing
            value in languages that don't support big numbers.
        """
        self.account_id: str = account_id
        self.paydex_address: str = paydex_address
        self.memo_type: Optional[str] = memo_type
        self.memo: Optional[str] = memo

    def __str__(self):
        return (
            "<FederationRecord [account_id={account_id}, paydex_address={paydex_address}, "
            "memo_type={memo_type}, memo={memo}]>".format(
                account_id=self.account_id,
                paydex_address=self.paydex_address,
                memo_type=self.memo_type,
                memo=self.memo,
            )
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented  # pragma: no cover
        return (
            self.account_id == other.account_id
            and self.paydex_address == other.paydex_address
            and self.memo_type == other.memo_type
            and self.memo == other.memo
        )


def resolve_paydex_address(
    paydex_address: str,
    client: Union[BaseAsyncClient, BaseSyncClient] = None,
    federation_url: str = None,
    use_http: bool = False,
) -> Union[Coroutine[Any, Any, FederationRecord], FederationRecord]:
    """Get the federation record if the user was found for a given Paydex address.

    :param paydex_address: address Paydex address (ex. bob*paydex.org).
    :param client: Http Client used to send the request.
    :param federation_url: The federation server URL,
        if you don't set this value, we will try to get it from ``paydex_address``.
    :param use_http: Specifies whether the request should go over plain HTTP vs HTTPS.
        Note it is recommend that you *always* use HTTPS.
    :return: Federation record.
    """
    if not client:
        client = RequestsClient()
    if isinstance(client, BaseAsyncClient):
        return __resolve_paydex_address_async(
            paydex_address, client, federation_url, use_http
        )
    elif isinstance(client, BaseSyncClient):
        return __resolve_paydex_address_sync(
            paydex_address, client, federation_url, use_http
        )
    else:
        raise TypeError(
            "This `client` class should be an instance "
            "of `paydex_sdk.client.base_async_client.BaseAsyncClient` "
            "or `paydex_sdk.client.base_sync_client.BaseSyncClient`."
        )


def resolve_account_id(
    account_id: str,
    domain: str = None,
    federation_url: str = None,
    client: Union[BaseAsyncClient, BaseSyncClient] = None,
    use_http: bool = False,
) -> Union[Coroutine[Any, Any, FederationRecord], FederationRecord]:
    """Given an account ID, get their federation record if the user was found

    :param account_id: Account ID (ex. GBYNR2QJXLBCBTRN44MRORCMI4YO7FZPFBCNOKTOBCAAFC7KC3LNPRYS)
    :param domain: Get ``federation_url`` from the domain, you don't need to set this value if ``federation_url`` is set.
    :param federation_url: The federation server URL.
    :param client: Http Client used to send the request.
    :param use_http: Specifies whether the request should go over plain HTTP vs HTTPS.
        Note it is recommend that you *always* use HTTPS.
    :return: Federation record.
    """
    if domain is None and federation_url is None:
        raise ValueError("You should provide either `domain` or `federation_url`.")

    if not client:
        client = RequestsClient()
    if isinstance(client, BaseAsyncClient):
        return __resolve_account_id_async(
            account_id, domain, federation_url, client, use_http
        )
    elif isinstance(client, BaseSyncClient):
        return __resolve_account_id_sync(
            account_id, domain, federation_url, client, use_http
        )
    else:
        raise TypeError(
            "This `client` class should be an instance "
            "of `paydex_sdk.client.base_async_client.BaseAsyncClient` "
            "or `paydex_sdk.client.base_sync_client.BaseSyncClient`."
        )


def __resolve_paydex_address_sync(
    paydex_address: str,
    client: BaseSyncClient,
    federation_url: str = None,
    use_http: bool = False,
) -> FederationRecord:
    parts = split_paydex_address(paydex_address)
    domain = parts["domain"]
    if federation_url is None:
        federation_url = fetch_paydex_toml(domain, use_http=use_http).get(
            FEDERATION_SERVER_KEY
        )
    if federation_url is None:
        raise FederationServerNotFoundError(
            "Unable to find federation server at {}.".format(domain)
        )
    raw_resp = client.get(federation_url, {"type": "name", "q": paydex_address})
    return __handle_raw_response(raw_resp, paydex_address=paydex_address)


async def __resolve_paydex_address_async(
    paydex_address: str,
    client: BaseAsyncClient,
    federation_url: str = None,
    use_http: bool = False,
) -> FederationRecord:
    parts = split_paydex_address(paydex_address)
    domain = parts["domain"]
    if federation_url is None:
        federation_url = (
            await fetch_paydex_toml(domain, client=client, use_http=use_http)
        ).get(FEDERATION_SERVER_KEY)
    if federation_url is None:
        raise FederationServerNotFoundError(
            "Unable to find federation server at {}.".format(domain)
        )
    raw_resp = await client.get(federation_url, {"type": "name", "q": paydex_address})
    return __handle_raw_response(raw_resp, paydex_address=paydex_address)


def __resolve_account_id_sync(
    account_id: str,
    domain: str = None,
    federation_url: str = None,
    client=None,
    use_http: bool = False,
) -> FederationRecord:
    if domain is not None:
        federation_url = fetch_paydex_toml(domain, client, use_http).get(
            FEDERATION_SERVER_KEY
        )
        if federation_url is None:
            raise FederationServerNotFoundError(
                "Unable to find federation server at {}.".format(domain)
            )
    raw_resp = client.get(federation_url, {"type": "id", "q": account_id})
    return __handle_raw_response(raw_resp, account_id=account_id)


async def __resolve_account_id_async(
    account_id: str,
    domain: str = None,
    federation_url: str = None,
    client=None,
    use_http: bool = False,
) -> FederationRecord:
    if domain is not None:
        federation_url = (await fetch_paydex_toml(domain, client, use_http)).get(
            FEDERATION_SERVER_KEY
        )
        if federation_url is None:
            raise FederationServerNotFoundError(
                "Unable to find federation server at {}.".format(domain)
            )
    raw_resp = await client.get(federation_url, {"type": "id", "q": account_id})
    return __handle_raw_response(raw_resp, account_id=account_id)


def __handle_raw_response(raw_resp: Response, paydex_address=None, account_id=None):
    if not 200 <= raw_resp.status_code < 300:
        raise BadFederationResponseError(raw_resp)
    data = raw_resp.json()
    account_id = account_id or data.get("account_id")
    paydex_address = paydex_address or data.get("paydex_address")
    memo_type = data.get("memo_type")
    memo = data.get("memo")
    return FederationRecord(
        account_id=account_id,
        paydex_address=paydex_address,
        memo_type=memo_type,
        memo=memo,
    )


def split_paydex_address(address: str) -> dict:
    parts = address.split(SEPARATOR)
    if len(parts) != 2:
        raise InvalidFederationAddress(
            "Address should be a valid address, such as `bob*paydex.org`"
        )
    name, domain = parts
    return {"name": name, "domain": domain}
