from .utils import sha256

__all__ = ["Network"]


class Network:
    """The :class:`Network` object, which represents a Paydex network.

    This class represents such a paydex network such as the Public network and the Test network.

    :param str network_passphrase: The passphrase for the network.
        (ex. 'paydex open-chain test-newtwork; March 2020')

    """

    PUBLIC_NETWORK_PASSPHRASE: str = "paydex core newtwork ;  September 2019"
    """Get the Public network passphrase."""

    TESTNET_NETWORK_PASSPHRASE: str = "paydex open-chain test-newtwork; March 2020"
    """Get the Test network passphrase."""

    def __init__(self, network_passphrase: str) -> None:
        self.network_passphrase: str = network_passphrase

    def network_id(self) -> bytes:
        """Get the network ID of the network, which is an XDR hash of the
        passphrase.

        :returns: The network ID of the network.
        """
        return sha256(self.network_passphrase.encode())

    @classmethod
    def public_network(cls) -> "Network":
        """Get the :class:`Network` object representing the PUBLIC Network.

        :return: PUBLIC Network
        """
        return cls(cls.PUBLIC_NETWORK_PASSPHRASE)

    @classmethod
    def testnet_network(cls) -> "Network":
        """Get the :class:`Network` object representing the TESTNET Network.

        :return: TESTNET Network
        """
        return cls(cls.TESTNET_NETWORK_PASSPHRASE)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented  # pragma: no cover
        return self.network_passphrase == other.network_passphrase

    def __str__(self):
        return "<Network [network_passphrase={network_passphrase}]>".format(
            network_passphrase=self.network_passphrase
        )
