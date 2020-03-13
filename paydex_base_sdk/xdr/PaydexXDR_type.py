import base64

from . import PaydexXDR_const as const
from . import PaydexXDR_pack as pack
class PublicKey:
    # XDR definition:
    # union PublicKey switch(PublicKeyType type) {
    #     case PUBLIC_KEY_TYPE_ED25519:
    #         uint256 ed25519;
    # };
    def __init__(self, type=None, ed25519=None):
        self.type = type
        self.ed25519 = ed25519

    switch = property(lambda s: {const.PUBLIC_KEY_TYPE_ED25519:s.ed25519,}[s.type])

    def to_xdr(self):
        publickey = pack.PaydexXDRPacker()
        publickey.pack_PublicKey(self)
        return base64.b64encode(publickey.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_PublicKey()

    def __getattr__(self, attr):
        if attr is '__setstate__':
            raise AttributeError
        return getattr(self.switch, attr)

    def __repr__(self):
        out = []
        if self.type is not None:
            out += ['type=%s' % const.PublicKeyType.get(self.type, self.type)]
        if self.ed25519 is not None:
            out += ['ed25519=%s' % repr(self.ed25519)]
        return 'PublicKey(%s)' % ', '.join(out)
    __str__ = __repr__

class SignerKey:
    # XDR definition:
    # union SignerKey switch(SignerKeyType type) {
    #     case SIGNER_KEY_TYPE_ED25519:
    #         uint256 ed25519;
    #     case SIGNER_KEY_TYPE_PRE_AUTH_TX:
    #         uint256 preAuthTx;
    #     case SIGNER_KEY_TYPE_HASH_X:
    #         uint256 hashX;
    # };
    def __init__(self, type=None, ed25519=None, preAuthTx=None, hashX=None):
        self.type = type
        self.ed25519 = ed25519
        self.preAuthTx = preAuthTx
        self.hashX = hashX

    switch = property(lambda s: {const.SIGNER_KEY_TYPE_ED25519:s.ed25519,const.SIGNER_KEY_TYPE_PRE_AUTH_TX:s.preAuthTx,const.SIGNER_KEY_TYPE_HASH_X:s.hashX,}[s.type])

    def to_xdr(self):
        signerkey = pack.PaydexXDRPacker()
        signerkey.pack_SignerKey(self)
        return base64.b64encode(signerkey.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_SignerKey()

    def __getattr__(self, attr):
        if attr is '__setstate__':
            raise AttributeError
        return getattr(self.switch, attr)

    def __repr__(self):
        out = []
        if self.type is not None:
            out += ['type=%s' % const.SignerKeyType.get(self.type, self.type)]
        if self.ed25519 is not None:
            out += ['ed25519=%s' % repr(self.ed25519)]
        if self.preAuthTx is not None:
            out += ['preAuthTx=%s' % repr(self.preAuthTx)]
        if self.hashX is not None:
            out += ['hashX=%s' % repr(self.hashX)]
        return 'SignerKey(%s)' % ', '.join(out)
    __str__ = __repr__

NodeID = PublicKey
class Curve25519Secret:
    # XDR definition:
    # struct Curve25519Secret {
    #     opaque key[32];
    # };
    def __init__(self, key=None):
        self.key = key

    def to_xdr(self):
        curve25519secret = pack.PaydexXDRPacker()
        curve25519secret.pack_Curve25519Secret(self)
        return base64.b64encode(curve25519secret.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_Curve25519Secret()

    def __repr__(self):
        out = []
        if self.key is not None:
            out += ['key=%s' % repr(self.key)]
        return 'Curve25519Secret(%s)' % ', '.join(out)
    __str__ = __repr__

class Curve25519Public:
    # XDR definition:
    # struct Curve25519Public {
    #     opaque key[32];
    # };
    def __init__(self, key=None):
        self.key = key

    def to_xdr(self):
        curve25519public = pack.PaydexXDRPacker()
        curve25519public.pack_Curve25519Public(self)
        return base64.b64encode(curve25519public.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_Curve25519Public()

    def __repr__(self):
        out = []
        if self.key is not None:
            out += ['key=%s' % repr(self.key)]
        return 'Curve25519Public(%s)' % ', '.join(out)
    __str__ = __repr__

class HmacSha256Key:
    # XDR definition:
    # struct HmacSha256Key {
    #     opaque key[32];
    # };
    def __init__(self, key=None):
        self.key = key

    def to_xdr(self):
        hmacsha256key = pack.PaydexXDRPacker()
        hmacsha256key.pack_HmacSha256Key(self)
        return base64.b64encode(hmacsha256key.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_HmacSha256Key()

    def __repr__(self):
        out = []
        if self.key is not None:
            out += ['key=%s' % repr(self.key)]
        return 'HmacSha256Key(%s)' % ', '.join(out)
    __str__ = __repr__

class HmacSha256Mac:
    # XDR definition:
    # struct HmacSha256Mac {
    #     opaque mac[32];
    # };
    def __init__(self, mac=None):
        self.mac = mac

    def to_xdr(self):
        hmacsha256mac = pack.PaydexXDRPacker()
        hmacsha256mac.pack_HmacSha256Mac(self)
        return base64.b64encode(hmacsha256mac.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_HmacSha256Mac()

    def __repr__(self):
        out = []
        if self.mac is not None:
            out += ['mac=%s' % repr(self.mac)]
        return 'HmacSha256Mac(%s)' % ', '.join(out)
    __str__ = __repr__

class SCPBallot:
    # XDR definition:
    # struct SCPBallot {
    #     uint32 counter;
    #     Value value;
    # };
    def __init__(self, counter=None, value=None):
        self.counter = counter
        self.value = value

    def to_xdr(self):
        scpballot = pack.PaydexXDRPacker()
        scpballot.pack_SCPBallot(self)
        return base64.b64encode(scpballot.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_SCPBallot()

    def __repr__(self):
        out = []
        if self.counter is not None:
            out += ['counter=%s' % repr(self.counter)]
        if self.value is not None:
            out += ['value=%s' % repr(self.value)]
        return 'SCPBallot(%s)' % ', '.join(out)
    __str__ = __repr__

class SCPNomination:
    # XDR definition:
    # struct SCPNomination {
    #     Hash quorumSetHash;
    #     Value votes<>;
    #     Value accepted<>;
    # };
    def __init__(self, quorumSetHash=None, votes=None, accepted=None):
        self.quorumSetHash = quorumSetHash
        self.votes = votes
        self.accepted = accepted

    def to_xdr(self):
        scpnomination = pack.PaydexXDRPacker()
        scpnomination.pack_SCPNomination(self)
        return base64.b64encode(scpnomination.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_SCPNomination()

    def __repr__(self):
        out = []
        if self.quorumSetHash is not None:
            out += ['quorumSetHash=%s' % repr(self.quorumSetHash)]
        if self.votes is not None:
            out += ['votes=%s' % repr(self.votes)]
        if self.accepted is not None:
            out += ['accepted=%s' % repr(self.accepted)]
        return 'SCPNomination(%s)' % ', '.join(out)
    __str__ = __repr__

class SCPStatement:
    # XDR definition:
    # struct SCPStatement {
    #     NodeID nodeID;
    #     uint64 slotIndex;
    #     union switch(SCPStatementType type) {
    #         case SCP_ST_PREPARE:
    #             struct {
    #                 Hash quorumSetHash;
    #                 SCPBallot ballot;
    #                 SCPBallot prepared<1>;
    #                 SCPBallot preparedPrime<1>;
    #                 uint32 nC;
    #                 uint32 nH;
    #             } prepare;
    #         case SCP_ST_CONFIRM:
    #             struct {
    #                 SCPBallot ballot;
    #                 uint32 nPrepared;
    #                 uint32 nCommit;
    #                 uint32 nH;
    #                 Hash quorumSetHash;
    #             } confirm;
    #         case SCP_ST_EXTERNALIZE:
    #             struct {
    #                 SCPBallot commit;
    #                 uint32 nH;
    #                 Hash commitQuorumSetHash;
    #             } externalize;
    #         case SCP_ST_NOMINATE:
    #             SCPNomination nominate;
    #     } pledges;
    # };
    def __init__(self, nodeID=None, slotIndex=None, pledges=None):
        self.nodeID = nodeID
        self.slotIndex = slotIndex
        self.pledges = pledges

    def to_xdr(self):
        scpstatement = pack.PaydexXDRPacker()
        scpstatement.pack_SCPStatement(self)
        return base64.b64encode(scpstatement.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_SCPStatement()

    def __repr__(self):
        out = []
        if self.nodeID is not None:
            out += ['nodeID=%s' % repr(self.nodeID)]
        if self.slotIndex is not None:
            out += ['slotIndex=%s' % repr(self.slotIndex)]
        if self.pledges is not None:
            out += ['pledges=%s' % repr(self.pledges)]
        return 'SCPStatement(%s)' % ', '.join(out)
    __str__ = __repr__

class SCPEnvelope:
    # XDR definition:
    # struct SCPEnvelope {
    #     SCPStatement statement;
    #     Signature signature;
    # };
    def __init__(self, statement=None, signature=None):
        self.statement = statement
        self.signature = signature

    def __getattr__(self, attr):
        if attr is '__setstate__':
            raise AttributeError
        return getattr(self.statement, attr)

    def to_xdr(self):
        scpenvelope = pack.PaydexXDRPacker()
        scpenvelope.pack_SCPEnvelope(self)
        return base64.b64encode(scpenvelope.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_SCPEnvelope()

    def __repr__(self):
        out = []
        if self.statement is not None:
            out += ['statement=%s' % repr(self.statement)]
        if self.signature is not None:
            out += ['signature=%s' % repr(self.signature)]
        return 'SCPEnvelope(%s)' % ', '.join(out)
    __str__ = __repr__

class SCPQuorumSet:
    # XDR definition:
    # struct SCPQuorumSet {
    #     uint32 threshold;
    #     PublicKey validators<>;
    #     SCPQuorumSet innerSets<>;
    # };
    def __init__(self, threshold=None, validators=None, innerSets=None):
        self.threshold = threshold
        self.validators = validators
        self.innerSets = innerSets

    def to_xdr(self):
        scpquorumset = pack.PaydexXDRPacker()
        scpquorumset.pack_SCPQuorumSet(self)
        return base64.b64encode(scpquorumset.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_SCPQuorumSet()

    def __repr__(self):
        out = []
        if self.threshold is not None:
            out += ['threshold=%s' % repr(self.threshold)]
        if self.validators is not None:
            out += ['validators=%s' % repr(self.validators)]
        if self.innerSets is not None:
            out += ['innerSets=%s' % repr(self.innerSets)]
        return 'SCPQuorumSet(%s)' % ', '.join(out)
    __str__ = __repr__

class LedgerCloseValueSignature:
    # XDR definition:
    # struct LedgerCloseValueSignature {
    #     NodeID nodeID;
    #     Signature signature;
    # };
    def __init__(self, nodeID=None, signature=None):
        self.nodeID = nodeID
        self.signature = signature

    def __getattr__(self, attr):
        if attr is '__setstate__':
            raise AttributeError
        return getattr(self.nodeID, attr)

    def to_xdr(self):
        ledgerclosevaluesignature = pack.PaydexXDRPacker()
        ledgerclosevaluesignature.pack_LedgerCloseValueSignature(self)
        return base64.b64encode(ledgerclosevaluesignature.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_LedgerCloseValueSignature()

    def __repr__(self):
        out = []
        if self.nodeID is not None:
            out += ['nodeID=%s' % repr(self.nodeID)]
        if self.signature is not None:
            out += ['signature=%s' % repr(self.signature)]
        return 'LedgerCloseValueSignature(%s)' % ', '.join(out)
    __str__ = __repr__

class PaydexValue:
    # XDR definition:
    # struct PaydexValue {
    #     Hash txSetHash;
    #     TimePoint closeTime;
    #     UpgradeType upgrades<6>;
    #     union switch(PaydexValueType v) {
    #         case PAYDEX_VALUE_BASIC:
    #             void;
    #         case PAYDEX_VALUE_SIGNED:
    #             LedgerCloseValueSignature lcValueSignature;
    #     } ext;
    # };
    def __init__(self, txSetHash=None, closeTime=None, upgrades=None, ext=None):
        self.txSetHash = txSetHash
        self.closeTime = closeTime
        self.upgrades = upgrades
        self.ext = ext

    def __getattr__(self, attr):
        if attr is '__setstate__':
            raise AttributeError
        return getattr(self.ext, attr)

    def to_xdr(self):
        paydexvalue = pack.PaydexXDRPacker()
        paydexvalue.pack_PaydexValue(self)
        return base64.b64encode(paydexvalue.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_PaydexValue()

    def __repr__(self):
        out = []
        if self.txSetHash is not None:
            out += ['txSetHash=%s' % repr(self.txSetHash)]
        if self.closeTime is not None:
            out += ['closeTime=%s' % repr(self.closeTime)]
        if self.upgrades is not None:
            out += ['upgrades=%s' % repr(self.upgrades)]
        if self.ext is not None:
            out += ['ext=%s' % repr(self.ext)]
        return 'PaydexValue(%s)' % ', '.join(out)
    __str__ = __repr__

class LedgerHeader:
    # XDR definition:
    # struct LedgerHeader {
    #     uint32 ledgerVersion;
    #     Hash previousLedgerHash;
    #     PaydexValue scpValue;
    #     Hash txSetResultHash;
    #     Hash bucketListHash;
    #     uint32 ledgerSeq;
    #     int64 totalCoins;
    #     int64 feePool;
    #     uint32 inflationSeq;
    #     uint64 idPool;
    #     uint32 baseFee;
    #     uint32 baseReserve;
    #     uint32 maxTxSetSize;
    #     Hash skipList[4];
    #     union switch(int v) {
    #         case 0:
    #             void;
    #     } ext;
    # };
    def __init__(self, ledgerVersion=None, previousLedgerHash=None, scpValue=None, txSetResultHash=None, bucketListHash=None, ledgerSeq=None, totalCoins=None, feePool=None, inflationSeq=None, idPool=None, baseFee=None, baseReserve=None, maxTxSetSize=None, skipList=None, ext=None):
        self.ledgerVersion = ledgerVersion
        self.previousLedgerHash = previousLedgerHash
        self.scpValue = scpValue
        self.txSetResultHash = txSetResultHash
        self.bucketListHash = bucketListHash
        self.ledgerSeq = ledgerSeq
        self.totalCoins = totalCoins
        self.feePool = feePool
        self.inflationSeq = inflationSeq
        self.idPool = idPool
        self.baseFee = baseFee
        self.baseReserve = baseReserve
        self.maxTxSetSize = maxTxSetSize
        self.skipList = skipList
        self.ext = ext

    def to_xdr(self):
        ledgerheader = pack.PaydexXDRPacker()
        ledgerheader.pack_LedgerHeader(self)
        return base64.b64encode(ledgerheader.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_LedgerHeader()

    def __repr__(self):
        out = []
        if self.ledgerVersion is not None:
            out += ['ledgerVersion=%s' % repr(self.ledgerVersion)]
        if self.previousLedgerHash is not None:
            out += ['previousLedgerHash=%s' % repr(self.previousLedgerHash)]
        if self.scpValue is not None:
            out += ['scpValue=%s' % repr(self.scpValue)]
        if self.txSetResultHash is not None:
            out += ['txSetResultHash=%s' % repr(self.txSetResultHash)]
        if self.bucketListHash is not None:
            out += ['bucketListHash=%s' % repr(self.bucketListHash)]
        if self.ledgerSeq is not None:
            out += ['ledgerSeq=%s' % repr(self.ledgerSeq)]
        if self.totalCoins is not None:
            out += ['totalCoins=%s' % repr(self.totalCoins)]
        if self.feePool is not None:
            out += ['feePool=%s' % repr(self.feePool)]
        if self.inflationSeq is not None:
            out += ['inflationSeq=%s' % repr(self.inflationSeq)]
        if self.idPool is not None:
            out += ['idPool=%s' % repr(self.idPool)]
        if self.baseFee is not None:
            out += ['baseFee=%s' % repr(self.baseFee)]
        if self.baseReserve is not None:
            out += ['baseReserve=%s' % repr(self.baseReserve)]
        if self.maxTxSetSize is not None:
            out += ['maxTxSetSize=%s' % repr(self.maxTxSetSize)]
        if self.skipList is not None:
            out += ['skipList=%s' % repr(self.skipList)]
        if self.ext is not None:
            out += ['ext=%s' % repr(self.ext)]
        return 'LedgerHeader(%s)' % ', '.join(out)
    __str__ = __repr__

class LedgerUpgrade:
    # XDR definition:
    # union LedgerUpgrade switch(LedgerUpgradeType type) {
    #     case LEDGER_UPGRADE_VERSION:
    #         uint32 newLedgerVersion;
    #     case LEDGER_UPGRADE_BASE_FEE:
    #         uint32 newBaseFee;
    #     case LEDGER_UPGRADE_MAX_TX_SET_SIZE:
    #         uint32 newMaxTxSetSize;
    #     case LEDGER_UPGRADE_BASE_RESERVE:
    #         uint32 newBaseReserve;
    # };
    def __init__(self, type=None, newLedgerVersion=None, newBaseFee=None, newMaxTxSetSize=None, newBaseReserve=None):
        self.type = type
        self.newLedgerVersion = newLedgerVersion
        self.newBaseFee = newBaseFee
        self.newMaxTxSetSize = newMaxTxSetSize
        self.newBaseReserve = newBaseReserve

    switch = property(lambda s: {const.LEDGER_UPGRADE_VERSION:s.newLedgerVersion,const.LEDGER_UPGRADE_BASE_FEE:s.newBaseFee,const.LEDGER_UPGRADE_MAX_TX_SET_SIZE:s.newMaxTxSetSize,const.LEDGER_UPGRADE_BASE_RESERVE:s.newBaseReserve,}[s.type])

    def to_xdr(self):
        ledgerupgrade = pack.PaydexXDRPacker()
        ledgerupgrade.pack_LedgerUpgrade(self)
        return base64.b64encode(ledgerupgrade.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_LedgerUpgrade()

    def __getattr__(self, attr):
        if attr is '__setstate__':
            raise AttributeError
        return getattr(self.switch, attr)

    def __repr__(self):
        out = []
        if self.type is not None:
            out += ['type=%s' % const.LedgerUpgradeType.get(self.type, self.type)]
        if self.newLedgerVersion is not None:
            out += ['newLedgerVersion=%s' % repr(self.newLedgerVersion)]
        if self.newBaseFee is not None:
            out += ['newBaseFee=%s' % repr(self.newBaseFee)]
        if self.newMaxTxSetSize is not None:
            out += ['newMaxTxSetSize=%s' % repr(self.newMaxTxSetSize)]
        if self.newBaseReserve is not None:
            out += ['newBaseReserve=%s' % repr(self.newBaseReserve)]
        return 'LedgerUpgrade(%s)' % ', '.join(out)
    __str__ = __repr__

class LedgerKey:
    # XDR definition:
    # union LedgerKey switch(LedgerEntryType type) {
    #     case ACCOUNT:
    #         struct {
    #             AccountID accountID;
    #         } account;
    #     case TRUSTLINE:
    #         struct {
    #             AccountID accountID;
    #             Asset asset;
    #         } trustLine;
    #     case OFFER:
    #         struct {
    #             AccountID sellerID;
    #             int64 offerID;
    #         } offer;
    #     case DATA:
    #         struct {
    #             AccountID accountID;
    #             string64 dataName;
    #         } data;
    # };
    def __init__(self, type=None, account=None, trustLine=None, offer=None, data=None):
        self.type = type
        self.account = account
        self.trustLine = trustLine
        self.offer = offer
        self.data = data

    switch = property(lambda s: {const.ACCOUNT:s.account,const.TRUSTLINE:s.trustLine,const.OFFER:s.offer,const.DATA:s.data,}[s.type])

    def to_xdr(self):
        ledgerkey = pack.PaydexXDRPacker()
        ledgerkey.pack_LedgerKey(self)
        return base64.b64encode(ledgerkey.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_LedgerKey()

    def __getattr__(self, attr):
        if attr is '__setstate__':
            raise AttributeError
        return getattr(self.switch, attr)

    def __repr__(self):
        out = []
        if self.type is not None:
            out += ['type=%s' % const.LedgerEntryType.get(self.type, self.type)]
        if self.account is not None:
            out += ['account=%s' % repr(self.account)]
        if self.trustLine is not None:
            out += ['trustLine=%s' % repr(self.trustLine)]
        if self.offer is not None:
            out += ['offer=%s' % repr(self.offer)]
        if self.data is not None:
            out += ['data=%s' % repr(self.data)]
        return 'LedgerKey(%s)' % ', '.join(out)
    __str__ = __repr__

class BucketMetadata:
    # XDR definition:
    # struct BucketMetadata {
    #     uint32 ledgerVersion;
    #     union switch(int v) {
    #         case 0:
    #             void;
    #     } ext;
    # };
    def __init__(self, ledgerVersion=None, ext=None):
        self.ledgerVersion = ledgerVersion
        self.ext = ext

    def __getattr__(self, attr):
        if attr is '__setstate__':
            raise AttributeError
        return getattr(self.ext, attr)

    def to_xdr(self):
        bucketmetadata = pack.PaydexXDRPacker()
        bucketmetadata.pack_BucketMetadata(self)
        return base64.b64encode(bucketmetadata.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_BucketMetadata()

    def __repr__(self):
        out = []
        if self.ledgerVersion is not None:
            out += ['ledgerVersion=%s' % repr(self.ledgerVersion)]
        if self.ext is not None:
            out += ['ext=%s' % repr(self.ext)]
        return 'BucketMetadata(%s)' % ', '.join(out)
    __str__ = __repr__

class BucketEntry:
    # XDR definition:
    # union BucketEntry switch(BucketEntryType type) {
    #     case LIVEENTRY:
    #     case INITENTRY:
    #         LedgerEntry liveEntry;
    #     case DEADENTRY:
    #         LedgerKey deadEntry;
    #     case METAENTRY:
    #         BucketMetadata metaEntry;
    # };
    def __init__(self, type=None, liveEntry=None, deadEntry=None, metaEntry=None):
        self.type = type
        self.liveEntry = liveEntry
        self.deadEntry = deadEntry
        self.metaEntry = metaEntry

    switch = property(lambda s: {const.LIVEENTRY:s.liveEntry,const.INITENTRY:s.liveEntry,const.DEADENTRY:s.deadEntry,const.METAENTRY:s.metaEntry,}[s.type])

    def to_xdr(self):
        bucketentry = pack.PaydexXDRPacker()
        bucketentry.pack_BucketEntry(self)
        return base64.b64encode(bucketentry.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_BucketEntry()

    def __getattr__(self, attr):
        if attr is '__setstate__':
            raise AttributeError
        return getattr(self.switch, attr)

    def __repr__(self):
        out = []
        if self.type is not None:
            out += ['type=%s' % const.BucketEntryType.get(self.type, self.type)]
        if self.liveEntry is not None:
            out += ['liveEntry=%s' % repr(self.liveEntry)]
        if self.deadEntry is not None:
            out += ['deadEntry=%s' % repr(self.deadEntry)]
        if self.metaEntry is not None:
            out += ['metaEntry=%s' % repr(self.metaEntry)]
        return 'BucketEntry(%s)' % ', '.join(out)
    __str__ = __repr__

class TransactionSet:
    # XDR definition:
    # struct TransactionSet {
    #     Hash previousLedgerHash;
    #     TransactionEnvelope txs<>;
    # };
    def __init__(self, previousLedgerHash=None, txs=None):
        self.previousLedgerHash = previousLedgerHash
        self.txs = txs

    def to_xdr(self):
        transactionset = pack.PaydexXDRPacker()
        transactionset.pack_TransactionSet(self)
        return base64.b64encode(transactionset.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_TransactionSet()

    def __repr__(self):
        out = []
        if self.previousLedgerHash is not None:
            out += ['previousLedgerHash=%s' % repr(self.previousLedgerHash)]
        if self.txs is not None:
            out += ['txs=%s' % repr(self.txs)]
        return 'TransactionSet(%s)' % ', '.join(out)
    __str__ = __repr__

class TransactionResultPair:
    # XDR definition:
    # struct TransactionResultPair {
    #     Hash transactionHash;
    #     TransactionResult result;
    # };
    def __init__(self, transactionHash=None, result=None):
        self.transactionHash = transactionHash
        self.result = result

    def __getattr__(self, attr):
        if attr is '__setstate__':
            raise AttributeError
        return getattr(self.result, attr)

    def to_xdr(self):
        transactionresultpair = pack.PaydexXDRPacker()
        transactionresultpair.pack_TransactionResultPair(self)
        return base64.b64encode(transactionresultpair.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_TransactionResultPair()

    def __repr__(self):
        out = []
        if self.transactionHash is not None:
            out += ['transactionHash=%s' % repr(self.transactionHash)]
        if self.result is not None:
            out += ['result=%s' % repr(self.result)]
        return 'TransactionResultPair(%s)' % ', '.join(out)
    __str__ = __repr__

class TransactionResultSet:
    # XDR definition:
    # struct TransactionResultSet {
    #     TransactionResultPair results<>;
    # };
    def __init__(self, results=None):
        self.results = results

    def to_xdr(self):
        transactionresultset = pack.PaydexXDRPacker()
        transactionresultset.pack_TransactionResultSet(self)
        return base64.b64encode(transactionresultset.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_TransactionResultSet()

    def __repr__(self):
        out = []
        if self.results is not None:
            out += ['results=%s' % repr(self.results)]
        return 'TransactionResultSet(%s)' % ', '.join(out)
    __str__ = __repr__

class TransactionHistoryEntry:
    # XDR definition:
    # struct TransactionHistoryEntry {
    #     uint32 ledgerSeq;
    #     TransactionSet txSet;
    #     union switch(int v) {
    #         case 0:
    #             void;
    #     } ext;
    # };
    def __init__(self, ledgerSeq=None, txSet=None, ext=None):
        self.ledgerSeq = ledgerSeq
        self.txSet = txSet
        self.ext = ext

    def to_xdr(self):
        transactionhistoryentry = pack.PaydexXDRPacker()
        transactionhistoryentry.pack_TransactionHistoryEntry(self)
        return base64.b64encode(transactionhistoryentry.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_TransactionHistoryEntry()

    def __repr__(self):
        out = []
        if self.ledgerSeq is not None:
            out += ['ledgerSeq=%s' % repr(self.ledgerSeq)]
        if self.txSet is not None:
            out += ['txSet=%s' % repr(self.txSet)]
        if self.ext is not None:
            out += ['ext=%s' % repr(self.ext)]
        return 'TransactionHistoryEntry(%s)' % ', '.join(out)
    __str__ = __repr__

class TransactionHistoryResultEntry:
    # XDR definition:
    # struct TransactionHistoryResultEntry {
    #     uint32 ledgerSeq;
    #     TransactionResultSet txResultSet;
    #     union switch(int v) {
    #         case 0:
    #             void;
    #     } ext;
    # };
    def __init__(self, ledgerSeq=None, txResultSet=None, ext=None):
        self.ledgerSeq = ledgerSeq
        self.txResultSet = txResultSet
        self.ext = ext

    def to_xdr(self):
        transactionhistoryresultentry = pack.PaydexXDRPacker()
        transactionhistoryresultentry.pack_TransactionHistoryResultEntry(self)
        return base64.b64encode(transactionhistoryresultentry.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_TransactionHistoryResultEntry()

    def __repr__(self):
        out = []
        if self.ledgerSeq is not None:
            out += ['ledgerSeq=%s' % repr(self.ledgerSeq)]
        if self.txResultSet is not None:
            out += ['txResultSet=%s' % repr(self.txResultSet)]
        if self.ext is not None:
            out += ['ext=%s' % repr(self.ext)]
        return 'TransactionHistoryResultEntry(%s)' % ', '.join(out)
    __str__ = __repr__

class LedgerHeaderHistoryEntry:
    # XDR definition:
    # struct LedgerHeaderHistoryEntry {
    #     Hash hash;
    #     LedgerHeader header;
    #     union switch(int v) {
    #         case 0:
    #             void;
    #     } ext;
    # };
    def __init__(self, hash=None, header=None, ext=None):
        self.hash = hash
        self.header = header
        self.ext = ext

    def to_xdr(self):
        ledgerheaderhistoryentry = pack.PaydexXDRPacker()
        ledgerheaderhistoryentry.pack_LedgerHeaderHistoryEntry(self)
        return base64.b64encode(ledgerheaderhistoryentry.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_LedgerHeaderHistoryEntry()

    def __repr__(self):
        out = []
        if self.hash is not None:
            out += ['hash=%s' % repr(self.hash)]
        if self.header is not None:
            out += ['header=%s' % repr(self.header)]
        if self.ext is not None:
            out += ['ext=%s' % repr(self.ext)]
        return 'LedgerHeaderHistoryEntry(%s)' % ', '.join(out)
    __str__ = __repr__

class LedgerSCPMessages:
    # XDR definition:
    # struct LedgerSCPMessages {
    #     uint32 ledgerSeq;
    #     SCPEnvelope messages<>;
    # };
    def __init__(self, ledgerSeq=None, messages=None):
        self.ledgerSeq = ledgerSeq
        self.messages = messages

    def to_xdr(self):
        ledgerscpmessages = pack.PaydexXDRPacker()
        ledgerscpmessages.pack_LedgerSCPMessages(self)
        return base64.b64encode(ledgerscpmessages.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_LedgerSCPMessages()

    def __repr__(self):
        out = []
        if self.ledgerSeq is not None:
            out += ['ledgerSeq=%s' % repr(self.ledgerSeq)]
        if self.messages is not None:
            out += ['messages=%s' % repr(self.messages)]
        return 'LedgerSCPMessages(%s)' % ', '.join(out)
    __str__ = __repr__

class SCPHistoryEntryV0:
    # XDR definition:
    # struct SCPHistoryEntryV0 {
    #     SCPQuorumSet quorumSets<>;
    #     LedgerSCPMessages ledgerMessages;
    # };
    def __init__(self, quorumSets=None, ledgerMessages=None):
        self.quorumSets = quorumSets
        self.ledgerMessages = ledgerMessages

    def __getattr__(self, attr):
        if attr is '__setstate__':
            raise AttributeError
        return getattr(self.ledgerMessages, attr)

    def to_xdr(self):
        scphistoryentryv0 = pack.PaydexXDRPacker()
        scphistoryentryv0.pack_SCPHistoryEntryV0(self)
        return base64.b64encode(scphistoryentryv0.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_SCPHistoryEntryV0()

    def __repr__(self):
        out = []
        if self.quorumSets is not None:
            out += ['quorumSets=%s' % repr(self.quorumSets)]
        if self.ledgerMessages is not None:
            out += ['ledgerMessages=%s' % repr(self.ledgerMessages)]
        return 'SCPHistoryEntryV0(%s)' % ', '.join(out)
    __str__ = __repr__

class SCPHistoryEntry:
    # XDR definition:
    # union SCPHistoryEntry switch(int v) {
    #     case 0:
    #         SCPHistoryEntryV0 v0;
    # };
    def __init__(self, v=None, v0=None):
        self.v = v
        self.v0 = v0

    switch = property(lambda s: {0:s.v0,}[s.v])

    def to_xdr(self):
        scphistoryentry = pack.PaydexXDRPacker()
        scphistoryentry.pack_SCPHistoryEntry(self)
        return base64.b64encode(scphistoryentry.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_SCPHistoryEntry()

    def __getattr__(self, attr):
        if attr is '__setstate__':
            raise AttributeError
        return getattr(self.switch, attr)

    def __repr__(self):
        out = []
        if self.v is not None:
            out += ['v=%s' % repr(self.v)]
        if self.v0 is not None:
            out += ['v0=%s' % repr(self.v0)]
        return 'SCPHistoryEntry(%s)' % ', '.join(out)
    __str__ = __repr__

class LedgerEntryChange:
    # XDR definition:
    # union LedgerEntryChange switch(LedgerEntryChangeType type) {
    #     case LEDGER_ENTRY_CREATED:
    #         LedgerEntry created;
    #     case LEDGER_ENTRY_UPDATED:
    #         LedgerEntry updated;
    #     case LEDGER_ENTRY_REMOVED:
    #         LedgerKey removed;
    #     case LEDGER_ENTRY_STATE:
    #         LedgerEntry state;
    # };
    def __init__(self, type=None, created=None, updated=None, removed=None, state=None):
        self.type = type
        self.created = created
        self.updated = updated
        self.removed = removed
        self.state = state

    switch = property(lambda s: {const.LEDGER_ENTRY_CREATED:s.created,const.LEDGER_ENTRY_UPDATED:s.updated,const.LEDGER_ENTRY_REMOVED:s.removed,const.LEDGER_ENTRY_STATE:s.state,}[s.type])

    def to_xdr(self):
        ledgerentrychange = pack.PaydexXDRPacker()
        ledgerentrychange.pack_LedgerEntryChange(self)
        return base64.b64encode(ledgerentrychange.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_LedgerEntryChange()

    def __getattr__(self, attr):
        if attr is '__setstate__':
            raise AttributeError
        return getattr(self.switch, attr)

    def __repr__(self):
        out = []
        if self.type is not None:
            out += ['type=%s' % const.LedgerEntryChangeType.get(self.type, self.type)]
        if self.created is not None:
            out += ['created=%s' % repr(self.created)]
        if self.updated is not None:
            out += ['updated=%s' % repr(self.updated)]
        if self.removed is not None:
            out += ['removed=%s' % repr(self.removed)]
        if self.state is not None:
            out += ['state=%s' % repr(self.state)]
        return 'LedgerEntryChange(%s)' % ', '.join(out)
    __str__ = __repr__

class OperationMeta:
    # XDR definition:
    # struct OperationMeta {
    #     LedgerEntryChanges changes;
    # };
    def __init__(self, changes=None):
        self.changes = changes

    def to_xdr(self):
        operationmeta = pack.PaydexXDRPacker()
        operationmeta.pack_OperationMeta(self)
        return base64.b64encode(operationmeta.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_OperationMeta()

    def __repr__(self):
        out = []
        if self.changes is not None:
            out += ['changes=%s' % repr(self.changes)]
        return 'OperationMeta(%s)' % ', '.join(out)
    __str__ = __repr__

class TransactionMetaV1:
    # XDR definition:
    # struct TransactionMetaV1 {
    #     LedgerEntryChanges txChanges;
    #     OperationMeta operations<>;
    # };
    def __init__(self, txChanges=None, operations=None):
        self.txChanges = txChanges
        self.operations = operations

    def to_xdr(self):
        transactionmetav1 = pack.PaydexXDRPacker()
        transactionmetav1.pack_TransactionMetaV1(self)
        return base64.b64encode(transactionmetav1.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_TransactionMetaV1()

    def __repr__(self):
        out = []
        if self.txChanges is not None:
            out += ['txChanges=%s' % repr(self.txChanges)]
        if self.operations is not None:
            out += ['operations=%s' % repr(self.operations)]
        return 'TransactionMetaV1(%s)' % ', '.join(out)
    __str__ = __repr__

class TransactionMetaV2:
    # XDR definition:
    # struct TransactionMetaV2 {
    #     LedgerEntryChanges txChangesBefore;
    #     OperationMeta operations<>;
    #     LedgerEntryChanges txChangesAfter;
    # };
    def __init__(self, txChangesBefore=None, operations=None, txChangesAfter=None):
        self.txChangesBefore = txChangesBefore
        self.operations = operations
        self.txChangesAfter = txChangesAfter

    def to_xdr(self):
        transactionmetav2 = pack.PaydexXDRPacker()
        transactionmetav2.pack_TransactionMetaV2(self)
        return base64.b64encode(transactionmetav2.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_TransactionMetaV2()

    def __repr__(self):
        out = []
        if self.txChangesBefore is not None:
            out += ['txChangesBefore=%s' % repr(self.txChangesBefore)]
        if self.operations is not None:
            out += ['operations=%s' % repr(self.operations)]
        if self.txChangesAfter is not None:
            out += ['txChangesAfter=%s' % repr(self.txChangesAfter)]
        return 'TransactionMetaV2(%s)' % ', '.join(out)
    __str__ = __repr__

class TransactionMeta:
    # XDR definition:
    # union TransactionMeta switch(int v) {
    #     case 0:
    #         OperationMeta operations<>;
    #     case 1:
    #         TransactionMetaV1 v1;
    #     case 2:
    #         TransactionMetaV2 v2;
    # };
    def __init__(self, v=None, operations=None, v1=None, v2=None):
        self.v = v
        self.operations = operations
        self.v1 = v1
        self.v2 = v2

    switch = property(lambda s: {0:s.operations,1:s.v1,2:s.v2,}[s.v])

    def to_xdr(self):
        transactionmeta = pack.PaydexXDRPacker()
        transactionmeta.pack_TransactionMeta(self)
        return base64.b64encode(transactionmeta.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_TransactionMeta()

    def __getattr__(self, attr):
        if attr is '__setstate__':
            raise AttributeError
        return getattr(self.switch, attr)

    def __repr__(self):
        out = []
        if self.v is not None:
            out += ['v=%s' % repr(self.v)]
        if self.operations is not None:
            out += ['operations=%s' % repr(self.operations)]
        if self.v1 is not None:
            out += ['v1=%s' % repr(self.v1)]
        if self.v2 is not None:
            out += ['v2=%s' % repr(self.v2)]
        return 'TransactionMeta(%s)' % ', '.join(out)
    __str__ = __repr__

class TransactionResultMeta:
    # XDR definition:
    # struct TransactionResultMeta {
    #     TransactionResultPair result;
    #     LedgerEntryChanges feeProcessing;
    #     TransactionMeta txApplyProcessing;
    # };
    def __init__(self, result=None, feeProcessing=None, txApplyProcessing=None):
        self.result = result
        self.feeProcessing = feeProcessing
        self.txApplyProcessing = txApplyProcessing

    def to_xdr(self):
        transactionresultmeta = pack.PaydexXDRPacker()
        transactionresultmeta.pack_TransactionResultMeta(self)
        return base64.b64encode(transactionresultmeta.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_TransactionResultMeta()

    def __repr__(self):
        out = []
        if self.result is not None:
            out += ['result=%s' % repr(self.result)]
        if self.feeProcessing is not None:
            out += ['feeProcessing=%s' % repr(self.feeProcessing)]
        if self.txApplyProcessing is not None:
            out += ['txApplyProcessing=%s' % repr(self.txApplyProcessing)]
        return 'TransactionResultMeta(%s)' % ', '.join(out)
    __str__ = __repr__

class UpgradeEntryMeta:
    # XDR definition:
    # struct UpgradeEntryMeta {
    #     LedgerUpgrade upgrade;
    #     LedgerEntryChanges changes;
    # };
    def __init__(self, upgrade=None, changes=None):
        self.upgrade = upgrade
        self.changes = changes

    def __getattr__(self, attr):
        if attr is '__setstate__':
            raise AttributeError
        return getattr(self.upgrade, attr)

    def to_xdr(self):
        upgradeentrymeta = pack.PaydexXDRPacker()
        upgradeentrymeta.pack_UpgradeEntryMeta(self)
        return base64.b64encode(upgradeentrymeta.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_UpgradeEntryMeta()

    def __repr__(self):
        out = []
        if self.upgrade is not None:
            out += ['upgrade=%s' % repr(self.upgrade)]
        if self.changes is not None:
            out += ['changes=%s' % repr(self.changes)]
        return 'UpgradeEntryMeta(%s)' % ', '.join(out)
    __str__ = __repr__

class LedgerCloseMetaV0:
    # XDR definition:
    # struct LedgerCloseMetaV0 {
    #     LedgerHeaderHistoryEntry ledgerHeader;
    #     TransactionSet txSet;
    #     TransactionResultMeta txProcessing<>;
    #     UpgradeEntryMeta upgradesProcessing<>;
    #     SCPHistoryEntry scpInfo<>;
    # };
    def __init__(self, ledgerHeader=None, txSet=None, txProcessing=None, upgradesProcessing=None, scpInfo=None):
        self.ledgerHeader = ledgerHeader
        self.txSet = txSet
        self.txProcessing = txProcessing
        self.upgradesProcessing = upgradesProcessing
        self.scpInfo = scpInfo

    def to_xdr(self):
        ledgerclosemetav0 = pack.PaydexXDRPacker()
        ledgerclosemetav0.pack_LedgerCloseMetaV0(self)
        return base64.b64encode(ledgerclosemetav0.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_LedgerCloseMetaV0()

    def __repr__(self):
        out = []
        if self.ledgerHeader is not None:
            out += ['ledgerHeader=%s' % repr(self.ledgerHeader)]
        if self.txSet is not None:
            out += ['txSet=%s' % repr(self.txSet)]
        if self.txProcessing is not None:
            out += ['txProcessing=%s' % repr(self.txProcessing)]
        if self.upgradesProcessing is not None:
            out += ['upgradesProcessing=%s' % repr(self.upgradesProcessing)]
        if self.scpInfo is not None:
            out += ['scpInfo=%s' % repr(self.scpInfo)]
        return 'LedgerCloseMetaV0(%s)' % ', '.join(out)
    __str__ = __repr__

class LedgerCloseMeta:
    # XDR definition:
    # union LedgerCloseMeta switch(int v) {
    #     case 0:
    #         LedgerCloseMetaV0 v0;
    # };
    def __init__(self, v=None, v0=None):
        self.v = v
        self.v0 = v0

    switch = property(lambda s: {0:s.v0,}[s.v])

    def to_xdr(self):
        ledgerclosemeta = pack.PaydexXDRPacker()
        ledgerclosemeta.pack_LedgerCloseMeta(self)
        return base64.b64encode(ledgerclosemeta.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_LedgerCloseMeta()

    def __getattr__(self, attr):
        if attr is '__setstate__':
            raise AttributeError
        return getattr(self.switch, attr)

    def __repr__(self):
        out = []
        if self.v is not None:
            out += ['v=%s' % repr(self.v)]
        if self.v0 is not None:
            out += ['v0=%s' % repr(self.v0)]
        return 'LedgerCloseMeta(%s)' % ', '.join(out)
    __str__ = __repr__

AccountID = PublicKey
class Asset:
    # XDR definition:
    # union Asset switch(AssetType type) {
    #     case ASSET_TYPE_NATIVE:
    #         void;
    #     case ASSET_TYPE_CREDIT_ALPHANUM4:
    #         struct {
    #             AssetCode4 assetCode;
    #             AccountID issuer;
    #         } alphaNum4;
    #     case ASSET_TYPE_CREDIT_ALPHANUM12:
    #         struct {
    #             AssetCode12 assetCode;
    #             AccountID issuer;
    #         } alphaNum12;
    # };
    def __init__(self, type=None, alphaNum4=None, alphaNum12=None):
        self.type = type
        self.alphaNum4 = alphaNum4
        self.alphaNum12 = alphaNum12

    switch = property(lambda s: {const.ASSET_TYPE_NATIVE:None,const.ASSET_TYPE_CREDIT_ALPHANUM4:s.alphaNum4,const.ASSET_TYPE_CREDIT_ALPHANUM12:s.alphaNum12,}[s.type])

    def to_xdr(self):
        asset = pack.PaydexXDRPacker()
        asset.pack_Asset(self)
        return base64.b64encode(asset.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_Asset()

    def __getattr__(self, attr):
        if attr is '__setstate__':
            raise AttributeError
        return getattr(self.switch, attr)

    def __repr__(self):
        out = []
        if self.type is not None:
            out += ['type=%s' % const.AssetType.get(self.type, self.type)]
        if self.alphaNum4 is not None:
            out += ['alphaNum4=%s' % repr(self.alphaNum4)]
        if self.alphaNum12 is not None:
            out += ['alphaNum12=%s' % repr(self.alphaNum12)]
        return 'Asset(%s)' % ', '.join(out)
    __str__ = __repr__

class Price:
    # XDR definition:
    # struct Price {
    #     int32 n;
    #     int32 d;
    # };
    def __init__(self, n=None, d=None):
        self.n = n
        self.d = d

    def to_xdr(self):
        price = pack.PaydexrXDRPacker()
        price.pack_Price(self)
        return base64.b64encode(price.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_Price()

    def __repr__(self):
        out = []
        if self.n is not None:
            out += ['n=%s' % repr(self.n)]
        if self.d is not None:
            out += ['d=%s' % repr(self.d)]
        return 'Price(%s)' % ', '.join(out)
    __str__ = __repr__

class Liabilities:
    # XDR definition:
    # struct Liabilities {
    #     int64 buying;
    #     int64 selling;
    # };
    def __init__(self, buying=None, selling=None):
        self.buying = buying
        self.selling = selling

    def to_xdr(self):
        liabilities = pack.PaydexXDRPacker()
        liabilities.pack_Liabilities(self)
        return base64.b64encode(liabilities.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_Liabilities()

    def __repr__(self):
        out = []
        if self.buying is not None:
            out += ['buying=%s' % repr(self.buying)]
        if self.selling is not None:
            out += ['selling=%s' % repr(self.selling)]
        return 'Liabilities(%s)' % ', '.join(out)
    __str__ = __repr__

class Signer:
    # XDR definition:
    # struct Signer {
    #     SignerKey key;
    #     uint32 weight;
    # };
    def __init__(self, key=None, weight=None):
        self.key = key
        self.weight = weight

    def __getattr__(self, attr):
        if attr is '__setstate__':
            raise AttributeError
        return getattr(self.key, attr)

    def to_xdr(self):
        signer = pack.PaydexXDRPacker()
        signer.pack_Signer(self)
        return base64.b64encode(signer.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_Signer()

    def __repr__(self):
        out = []
        if self.key is not None:
            out += ['key=%s' % repr(self.key)]
        if self.weight is not None:
            out += ['weight=%s' % repr(self.weight)]
        return 'Signer(%s)' % ', '.join(out)
    __str__ = __repr__

class AccountEntry:
    # XDR definition:
    # struct AccountEntry {
    #     AccountID accountID;
    #     int64 balance;
    #     SequenceNumber seqNum;
    #     uint32 numSubEntries;
    #     AccountID inflationDest<1>;
    #     uint32 flags;
    #     string32 homeDomain;
    #     Thresholds thresholds;
    #     Signer signers<20>;
    #     union switch(int v) {
    #         case 0:
    #             void;
    #         case 1:
    #             struct {
    #                 Liabilities liabilities;
    #                 union switch(int v) {
    #                     case 0:
    #                         void;
    #                 } ext;
    #             } v1;
    #     } ext;
    # };
    def __init__(self, accountID=None, balance=None, seqNum=None, numSubEntries=None, inflationDest=None, flags=None, homeDomain=None, thresholds=None, signers=None, ext=None):
        self.accountID = accountID
        self.balance = balance
        self.seqNum = seqNum
        self.numSubEntries = numSubEntries
        self.inflationDest = inflationDest
        self.flags = flags
        self.homeDomain = homeDomain
        self.thresholds = thresholds
        self.signers = signers
        self.ext = ext

    def to_xdr(self):
        accountentry = pack.PaydexXDRPacker()
        accountentry.pack_AccountEntry(self)
        return base64.b64encode(accountentry.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_AccountEntry()

    def __repr__(self):
        out = []
        if self.accountID is not None:
            out += ['accountID=%s' % repr(self.accountID)]
        if self.balance is not None:
            out += ['balance=%s' % repr(self.balance)]
        if self.seqNum is not None:
            out += ['seqNum=%s' % repr(self.seqNum)]
        if self.numSubEntries is not None:
            out += ['numSubEntries=%s' % repr(self.numSubEntries)]
        if self.inflationDest is not None:
            out += ['inflationDest=%s' % repr(self.inflationDest)]
        if self.flags is not None:
            out += ['flags=%s' % repr(self.flags)]
        if self.homeDomain is not None:
            out += ['homeDomain=%s' % repr(self.homeDomain)]
        if self.thresholds is not None:
            out += ['thresholds=%s' % repr(self.thresholds)]
        if self.signers is not None:
            out += ['signers=%s' % repr(self.signers)]
        if self.ext is not None:
            out += ['ext=%s' % repr(self.ext)]
        return 'AccountEntry(%s)' % ', '.join(out)
    __str__ = __repr__

class TrustLineEntry:
    # XDR definition:
    # struct TrustLineEntry {
    #     AccountID accountID;
    #     Asset asset;
    #     int64 balance;
    #     int64 limit;
    #     uint32 flags;
    #     union switch(int v) {
    #         case 0:
    #             void;
    #         case 1:
    #             struct {
    #                 Liabilities liabilities;
    #                 union switch(int v) {
    #                     case 0:
    #                         void;
    #                 } ext;
    #             } v1;
    #     } ext;
    # };
    def __init__(self, accountID=None, asset=None, balance=None, limit=None, flags=None, ext=None):
        self.accountID = accountID
        self.asset = asset
        self.balance = balance
        self.limit = limit
        self.flags = flags
        self.ext = ext

    def to_xdr(self):
        trustlineentry = pack.PaydexXDRPacker()
        trustlineentry.pack_TrustLineEntry(self)
        return base64.b64encode(trustlineentry.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_TrustLineEntry()

    def __repr__(self):
        out = []
        if self.accountID is not None:
            out += ['accountID=%s' % repr(self.accountID)]
        if self.asset is not None:
            out += ['asset=%s' % repr(self.asset)]
        if self.balance is not None:
            out += ['balance=%s' % repr(self.balance)]
        if self.limit is not None:
            out += ['limit=%s' % repr(self.limit)]
        if self.flags is not None:
            out += ['flags=%s' % repr(self.flags)]
        if self.ext is not None:
            out += ['ext=%s' % repr(self.ext)]
        return 'TrustLineEntry(%s)' % ', '.join(out)
    __str__ = __repr__

class OfferEntry:
    # XDR definition:
    # struct OfferEntry {
    #     AccountID sellerID;
    #     int64 offerID;
    #     Asset selling;
    #     Asset buying;
    #     int64 amount;
    #     Price price;
    #     uint32 flags;
    #     union switch(int v) {
    #         case 0:
    #             void;
    #     } ext;
    # };
    def __init__(self, sellerID=None, offerID=None, selling=None, buying=None, amount=None, price=None, flags=None, ext=None):
        self.sellerID = sellerID
        self.offerID = offerID
        self.selling = selling
        self.buying = buying
        self.amount = amount
        self.price = price
        self.flags = flags
        self.ext = ext

    def to_xdr(self):
        offerentry = pack.PaydexXDRPacker()
        offerentry.pack_OfferEntry(self)
        return base64.b64encode(offerentry.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_OfferEntry()

    def __repr__(self):
        out = []
        if self.sellerID is not None:
            out += ['sellerID=%s' % repr(self.sellerID)]
        if self.offerID is not None:
            out += ['offerID=%s' % repr(self.offerID)]
        if self.selling is not None:
            out += ['selling=%s' % repr(self.selling)]
        if self.buying is not None:
            out += ['buying=%s' % repr(self.buying)]
        if self.amount is not None:
            out += ['amount=%s' % repr(self.amount)]
        if self.price is not None:
            out += ['price=%s' % repr(self.price)]
        if self.flags is not None:
            out += ['flags=%s' % repr(self.flags)]
        if self.ext is not None:
            out += ['ext=%s' % repr(self.ext)]
        return 'OfferEntry(%s)' % ', '.join(out)
    __str__ = __repr__

class DataEntry:
    # XDR definition:
    # struct DataEntry {
    #     AccountID accountID;
    #     string64 dataName;
    #     DataValue dataValue;
    #     union switch(int v) {
    #         case 0:
    #             void;
    #     } ext;
    # };
    def __init__(self, accountID=None, dataName=None, dataValue=None, ext=None):
        self.accountID = accountID
        self.dataName = dataName
        self.dataValue = dataValue
        self.ext = ext

    def to_xdr(self):
        dataentry = pack.PaydexXDRPacker()
        dataentry.pack_DataEntry(self)
        return base64.b64encode(dataentry.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_DataEntry()

    def __repr__(self):
        out = []
        if self.accountID is not None:
            out += ['accountID=%s' % repr(self.accountID)]
        if self.dataName is not None:
            out += ['dataName=%s' % repr(self.dataName)]
        if self.dataValue is not None:
            out += ['dataValue=%s' % repr(self.dataValue)]
        if self.ext is not None:
            out += ['ext=%s' % repr(self.ext)]
        return 'DataEntry(%s)' % ', '.join(out)
    __str__ = __repr__

class LedgerEntry:
    # XDR definition:
    # struct LedgerEntry {
    #     uint32 lastModifiedLedgerSeq;
    #     union switch(LedgerEntryType type) {
    #         case ACCOUNT:
    #             AccountEntry account;
    #         case TRUSTLINE:
    #             TrustLineEntry trustLine;
    #         case OFFER:
    #             OfferEntry offer;
    #         case DATA:
    #             DataEntry data;
    #     } data;
    #     union switch(int v) {
    #         case 0:
    #             void;
    #     } ext;
    # };
    def __init__(self, lastModifiedLedgerSeq=None, data=None, ext=None):
        self.lastModifiedLedgerSeq = lastModifiedLedgerSeq
        self.data = data
        self.ext = ext

    def to_xdr(self):
        ledgerentry = pack.PaydexXDRPacker()
        ledgerentry.pack_LedgerEntry(self)
        return base64.b64encode(ledgerentry.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_LedgerEntry()

    def __repr__(self):
        out = []
        if self.lastModifiedLedgerSeq is not None:
            out += ['lastModifiedLedgerSeq=%s' % repr(self.lastModifiedLedgerSeq)]
        if self.data is not None:
            out += ['data=%s' % repr(self.data)]
        if self.ext is not None:
            out += ['ext=%s' % repr(self.ext)]
        return 'LedgerEntry(%s)' % ', '.join(out)
    __str__ = __repr__

class DecoratedSignature:
    # XDR definition:
    # struct DecoratedSignature {
    #     SignatureHint hint;
    #     Signature signature;
    # };
    def __init__(self, hint=None, signature=None):
        self.hint = hint
        self.signature = signature

    def to_xdr(self):
        decoratedsignature = pack.PaydexXDRPacker()
        decoratedsignature.pack_DecoratedSignature(self)
        return base64.b64encode(decoratedsignature.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_DecoratedSignature()

    def __repr__(self):
        out = []
        if self.hint is not None:
            out += ['hint=%s' % repr(self.hint)]
        if self.signature is not None:
            out += ['signature=%s' % repr(self.signature)]
        return 'DecoratedSignature(%s)' % ', '.join(out)
    __str__ = __repr__

class CreateAccountOp:
    # XDR definition:
    # struct CreateAccountOp {
    #     AccountID destination;
    #     int64 startingBalance;
    # };
    def __init__(self, destination=None, startingBalance=None):
        self.destination = destination
        self.startingBalance = startingBalance

    def __getattr__(self, attr):
        if attr is '__setstate__':
            raise AttributeError
        return getattr(self.destination, attr)

    def to_xdr(self):
        createaccountop = pack.PaydexXDRPacker()
        createaccountop.pack_CreateAccountOp(self)
        return base64.b64encode(createaccountop.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_CreateAccountOp()

    def __repr__(self):
        out = []
        if self.destination is not None:
            out += ['destination=%s' % repr(self.destination)]
        if self.startingBalance is not None:
            out += ['startingBalance=%s' % repr(self.startingBalance)]
        return 'CreateAccountOp(%s)' % ', '.join(out)
    __str__ = __repr__

class PaymentOp:
    # XDR definition:
    # struct PaymentOp {
    #     AccountID destination;
    #     Asset asset;
    #     int64 amount;
    # };
    def __init__(self, destination=None, asset=None, amount=None):
        self.destination = destination
        self.asset = asset
        self.amount = amount

    def to_xdr(self):
        paymentop = pack.PaydexXDRPacker()
        paymentop.pack_PaymentOp(self)
        return base64.b64encode(paymentop.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_PaymentOp()

    def __repr__(self):
        out = []
        if self.destination is not None:
            out += ['destination=%s' % repr(self.destination)]
        if self.asset is not None:
            out += ['asset=%s' % repr(self.asset)]
        if self.amount is not None:
            out += ['amount=%s' % repr(self.amount)]
        return 'PaymentOp(%s)' % ', '.join(out)
    __str__ = __repr__

class PathPaymentStrictReceiveOp:
    # XDR definition:
    # struct PathPaymentStrictReceiveOp {
    #     Asset sendAsset;
    #     int64 sendMax;
    #     AccountID destination;
    #     Asset destAsset;
    #     int64 destAmount;
    #     Asset path<5>;
    # };
    def __init__(self, sendAsset=None, sendMax=None, destination=None, destAsset=None, destAmount=None, path=None):
        self.sendAsset = sendAsset
        self.sendMax = sendMax
        self.destination = destination
        self.destAsset = destAsset
        self.destAmount = destAmount
        self.path = path

    def to_xdr(self):
        pathpaymentstrictreceiveop = pack.PaydexXDRPacker()
        pathpaymentstrictreceiveop.pack_PathPaymentStrictReceiveOp(self)
        return base64.b64encode(pathpaymentstrictreceiveop.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_PathPaymentStrictReceiveOp()

    def __repr__(self):
        out = []
        if self.sendAsset is not None:
            out += ['sendAsset=%s' % repr(self.sendAsset)]
        if self.sendMax is not None:
            out += ['sendMax=%s' % repr(self.sendMax)]
        if self.destination is not None:
            out += ['destination=%s' % repr(self.destination)]
        if self.destAsset is not None:
            out += ['destAsset=%s' % repr(self.destAsset)]
        if self.destAmount is not None:
            out += ['destAmount=%s' % repr(self.destAmount)]
        if self.path is not None:
            out += ['path=%s' % repr(self.path)]
        return 'PathPaymentStrictReceiveOp(%s)' % ', '.join(out)
    __str__ = __repr__

class PathPaymentStrictSendOp:
    # XDR definition:
    # struct PathPaymentStrictSendOp {
    #     Asset sendAsset;
    #     int64 sendAmount;
    #     AccountID destination;
    #     Asset destAsset;
    #     int64 destMin;
    #     Asset path<5>;
    # };
    def __init__(self, sendAsset=None, sendAmount=None, destination=None, destAsset=None, destMin=None, path=None):
        self.sendAsset = sendAsset
        self.sendAmount = sendAmount
        self.destination = destination
        self.destAsset = destAsset
        self.destMin = destMin
        self.path = path

    def to_xdr(self):
        pathpaymentstrictsendop = pack.PaydexXDRPacker()
        pathpaymentstrictsendop.pack_PathPaymentStrictSendOp(self)
        return base64.b64encode(pathpaymentstrictsendop.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_PathPaymentStrictSendOp()

    def __repr__(self):
        out = []
        if self.sendAsset is not None:
            out += ['sendAsset=%s' % repr(self.sendAsset)]
        if self.sendAmount is not None:
            out += ['sendAmount=%s' % repr(self.sendAmount)]
        if self.destination is not None:
            out += ['destination=%s' % repr(self.destination)]
        if self.destAsset is not None:
            out += ['destAsset=%s' % repr(self.destAsset)]
        if self.destMin is not None:
            out += ['destMin=%s' % repr(self.destMin)]
        if self.path is not None:
            out += ['path=%s' % repr(self.path)]
        return 'PathPaymentStrictSendOp(%s)' % ', '.join(out)
    __str__ = __repr__

class ManageSellOfferOp:
    # XDR definition:
    # struct ManageSellOfferOp {
    #     Asset selling;
    #     Asset buying;
    #     int64 amount;
    #     Price price;
    #     int64 offerID;
    # };
    def __init__(self, selling=None, buying=None, amount=None, price=None, offerID=None):
        self.selling = selling
        self.buying = buying
        self.amount = amount
        self.price = price
        self.offerID = offerID

    def to_xdr(self):
        managesellofferop = pack.PaydexXDRPacker()
        managesellofferop.pack_ManageSellOfferOp(self)
        return base64.b64encode(managesellofferop.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_ManageSellOfferOp()

    def __repr__(self):
        out = []
        if self.selling is not None:
            out += ['selling=%s' % repr(self.selling)]
        if self.buying is not None:
            out += ['buying=%s' % repr(self.buying)]
        if self.amount is not None:
            out += ['amount=%s' % repr(self.amount)]
        if self.price is not None:
            out += ['price=%s' % repr(self.price)]
        if self.offerID is not None:
            out += ['offerID=%s' % repr(self.offerID)]
        return 'ManageSellOfferOp(%s)' % ', '.join(out)
    __str__ = __repr__

class ManageBuyOfferOp:
    # XDR definition:
    # struct ManageBuyOfferOp {
    #     Asset selling;
    #     Asset buying;
    #     int64 buyAmount;
    #     Price price;
    #     int64 offerID;
    # };
    def __init__(self, selling=None, buying=None, buyAmount=None, price=None, offerID=None):
        self.selling = selling
        self.buying = buying
        self.buyAmount = buyAmount
        self.price = price
        self.offerID = offerID

    def to_xdr(self):
        managebuyofferop = pack.PaydexXDRPacker()
        managebuyofferop.pack_ManageBuyOfferOp(self)
        return base64.b64encode(managebuyofferop.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_ManageBuyOfferOp()

    def __repr__(self):
        out = []
        if self.selling is not None:
            out += ['selling=%s' % repr(self.selling)]
        if self.buying is not None:
            out += ['buying=%s' % repr(self.buying)]
        if self.buyAmount is not None:
            out += ['buyAmount=%s' % repr(self.buyAmount)]
        if self.price is not None:
            out += ['price=%s' % repr(self.price)]
        if self.offerID is not None:
            out += ['offerID=%s' % repr(self.offerID)]
        return 'ManageBuyOfferOp(%s)' % ', '.join(out)
    __str__ = __repr__

class CreatePassiveSellOfferOp:
    # XDR definition:
    # struct CreatePassiveSellOfferOp {
    #     Asset selling;
    #     Asset buying;
    #     int64 amount;
    #     Price price;
    # };
    def __init__(self, selling=None, buying=None, amount=None, price=None):
        self.selling = selling
        self.buying = buying
        self.amount = amount
        self.price = price

    def to_xdr(self):
        createpassivesellofferop = pack.PaydexXDRPacker()
        createpassivesellofferop.pack_CreatePassiveSellOfferOp(self)
        return base64.b64encode(createpassivesellofferop.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_CreatePassiveSellOfferOp()

    def __repr__(self):
        out = []
        if self.selling is not None:
            out += ['selling=%s' % repr(self.selling)]
        if self.buying is not None:
            out += ['buying=%s' % repr(self.buying)]
        if self.amount is not None:
            out += ['amount=%s' % repr(self.amount)]
        if self.price is not None:
            out += ['price=%s' % repr(self.price)]
        return 'CreatePassiveSellOfferOp(%s)' % ', '.join(out)
    __str__ = __repr__

class SetOptionsOp:
    # XDR definition:
    # struct SetOptionsOp {
    #     AccountID inflationDest<1>;
    #     uint32 clearFlags<1>;
    #     uint32 setFlags<1>;
    #     uint32 masterWeight<1>;
    #     uint32 lowThreshold<1>;
    #     uint32 medThreshold<1>;
    #     uint32 highThreshold<1>;
    #     string32 homeDomain<1>;
    #     Signer signer<1>;
    # };
    def __init__(self, inflationDest=None, clearFlags=None, setFlags=None, masterWeight=None, lowThreshold=None, medThreshold=None, highThreshold=None, homeDomain=None, signer=None):
        self.inflationDest = inflationDest
        self.clearFlags = clearFlags
        self.setFlags = setFlags
        self.masterWeight = masterWeight
        self.lowThreshold = lowThreshold
        self.medThreshold = medThreshold
        self.highThreshold = highThreshold
        self.homeDomain = homeDomain
        self.signer = signer

    def to_xdr(self):
        setoptionsop = pack.PaydexXDRPacker()
        setoptionsop.pack_SetOptionsOp(self)
        return base64.b64encode(setoptionsop.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_SetOptionsOp()

    def __repr__(self):
        out = []
        if self.inflationDest is not None:
            out += ['inflationDest=%s' % repr(self.inflationDest)]
        if self.clearFlags is not None:
            out += ['clearFlags=%s' % repr(self.clearFlags)]
        if self.setFlags is not None:
            out += ['setFlags=%s' % repr(self.setFlags)]
        if self.masterWeight is not None:
            out += ['masterWeight=%s' % repr(self.masterWeight)]
        if self.lowThreshold is not None:
            out += ['lowThreshold=%s' % repr(self.lowThreshold)]
        if self.medThreshold is not None:
            out += ['medThreshold=%s' % repr(self.medThreshold)]
        if self.highThreshold is not None:
            out += ['highThreshold=%s' % repr(self.highThreshold)]
        if self.homeDomain is not None:
            out += ['homeDomain=%s' % repr(self.homeDomain)]
        if self.signer is not None:
            out += ['signer=%s' % repr(self.signer)]
        return 'SetOptionsOp(%s)' % ', '.join(out)
    __str__ = __repr__

class ChangeTrustOp:
    # XDR definition:
    # struct ChangeTrustOp {
    #     Asset line;
    #     int64 limit;
    # };
    def __init__(self, line=None, limit=None):
        self.line = line
        self.limit = limit

    def __getattr__(self, attr):
        if attr is '__setstate__':
            raise AttributeError
        return getattr(self.line, attr)

    def to_xdr(self):
        changetrustop = pack.PaydexXDRPacker()
        changetrustop.pack_ChangeTrustOp(self)
        return base64.b64encode(changetrustop.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_ChangeTrustOp()

    def __repr__(self):
        out = []
        if self.line is not None:
            out += ['line=%s' % repr(self.line)]
        if self.limit is not None:
            out += ['limit=%s' % repr(self.limit)]
        return 'ChangeTrustOp(%s)' % ', '.join(out)
    __str__ = __repr__

class AllowTrustOp:
    # XDR definition:
    # struct AllowTrustOp {
    #     AccountID trustor;
    #     union switch(AssetType type) {
    #         case ASSET_TYPE_CREDIT_ALPHANUM4:
    #             AssetCode4 assetCode4;
    #         case ASSET_TYPE_CREDIT_ALPHANUM12:
    #             AssetCode12 assetCode12;
    #     } asset;
    #     bool authorize;
    # };
    def __init__(self, trustor=None, asset=None, authorize=None):
        self.trustor = trustor
        self.asset = asset
        self.authorize = authorize

    def to_xdr(self):
        allowtrustop = pack.PaydexXDRPacker()
        allowtrustop.pack_AllowTrustOp(self)
        return base64.b64encode(allowtrustop.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_AllowTrustOp()

    def __repr__(self):
        out = []
        if self.trustor is not None:
            out += ['trustor=%s' % repr(self.trustor)]
        if self.asset is not None:
            out += ['asset=%s' % repr(self.asset)]
        if self.authorize is not None:
            out += ['authorize=%s' % repr(self.authorize)]
        return 'AllowTrustOp(%s)' % ', '.join(out)
    __str__ = __repr__

class ManageDataOp:
    # XDR definition:
    # struct ManageDataOp {
    #     string64 dataName;
    #     DataValue dataValue<1>;
    # };
    def __init__(self, dataName=None, dataValue=None):
        self.dataName = dataName
        self.dataValue = dataValue

    def to_xdr(self):
        managedataop = pack.PaydexXDRPacker()
        managedataop.pack_ManageDataOp(self)
        return base64.b64encode(managedataop.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_ManageDataOp()

    def __repr__(self):
        out = []
        if self.dataName is not None:
            out += ['dataName=%s' % repr(self.dataName)]
        if self.dataValue is not None:
            out += ['dataValue=%s' % repr(self.dataValue)]
        return 'ManageDataOp(%s)' % ', '.join(out)
    __str__ = __repr__

class BumpSequenceOp:
    # XDR definition:
    # struct BumpSequenceOp {
    #     SequenceNumber bumpTo;
    # };
    def __init__(self, bumpTo=None):
        self.bumpTo = bumpTo

    def to_xdr(self):
        bumpsequenceop = pack.PaydexXDRPacker()
        bumpsequenceop.pack_BumpSequenceOp(self)
        return base64.b64encode(bumpsequenceop.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_BumpSequenceOp()

    def __repr__(self):
        out = []
        if self.bumpTo is not None:
            out += ['bumpTo=%s' % repr(self.bumpTo)]
        return 'BumpSequenceOp(%s)' % ', '.join(out)
    __str__ = __repr__

class Operation:
    # XDR definition:
    # struct Operation {
    #     AccountID sourceAccount<1>;
    #     union switch(OperationType type) {
    #         case CREATE_ACCOUNT:
    #             CreateAccountOp createAccountOp;
    #         case PAYMENT:
    #             PaymentOp paymentOp;
    #         case PATH_PAYMENT_STRICT_RECEIVE:
    #             PathPaymentStrictReceiveOp pathPaymentStrictReceiveOp;
    #         case MANAGE_SELL_OFFER:
    #             ManageSellOfferOp manageSellOfferOp;
    #         case CREATE_PASSIVE_SELL_OFFER:
    #             CreatePassiveSellOfferOp createPassiveSellOfferOp;
    #         case SET_OPTIONS:
    #             SetOptionsOp setOptionsOp;
    #         case CHANGE_TRUST:
    #             ChangeTrustOp changeTrustOp;
    #         case ALLOW_TRUST:
    #             AllowTrustOp allowTrustOp;
    #         case ACCOUNT_MERGE:
    #             AccountID destination;
    #         case INFLATION:
    #             void;
    #         case MANAGE_DATA:
    #             ManageDataOp manageDataOp;
    #         case BUMP_SEQUENCE:
    #             BumpSequenceOp bumpSequenceOp;
    #         case MANAGE_BUY_OFFER:
    #             ManageBuyOfferOp manageBuyOfferOp;
    #         case PATH_PAYMENT_STRICT_SEND:
    #             PathPaymentStrictSendOp pathPaymentStrictSendOp;
    #     } body;
    # };
    def __init__(self, sourceAccount=None, body=None):
        self.sourceAccount = sourceAccount
        self.body = body

    def __getattr__(self, attr):
        if attr is '__setstate__':
            raise AttributeError
        return getattr(self.body, attr)

    def to_xdr(self):
        operation = pack.PaydexXDRPacker()
        operation.pack_Operation(self)
        return base64.b64encode(operation.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_Operation()

    def __repr__(self):
        out = []
        if self.sourceAccount is not None:
            out += ['sourceAccount=%s' % repr(self.sourceAccount)]
        if self.body is not None:
            out += ['body=%s' % repr(self.body)]
        return 'Operation(%s)' % ', '.join(out)
    __str__ = __repr__

class Memo:
    # XDR definition:
    # union Memo switch(MemoType type) {
    #     case MEMO_NONE:
    #         void;
    #     case MEMO_TEXT:
    #         string text<28>;
    #     case MEMO_ID:
    #         uint64 id;
    #     case MEMO_HASH:
    #         Hash hash;
    #     case MEMO_RETURN:
    #         Hash retHash;
    # };
    def __init__(self, type=None, text=None, id=None, hash=None, retHash=None):
        self.type = type
        self.text = text
        self.id = id
        self.hash = hash
        self.retHash = retHash

    switch = property(lambda s: {const.MEMO_NONE:None,const.MEMO_TEXT:s.text,const.MEMO_ID:s.id,const.MEMO_HASH:s.hash,const.MEMO_RETURN:s.retHash,}[s.type])

    def to_xdr(self):
        memo = pack.PaydexXDRPacker()
        memo.pack_Memo(self)
        return base64.b64encode(memo.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_Memo()

    def __getattr__(self, attr):
        if attr is '__setstate__':
            raise AttributeError
        return getattr(self.switch, attr)

    def __repr__(self):
        out = []
        if self.type is not None:
            out += ['type=%s' % const.MemoType.get(self.type, self.type)]
        if self.text is not None:
            out += ['text=%s' % repr(self.text)]
        if self.id is not None:
            out += ['id=%s' % repr(self.id)]
        if self.hash is not None:
            out += ['hash=%s' % repr(self.hash)]
        if self.retHash is not None:
            out += ['retHash=%s' % repr(self.retHash)]
        return 'Memo(%s)' % ', '.join(out)
    __str__ = __repr__

class TimeBounds:
    # XDR definition:
    # struct TimeBounds {
    #     TimePoint minTime;
    #     TimePoint maxTime;
    # };
    def __init__(self, minTime=None, maxTime=None):
        self.minTime = minTime
        self.maxTime = maxTime

    def to_xdr(self):
        timebounds = pack.PaydexXDRPacker()
        timebounds.pack_TimeBounds(self)
        return base64.b64encode(timebounds.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_TimeBounds()

    def __repr__(self):
        out = []
        if self.minTime is not None:
            out += ['minTime=%s' % repr(self.minTime)]
        if self.maxTime is not None:
            out += ['maxTime=%s' % repr(self.maxTime)]
        return 'TimeBounds(%s)' % ', '.join(out)
    __str__ = __repr__

class Transaction:
    # XDR definition:
    # struct Transaction {
    #     AccountID sourceAccount;
    #     uint32 fee;
    #     SequenceNumber seqNum;
    #     TimeBounds timeBounds<1>;
    #     Memo memo;
    #     Operation operations<MAX_OPS_PER_TX>;
    #     union switch(int v) {
    #         case 0:
    #             void;
    #     } ext;
    # };
    def __init__(self, sourceAccount=None, fee=None, seqNum=None, timeBounds=None, memo=None, operations=None, ext=None):
        self.sourceAccount = sourceAccount
        self.fee = fee
        self.seqNum = seqNum
        self.timeBounds = timeBounds
        self.memo = memo
        self.operations = operations
        self.ext = ext

    def to_xdr(self):
        transaction = pack.PaydexXDRPacker()
        transaction.pack_Transaction(self)
        return base64.b64encode(transaction.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_Transaction()

    def __repr__(self):
        out = []
        if self.sourceAccount is not None:
            out += ['sourceAccount=%s' % repr(self.sourceAccount)]
        if self.fee is not None:
            out += ['fee=%s' % repr(self.fee)]
        if self.seqNum is not None:
            out += ['seqNum=%s' % repr(self.seqNum)]
        if self.timeBounds is not None:
            out += ['timeBounds=%s' % repr(self.timeBounds)]
        if self.memo is not None:
            out += ['memo=%s' % repr(self.memo)]
        if self.operations is not None:
            out += ['operations=%s' % repr(self.operations)]
        if self.ext is not None:
            out += ['ext=%s' % repr(self.ext)]
        return 'Transaction(%s)' % ', '.join(out)
    __str__ = __repr__

class TransactionSignaturePayload:
    # XDR definition:
    # struct TransactionSignaturePayload {
    #     Hash networkId;
    #     union switch(EnvelopeType type) {
    #         case ENVELOPE_TYPE_TX:
    #             Transaction tx;
    #     } taggedTransaction;
    # };
    def __init__(self, networkId=None, taggedTransaction=None):
        self.networkId = networkId
        self.taggedTransaction = taggedTransaction

    def __getattr__(self, attr):
        if attr is '__setstate__':
            raise AttributeError
        return getattr(self.taggedTransaction, attr)

    def to_xdr(self):
        transactionsignaturepayload = pack.PaydexXDRPacker()
        transactionsignaturepayload.pack_TransactionSignaturePayload(self)
        return base64.b64encode(transactionsignaturepayload.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_TransactionSignaturePayload()

    def __repr__(self):
        out = []
        if self.networkId is not None:
            out += ['networkId=%s' % repr(self.networkId)]
        if self.taggedTransaction is not None:
            out += ['taggedTransaction=%s' % repr(self.taggedTransaction)]
        return 'TransactionSignaturePayload(%s)' % ', '.join(out)
    __str__ = __repr__

class TransactionEnvelope:
    # XDR definition:
    # struct TransactionEnvelope {
    #     Transaction tx;
    #     DecoratedSignature signatures<20>;
    # };
    def __init__(self, tx=None, signatures=None):
        self.tx = tx
        self.signatures = signatures

    def __getattr__(self, attr):
        if attr is '__setstate__':
            raise AttributeError
        return getattr(self.tx, attr)

    def to_xdr(self):
        transactionenvelope = pack.PaydexXDRPacker()
        transactionenvelope.pack_TransactionEnvelope(self)
        return base64.b64encode(transactionenvelope.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_TransactionEnvelope()

    def __repr__(self):
        out = []
        if self.tx is not None:
            out += ['tx=%s' % repr(self.tx)]
        if self.signatures is not None:
            out += ['signatures=%s' % repr(self.signatures)]
        return 'TransactionEnvelope(%s)' % ', '.join(out)
    __str__ = __repr__

class ClaimOfferAtom:
    # XDR definition:
    # struct ClaimOfferAtom {
    #     AccountID sellerID;
    #     int64 offerID;
    #     Asset assetSold;
    #     int64 amountSold;
    #     Asset assetBought;
    #     int64 amountBought;
    # };
    def __init__(self, sellerID=None, offerID=None, assetSold=None, amountSold=None, assetBought=None, amountBought=None):
        self.sellerID = sellerID
        self.offerID = offerID
        self.assetSold = assetSold
        self.amountSold = amountSold
        self.assetBought = assetBought
        self.amountBought = amountBought

    def to_xdr(self):
        claimofferatom = pack.PaydexXDRPacker()
        claimofferatom.pack_ClaimOfferAtom(self)
        return base64.b64encode(claimofferatom.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_ClaimOfferAtom()

    def __repr__(self):
        out = []
        if self.sellerID is not None:
            out += ['sellerID=%s' % repr(self.sellerID)]
        if self.offerID is not None:
            out += ['offerID=%s' % repr(self.offerID)]
        if self.assetSold is not None:
            out += ['assetSold=%s' % repr(self.assetSold)]
        if self.amountSold is not None:
            out += ['amountSold=%s' % repr(self.amountSold)]
        if self.assetBought is not None:
            out += ['assetBought=%s' % repr(self.assetBought)]
        if self.amountBought is not None:
            out += ['amountBought=%s' % repr(self.amountBought)]
        return 'ClaimOfferAtom(%s)' % ', '.join(out)
    __str__ = __repr__

class CreateAccountResult:
    # XDR definition:
    # union CreateAccountResult switch(CreateAccountResultCode code) {
    #     case CREATE_ACCOUNT_SUCCESS:
    #         void;
    #     default:
    #         void;
    # };
    def __init__(self, code=None):
        self.code = code

    switch = property(lambda s: {const.CREATE_ACCOUNT_SUCCESS:None,}.get(s.code, None))

    def to_xdr(self):
        createaccountresult = pack.PaydexXDRPacker()
        createaccountresult.pack_CreateAccountResult(self)
        return base64.b64encode(createaccountresult.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_CreateAccountResult()

    def __getattr__(self, attr):
        if attr is '__setstate__':
            raise AttributeError
        return getattr(self.switch, attr)

    def __repr__(self):
        out = []
        if self.code is not None:
            out += ['code=%s' % const.CreateAccountResultCode.get(self.code, self.code)]
        return 'CreateAccountResult(%s)' % ', '.join(out)
    __str__ = __repr__

class PaymentResult:
    # XDR definition:
    # union PaymentResult switch(PaymentResultCode code) {
    #     case PAYMENT_SUCCESS:
    #         void;
    #     default:
    #         void;
    # };
    def __init__(self, code=None):
        self.code = code

    switch = property(lambda s: {const.PAYMENT_SUCCESS:None,}.get(s.code, None))

    def to_xdr(self):
        paymentresult = pack.PaydexXDRPacker()
        paymentresult.pack_PaymentResult(self)
        return base64.b64encode(paymentresult.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_PaymentResult()

    def __getattr__(self, attr):
        if attr is '__setstate__':
            raise AttributeError
        return getattr(self.switch, attr)

    def __repr__(self):
        out = []
        if self.code is not None:
            out += ['code=%s' % const.PaymentResultCode.get(self.code, self.code)]
        return 'PaymentResult(%s)' % ', '.join(out)
    __str__ = __repr__

class SimplePaymentResult:
    # XDR definition:
    # struct SimplePaymentResult {
    #     AccountID destination;
    #     Asset asset;
    #     int64 amount;
    # };
    def __init__(self, destination=None, asset=None, amount=None):
        self.destination = destination
        self.asset = asset
        self.amount = amount

    def to_xdr(self):
        simplepaymentresult = pack.PaydexXDRPacker()
        simplepaymentresult.pack_SimplePaymentResult(self)
        return base64.b64encode(simplepaymentresult.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_SimplePaymentResult()

    def __repr__(self):
        out = []
        if self.destination is not None:
            out += ['destination=%s' % repr(self.destination)]
        if self.asset is not None:
            out += ['asset=%s' % repr(self.asset)]
        if self.amount is not None:
            out += ['amount=%s' % repr(self.amount)]
        return 'SimplePaymentResult(%s)' % ', '.join(out)
    __str__ = __repr__

class PathPaymentStrictReceiveResult:
    # XDR definition:
    # union PathPaymentStrictReceiveResult switch(PathPaymentStrictReceiveResultCode code) {
    #     case PATH_PAYMENT_STRICT_RECEIVE_SUCCESS:
    #         struct {
    #             ClaimOfferAtom offers<>;
    #             SimplePaymentResult last;
    #         } success;
    #     case PATH_PAYMENT_STRICT_RECEIVE_NO_ISSUER:
    #         Asset noIssuer;
    #     default:
    #         void;
    # };
    def __init__(self, code=None, success=None, noIssuer=None):
        self.code = code
        self.success = success
        self.noIssuer = noIssuer

    switch = property(lambda s: {const.PATH_PAYMENT_STRICT_RECEIVE_SUCCESS:s.success,const.PATH_PAYMENT_STRICT_RECEIVE_NO_ISSUER:s.noIssuer,}.get(s.code, None))

    def to_xdr(self):
        pathpaymentstrictreceiveresult = pack.PaydexXDRPacker()
        pathpaymentstrictreceiveresult.pack_PathPaymentStrictReceiveResult(self)
        return base64.b64encode(pathpaymentstrictreceiveresult.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_PathPaymentStrictReceiveResult()

    def __getattr__(self, attr):
        if attr is '__setstate__':
            raise AttributeError
        return getattr(self.switch, attr)

    def __repr__(self):
        out = []
        if self.code is not None:
            out += ['code=%s' % const.PathPaymentStrictReceiveResultCode.get(self.code, self.code)]
        if self.success is not None:
            out += ['success=%s' % repr(self.success)]
        if self.noIssuer is not None:
            out += ['noIssuer=%s' % repr(self.noIssuer)]
        return 'PathPaymentStrictReceiveResult(%s)' % ', '.join(out)
    __str__ = __repr__

class PathPaymentStrictSendResult:
    # XDR definition:
    # union PathPaymentStrictSendResult switch(PathPaymentStrictSendResultCode code) {
    #     case PATH_PAYMENT_STRICT_SEND_SUCCESS:
    #         struct {
    #             ClaimOfferAtom offers<>;
    #             SimplePaymentResult last;
    #         } success;
    #     case PATH_PAYMENT_STRICT_SEND_NO_ISSUER:
    #         Asset noIssuer;
    #     default:
    #         void;
    # };
    def __init__(self, code=None, success=None, noIssuer=None):
        self.code = code
        self.success = success
        self.noIssuer = noIssuer

    switch = property(lambda s: {const.PATH_PAYMENT_STRICT_SEND_SUCCESS:s.success,const.PATH_PAYMENT_STRICT_SEND_NO_ISSUER:s.noIssuer,}.get(s.code, None))

    def to_xdr(self):
        pathpaymentstrictsendresult = pack.PaydexXDRPacker()
        pathpaymentstrictsendresult.pack_PathPaymentStrictSendResult(self)
        return base64.b64encode(pathpaymentstrictsendresult.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_PathPaymentStrictSendResult()

    def __getattr__(self, attr):
        if attr is '__setstate__':
            raise AttributeError
        return getattr(self.switch, attr)

    def __repr__(self):
        out = []
        if self.code is not None:
            out += ['code=%s' % const.PathPaymentStrictSendResultCode.get(self.code, self.code)]
        if self.success is not None:
            out += ['success=%s' % repr(self.success)]
        if self.noIssuer is not None:
            out += ['noIssuer=%s' % repr(self.noIssuer)]
        return 'PathPaymentStrictSendResult(%s)' % ', '.join(out)
    __str__ = __repr__

class ManageOfferSuccessResult:
    # XDR definition:
    # struct ManageOfferSuccessResult {
    #     ClaimOfferAtom offersClaimed<>;
    #     union switch(ManageOfferEffect effect) {
    #         case MANAGE_OFFER_CREATED:
    #         case MANAGE_OFFER_UPDATED:
    #             OfferEntry offer;
    #         default:
    #             void;
    #     } offer;
    # };
    def __init__(self, offersClaimed=None, offer=None):
        self.offersClaimed = offersClaimed
        self.offer = offer

    def __getattr__(self, attr):
        if attr is '__setstate__':
            raise AttributeError
        return getattr(self.offer, attr)

    def to_xdr(self):
        manageoffersuccessresult = pack.PaydexXDRPacker()
        manageoffersuccessresult.pack_ManageOfferSuccessResult(self)
        return base64.b64encode(manageoffersuccessresult.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_ManageOfferSuccessResult()

    def __repr__(self):
        out = []
        if self.offersClaimed is not None:
            out += ['offersClaimed=%s' % repr(self.offersClaimed)]
        if self.offer is not None:
            out += ['offer=%s' % repr(self.offer)]
        return 'ManageOfferSuccessResult(%s)' % ', '.join(out)
    __str__ = __repr__

class ManageSellOfferResult:
    # XDR definition:
    # union ManageSellOfferResult switch(ManageSellOfferResultCode code) {
    #     case MANAGE_SELL_OFFER_SUCCESS:
    #         ManageOfferSuccessResult success;
    #     default:
    #         void;
    # };
    def __init__(self, code=None, success=None):
        self.code = code
        self.success = success

    switch = property(lambda s: {const.MANAGE_SELL_OFFER_SUCCESS:s.success,}.get(s.code, None))

    def to_xdr(self):
        managesellofferresult = pack.PaydexXDRPacker()
        managesellofferresult.pack_ManageSellOfferResult(self)
        return base64.b64encode(managesellofferresult.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_ManageSellOfferResult()

    def __getattr__(self, attr):
        if attr is '__setstate__':
            raise AttributeError
        return getattr(self.switch, attr)

    def __repr__(self):
        out = []
        if self.code is not None:
            out += ['code=%s' % const.ManageSellOfferResultCode.get(self.code, self.code)]
        if self.success is not None:
            out += ['success=%s' % repr(self.success)]
        return 'ManageSellOfferResult(%s)' % ', '.join(out)
    __str__ = __repr__

class ManageBuyOfferResult:
    # XDR definition:
    # union ManageBuyOfferResult switch(ManageBuyOfferResultCode code) {
    #     case MANAGE_BUY_OFFER_SUCCESS:
    #         ManageOfferSuccessResult success;
    #     default:
    #         void;
    # };
    def __init__(self, code=None, success=None):
        self.code = code
        self.success = success

    switch = property(lambda s: {const.MANAGE_BUY_OFFER_SUCCESS:s.success,}.get(s.code, None))

    def to_xdr(self):
        managebuyofferresult = pack.PaydexXDRPacker()
        managebuyofferresult.pack_ManageBuyOfferResult(self)
        return base64.b64encode(managebuyofferresult.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_ManageBuyOfferResult()

    def __getattr__(self, attr):
        if attr is '__setstate__':
            raise AttributeError
        return getattr(self.switch, attr)

    def __repr__(self):
        out = []
        if self.code is not None:
            out += ['code=%s' % const.ManageBuyOfferResultCode.get(self.code, self.code)]
        if self.success is not None:
            out += ['success=%s' % repr(self.success)]
        return 'ManageBuyOfferResult(%s)' % ', '.join(out)
    __str__ = __repr__

class SetOptionsResult:
    # XDR definition:
    # union SetOptionsResult switch(SetOptionsResultCode code) {
    #     case SET_OPTIONS_SUCCESS:
    #         void;
    #     default:
    #         void;
    # };
    def __init__(self, code=None):
        self.code = code

    switch = property(lambda s: {const.SET_OPTIONS_SUCCESS:None,}.get(s.code, None))

    def to_xdr(self):
        setoptionsresult = pack.PaydexXDRPacker()
        setoptionsresult.pack_SetOptionsResult(self)
        return base64.b64encode(setoptionsresult.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_SetOptionsResult()

    def __getattr__(self, attr):
        if attr is '__setstate__':
            raise AttributeError
        return getattr(self.switch, attr)

    def __repr__(self):
        out = []
        if self.code is not None:
            out += ['code=%s' % const.SetOptionsResultCode.get(self.code, self.code)]
        return 'SetOptionsResult(%s)' % ', '.join(out)
    __str__ = __repr__

class ChangeTrustResult:
    # XDR definition:
    # union ChangeTrustResult switch(ChangeTrustResultCode code) {
    #     case CHANGE_TRUST_SUCCESS:
    #         void;
    #     default:
    #         void;
    # };
    def __init__(self, code=None):
        self.code = code

    switch = property(lambda s: {const.CHANGE_TRUST_SUCCESS:None,}.get(s.code, None))

    def to_xdr(self):
        changetrustresult = pack.PaydexXDRPacker()
        changetrustresult.pack_ChangeTrustResult(self)
        return base64.b64encode(changetrustresult.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_ChangeTrustResult()

    def __getattr__(self, attr):
        if attr is '__setstate__':
            raise AttributeError
        return getattr(self.switch, attr)

    def __repr__(self):
        out = []
        if self.code is not None:
            out += ['code=%s' % const.ChangeTrustResultCode.get(self.code, self.code)]
        return 'ChangeTrustResult(%s)' % ', '.join(out)
    __str__ = __repr__

class AllowTrustResult:
    # XDR definition:
    # union AllowTrustResult switch(AllowTrustResultCode code) {
    #     case ALLOW_TRUST_SUCCESS:
    #         void;
    #     default:
    #         void;
    # };
    def __init__(self, code=None):
        self.code = code

    switch = property(lambda s: {const.ALLOW_TRUST_SUCCESS:None,}.get(s.code, None))

    def to_xdr(self):
        allowtrustresult = pack.PaydexXDRPacker()
        allowtrustresult.pack_AllowTrustResult(self)
        return base64.b64encode(allowtrustresult.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_AllowTrustResult()

    def __getattr__(self, attr):
        if attr is '__setstate__':
            raise AttributeError
        return getattr(self.switch, attr)

    def __repr__(self):
        out = []
        if self.code is not None:
            out += ['code=%s' % const.AllowTrustResultCode.get(self.code, self.code)]
        return 'AllowTrustResult(%s)' % ', '.join(out)
    __str__ = __repr__

class AccountMergeResult:
    # XDR definition:
    # union AccountMergeResult switch(AccountMergeResultCode code) {
    #     case ACCOUNT_MERGE_SUCCESS:
    #         int64 sourceAccountBalance;
    #     default:
    #         void;
    # };
    def __init__(self, code=None, sourceAccountBalance=None):
        self.code = code
        self.sourceAccountBalance = sourceAccountBalance

    switch = property(lambda s: {const.ACCOUNT_MERGE_SUCCESS:s.sourceAccountBalance,}.get(s.code, None))

    def to_xdr(self):
        accountmergeresult = pack.PaydexXDRPacker()
        accountmergeresult.pack_AccountMergeResult(self)
        return base64.b64encode(accountmergeresult.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_AccountMergeResult()

    def __getattr__(self, attr):
        if attr is '__setstate__':
            raise AttributeError
        return getattr(self.switch, attr)

    def __repr__(self):
        out = []
        if self.code is not None:
            out += ['code=%s' % const.AccountMergeResultCode.get(self.code, self.code)]
        if self.sourceAccountBalance is not None:
            out += ['sourceAccountBalance=%s' % repr(self.sourceAccountBalance)]
        return 'AccountMergeResult(%s)' % ', '.join(out)
    __str__ = __repr__

class InflationPayout:
    # XDR definition:
    # struct InflationPayout {
    #     AccountID destination;
    #     int64 amount;
    # };
    def __init__(self, destination=None, amount=None):
        self.destination = destination
        self.amount = amount

    def __getattr__(self, attr):
        if attr is '__setstate__':
            raise AttributeError
        return getattr(self.destination, attr)

    def to_xdr(self):
        inflationpayout = pack.PaydexXDRPacker()
        inflationpayout.pack_InflationPayout(self)
        return base64.b64encode(inflationpayout.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_InflationPayout()

    def __repr__(self):
        out = []
        if self.destination is not None:
            out += ['destination=%s' % repr(self.destination)]
        if self.amount is not None:
            out += ['amount=%s' % repr(self.amount)]
        return 'InflationPayout(%s)' % ', '.join(out)
    __str__ = __repr__

class InflationResult:
    # XDR definition:
    # union InflationResult switch(InflationResultCode code) {
    #     case INFLATION_SUCCESS:
    #         InflationPayout payouts<>;
    #     default:
    #         void;
    # };
    def __init__(self, code=None, payouts=None):
        self.code = code
        self.payouts = payouts

    switch = property(lambda s: {const.INFLATION_SUCCESS:s.payouts,}.get(s.code, None))

    def to_xdr(self):
        inflationresult = pack.PaydexXDRPacker()
        inflationresult.pack_InflationResult(self)
        return base64.b64encode(inflationresult.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_InflationResult()

    def __getattr__(self, attr):
        if attr is '__setstate__':
            raise AttributeError
        return getattr(self.switch, attr)

    def __repr__(self):
        out = []
        if self.code is not None:
            out += ['code=%s' % const.InflationResultCode.get(self.code, self.code)]
        if self.payouts is not None:
            out += ['payouts=%s' % repr(self.payouts)]
        return 'InflationResult(%s)' % ', '.join(out)
    __str__ = __repr__

class ManageDataResult:
    # XDR definition:
    # union ManageDataResult switch(ManageDataResultCode code) {
    #     case MANAGE_DATA_SUCCESS:
    #         void;
    #     default:
    #         void;
    # };
    def __init__(self, code=None):
        self.code = code

    switch = property(lambda s: {const.MANAGE_DATA_SUCCESS:None,}.get(s.code, None))

    def to_xdr(self):
        managedataresult = pack.PaydexXDRPacker()
        managedataresult.pack_ManageDataResult(self)
        return base64.b64encode(managedataresult.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_ManageDataResult()

    def __getattr__(self, attr):
        if attr is '__setstate__':
            raise AttributeError
        return getattr(self.switch, attr)

    def __repr__(self):
        out = []
        if self.code is not None:
            out += ['code=%s' % const.ManageDataResultCode.get(self.code, self.code)]
        return 'ManageDataResult(%s)' % ', '.join(out)
    __str__ = __repr__

class BumpSequenceResult:
    # XDR definition:
    # union BumpSequenceResult switch(BumpSequenceResultCode code) {
    #     case BUMP_SEQUENCE_SUCCESS:
    #         void;
    #     default:
    #         void;
    # };
    def __init__(self, code=None):
        self.code = code

    switch = property(lambda s: {const.BUMP_SEQUENCE_SUCCESS:None,}.get(s.code, None))

    def to_xdr(self):
        bumpsequenceresult = pack.PaydexXDRPacker()
        bumpsequenceresult.pack_BumpSequenceResult(self)
        return base64.b64encode(bumpsequenceresult.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_BumpSequenceResult()

    def __getattr__(self, attr):
        if attr is '__setstate__':
            raise AttributeError
        return getattr(self.switch, attr)

    def __repr__(self):
        out = []
        if self.code is not None:
            out += ['code=%s' % const.BumpSequenceResultCode.get(self.code, self.code)]
        return 'BumpSequenceResult(%s)' % ', '.join(out)
    __str__ = __repr__

class OperationResult:
    # XDR definition:
    # union OperationResult switch(OperationResultCode code) {
    #     case opINNER:
    #         union switch(OperationType type) {
    #             case CREATE_ACCOUNT:
    #                 CreateAccountResult createAccountResult;
    #             case PAYMENT:
    #                 PaymentResult paymentResult;
    #             case PATH_PAYMENT_STRICT_RECEIVE:
    #                 PathPaymentStrictReceiveResult pathPaymentStrictReceiveResult;
    #             case MANAGE_SELL_OFFER:
    #                 ManageSellOfferResult manageSellOfferResult;
    #             case CREATE_PASSIVE_SELL_OFFER:
    #                 ManageSellOfferResult createPassiveSellOfferResult;
    #             case SET_OPTIONS:
    #                 SetOptionsResult setOptionsResult;
    #             case CHANGE_TRUST:
    #                 ChangeTrustResult changeTrustResult;
    #             case ALLOW_TRUST:
    #                 AllowTrustResult allowTrustResult;
    #             case ACCOUNT_MERGE:
    #                 AccountMergeResult accountMergeResult;
    #             case INFLATION:
    #                 InflationResult inflationResult;
    #             case MANAGE_DATA:
    #                 ManageDataResult manageDataResult;
    #             case BUMP_SEQUENCE:
    #                 BumpSequenceResult bumpSeqResult;
    #             case MANAGE_BUY_OFFER:
    #                 ManageBuyOfferResult manageBuyOfferResult;
    #             case PATH_PAYMENT_STRICT_SEND:
    #                 PathPaymentStrictSendResult pathPaymentStrictSendResult;
    #         } tr;
    #     default:
    #         void;
    # };
    def __init__(self, code=None, tr=None):
        self.code = code
        self.tr = tr

    switch = property(lambda s: {const.opINNER:s.tr,}.get(s.code, None))

    def to_xdr(self):
        operationresult = pack.PaydexXDRPacker()
        operationresult.pack_OperationResult(self)
        return base64.b64encode(operationresult.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_OperationResult()

    def __getattr__(self, attr):
        if attr is '__setstate__':
            raise AttributeError
        return getattr(self.switch, attr)

    def __repr__(self):
        out = []
        if self.code is not None:
            out += ['code=%s' % const.OperationResultCode.get(self.code, self.code)]
        if self.tr is not None:
            out += ['tr=%s' % repr(self.tr)]
        return 'OperationResult(%s)' % ', '.join(out)
    __str__ = __repr__

class TransactionResult:
    # XDR definition:
    # struct TransactionResult {
    #     int64 feeCharged;
    #     union switch(TransactionResultCode code) {
    #         case txSUCCESS:
    #         case txFAILED:
    #             OperationResult results<>;
    #         default:
    #             void;
    #     } result;
    #     union switch(int v) {
    #         case 0:
    #             void;
    #     } ext;
    # };
    def __init__(self, feeCharged=None, result=None, ext=None):
        self.feeCharged = feeCharged
        self.result = result
        self.ext = ext

    def to_xdr(self):
        transactionresult = pack.PaydexXDRPacker()
        transactionresult.pack_TransactionResult(self)
        return base64.b64encode(transactionresult.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_TransactionResult()

    def __repr__(self):
        out = []
        if self.feeCharged is not None:
            out += ['feeCharged=%s' % repr(self.feeCharged)]
        if self.result is not None:
            out += ['result=%s' % repr(self.result)]
        if self.ext is not None:
            out += ['ext=%s' % repr(self.ext)]
        return 'TransactionResult(%s)' % ', '.join(out)
    __str__ = __repr__

class Error:
    # XDR definition:
    # struct Error {
    #     ErrorCode code;
    #     string msg<100>;
    # };
    def __init__(self, code=None, msg=None):
        self.code = code
        self.msg = msg

    def to_xdr(self):
        error = pack.PaydexXDRPacker()
        error.pack_Error(self)
        return base64.b64encode(error.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_Error()

    def __repr__(self):
        out = []
        if self.code is not None:
            out += ['code=%s' % const.ErrorCode.get(self.code, self.code)]
        if self.msg is not None:
            out += ['msg=%s' % repr(self.msg)]
        return 'Error(%s)' % ', '.join(out)
    __str__ = __repr__

class AuthCert:
    # XDR definition:
    # struct AuthCert {
    #     Curve25519Public pubkey;
    #     uint64 expiration;
    #     Signature sig;
    # };
    def __init__(self, pubkey=None, expiration=None, sig=None):
        self.pubkey = pubkey
        self.expiration = expiration
        self.sig = sig

    def __getattr__(self, attr):
        if attr is '__setstate__':
            raise AttributeError
        return getattr(self.pubkey, attr)

    def to_xdr(self):
        authcert = pack.PaydexXDRPacker()
        authcert.pack_AuthCert(self)
        return base64.b64encode(authcert.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_AuthCert()

    def __repr__(self):
        out = []
        if self.pubkey is not None:
            out += ['pubkey=%s' % repr(self.pubkey)]
        if self.expiration is not None:
            out += ['expiration=%s' % repr(self.expiration)]
        if self.sig is not None:
            out += ['sig=%s' % repr(self.sig)]
        return 'AuthCert(%s)' % ', '.join(out)
    __str__ = __repr__

class Hello:
    # XDR definition:
    # struct Hello {
    #     uint32 ledgerVersion;
    #     uint32 overlayVersion;
    #     uint32 overlayMinVersion;
    #     Hash networkID;
    #     string versionStr<100>;
    #     int listeningPort;
    #     NodeID peerID;
    #     AuthCert cert;
    #     uint256 nonce;
    # };
    def __init__(self, ledgerVersion=None, overlayVersion=None, overlayMinVersion=None, networkID=None, versionStr=None, listeningPort=None, peerID=None, cert=None, nonce=None):
        self.ledgerVersion = ledgerVersion
        self.overlayVersion = overlayVersion
        self.overlayMinVersion = overlayMinVersion
        self.networkID = networkID
        self.versionStr = versionStr
        self.listeningPort = listeningPort
        self.peerID = peerID
        self.cert = cert
        self.nonce = nonce

    def to_xdr(self):
        hello = pack.PaydexXDRPacker()
        hello.pack_Hello(self)
        return base64.b64encode(hello.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_Hello()

    def __repr__(self):
        out = []
        if self.ledgerVersion is not None:
            out += ['ledgerVersion=%s' % repr(self.ledgerVersion)]
        if self.overlayVersion is not None:
            out += ['overlayVersion=%s' % repr(self.overlayVersion)]
        if self.overlayMinVersion is not None:
            out += ['overlayMinVersion=%s' % repr(self.overlayMinVersion)]
        if self.networkID is not None:
            out += ['networkID=%s' % repr(self.networkID)]
        if self.versionStr is not None:
            out += ['versionStr=%s' % repr(self.versionStr)]
        if self.listeningPort is not None:
            out += ['listeningPort=%s' % repr(self.listeningPort)]
        if self.peerID is not None:
            out += ['peerID=%s' % repr(self.peerID)]
        if self.cert is not None:
            out += ['cert=%s' % repr(self.cert)]
        if self.nonce is not None:
            out += ['nonce=%s' % repr(self.nonce)]
        return 'Hello(%s)' % ', '.join(out)
    __str__ = __repr__

class Auth:
    # XDR definition:
    # struct Auth {
    #     int unused;
    # };
    def __init__(self, unused=None):
        self.unused = unused

    def to_xdr(self):
        auth = pack.PaydexXDRPacker()
        auth.pack_Auth(self)
        return base64.b64encode(auth.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_Auth()

    def __repr__(self):
        out = []
        if self.unused is not None:
            out += ['unused=%s' % repr(self.unused)]
        return 'Auth(%s)' % ', '.join(out)
    __str__ = __repr__

class PeerAddress:
    # XDR definition:
    # struct PeerAddress {
    #     union switch(IPAddrType type) {
    #         case IPv4:
    #             opaque ipv4[4];
    #         case IPv6:
    #             opaque ipv6[16];
    #     } ip;
    #     uint32 port;
    #     uint32 numFailures;
    # };
    def __init__(self, ip=None, port=None, numFailures=None):
        self.ip = ip
        self.port = port
        self.numFailures = numFailures

    def __getattr__(self, attr):
        if attr is '__setstate__':
            raise AttributeError
        return getattr(self.ip, attr)

    def to_xdr(self):
        peeraddress = pack.PaydexXDRPacker()
        peeraddress.pack_PeerAddress(self)
        return base64.b64encode(peeraddress.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_PeerAddress()

    def __repr__(self):
        out = []
        if self.ip is not None:
            out += ['ip=%s' % repr(self.ip)]
        if self.port is not None:
            out += ['port=%s' % repr(self.port)]
        if self.numFailures is not None:
            out += ['numFailures=%s' % repr(self.numFailures)]
        return 'PeerAddress(%s)' % ', '.join(out)
    __str__ = __repr__

class DontHave:
    # XDR definition:
    # struct DontHave {
    #     MessageType type;
    #     uint256 reqHash;
    # };
    def __init__(self, type=None, reqHash=None):
        self.type = type
        self.reqHash = reqHash

    def to_xdr(self):
        donthave = pack.PaydexXDRPacker()
        donthave.pack_DontHave(self)
        return base64.b64encode(donthave.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_DontHave()

    def __repr__(self):
        out = []
        if self.type is not None:
            out += ['type=%s' % const.MessageType.get(self.type, self.type)]
        if self.reqHash is not None:
            out += ['reqHash=%s' % repr(self.reqHash)]
        return 'DontHave(%s)' % ', '.join(out)
    __str__ = __repr__

class SurveyRequestMessage:
    # XDR definition:
    # struct SurveyRequestMessage {
    #     NodeID surveyorPeerID;
    #     NodeID surveyedPeerID;
    #     uint32 ledgerNum;
    #     Curve25519Public encryptionKey;
    #     SurveyMessageCommandType commandType;
    # };
    def __init__(self, surveyorPeerID=None, surveyedPeerID=None, ledgerNum=None, encryptionKey=None, commandType=None):
        self.surveyorPeerID = surveyorPeerID
        self.surveyedPeerID = surveyedPeerID
        self.ledgerNum = ledgerNum
        self.encryptionKey = encryptionKey
        self.commandType = commandType

    def to_xdr(self):
        surveyrequestmessage = pack.PaydexXDRPacker()
        surveyrequestmessage.pack_SurveyRequestMessage(self)
        return base64.b64encode(surveyrequestmessage.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_SurveyRequestMessage()

    def __repr__(self):
        out = []
        if self.surveyorPeerID is not None:
            out += ['surveyorPeerID=%s' % repr(self.surveyorPeerID)]
        if self.surveyedPeerID is not None:
            out += ['surveyedPeerID=%s' % repr(self.surveyedPeerID)]
        if self.ledgerNum is not None:
            out += ['ledgerNum=%s' % repr(self.ledgerNum)]
        if self.encryptionKey is not None:
            out += ['encryptionKey=%s' % repr(self.encryptionKey)]
        if self.commandType is not None:
            out += ['commandType=%s' % const.SurveyMessageCommandType.get(self.commandType, self.commandType)]
        return 'SurveyRequestMessage(%s)' % ', '.join(out)
    __str__ = __repr__

class SignedSurveyRequestMessage:
    # XDR definition:
    # struct SignedSurveyRequestMessage {
    #     Signature requestSignature;
    #     SurveyRequestMessage request;
    # };
    def __init__(self, requestSignature=None, request=None):
        self.requestSignature = requestSignature
        self.request = request

    def __getattr__(self, attr):
        if attr is '__setstate__':
            raise AttributeError
        return getattr(self.request, attr)

    def to_xdr(self):
        signedsurveyrequestmessage = pack.PaydexXDRPacker()
        signedsurveyrequestmessage.pack_SignedSurveyRequestMessage(self)
        return base64.b64encode(signedsurveyrequestmessage.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_SignedSurveyRequestMessage()

    def __repr__(self):
        out = []
        if self.requestSignature is not None:
            out += ['requestSignature=%s' % repr(self.requestSignature)]
        if self.request is not None:
            out += ['request=%s' % repr(self.request)]
        return 'SignedSurveyRequestMessage(%s)' % ', '.join(out)
    __str__ = __repr__

class SurveyResponseMessage:
    # XDR definition:
    # struct SurveyResponseMessage {
    #     NodeID surveyorPeerID;
    #     NodeID surveyedPeerID;
    #     uint32 ledgerNum;
    #     SurveyMessageCommandType commandType;
    #     EncryptedBody encryptedBody;
    # };
    def __init__(self, surveyorPeerID=None, surveyedPeerID=None, ledgerNum=None, commandType=None, encryptedBody=None):
        self.surveyorPeerID = surveyorPeerID
        self.surveyedPeerID = surveyedPeerID
        self.ledgerNum = ledgerNum
        self.commandType = commandType
        self.encryptedBody = encryptedBody

    def to_xdr(self):
        surveyresponsemessage = pack.PaydexXDRPacker()
        surveyresponsemessage.pack_SurveyResponseMessage(self)
        return base64.b64encode(surveyresponsemessage.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_SurveyResponseMessage()

    def __repr__(self):
        out = []
        if self.surveyorPeerID is not None:
            out += ['surveyorPeerID=%s' % repr(self.surveyorPeerID)]
        if self.surveyedPeerID is not None:
            out += ['surveyedPeerID=%s' % repr(self.surveyedPeerID)]
        if self.ledgerNum is not None:
            out += ['ledgerNum=%s' % repr(self.ledgerNum)]
        if self.commandType is not None:
            out += ['commandType=%s' % const.SurveyMessageCommandType.get(self.commandType, self.commandType)]
        if self.encryptedBody is not None:
            out += ['encryptedBody=%s' % repr(self.encryptedBody)]
        return 'SurveyResponseMessage(%s)' % ', '.join(out)
    __str__ = __repr__

class SignedSurveyResponseMessage:
    # XDR definition:
    # struct SignedSurveyResponseMessage {
    #     Signature responseSignature;
    #     SurveyResponseMessage response;
    # };
    def __init__(self, responseSignature=None, response=None):
        self.responseSignature = responseSignature
        self.response = response

    def __getattr__(self, attr):
        if attr is '__setstate__':
            raise AttributeError
        return getattr(self.response, attr)

    def to_xdr(self):
        signedsurveyresponsemessage = pack.PaydexXDRPacker()
        signedsurveyresponsemessage.pack_SignedSurveyResponseMessage(self)
        return base64.b64encode(signedsurveyresponsemessage.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_SignedSurveyResponseMessage()

    def __repr__(self):
        out = []
        if self.responseSignature is not None:
            out += ['responseSignature=%s' % repr(self.responseSignature)]
        if self.response is not None:
            out += ['response=%s' % repr(self.response)]
        return 'SignedSurveyResponseMessage(%s)' % ', '.join(out)
    __str__ = __repr__

class PeerStats:
    # XDR definition:
    # struct PeerStats {
    #     NodeID id;
    #     string versionStr<100>;
    #     uint64 messagesRead;
    #     uint64 messagesWritten;
    #     uint64 bytesRead;
    #     uint64 bytesWritten;
    #     uint64 secondsConnected;
    #     uint64 uniqueFloodBytesRecv;
    #     uint64 duplicateFloodBytesRecv;
    #     uint64 uniqueFetchBytesRecv;
    #     uint64 duplicateFetchBytesRecv;
    #     uint64 uniqueFloodMessageRecv;
    #     uint64 duplicateFloodMessageRecv;
    #     uint64 uniqueFetchMessageRecv;
    #     uint64 duplicateFetchMessageRecv;
    # };
    def __init__(self, id=None, versionStr=None, messagesRead=None, messagesWritten=None, bytesRead=None, bytesWritten=None, secondsConnected=None, uniqueFloodBytesRecv=None, duplicateFloodBytesRecv=None, uniqueFetchBytesRecv=None, duplicateFetchBytesRecv=None, uniqueFloodMessageRecv=None, duplicateFloodMessageRecv=None, uniqueFetchMessageRecv=None, duplicateFetchMessageRecv=None):
        self.id = id
        self.versionStr = versionStr
        self.messagesRead = messagesRead
        self.messagesWritten = messagesWritten
        self.bytesRead = bytesRead
        self.bytesWritten = bytesWritten
        self.secondsConnected = secondsConnected
        self.uniqueFloodBytesRecv = uniqueFloodBytesRecv
        self.duplicateFloodBytesRecv = duplicateFloodBytesRecv
        self.uniqueFetchBytesRecv = uniqueFetchBytesRecv
        self.duplicateFetchBytesRecv = duplicateFetchBytesRecv
        self.uniqueFloodMessageRecv = uniqueFloodMessageRecv
        self.duplicateFloodMessageRecv = duplicateFloodMessageRecv
        self.uniqueFetchMessageRecv = uniqueFetchMessageRecv
        self.duplicateFetchMessageRecv = duplicateFetchMessageRecv

    def __getattr__(self, attr):
        if attr is '__setstate__':
            raise AttributeError
        return getattr(self.id, attr)

    def to_xdr(self):
        peerstats = pack.PaydexXDRPacker()
        peerstats.pack_PeerStats(self)
        return base64.b64encode(peerstats.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_PeerStats()

    def __repr__(self):
        out = []
        if self.id is not None:
            out += ['id=%s' % repr(self.id)]
        if self.versionStr is not None:
            out += ['versionStr=%s' % repr(self.versionStr)]
        if self.messagesRead is not None:
            out += ['messagesRead=%s' % repr(self.messagesRead)]
        if self.messagesWritten is not None:
            out += ['messagesWritten=%s' % repr(self.messagesWritten)]
        if self.bytesRead is not None:
            out += ['bytesRead=%s' % repr(self.bytesRead)]
        if self.bytesWritten is not None:
            out += ['bytesWritten=%s' % repr(self.bytesWritten)]
        if self.secondsConnected is not None:
            out += ['secondsConnected=%s' % repr(self.secondsConnected)]
        if self.uniqueFloodBytesRecv is not None:
            out += ['uniqueFloodBytesRecv=%s' % repr(self.uniqueFloodBytesRecv)]
        if self.duplicateFloodBytesRecv is not None:
            out += ['duplicateFloodBytesRecv=%s' % repr(self.duplicateFloodBytesRecv)]
        if self.uniqueFetchBytesRecv is not None:
            out += ['uniqueFetchBytesRecv=%s' % repr(self.uniqueFetchBytesRecv)]
        if self.duplicateFetchBytesRecv is not None:
            out += ['duplicateFetchBytesRecv=%s' % repr(self.duplicateFetchBytesRecv)]
        if self.uniqueFloodMessageRecv is not None:
            out += ['uniqueFloodMessageRecv=%s' % repr(self.uniqueFloodMessageRecv)]
        if self.duplicateFloodMessageRecv is not None:
            out += ['duplicateFloodMessageRecv=%s' % repr(self.duplicateFloodMessageRecv)]
        if self.uniqueFetchMessageRecv is not None:
            out += ['uniqueFetchMessageRecv=%s' % repr(self.uniqueFetchMessageRecv)]
        if self.duplicateFetchMessageRecv is not None:
            out += ['duplicateFetchMessageRecv=%s' % repr(self.duplicateFetchMessageRecv)]
        return 'PeerStats(%s)' % ', '.join(out)
    __str__ = __repr__

class TopologyResponseBody:
    # XDR definition:
    # struct TopologyResponseBody {
    #     PeerStatList inboundPeers;
    #     PeerStatList outboundPeers;
    #     uint32 totalInboundPeerCount;
    #     uint32 totalOutboundPeerCount;
    # };
    def __init__(self, inboundPeers=None, outboundPeers=None, totalInboundPeerCount=None, totalOutboundPeerCount=None):
        self.inboundPeers = inboundPeers
        self.outboundPeers = outboundPeers
        self.totalInboundPeerCount = totalInboundPeerCount
        self.totalOutboundPeerCount = totalOutboundPeerCount

    def to_xdr(self):
        topologyresponsebody = pack.PaydexXDRPacker()
        topologyresponsebody.pack_TopologyResponseBody(self)
        return base64.b64encode(topologyresponsebody.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_TopologyResponseBody()

    def __repr__(self):
        out = []
        if self.inboundPeers is not None:
            out += ['inboundPeers=%s' % repr(self.inboundPeers)]
        if self.outboundPeers is not None:
            out += ['outboundPeers=%s' % repr(self.outboundPeers)]
        if self.totalInboundPeerCount is not None:
            out += ['totalInboundPeerCount=%s' % repr(self.totalInboundPeerCount)]
        if self.totalOutboundPeerCount is not None:
            out += ['totalOutboundPeerCount=%s' % repr(self.totalOutboundPeerCount)]
        return 'TopologyResponseBody(%s)' % ', '.join(out)
    __str__ = __repr__

class SurveyResponseBody:
    # XDR definition:
    # union SurveyResponseBody switch(SurveyMessageCommandType type) {
    #     case SURVEY_TOPOLOGY:
    #         TopologyResponseBody topologyResponseBody;
    # };
    def __init__(self, type=None, topologyResponseBody=None):
        self.type = type
        self.topologyResponseBody = topologyResponseBody

    switch = property(lambda s: {const.SURVEY_TOPOLOGY:s.topologyResponseBody,}[s.type])

    def to_xdr(self):
        surveyresponsebody = pack.PaydexXDRPacker()
        surveyresponsebody.pack_SurveyResponseBody(self)
        return base64.b64encode(surveyresponsebody.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_SurveyResponseBody()

    def __getattr__(self, attr):
        if attr is '__setstate__':
            raise AttributeError
        return getattr(self.switch, attr)

    def __repr__(self):
        out = []
        if self.type is not None:
            out += ['type=%s' % const.SurveyMessageCommandType.get(self.type, self.type)]
        if self.topologyResponseBody is not None:
            out += ['topologyResponseBody=%s' % repr(self.topologyResponseBody)]
        return 'SurveyResponseBody(%s)' % ', '.join(out)
    __str__ = __repr__

class PaydexMessage:
    # XDR definition:
    # union PaydexMessage switch(MessageType type) {
    #     case ERROR_MSG:
    #         Error error;
    #     case HELLO:
    #         Hello hello;
    #     case AUTH:
    #         Auth auth;
    #     case DONT_HAVE:
    #         DontHave dontHave;
    #     case GET_PEERS:
    #         void;
    #     case PEERS:
    #         PeerAddress peers<100>;
    #     case GET_TX_SET:
    #         uint256 txSetHash;
    #     case TX_SET:
    #         TransactionSet txSet;
    #     case TRANSACTION:
    #         TransactionEnvelope transaction;
    #     case SURVEY_REQUEST:
    #         SignedSurveyRequestMessage signedSurveyRequestMessage;
    #     case SURVEY_RESPONSE:
    #         SignedSurveyResponseMessage signedSurveyResponseMessage;
    #     case GET_SCP_QUORUMSET:
    #         uint256 qSetHash;
    #     case SCP_QUORUMSET:
    #         SCPQuorumSet qSet;
    #     case SCP_MESSAGE:
    #         SCPEnvelope envelope;
    #     case GET_SCP_STATE:
    #         uint32 getSCPLedgerSeq;
    # };
    def __init__(self, type=None, error=None, hello=None, auth=None, dontHave=None, peers=None, txSetHash=None, txSet=None, transaction=None, signedSurveyRequestMessage=None, signedSurveyResponseMessage=None, qSetHash=None, qSet=None, envelope=None, getSCPLedgerSeq=None):
        self.type = type
        self.error = error
        self.hello = hello
        self.auth = auth
        self.dontHave = dontHave
        self.peers = peers
        self.txSetHash = txSetHash
        self.txSet = txSet
        self.transaction = transaction
        self.signedSurveyRequestMessage = signedSurveyRequestMessage
        self.signedSurveyResponseMessage = signedSurveyResponseMessage
        self.qSetHash = qSetHash
        self.qSet = qSet
        self.envelope = envelope
        self.getSCPLedgerSeq = getSCPLedgerSeq

    switch = property(lambda s: {const.ERROR_MSG:s.error,const.HELLO:s.hello,const.AUTH:s.auth,const.DONT_HAVE:s.dontHave,const.GET_PEERS:None,const.PEERS:s.peers,const.GET_TX_SET:s.txSetHash,const.TX_SET:s.txSet,const.TRANSACTION:s.transaction,const.SURVEY_REQUEST:s.signedSurveyRequestMessage,const.SURVEY_RESPONSE:s.signedSurveyResponseMessage,const.GET_SCP_QUORUMSET:s.qSetHash,const.SCP_QUORUMSET:s.qSet,const.SCP_MESSAGE:s.envelope,const.GET_SCP_STATE:s.getSCPLedgerSeq,}[s.type])

    def to_xdr(self):
        paydexmessage = pack.PaydexXDRPacker()
        paydexmessage.pack_PaydexMessage(self)
        return base64.b64encode(paydexmessage.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_PaydexMessage()

    def __getattr__(self, attr):
        if attr is '__setstate__':
            raise AttributeError
        return getattr(self.switch, attr)

    def __repr__(self):
        out = []
        if self.type is not None:
            out += ['type=%s' % const.MessageType.get(self.type, self.type)]
        if self.error is not None:
            out += ['error=%s' % repr(self.error)]
        if self.hello is not None:
            out += ['hello=%s' % repr(self.hello)]
        if self.auth is not None:
            out += ['auth=%s' % repr(self.auth)]
        if self.dontHave is not None:
            out += ['dontHave=%s' % repr(self.dontHave)]
        if self.peers is not None:
            out += ['peers=%s' % repr(self.peers)]
        if self.txSetHash is not None:
            out += ['txSetHash=%s' % repr(self.txSetHash)]
        if self.txSet is not None:
            out += ['txSet=%s' % repr(self.txSet)]
        if self.transaction is not None:
            out += ['transaction=%s' % repr(self.transaction)]
        if self.signedSurveyRequestMessage is not None:
            out += ['signedSurveyRequestMessage=%s' % repr(self.signedSurveyRequestMessage)]
        if self.signedSurveyResponseMessage is not None:
            out += ['signedSurveyResponseMessage=%s' % repr(self.signedSurveyResponseMessage)]
        if self.qSetHash is not None:
            out += ['qSetHash=%s' % repr(self.qSetHash)]
        if self.qSet is not None:
            out += ['qSet=%s' % repr(self.qSet)]
        if self.envelope is not None:
            out += ['envelope=%s' % repr(self.envelope)]
        if self.getSCPLedgerSeq is not None:
            out += ['getSCPLedgerSeq=%s' % repr(self.getSCPLedgerSeq)]
        return 'PaydexMessage(%s)' % ', '.join(out)
    __str__ = __repr__

class AuthenticatedMessage:
    # XDR definition:
    # union AuthenticatedMessage switch(uint32 v) {
    #     case 0:
    #         struct {
    #             uint64 sequence;
    #             PaydexMessage message;
    #             HmacSha256Mac mac;
    #         } v0;
    # };
    def __init__(self, v=None, v0=None):
        self.v = v
        self.v0 = v0

    switch = property(lambda s: {0:s.v0,}[s.v])

    def to_xdr(self):
        authenticatedmessage = pack.PaydexXDRPacker()
        authenticatedmessage.pack_AuthenticatedMessage(self)
        return base64.b64encode(authenticatedmessage.get_buffer()).decode()

    @staticmethod
    def from_xdr(xdr):
        xdr_decoded = base64.b64decode(xdr)
        xdr_unpacked = pack.PaydexXDRUnpacker(xdr_decoded)
        return xdr_unpacked.unpack_AuthenticatedMessage()

    def __getattr__(self, attr):
        if attr is '__setstate__':
            raise AttributeError
        return getattr(self.switch, attr)

    def __repr__(self):
        out = []
        if self.v is not None:
            out += ['v=%s' % repr(self.v)]
        if self.v0 is not None:
            out += ['v0=%s' % repr(self.v0)]
        return 'AuthenticatedMessage(%s)' % ', '.join(out)
    __str__ = __repr__

