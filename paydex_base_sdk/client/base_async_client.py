from abc import ABCMeta, abstractmethod
from typing import AsyncGenerator, Dict, Union, Any

from .response import Response


class BaseAsyncClient(metaclass=ABCMeta):
    """This is an abstract class,
    and if you want to implement your own asynchronous client, you **must** implement this class.

    """

    @abstractmethod
    async def get(self, url: str, params: Dict[str, str] = None) -> Response:
        """Perform HTTP GET request.

        :param url: the request url
        :param params: the request params
        :return: the response from server
        :raise: :exc:`ConnectionError <paydex_sdk.exceptions.ConnectionError>`
        """
        pass

    @abstractmethod
    async def post(self, url: str, data: Dict[str, str]) -> Response:
        """Perform HTTP POST request.

        :param url: the request url
        :param data: the data send to server
        :return: the response from server
        :raise: :exc:`ConnectionError <paydex_sdk.exceptions.ConnectionError>`
        """
        pass

    @abstractmethod
    async def stream(
        self, url: str, params: Dict[str, str] = None
    ) -> AsyncGenerator[Dict[str, Any], None]:
        """Creates an EventSource that listens for incoming messages from the server.


        :param url: the request url
        :param params: the request params
        :return: a dict AsyncGenerator for server response
        :raise: :exc:`ConnectionError <paydex_sdk.exceptions.ConnectionError>`
        """
        pass

    @abstractmethod
    async def close(self) -> None:
        pass
