from typing import Union

from ..call_builder.base_call_builder import BaseCallBuilder
from ..client.base_async_client import BaseAsyncClient
from ..client.base_sync_client import BaseSyncClient


class LedgersCallBuilder(BaseCallBuilder):
    """ Creates a new :class:`LedgersCallBuilder` pointed to server defined by horizon_url.
    Do not create this object directly, use :func:`paydex_sdk.server.Server.ledgers`.


    :param horizon_url: Horizon server URL.
    :param client: The client instance used to send request.
    """

    def __init__(
        self, horizon_url: str, client: Union[BaseAsyncClient, BaseSyncClient]
    ) -> None:
        super().__init__(horizon_url, client)
        self.endpoint: str = "ledgers"

    def ledger(self, sequence: Union[int, str]) -> "LedgersCallBuilder":
        """Provides information on a single ledger.

        :param sequence: Ledger sequence
        :return: current LedgerCallBuilder instance
        """
        self.endpoint = "ledgers/{sequence}".format(sequence=sequence)
        return self
