"""
SEP: 0001
Title: paydex.toml
Author: paydex.org
Status: Active
Created: 2017-10-30
Updated: 2019-06-12
Version: 2.1.0
"""
from typing import Union, Dict, Any, Coroutine

import toml

from .exceptions import PaydexTomlNotFoundError
from ..client.base_async_client import BaseAsyncClient
from ..client.base_sync_client import BaseSyncClient
from ..client.requests_client import RequestsClient
from ..client.response import Response


def fetch_paydex_toml(
    domain: str,
    client: Union[BaseAsyncClient, BaseSyncClient] = None,
    use_http: bool = False,
) -> Union[Coroutine[Any, Any, Dict[str, Any]], Dict[str, Any]]:
    """Retrieve the paydex.toml file from a given domain.

    Retrieve the paydex.toml file for information about interacting with
    Paydex's federation protocol for a given Paydex Anchor (specified by a
    domain).

    :param domain: The domain the .toml file is hosted at.
    :param use_http: Specifies whether the request should go over plain HTTP vs HTTPS.
        Note it is recommend that you *always* use HTTPS.
    :param client: Http Client used to send the request.
    :return: The paydex.toml file as a an object via :func:`toml.loads`.
    :raises: :exc:`PaydexTomlNotFoundError <paydex_sdk.sep.exceptions.PaydexTomlNotFoundError>`:
        if the Paydex toml file could not not be found.
    """
    if not client:
        client = RequestsClient()

    toml_link = "/.well-known/paydex.toml"
    protocol = "https://"
    if use_http:
        protocol = "http://"
    url = protocol + domain + toml_link

    if isinstance(client, BaseAsyncClient):
        return __fetch_async(url, client)
    elif isinstance(client, BaseSyncClient):
        return __fetch_sync(url, client)
    else:
        raise TypeError(
            "This `client` class should be an instance "
            "of `paydex_sdk.client.base_async_client.BaseAsyncClient` "
            "or `paydex_sdk.client.base_sync_client.BaseSyncClient`."
        )


async def __fetch_async(url: str, client: BaseAsyncClient) -> Dict[str, Any]:
    raw_resp = await client.get(url)
    return __handle_raw_response(raw_resp)


def __fetch_sync(url: str, client: BaseSyncClient) -> Dict[str, Any]:
    raw_resp = client.get(url)
    return __handle_raw_response(raw_resp)


def __handle_raw_response(raw_resp: Response) -> Dict[str, Any]:
    if raw_resp.status_code == 404:
        raise PaydexTomlNotFoundError
    resp = raw_resp.text
    return toml.loads(resp)
