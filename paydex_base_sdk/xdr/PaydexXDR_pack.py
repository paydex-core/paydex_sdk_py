from . import PaydexXDR_const as const
from . import PaydexXDR_type as types
import xdrlib
from xdrlib import Error as XDRError

class nullclass(object):
    pass

class PaydexXDRPacker(xdrlib.Packer):
    def __init__(self, check_enum=True, check_array=True):
        xdrlib.Packer.__init__(self)
        self.check_enum = check_enum
        self.check_array = check_array

    pack_int = xdrlib.Packer.pack_int
    pack_uint = xdrlib.Packer.pack_uint
    pack_unsigned = xdrlib.Packer.pack_uint
    pack_hyper = xdrlib.Packer.pack_hyper
    pack_uhyper = xdrlib.Packer.pack_uhyper
    pack_float = xdrlib.Packer.pack_float
    pack_double = xdrlib.Packer.pack_double
    pack_quadruple = xdrlib.Packer.pack_double
    pack_bool = xdrlib.Packer.pack_bool
    pack_opaque = xdrlib.Packer.pack_opaque
    pack_string = xdrlib.Packer.pack_string
    def pack_Hash(self, data):
        if hasattr(self, 'filter_Hash'):
            data = getattr(self, 'filter_Hash')(data)
        self.pack_fopaque(32, data)

    def pack_uint256(self, data):
        if hasattr(self, 'filter_uint256'):
            data = getattr(self, 'filter_uint256')(data)
        self.pack_fopaque(32, data)

    pack_uint32 = pack_uint

    pack_int32 = pack_int

    pack_uint64 = pack_uhyper

    pack_int64 = pack_hyper

    def pack_CryptoKeyType(self, data):
        if hasattr(self, 'filter_CryptoKeyType'):
            data = getattr(self, 'filter_CryptoKeyType')(data)
        if self.check_enum and data not in [const.KEY_TYPE_ED25519, const.KEY_TYPE_PRE_AUTH_TX, const.KEY_TYPE_HASH_X]:
            raise XDRError('value=%s not in enum CryptoKeyType' % data)
        self.pack_int(data)

    def pack_PublicKeyType(self, data):
        if hasattr(self, 'filter_PublicKeyType'):
            data = getattr(self, 'filter_PublicKeyType')(data)
        if self.check_enum and data not in [const.PUBLIC_KEY_TYPE_ED25519]:
            raise XDRError('value=%s not in enum PublicKeyType' % data)
        self.pack_int(data)

    def pack_SignerKeyType(self, data):
        if hasattr(self, 'filter_SignerKeyType'):
            data = getattr(self, 'filter_SignerKeyType')(data)
        if self.check_enum and data not in [const.SIGNER_KEY_TYPE_ED25519, const.SIGNER_KEY_TYPE_PRE_AUTH_TX, const.SIGNER_KEY_TYPE_HASH_X]:
            raise XDRError('value=%s not in enum SignerKeyType' % data)
        self.pack_int(data)

    def pack_PublicKey(self, data):
        if hasattr(self, 'filter_PublicKey'):
            data = getattr(self, 'filter_PublicKey')(data)
        if data.type is None:
            raise TypeError('data.type == None')
        self.pack_PublicKeyType(data.type)
        if data.type == const.PUBLIC_KEY_TYPE_ED25519:
            if data.ed25519 is None:
                raise TypeError('data.ed25519 == None')
            self.pack_uint256(data.ed25519)
        else:
            raise XDRError('bad switch=%s' % data.type)

    def pack_SignerKey(self, data):
        if hasattr(self, 'filter_SignerKey'):
            data = getattr(self, 'filter_SignerKey')(data)
        if data.type is None:
            raise TypeError('data.type == None')
        self.pack_SignerKeyType(data.type)
        if data.type == const.SIGNER_KEY_TYPE_ED25519:
            if data.ed25519 is None:
                raise TypeError('data.ed25519 == None')
            self.pack_uint256(data.ed25519)
        elif data.type == const.SIGNER_KEY_TYPE_PRE_AUTH_TX:
            if data.preAuthTx is None:
                raise TypeError('data.preAuthTx == None')
            self.pack_uint256(data.preAuthTx)
        elif data.type == const.SIGNER_KEY_TYPE_HASH_X:
            if data.hashX is None:
                raise TypeError('data.hashX == None')
            self.pack_uint256(data.hashX)
        else:
            raise XDRError('bad switch=%s' % data.type)

    def pack_Signature(self, data):
        if hasattr(self, 'filter_Signature'):
            data = getattr(self, 'filter_Signature')(data)
        if len(data) > 64 and self.check_array:
            raise XDRError('array length too long for data')
        self.pack_opaque(data)

    def pack_SignatureHint(self, data):
        if hasattr(self, 'filter_SignatureHint'):
            data = getattr(self, 'filter_SignatureHint')(data)
        self.pack_fopaque(4, data)

    pack_NodeID = pack_PublicKey

    def pack_Curve25519Secret(self, data):
        if hasattr(self, 'filter_Curve25519Secret'):
            data = getattr(self, 'filter_Curve25519Secret')(data)
        if data.key is None:
            raise TypeError('data.key == None')
        self.pack_fopaque(32, data.key)

    def pack_Curve25519Public(self, data):
        if hasattr(self, 'filter_Curve25519Public'):
            data = getattr(self, 'filter_Curve25519Public')(data)
        if data.key is None:
            raise TypeError('data.key == None')
        self.pack_fopaque(32, data.key)

    def pack_HmacSha256Key(self, data):
        if hasattr(self, 'filter_HmacSha256Key'):
            data = getattr(self, 'filter_HmacSha256Key')(data)
        if data.key is None:
            raise TypeError('data.key == None')
        self.pack_fopaque(32, data.key)

    def pack_HmacSha256Mac(self, data):
        if hasattr(self, 'filter_HmacSha256Mac'):
            data = getattr(self, 'filter_HmacSha256Mac')(data)
        if data.mac is None:
            raise TypeError('data.mac == None')
        self.pack_fopaque(32, data.mac)

    def pack_Value(self, data):
        if hasattr(self, 'filter_Value'):
            data = getattr(self, 'filter_Value')(data)
        self.pack_opaque(data)

    def pack_SCPBallot(self, data):
        if hasattr(self, 'filter_SCPBallot'):
            data = getattr(self, 'filter_SCPBallot')(data)
        if data.counter is None:
            raise TypeError('data.counter == None')
        self.pack_uint32(data.counter)
        if data.value is None:
            raise TypeError('data.value == None')
        self.pack_Value(data.value)

    def pack_SCPStatementType(self, data):
        if hasattr(self, 'filter_SCPStatementType'):
            data = getattr(self, 'filter_SCPStatementType')(data)
        if self.check_enum and data not in [const.SCP_ST_PREPARE, const.SCP_ST_CONFIRM, const.SCP_ST_EXTERNALIZE, const.SCP_ST_NOMINATE]:
            raise XDRError('value=%s not in enum SCPStatementType' % data)
        self.pack_int(data)

    def pack_SCPNomination(self, data):
        if hasattr(self, 'filter_SCPNomination'):
            data = getattr(self, 'filter_SCPNomination')(data)
        if data.quorumSetHash is None:
            raise TypeError('data.quorumSetHash == None')
        self.pack_Hash(data.quorumSetHash)
        if data.votes is None:
            raise TypeError('data.votes == None')
        self.pack_array(data.votes, self.pack_Value)
        if data.accepted is None:
            raise TypeError('data.accepted == None')
        self.pack_array(data.accepted, self.pack_Value)

    def pack_SCPStatement(self, data):
        if hasattr(self, 'filter_SCPStatement'):
            data = getattr(self, 'filter_SCPStatement')(data)
        if data.nodeID is None:
            raise TypeError('data.nodeID == None')
        self.pack_NodeID(data.nodeID)
        if data.slotIndex is None:
            raise TypeError('data.slotIndex == None')
        self.pack_uint64(data.slotIndex)
        if data.pledges is None:
            raise TypeError('data.pledges == None')
        if data.pledges.type is None:
            raise TypeError('data.pledges.type == None')
        self.pack_SCPStatementType(data.pledges.type)
        if data.pledges.type == const.SCP_ST_PREPARE:
            if data.pledges.prepare is None:
                raise TypeError('data.pledges.prepare == None')
            if data.pledges.prepare.quorumSetHash is None:
                raise TypeError('data.pledges.prepare.quorumSetHash == None')
            self.pack_Hash(data.pledges.prepare.quorumSetHash)
            if data.pledges.prepare.ballot is None:
                raise TypeError('data.pledges.prepare.ballot == None')
            self.pack_SCPBallot(data.pledges.prepare.ballot)
            if data.pledges.prepare.prepared is None:
                raise TypeError('data.pledges.prepare.prepared == None')
            if len(data.pledges.prepare.prepared) > 1 and self.check_array:
                raise XDRError('array length too long for data.pledges.prepare.prepared')
            self.pack_array(data.pledges.prepare.prepared, self.pack_SCPBallot)
            if data.pledges.prepare.preparedPrime is None:
                raise TypeError('data.pledges.prepare.preparedPrime == None')
            if len(data.pledges.prepare.preparedPrime) > 1 and self.check_array:
                raise XDRError('array length too long for data.pledges.prepare.preparedPrime')
            self.pack_array(data.pledges.prepare.preparedPrime, self.pack_SCPBallot)
            if data.pledges.prepare.nC is None:
                raise TypeError('data.pledges.prepare.nC == None')
            self.pack_uint32(data.pledges.prepare.nC)
            if data.pledges.prepare.nH is None:
                raise TypeError('data.pledges.prepare.nH == None')
            self.pack_uint32(data.pledges.prepare.nH)
        elif data.pledges.type == const.SCP_ST_CONFIRM:
            if data.pledges.confirm is None:
                raise TypeError('data.pledges.confirm == None')
            if data.pledges.confirm.ballot is None:
                raise TypeError('data.pledges.confirm.ballot == None')
            self.pack_SCPBallot(data.pledges.confirm.ballot)
            if data.pledges.confirm.nPrepared is None:
                raise TypeError('data.pledges.confirm.nPrepared == None')
            self.pack_uint32(data.pledges.confirm.nPrepared)
            if data.pledges.confirm.nCommit is None:
                raise TypeError('data.pledges.confirm.nCommit == None')
            self.pack_uint32(data.pledges.confirm.nCommit)
            if data.pledges.confirm.nH is None:
                raise TypeError('data.pledges.confirm.nH == None')
            self.pack_uint32(data.pledges.confirm.nH)
            if data.pledges.confirm.quorumSetHash is None:
                raise TypeError('data.pledges.confirm.quorumSetHash == None')
            self.pack_Hash(data.pledges.confirm.quorumSetHash)
        elif data.pledges.type == const.SCP_ST_EXTERNALIZE:
            if data.pledges.externalize is None:
                raise TypeError('data.pledges.externalize == None')
            if data.pledges.externalize.commit is None:
                raise TypeError('data.pledges.externalize.commit == None')
            self.pack_SCPBallot(data.pledges.externalize.commit)
            if data.pledges.externalize.nH is None:
                raise TypeError('data.pledges.externalize.nH == None')
            self.pack_uint32(data.pledges.externalize.nH)
            if data.pledges.externalize.commitQuorumSetHash is None:
                raise TypeError('data.pledges.externalize.commitQuorumSetHash == None')
            self.pack_Hash(data.pledges.externalize.commitQuorumSetHash)
        elif data.pledges.type == const.SCP_ST_NOMINATE:
            if data.pledges.nominate is None:
                raise TypeError('data.pledges.nominate == None')
            self.pack_SCPNomination(data.pledges.nominate)
        else:
            raise XDRError('bad switch=%s' % data.pledges.type)

    def pack_SCPEnvelope(self, data):
        if hasattr(self, 'filter_SCPEnvelope'):
            data = getattr(self, 'filter_SCPEnvelope')(data)
        if data.statement is None:
            raise TypeError('data.statement == None')
        self.pack_SCPStatement(data.statement)
        if data.signature is None:
            raise TypeError('data.signature == None')
        self.pack_Signature(data.signature)

    def pack_SCPQuorumSet(self, data):
        if hasattr(self, 'filter_SCPQuorumSet'):
            data = getattr(self, 'filter_SCPQuorumSet')(data)
        if data.threshold is None:
            raise TypeError('data.threshold == None')
        self.pack_uint32(data.threshold)
        if data.validators is None:
            raise TypeError('data.validators == None')
        self.pack_array(data.validators, self.pack_PublicKey)
        if data.innerSets is None:
            raise TypeError('data.innerSets == None')
        self.pack_array(data.innerSets, self.pack_SCPQuorumSet)

    def pack_UpgradeType(self, data):
        if hasattr(self, 'filter_UpgradeType'):
            data = getattr(self, 'filter_UpgradeType')(data)
        if len(data) > 128 and self.check_array:
            raise XDRError('array length too long for data')
        self.pack_opaque(data)

    def pack_PaydexValueType(self, data):
        if hasattr(self, 'filter_PaydexValueType'):
            data = getattr(self, 'filter_PaydexValueType')(data)
        if self.check_enum and data not in [const.PAYDEX_VALUE_BASIC, const.PAYDEX_VALUE_SIGNED]:
            raise XDRError('value=%s not in enum PaydexValueType' % data)
        self.pack_int(data)

    def pack_LedgerCloseValueSignature(self, data):
        if hasattr(self, 'filter_LedgerCloseValueSignature'):
            data = getattr(self, 'filter_LedgerCloseValueSignature')(data)
        if data.nodeID is None:
            raise TypeError('data.nodeID == None')
        self.pack_NodeID(data.nodeID)
        if data.signature is None:
            raise TypeError('data.signature == None')
        self.pack_Signature(data.signature)

    def pack_PaydexValue(self, data):
        if hasattr(self, 'filter_PaydexValue'):
            data = getattr(self, 'filter_PaydexValue')(data)
        if data.txSetHash is None:
            raise TypeError('data.txSetHash == None')
        self.pack_Hash(data.txSetHash)
        if data.closeTime is None:
            raise TypeError('data.closeTime == None')
        self.pack_TimePoint(data.closeTime)
        if data.upgrades is None:
            raise TypeError('data.upgrades == None')
        if len(data.upgrades) > 6 and self.check_array:
            raise XDRError('array length too long for data.upgrades')
        self.pack_array(data.upgrades, self.pack_UpgradeType)
        if data.ext is None:
            raise TypeError('data.ext == None')
        if data.ext.v is None:
            raise TypeError('data.ext.v == None')
        self.pack_PaydexValueType(data.ext.v)
        if data.ext.v == const.PAYDEX_VALUE_BASIC:
            pass
        elif data.ext.v == const.PAYDEX_VALUE_SIGNED:
            if data.ext.lcValueSignature is None:
                raise TypeError('data.ext.lcValueSignature == None')
            self.pack_LedgerCloseValueSignature(data.ext.lcValueSignature)
        else:
            raise XDRError('bad switch=%s' % data.ext.v)

    def pack_LedgerHeader(self, data):
        if hasattr(self, 'filter_LedgerHeader'):
            data = getattr(self, 'filter_LedgerHeader')(data)
        if data.ledgerVersion is None:
            raise TypeError('data.ledgerVersion == None')
        self.pack_uint32(data.ledgerVersion)
        if data.previousLedgerHash is None:
            raise TypeError('data.previousLedgerHash == None')
        self.pack_Hash(data.previousLedgerHash)
        if data.scpValue is None:
            raise TypeError('data.scpValue == None')
        self.pack_PaydexValue(data.scpValue)
        if data.txSetResultHash is None:
            raise TypeError('data.txSetResultHash == None')
        self.pack_Hash(data.txSetResultHash)
        if data.bucketListHash is None:
            raise TypeError('data.bucketListHash == None')
        self.pack_Hash(data.bucketListHash)
        if data.ledgerSeq is None:
            raise TypeError('data.ledgerSeq == None')
        self.pack_uint32(data.ledgerSeq)
        if data.totalCoins is None:
            raise TypeError('data.totalCoins == None')
        self.pack_int64(data.totalCoins)
        if data.feePool is None:
            raise TypeError('data.feePool == None')
        self.pack_int64(data.feePool)
        if data.inflationSeq is None:
            raise TypeError('data.inflationSeq == None')
        self.pack_uint32(data.inflationSeq)
        if data.idPool is None:
            raise TypeError('data.idPool == None')
        self.pack_uint64(data.idPool)
        if data.baseFee is None:
            raise TypeError('data.baseFee == None')
        self.pack_uint32(data.baseFee)
        if data.baseReserve is None:
            raise TypeError('data.baseReserve == None')
        self.pack_uint32(data.baseReserve)
        if data.maxTxSetSize is None:
            raise TypeError('data.maxTxSetSize == None')
        self.pack_uint32(data.maxTxSetSize)
        if data.skipList is None:
            raise TypeError('data.skipList == None')
        self.pack_farray(4, data.skipList, self.pack_Hash)
        if data.ext is None:
            raise TypeError('data.ext == None')
        if data.ext.v is None:
            raise TypeError('data.ext.v == None')
        self.pack_int(data.ext.v)
        if data.ext.v == 0:
            pass
        else:
            raise XDRError('bad switch=%s' % data.ext.v)

    def pack_LedgerUpgradeType(self, data):
        if hasattr(self, 'filter_LedgerUpgradeType'):
            data = getattr(self, 'filter_LedgerUpgradeType')(data)
        if self.check_enum and data not in [const.LEDGER_UPGRADE_VERSION, const.LEDGER_UPGRADE_BASE_FEE, const.LEDGER_UPGRADE_MAX_TX_SET_SIZE, const.LEDGER_UPGRADE_BASE_RESERVE]:
            raise XDRError('value=%s not in enum LedgerUpgradeType' % data)
        self.pack_int(data)

    def pack_LedgerUpgrade(self, data):
        if hasattr(self, 'filter_LedgerUpgrade'):
            data = getattr(self, 'filter_LedgerUpgrade')(data)
        if data.type is None:
            raise TypeError('data.type == None')
        self.pack_LedgerUpgradeType(data.type)
        if data.type == const.LEDGER_UPGRADE_VERSION:
            if data.newLedgerVersion is None:
                raise TypeError('data.newLedgerVersion == None')
            self.pack_uint32(data.newLedgerVersion)
        elif data.type == const.LEDGER_UPGRADE_BASE_FEE:
            if data.newBaseFee is None:
                raise TypeError('data.newBaseFee == None')
            self.pack_uint32(data.newBaseFee)
        elif data.type == const.LEDGER_UPGRADE_MAX_TX_SET_SIZE:
            if data.newMaxTxSetSize is None:
                raise TypeError('data.newMaxTxSetSize == None')
            self.pack_uint32(data.newMaxTxSetSize)
        elif data.type == const.LEDGER_UPGRADE_BASE_RESERVE:
            if data.newBaseReserve is None:
                raise TypeError('data.newBaseReserve == None')
            self.pack_uint32(data.newBaseReserve)
        else:
            raise XDRError('bad switch=%s' % data.type)

    def pack_LedgerKey(self, data):
        if hasattr(self, 'filter_LedgerKey'):
            data = getattr(self, 'filter_LedgerKey')(data)
        if data.type is None:
            raise TypeError('data.type == None')
        self.pack_LedgerEntryType(data.type)
        if data.type == const.ACCOUNT:
            if data.account is None:
                raise TypeError('data.account == None')
            if data.account.accountID is None:
                raise TypeError('data.account.accountID == None')
            self.pack_AccountID(data.account.accountID)
        elif data.type == const.TRUSTLINE:
            if data.trustLine is None:
                raise TypeError('data.trustLine == None')
            if data.trustLine.accountID is None:
                raise TypeError('data.trustLine.accountID == None')
            self.pack_AccountID(data.trustLine.accountID)
            if data.trustLine.asset is None:
                raise TypeError('data.trustLine.asset == None')
            self.pack_Asset(data.trustLine.asset)
        elif data.type == const.OFFER:
            if data.offer is None:
                raise TypeError('data.offer == None')
            if data.offer.sellerID is None:
                raise TypeError('data.offer.sellerID == None')
            self.pack_AccountID(data.offer.sellerID)
            if data.offer.offerID is None:
                raise TypeError('data.offer.offerID == None')
            self.pack_int64(data.offer.offerID)
        elif data.type == const.DATA:
            if data.data is None:
                raise TypeError('data.data == None')
            if data.data.accountID is None:
                raise TypeError('data.data.accountID == None')
            self.pack_AccountID(data.data.accountID)
            if data.data.dataName is None:
                raise TypeError('data.data.dataName == None')
            self.pack_string64(data.data.dataName)
        else:
            raise XDRError('bad switch=%s' % data.type)

    def pack_BucketEntryType(self, data):
        if hasattr(self, 'filter_BucketEntryType'):
            data = getattr(self, 'filter_BucketEntryType')(data)
        if self.check_enum and data not in [const.METAENTRY, const.LIVEENTRY, const.DEADENTRY, const.INITENTRY]:
            raise XDRError('value=%s not in enum BucketEntryType' % data)
        self.pack_int(data)

    def pack_BucketMetadata(self, data):
        if hasattr(self, 'filter_BucketMetadata'):
            data = getattr(self, 'filter_BucketMetadata')(data)
        if data.ledgerVersion is None:
            raise TypeError('data.ledgerVersion == None')
        self.pack_uint32(data.ledgerVersion)
        if data.ext is None:
            raise TypeError('data.ext == None')
        if data.ext.v is None:
            raise TypeError('data.ext.v == None')
        self.pack_int(data.ext.v)
        if data.ext.v == 0:
            pass
        else:
            raise XDRError('bad switch=%s' % data.ext.v)

    def pack_BucketEntry(self, data):
        if hasattr(self, 'filter_BucketEntry'):
            data = getattr(self, 'filter_BucketEntry')(data)
        if data.type is None:
            raise TypeError('data.type == None')
        self.pack_BucketEntryType(data.type)
        if data.type == const.LIVEENTRY or data.type == const.INITENTRY:
            if data.liveEntry is None:
                raise TypeError('data.liveEntry == None')
            self.pack_LedgerEntry(data.liveEntry)
        elif data.type == const.DEADENTRY:
            if data.deadEntry is None:
                raise TypeError('data.deadEntry == None')
            self.pack_LedgerKey(data.deadEntry)
        elif data.type == const.METAENTRY:
            if data.metaEntry is None:
                raise TypeError('data.metaEntry == None')
            self.pack_BucketMetadata(data.metaEntry)
        else:
            raise XDRError('bad switch=%s' % data.type)

    def pack_TransactionSet(self, data):
        if hasattr(self, 'filter_TransactionSet'):
            data = getattr(self, 'filter_TransactionSet')(data)
        if data.previousLedgerHash is None:
            raise TypeError('data.previousLedgerHash == None')
        self.pack_Hash(data.previousLedgerHash)
        if data.txs is None:
            raise TypeError('data.txs == None')
        self.pack_array(data.txs, self.pack_TransactionEnvelope)

    def pack_TransactionResultPair(self, data):
        if hasattr(self, 'filter_TransactionResultPair'):
            data = getattr(self, 'filter_TransactionResultPair')(data)
        if data.transactionHash is None:
            raise TypeError('data.transactionHash == None')
        self.pack_Hash(data.transactionHash)
        if data.result is None:
            raise TypeError('data.result == None')
        self.pack_TransactionResult(data.result)

    def pack_TransactionResultSet(self, data):
        if hasattr(self, 'filter_TransactionResultSet'):
            data = getattr(self, 'filter_TransactionResultSet')(data)
        if data.results is None:
            raise TypeError('data.results == None')
        self.pack_array(data.results, self.pack_TransactionResultPair)

    def pack_TransactionHistoryEntry(self, data):
        if hasattr(self, 'filter_TransactionHistoryEntry'):
            data = getattr(self, 'filter_TransactionHistoryEntry')(data)
        if data.ledgerSeq is None:
            raise TypeError('data.ledgerSeq == None')
        self.pack_uint32(data.ledgerSeq)
        if data.txSet is None:
            raise TypeError('data.txSet == None')
        self.pack_TransactionSet(data.txSet)
        if data.ext is None:
            raise TypeError('data.ext == None')
        if data.ext.v is None:
            raise TypeError('data.ext.v == None')
        self.pack_int(data.ext.v)
        if data.ext.v == 0:
            pass
        else:
            raise XDRError('bad switch=%s' % data.ext.v)

    def pack_TransactionHistoryResultEntry(self, data):
        if hasattr(self, 'filter_TransactionHistoryResultEntry'):
            data = getattr(self, 'filter_TransactionHistoryResultEntry')(data)
        if data.ledgerSeq is None:
            raise TypeError('data.ledgerSeq == None')
        self.pack_uint32(data.ledgerSeq)
        if data.txResultSet is None:
            raise TypeError('data.txResultSet == None')
        self.pack_TransactionResultSet(data.txResultSet)
        if data.ext is None:
            raise TypeError('data.ext == None')
        if data.ext.v is None:
            raise TypeError('data.ext.v == None')
        self.pack_int(data.ext.v)
        if data.ext.v == 0:
            pass
        else:
            raise XDRError('bad switch=%s' % data.ext.v)

    def pack_LedgerHeaderHistoryEntry(self, data):
        if hasattr(self, 'filter_LedgerHeaderHistoryEntry'):
            data = getattr(self, 'filter_LedgerHeaderHistoryEntry')(data)
        if data.hash is None:
            raise TypeError('data.hash == None')
        self.pack_Hash(data.hash)
        if data.header is None:
            raise TypeError('data.header == None')
        self.pack_LedgerHeader(data.header)
        if data.ext is None:
            raise TypeError('data.ext == None')
        if data.ext.v is None:
            raise TypeError('data.ext.v == None')
        self.pack_int(data.ext.v)
        if data.ext.v == 0:
            pass
        else:
            raise XDRError('bad switch=%s' % data.ext.v)

    def pack_LedgerSCPMessages(self, data):
        if hasattr(self, 'filter_LedgerSCPMessages'):
            data = getattr(self, 'filter_LedgerSCPMessages')(data)
        if data.ledgerSeq is None:
            raise TypeError('data.ledgerSeq == None')
        self.pack_uint32(data.ledgerSeq)
        if data.messages is None:
            raise TypeError('data.messages == None')
        self.pack_array(data.messages, self.pack_SCPEnvelope)

    def pack_SCPHistoryEntryV0(self, data):
        if hasattr(self, 'filter_SCPHistoryEntryV0'):
            data = getattr(self, 'filter_SCPHistoryEntryV0')(data)
        if data.quorumSets is None:
            raise TypeError('data.quorumSets == None')
        self.pack_array(data.quorumSets, self.pack_SCPQuorumSet)
        if data.ledgerMessages is None:
            raise TypeError('data.ledgerMessages == None')
        self.pack_LedgerSCPMessages(data.ledgerMessages)

    def pack_SCPHistoryEntry(self, data):
        if hasattr(self, 'filter_SCPHistoryEntry'):
            data = getattr(self, 'filter_SCPHistoryEntry')(data)
        if data.v is None:
            raise TypeError('data.v == None')
        self.pack_int(data.v)
        if data.v == 0:
            if data.v0 is None:
                raise TypeError('data.v0 == None')
            self.pack_SCPHistoryEntryV0(data.v0)
        else:
            raise XDRError('bad switch=%s' % data.v)

    def pack_LedgerEntryChangeType(self, data):
        if hasattr(self, 'filter_LedgerEntryChangeType'):
            data = getattr(self, 'filter_LedgerEntryChangeType')(data)
        if self.check_enum and data not in [const.LEDGER_ENTRY_CREATED, const.LEDGER_ENTRY_UPDATED, const.LEDGER_ENTRY_REMOVED, const.LEDGER_ENTRY_STATE]:
            raise XDRError('value=%s not in enum LedgerEntryChangeType' % data)
        self.pack_int(data)

    def pack_LedgerEntryChange(self, data):
        if hasattr(self, 'filter_LedgerEntryChange'):
            data = getattr(self, 'filter_LedgerEntryChange')(data)
        if data.type is None:
            raise TypeError('data.type == None')
        self.pack_LedgerEntryChangeType(data.type)
        if data.type == const.LEDGER_ENTRY_CREATED:
            if data.created is None:
                raise TypeError('data.created == None')
            self.pack_LedgerEntry(data.created)
        elif data.type == const.LEDGER_ENTRY_UPDATED:
            if data.updated is None:
                raise TypeError('data.updated == None')
            self.pack_LedgerEntry(data.updated)
        elif data.type == const.LEDGER_ENTRY_REMOVED:
            if data.removed is None:
                raise TypeError('data.removed == None')
            self.pack_LedgerKey(data.removed)
        elif data.type == const.LEDGER_ENTRY_STATE:
            if data.state is None:
                raise TypeError('data.state == None')
            self.pack_LedgerEntry(data.state)
        else:
            raise XDRError('bad switch=%s' % data.type)

    def pack_LedgerEntryChanges(self, data):
        if hasattr(self, 'filter_LedgerEntryChanges'):
            data = getattr(self, 'filter_LedgerEntryChanges')(data)
        self.pack_array(data, self.pack_LedgerEntryChange)

    def pack_OperationMeta(self, data):
        if hasattr(self, 'filter_OperationMeta'):
            data = getattr(self, 'filter_OperationMeta')(data)
        if data.changes is None:
            raise TypeError('data.changes == None')
        self.pack_LedgerEntryChanges(data.changes)

    def pack_TransactionMetaV1(self, data):
        if hasattr(self, 'filter_TransactionMetaV1'):
            data = getattr(self, 'filter_TransactionMetaV1')(data)
        if data.txChanges is None:
            raise TypeError('data.txChanges == None')
        self.pack_LedgerEntryChanges(data.txChanges)
        if data.operations is None:
            raise TypeError('data.operations == None')
        self.pack_array(data.operations, self.pack_OperationMeta)

    def pack_TransactionMetaV2(self, data):
        if hasattr(self, 'filter_TransactionMetaV2'):
            data = getattr(self, 'filter_TransactionMetaV2')(data)
        if data.txChangesBefore is None:
            raise TypeError('data.txChangesBefore == None')
        self.pack_LedgerEntryChanges(data.txChangesBefore)
        if data.operations is None:
            raise TypeError('data.operations == None')
        self.pack_array(data.operations, self.pack_OperationMeta)
        if data.txChangesAfter is None:
            raise TypeError('data.txChangesAfter == None')
        self.pack_LedgerEntryChanges(data.txChangesAfter)

    def pack_TransactionMeta(self, data):
        if hasattr(self, 'filter_TransactionMeta'):
            data = getattr(self, 'filter_TransactionMeta')(data)
        if data.v is None:
            raise TypeError('data.v == None')
        self.pack_int(data.v)
        if data.v == 0:
            if data.operations is None:
                raise TypeError('data.operations == None')
            self.pack_array(data.operations, self.pack_OperationMeta)
        elif data.v == 1:
            if data.v1 is None:
                raise TypeError('data.v1 == None')
            self.pack_TransactionMetaV1(data.v1)
        elif data.v == 2:
            if data.v2 is None:
                raise TypeError('data.v2 == None')
            self.pack_TransactionMetaV2(data.v2)
        else:
            raise XDRError('bad switch=%s' % data.v)

    def pack_TransactionResultMeta(self, data):
        if hasattr(self, 'filter_TransactionResultMeta'):
            data = getattr(self, 'filter_TransactionResultMeta')(data)
        if data.result is None:
            raise TypeError('data.result == None')
        self.pack_TransactionResultPair(data.result)
        if data.feeProcessing is None:
            raise TypeError('data.feeProcessing == None')
        self.pack_LedgerEntryChanges(data.feeProcessing)
        if data.txApplyProcessing is None:
            raise TypeError('data.txApplyProcessing == None')
        self.pack_TransactionMeta(data.txApplyProcessing)

    def pack_UpgradeEntryMeta(self, data):
        if hasattr(self, 'filter_UpgradeEntryMeta'):
            data = getattr(self, 'filter_UpgradeEntryMeta')(data)
        if data.upgrade is None:
            raise TypeError('data.upgrade == None')
        self.pack_LedgerUpgrade(data.upgrade)
        if data.changes is None:
            raise TypeError('data.changes == None')
        self.pack_LedgerEntryChanges(data.changes)

    def pack_LedgerCloseMetaV0(self, data):
        if hasattr(self, 'filter_LedgerCloseMetaV0'):
            data = getattr(self, 'filter_LedgerCloseMetaV0')(data)
        if data.ledgerHeader is None:
            raise TypeError('data.ledgerHeader == None')
        self.pack_LedgerHeaderHistoryEntry(data.ledgerHeader)
        if data.txSet is None:
            raise TypeError('data.txSet == None')
        self.pack_TransactionSet(data.txSet)
        if data.txProcessing is None:
            raise TypeError('data.txProcessing == None')
        self.pack_array(data.txProcessing, self.pack_TransactionResultMeta)
        if data.upgradesProcessing is None:
            raise TypeError('data.upgradesProcessing == None')
        self.pack_array(data.upgradesProcessing, self.pack_UpgradeEntryMeta)
        if data.scpInfo is None:
            raise TypeError('data.scpInfo == None')
        self.pack_array(data.scpInfo, self.pack_SCPHistoryEntry)

    def pack_LedgerCloseMeta(self, data):
        if hasattr(self, 'filter_LedgerCloseMeta'):
            data = getattr(self, 'filter_LedgerCloseMeta')(data)
        if data.v is None:
            raise TypeError('data.v == None')
        self.pack_int(data.v)
        if data.v == 0:
            if data.v0 is None:
                raise TypeError('data.v0 == None')
            self.pack_LedgerCloseMetaV0(data.v0)
        else:
            raise XDRError('bad switch=%s' % data.v)

    pack_AccountID = pack_PublicKey

    def pack_Thresholds(self, data):
        if hasattr(self, 'filter_Thresholds'):
            data = getattr(self, 'filter_Thresholds')(data)
        self.pack_fopaque(4, data)

    def pack_string32(self, data):
        if hasattr(self, 'filter_string32'):
            data = getattr(self, 'filter_string32')(data)
        if len(data) > 32 and self.check_array:
            raise XDRError('array length too long for data')
        self.pack_string(data)

    def pack_string64(self, data):
        if hasattr(self, 'filter_string64'):
            data = getattr(self, 'filter_string64')(data)
        if len(data) > 64 and self.check_array:
            raise XDRError('array length too long for data')
        self.pack_string(data)

    pack_SequenceNumber = pack_int64

    pack_TimePoint = pack_uint64

    def pack_DataValue(self, data):
        if hasattr(self, 'filter_DataValue'):
            data = getattr(self, 'filter_DataValue')(data)
        if len(data) > 64 and self.check_array:
            raise XDRError('array length too long for data')
        self.pack_opaque(data)

    def pack_AssetCode4(self, data):
        if hasattr(self, 'filter_AssetCode4'):
            data = getattr(self, 'filter_AssetCode4')(data)
        self.pack_fopaque(4, data)

    def pack_AssetCode12(self, data):
        if hasattr(self, 'filter_AssetCode12'):
            data = getattr(self, 'filter_AssetCode12')(data)
        self.pack_fopaque(12, data)

    def pack_AssetType(self, data):
        if hasattr(self, 'filter_AssetType'):
            data = getattr(self, 'filter_AssetType')(data)
        if self.check_enum and data not in [const.ASSET_TYPE_NATIVE, const.ASSET_TYPE_CREDIT_ALPHANUM4, const.ASSET_TYPE_CREDIT_ALPHANUM12]:
            raise XDRError('value=%s not in enum AssetType' % data)
        self.pack_int(data)

    def pack_Asset(self, data):
        if hasattr(self, 'filter_Asset'):
            data = getattr(self, 'filter_Asset')(data)
        if data.type is None:
            raise TypeError('data.type == None')
        self.pack_AssetType(data.type)
        if data.type == const.ASSET_TYPE_NATIVE:
            pass
        elif data.type == const.ASSET_TYPE_CREDIT_ALPHANUM4:
            if data.alphaNum4 is None:
                raise TypeError('data.alphaNum4 == None')
            if data.alphaNum4.assetCode is None:
                raise TypeError('data.alphaNum4.assetCode == None')
            self.pack_AssetCode4(data.alphaNum4.assetCode)
            if data.alphaNum4.issuer is None:
                raise TypeError('data.alphaNum4.issuer == None')
            self.pack_AccountID(data.alphaNum4.issuer)
        elif data.type == const.ASSET_TYPE_CREDIT_ALPHANUM12:
            if data.alphaNum12 is None:
                raise TypeError('data.alphaNum12 == None')
            if data.alphaNum12.assetCode is None:
                raise TypeError('data.alphaNum12.assetCode == None')
            self.pack_AssetCode12(data.alphaNum12.assetCode)
            if data.alphaNum12.issuer is None:
                raise TypeError('data.alphaNum12.issuer == None')
            self.pack_AccountID(data.alphaNum12.issuer)
        else:
            raise XDRError('bad switch=%s' % data.type)

    def pack_Price(self, data):
        if hasattr(self, 'filter_Price'):
            data = getattr(self, 'filter_Price')(data)
        if data.n is None:
            raise TypeError('data.n == None')
        self.pack_int32(data.n)
        if data.d is None:
            raise TypeError('data.d == None')
        self.pack_int32(data.d)

    def pack_Liabilities(self, data):
        if hasattr(self, 'filter_Liabilities'):
            data = getattr(self, 'filter_Liabilities')(data)
        if data.buying is None:
            raise TypeError('data.buying == None')
        self.pack_int64(data.buying)
        if data.selling is None:
            raise TypeError('data.selling == None')
        self.pack_int64(data.selling)

    def pack_ThresholdIndexes(self, data):
        if hasattr(self, 'filter_ThresholdIndexes'):
            data = getattr(self, 'filter_ThresholdIndexes')(data)
        if self.check_enum and data not in [const.THRESHOLD_MASTER_WEIGHT, const.THRESHOLD_LOW, const.THRESHOLD_MED, const.THRESHOLD_HIGH]:
            raise XDRError('value=%s not in enum ThresholdIndexes' % data)
        self.pack_int(data)

    def pack_LedgerEntryType(self, data):
        if hasattr(self, 'filter_LedgerEntryType'):
            data = getattr(self, 'filter_LedgerEntryType')(data)
        if self.check_enum and data not in [const.ACCOUNT, const.TRUSTLINE, const.OFFER, const.DATA]:
            raise XDRError('value=%s not in enum LedgerEntryType' % data)
        self.pack_int(data)

    def pack_Signer(self, data):
        if hasattr(self, 'filter_Signer'):
            data = getattr(self, 'filter_Signer')(data)
        if data.key is None:
            raise TypeError('data.key == None')
        self.pack_SignerKey(data.key)
        if data.weight is None:
            raise TypeError('data.weight == None')
        self.pack_uint32(data.weight)

    def pack_AccountFlags(self, data):
        if hasattr(self, 'filter_AccountFlags'):
            data = getattr(self, 'filter_AccountFlags')(data)
        if self.check_enum and data not in [const.AUTH_REQUIRED_FLAG, const.AUTH_REVOCABLE_FLAG, const.AUTH_IMMUTABLE_FLAG]:
            raise XDRError('value=%s not in enum AccountFlags' % data)
        self.pack_int(data)

    def pack_AccountEntry(self, data):
        if hasattr(self, 'filter_AccountEntry'):
            data = getattr(self, 'filter_AccountEntry')(data)
        if data.accountID is None:
            raise TypeError('data.accountID == None')
        self.pack_AccountID(data.accountID)
        if data.balance is None:
            raise TypeError('data.balance == None')
        self.pack_int64(data.balance)
        if data.seqNum is None:
            raise TypeError('data.seqNum == None')
        self.pack_SequenceNumber(data.seqNum)
        if data.numSubEntries is None:
            raise TypeError('data.numSubEntries == None')
        self.pack_uint32(data.numSubEntries)
        if data.inflationDest is None:
            raise TypeError('data.inflationDest == None')
        if len(data.inflationDest) > 1 and self.check_array:
            raise XDRError('array length too long for data.inflationDest')
        self.pack_array(data.inflationDest, self.pack_AccountID)
        if data.flags is None:
            raise TypeError('data.flags == None')
        self.pack_uint32(data.flags)
        if data.homeDomain is None:
            raise TypeError('data.homeDomain == None')
        self.pack_string32(data.homeDomain)
        if data.thresholds is None:
            raise TypeError('data.thresholds == None')
        self.pack_Thresholds(data.thresholds)
        if data.signers is None:
            raise TypeError('data.signers == None')
        if len(data.signers) > 20 and self.check_array:
            raise XDRError('array length too long for data.signers')
        self.pack_array(data.signers, self.pack_Signer)
        if data.ext is None:
            raise TypeError('data.ext == None')
        if data.ext.v is None:
            raise TypeError('data.ext.v == None')
        self.pack_int(data.ext.v)
        if data.ext.v == 0:
            pass
        elif data.ext.v == 1:
            if data.ext.v1 is None:
                raise TypeError('data.ext.v1 == None')
            if data.ext.v1.liabilities is None:
                raise TypeError('data.ext.v1.liabilities == None')
            self.pack_Liabilities(data.ext.v1.liabilities)
            if data.ext.v1.ext is None:
                raise TypeError('data.ext.v1.ext == None')
            if data.ext.v1.ext.v is None:
                raise TypeError('data.ext.v1.ext.v == None')
            self.pack_int(data.ext.v1.ext.v)
            if data.ext.v1.ext.v == 0:
                pass
            else:
                raise XDRError('bad switch=%s' % data.ext.v1.ext.v)
        else:
            raise XDRError('bad switch=%s' % data.ext.v)

    def pack_TrustLineFlags(self, data):
        if hasattr(self, 'filter_TrustLineFlags'):
            data = getattr(self, 'filter_TrustLineFlags')(data)
        if self.check_enum and data not in [const.AUTHORIZED_FLAG]:
            raise XDRError('value=%s not in enum TrustLineFlags' % data)
        self.pack_int(data)

    def pack_TrustLineEntry(self, data):
        if hasattr(self, 'filter_TrustLineEntry'):
            data = getattr(self, 'filter_TrustLineEntry')(data)
        if data.accountID is None:
            raise TypeError('data.accountID == None')
        self.pack_AccountID(data.accountID)
        if data.asset is None:
            raise TypeError('data.asset == None')
        self.pack_Asset(data.asset)
        if data.balance is None:
            raise TypeError('data.balance == None')
        self.pack_int64(data.balance)
        if data.limit is None:
            raise TypeError('data.limit == None')
        self.pack_int64(data.limit)
        if data.flags is None:
            raise TypeError('data.flags == None')
        self.pack_uint32(data.flags)
        if data.ext is None:
            raise TypeError('data.ext == None')
        if data.ext.v is None:
            raise TypeError('data.ext.v == None')
        self.pack_int(data.ext.v)
        if data.ext.v == 0:
            pass
        elif data.ext.v == 1:
            if data.ext.v1 is None:
                raise TypeError('data.ext.v1 == None')
            if data.ext.v1.liabilities is None:
                raise TypeError('data.ext.v1.liabilities == None')
            self.pack_Liabilities(data.ext.v1.liabilities)
            if data.ext.v1.ext is None:
                raise TypeError('data.ext.v1.ext == None')
            if data.ext.v1.ext.v is None:
                raise TypeError('data.ext.v1.ext.v == None')
            self.pack_int(data.ext.v1.ext.v)
            if data.ext.v1.ext.v == 0:
                pass
            else:
                raise XDRError('bad switch=%s' % data.ext.v1.ext.v)
        else:
            raise XDRError('bad switch=%s' % data.ext.v)

    def pack_OfferEntryFlags(self, data):
        if hasattr(self, 'filter_OfferEntryFlags'):
            data = getattr(self, 'filter_OfferEntryFlags')(data)
        if self.check_enum and data not in [const.PASSIVE_FLAG]:
            raise XDRError('value=%s not in enum OfferEntryFlags' % data)
        self.pack_int(data)

    def pack_OfferEntry(self, data):
        if hasattr(self, 'filter_OfferEntry'):
            data = getattr(self, 'filter_OfferEntry')(data)
        if data.sellerID is None:
            raise TypeError('data.sellerID == None')
        self.pack_AccountID(data.sellerID)
        if data.offerID is None:
            raise TypeError('data.offerID == None')
        self.pack_int64(data.offerID)
        if data.selling is None:
            raise TypeError('data.selling == None')
        self.pack_Asset(data.selling)
        if data.buying is None:
            raise TypeError('data.buying == None')
        self.pack_Asset(data.buying)
        if data.amount is None:
            raise TypeError('data.amount == None')
        self.pack_int64(data.amount)
        if data.price is None:
            raise TypeError('data.price == None')
        self.pack_Price(data.price)
        if data.flags is None:
            raise TypeError('data.flags == None')
        self.pack_uint32(data.flags)
        if data.ext is None:
            raise TypeError('data.ext == None')
        if data.ext.v is None:
            raise TypeError('data.ext.v == None')
        self.pack_int(data.ext.v)
        if data.ext.v == 0:
            pass
        else:
            raise XDRError('bad switch=%s' % data.ext.v)

    def pack_DataEntry(self, data):
        if hasattr(self, 'filter_DataEntry'):
            data = getattr(self, 'filter_DataEntry')(data)
        if data.accountID is None:
            raise TypeError('data.accountID == None')
        self.pack_AccountID(data.accountID)
        if data.dataName is None:
            raise TypeError('data.dataName == None')
        self.pack_string64(data.dataName)
        if data.dataValue is None:
            raise TypeError('data.dataValue == None')
        self.pack_DataValue(data.dataValue)
        if data.ext is None:
            raise TypeError('data.ext == None')
        if data.ext.v is None:
            raise TypeError('data.ext.v == None')
        self.pack_int(data.ext.v)
        if data.ext.v == 0:
            pass
        else:
            raise XDRError('bad switch=%s' % data.ext.v)

    def pack_LedgerEntry(self, data):
        if hasattr(self, 'filter_LedgerEntry'):
            data = getattr(self, 'filter_LedgerEntry')(data)
        if data.lastModifiedLedgerSeq is None:
            raise TypeError('data.lastModifiedLedgerSeq == None')
        self.pack_uint32(data.lastModifiedLedgerSeq)
        if data.data is None:
            raise TypeError('data.data == None')
        if data.data.type is None:
            raise TypeError('data.data.type == None')
        self.pack_LedgerEntryType(data.data.type)
        if data.data.type == const.ACCOUNT:
            if data.data.account is None:
                raise TypeError('data.data.account == None')
            self.pack_AccountEntry(data.data.account)
        elif data.data.type == const.TRUSTLINE:
            if data.data.trustLine is None:
                raise TypeError('data.data.trustLine == None')
            self.pack_TrustLineEntry(data.data.trustLine)
        elif data.data.type == const.OFFER:
            if data.data.offer is None:
                raise TypeError('data.data.offer == None')
            self.pack_OfferEntry(data.data.offer)
        elif data.data.type == const.DATA:
            if data.data.data is None:
                raise TypeError('data.data.data == None')
            self.pack_DataEntry(data.data.data)
        else:
            raise XDRError('bad switch=%s' % data.data.type)
        if data.ext is None:
            raise TypeError('data.ext == None')
        if data.ext.v is None:
            raise TypeError('data.ext.v == None')
        self.pack_int(data.ext.v)
        if data.ext.v == 0:
            pass
        else:
            raise XDRError('bad switch=%s' % data.ext.v)

    def pack_EnvelopeType(self, data):
        if hasattr(self, 'filter_EnvelopeType'):
            data = getattr(self, 'filter_EnvelopeType')(data)
        if self.check_enum and data not in [const.ENVELOPE_TYPE_SCP, const.ENVELOPE_TYPE_TX, const.ENVELOPE_TYPE_AUTH, const.ENVELOPE_TYPE_SCPVALUE]:
            raise XDRError('value=%s not in enum EnvelopeType' % data)
        self.pack_int(data)

    def pack_DecoratedSignature(self, data):
        if hasattr(self, 'filter_DecoratedSignature'):
            data = getattr(self, 'filter_DecoratedSignature')(data)
        if data.hint is None:
            raise TypeError('data.hint == None')
        self.pack_SignatureHint(data.hint)
        if data.signature is None:
            raise TypeError('data.signature == None')
        self.pack_Signature(data.signature)

    def pack_OperationType(self, data):
        if hasattr(self, 'filter_OperationType'):
            data = getattr(self, 'filter_OperationType')(data)
        if self.check_enum and data not in [const.CREATE_ACCOUNT, const.PAYMENT, const.PATH_PAYMENT_STRICT_RECEIVE, const.MANAGE_SELL_OFFER, const.CREATE_PASSIVE_SELL_OFFER, const.SET_OPTIONS, const.CHANGE_TRUST, const.ALLOW_TRUST, const.ACCOUNT_MERGE, const.INFLATION, const.MANAGE_DATA, const.BUMP_SEQUENCE, const.MANAGE_BUY_OFFER, const.PATH_PAYMENT_STRICT_SEND]:
            raise XDRError('value=%s not in enum OperationType' % data)
        self.pack_int(data)

    def pack_CreateAccountOp(self, data):
        if hasattr(self, 'filter_CreateAccountOp'):
            data = getattr(self, 'filter_CreateAccountOp')(data)
        if data.destination is None:
            raise TypeError('data.destination == None')
        self.pack_AccountID(data.destination)
        if data.startingBalance is None:
            raise TypeError('data.startingBalance == None')
        self.pack_int64(data.startingBalance)

    def pack_PaymentOp(self, data):
        if hasattr(self, 'filter_PaymentOp'):
            data = getattr(self, 'filter_PaymentOp')(data)
        if data.destination is None:
            raise TypeError('data.destination == None')
        self.pack_AccountID(data.destination)
        if data.asset is None:
            raise TypeError('data.asset == None')
        self.pack_Asset(data.asset)
        if data.amount is None:
            raise TypeError('data.amount == None')
        self.pack_int64(data.amount)

    def pack_PathPaymentStrictReceiveOp(self, data):
        if hasattr(self, 'filter_PathPaymentStrictReceiveOp'):
            data = getattr(self, 'filter_PathPaymentStrictReceiveOp')(data)
        if data.sendAsset is None:
            raise TypeError('data.sendAsset == None')
        self.pack_Asset(data.sendAsset)
        if data.sendMax is None:
            raise TypeError('data.sendMax == None')
        self.pack_int64(data.sendMax)
        if data.destination is None:
            raise TypeError('data.destination == None')
        self.pack_AccountID(data.destination)
        if data.destAsset is None:
            raise TypeError('data.destAsset == None')
        self.pack_Asset(data.destAsset)
        if data.destAmount is None:
            raise TypeError('data.destAmount == None')
        self.pack_int64(data.destAmount)
        if data.path is None:
            raise TypeError('data.path == None')
        if len(data.path) > 5 and self.check_array:
            raise XDRError('array length too long for data.path')
        self.pack_array(data.path, self.pack_Asset)

    def pack_PathPaymentStrictSendOp(self, data):
        if hasattr(self, 'filter_PathPaymentStrictSendOp'):
            data = getattr(self, 'filter_PathPaymentStrictSendOp')(data)
        if data.sendAsset is None:
            raise TypeError('data.sendAsset == None')
        self.pack_Asset(data.sendAsset)
        if data.sendAmount is None:
            raise TypeError('data.sendAmount == None')
        self.pack_int64(data.sendAmount)
        if data.destination is None:
            raise TypeError('data.destination == None')
        self.pack_AccountID(data.destination)
        if data.destAsset is None:
            raise TypeError('data.destAsset == None')
        self.pack_Asset(data.destAsset)
        if data.destMin is None:
            raise TypeError('data.destMin == None')
        self.pack_int64(data.destMin)
        if data.path is None:
            raise TypeError('data.path == None')
        if len(data.path) > 5 and self.check_array:
            raise XDRError('array length too long for data.path')
        self.pack_array(data.path, self.pack_Asset)

    def pack_ManageSellOfferOp(self, data):
        if hasattr(self, 'filter_ManageSellOfferOp'):
            data = getattr(self, 'filter_ManageSellOfferOp')(data)
        if data.selling is None:
            raise TypeError('data.selling == None')
        self.pack_Asset(data.selling)
        if data.buying is None:
            raise TypeError('data.buying == None')
        self.pack_Asset(data.buying)
        if data.amount is None:
            raise TypeError('data.amount == None')
        self.pack_int64(data.amount)
        if data.price is None:
            raise TypeError('data.price == None')
        self.pack_Price(data.price)
        if data.offerID is None:
            raise TypeError('data.offerID == None')
        self.pack_int64(data.offerID)

    def pack_ManageBuyOfferOp(self, data):
        if hasattr(self, 'filter_ManageBuyOfferOp'):
            data = getattr(self, 'filter_ManageBuyOfferOp')(data)
        if data.selling is None:
            raise TypeError('data.selling == None')
        self.pack_Asset(data.selling)
        if data.buying is None:
            raise TypeError('data.buying == None')
        self.pack_Asset(data.buying)
        if data.buyAmount is None:
            raise TypeError('data.buyAmount == None')
        self.pack_int64(data.buyAmount)
        if data.price is None:
            raise TypeError('data.price == None')
        self.pack_Price(data.price)
        if data.offerID is None:
            raise TypeError('data.offerID == None')
        self.pack_int64(data.offerID)

    def pack_CreatePassiveSellOfferOp(self, data):
        if hasattr(self, 'filter_CreatePassiveSellOfferOp'):
            data = getattr(self, 'filter_CreatePassiveSellOfferOp')(data)
        if data.selling is None:
            raise TypeError('data.selling == None')
        self.pack_Asset(data.selling)
        if data.buying is None:
            raise TypeError('data.buying == None')
        self.pack_Asset(data.buying)
        if data.amount is None:
            raise TypeError('data.amount == None')
        self.pack_int64(data.amount)
        if data.price is None:
            raise TypeError('data.price == None')
        self.pack_Price(data.price)

    def pack_SetOptionsOp(self, data):
        if hasattr(self, 'filter_SetOptionsOp'):
            data = getattr(self, 'filter_SetOptionsOp')(data)
        if data.inflationDest is None:
            raise TypeError('data.inflationDest == None')
        if len(data.inflationDest) > 1 and self.check_array:
            raise XDRError('array length too long for data.inflationDest')
        self.pack_array(data.inflationDest, self.pack_AccountID)
        if data.clearFlags is None:
            raise TypeError('data.clearFlags == None')
        if len(data.clearFlags) > 1 and self.check_array:
            raise XDRError('array length too long for data.clearFlags')
        self.pack_array(data.clearFlags, self.pack_uint32)
        if data.setFlags is None:
            raise TypeError('data.setFlags == None')
        if len(data.setFlags) > 1 and self.check_array:
            raise XDRError('array length too long for data.setFlags')
        self.pack_array(data.setFlags, self.pack_uint32)
        if data.masterWeight is None:
            raise TypeError('data.masterWeight == None')
        if len(data.masterWeight) > 1 and self.check_array:
            raise XDRError('array length too long for data.masterWeight')
        self.pack_array(data.masterWeight, self.pack_uint32)
        if data.lowThreshold is None:
            raise TypeError('data.lowThreshold == None')
        if len(data.lowThreshold) > 1 and self.check_array:
            raise XDRError('array length too long for data.lowThreshold')
        self.pack_array(data.lowThreshold, self.pack_uint32)
        if data.medThreshold is None:
            raise TypeError('data.medThreshold == None')
        if len(data.medThreshold) > 1 and self.check_array:
            raise XDRError('array length too long for data.medThreshold')
        self.pack_array(data.medThreshold, self.pack_uint32)
        if data.highThreshold is None:
            raise TypeError('data.highThreshold == None')
        if len(data.highThreshold) > 1 and self.check_array:
            raise XDRError('array length too long for data.highThreshold')
        self.pack_array(data.highThreshold, self.pack_uint32)
        if data.homeDomain is None:
            raise TypeError('data.homeDomain == None')
        if len(data.homeDomain) > 1 and self.check_array:
            raise XDRError('array length too long for data.homeDomain')
        self.pack_array(data.homeDomain, self.pack_string32)
        if data.signer is None:
            raise TypeError('data.signer == None')
        if len(data.signer) > 1 and self.check_array:
            raise XDRError('array length too long for data.signer')
        self.pack_array(data.signer, self.pack_Signer)

    def pack_ChangeTrustOp(self, data):
        if hasattr(self, 'filter_ChangeTrustOp'):
            data = getattr(self, 'filter_ChangeTrustOp')(data)
        if data.line is None:
            raise TypeError('data.line == None')
        self.pack_Asset(data.line)
        if data.limit is None:
            raise TypeError('data.limit == None')
        self.pack_int64(data.limit)

    def pack_AllowTrustOp(self, data):
        if hasattr(self, 'filter_AllowTrustOp'):
            data = getattr(self, 'filter_AllowTrustOp')(data)
        if data.trustor is None:
            raise TypeError('data.trustor == None')
        self.pack_AccountID(data.trustor)
        if data.asset is None:
            raise TypeError('data.asset == None')
        if data.asset.type is None:
            raise TypeError('data.asset.type == None')
        self.pack_AssetType(data.asset.type)
        if data.asset.type == const.ASSET_TYPE_CREDIT_ALPHANUM4:
            if data.asset.assetCode4 is None:
                raise TypeError('data.asset.assetCode4 == None')
            self.pack_AssetCode4(data.asset.assetCode4)
        elif data.asset.type == const.ASSET_TYPE_CREDIT_ALPHANUM12:
            if data.asset.assetCode12 is None:
                raise TypeError('data.asset.assetCode12 == None')
            self.pack_AssetCode12(data.asset.assetCode12)
        else:
            raise XDRError('bad switch=%s' % data.asset.type)
        if data.authorize is None:
            raise TypeError('data.authorize == None')
        self.pack_bool(data.authorize)

    def pack_ManageDataOp(self, data):
        if hasattr(self, 'filter_ManageDataOp'):
            data = getattr(self, 'filter_ManageDataOp')(data)
        if data.dataName is None:
            raise TypeError('data.dataName == None')
        self.pack_string64(data.dataName)
        if data.dataValue is None:
            raise TypeError('data.dataValue == None')
        if len(data.dataValue) > 1 and self.check_array:
            raise XDRError('array length too long for data.dataValue')
        self.pack_array(data.dataValue, self.pack_DataValue)

    def pack_BumpSequenceOp(self, data):
        if hasattr(self, 'filter_BumpSequenceOp'):
            data = getattr(self, 'filter_BumpSequenceOp')(data)
        if data.bumpTo is None:
            raise TypeError('data.bumpTo == None')
        self.pack_SequenceNumber(data.bumpTo)

    def pack_Operation(self, data):
        if hasattr(self, 'filter_Operation'):
            data = getattr(self, 'filter_Operation')(data)
        if data.sourceAccount is None:
            raise TypeError('data.sourceAccount == None')
        if len(data.sourceAccount) > 1 and self.check_array:
            raise XDRError('array length too long for data.sourceAccount')
        self.pack_array(data.sourceAccount, self.pack_AccountID)
        if data.body is None:
            raise TypeError('data.body == None')
        if data.body.type is None:
            raise TypeError('data.body.type == None')
        self.pack_OperationType(data.body.type)
        if data.body.type == const.CREATE_ACCOUNT:
            if data.body.createAccountOp is None:
                raise TypeError('data.body.createAccountOp == None')
            self.pack_CreateAccountOp(data.body.createAccountOp)
        elif data.body.type == const.PAYMENT:
            if data.body.paymentOp is None:
                raise TypeError('data.body.paymentOp == None')
            self.pack_PaymentOp(data.body.paymentOp)
        elif data.body.type == const.PATH_PAYMENT_STRICT_RECEIVE:
            if data.body.pathPaymentStrictReceiveOp is None:
                raise TypeError('data.body.pathPaymentStrictReceiveOp == None')
            self.pack_PathPaymentStrictReceiveOp(data.body.pathPaymentStrictReceiveOp)
        elif data.body.type == const.MANAGE_SELL_OFFER:
            if data.body.manageSellOfferOp is None:
                raise TypeError('data.body.manageSellOfferOp == None')
            self.pack_ManageSellOfferOp(data.body.manageSellOfferOp)
        elif data.body.type == const.CREATE_PASSIVE_SELL_OFFER:
            if data.body.createPassiveSellOfferOp is None:
                raise TypeError('data.body.createPassiveSellOfferOp == None')
            self.pack_CreatePassiveSellOfferOp(data.body.createPassiveSellOfferOp)
        elif data.body.type == const.SET_OPTIONS:
            if data.body.setOptionsOp is None:
                raise TypeError('data.body.setOptionsOp == None')
            self.pack_SetOptionsOp(data.body.setOptionsOp)
        elif data.body.type == const.CHANGE_TRUST:
            if data.body.changeTrustOp is None:
                raise TypeError('data.body.changeTrustOp == None')
            self.pack_ChangeTrustOp(data.body.changeTrustOp)
        elif data.body.type == const.ALLOW_TRUST:
            if data.body.allowTrustOp is None:
                raise TypeError('data.body.allowTrustOp == None')
            self.pack_AllowTrustOp(data.body.allowTrustOp)
        elif data.body.type == const.ACCOUNT_MERGE:
            if data.body.destination is None:
                raise TypeError('data.body.destination == None')
            self.pack_AccountID(data.body.destination)
        elif data.body.type == const.INFLATION:
            pass
        elif data.body.type == const.MANAGE_DATA:
            if data.body.manageDataOp is None:
                raise TypeError('data.body.manageDataOp == None')
            self.pack_ManageDataOp(data.body.manageDataOp)
        elif data.body.type == const.BUMP_SEQUENCE:
            if data.body.bumpSequenceOp is None:
                raise TypeError('data.body.bumpSequenceOp == None')
            self.pack_BumpSequenceOp(data.body.bumpSequenceOp)
        elif data.body.type == const.MANAGE_BUY_OFFER:
            if data.body.manageBuyOfferOp is None:
                raise TypeError('data.body.manageBuyOfferOp == None')
            self.pack_ManageBuyOfferOp(data.body.manageBuyOfferOp)
        elif data.body.type == const.PATH_PAYMENT_STRICT_SEND:
            if data.body.pathPaymentStrictSendOp is None:
                raise TypeError('data.body.pathPaymentStrictSendOp == None')
            self.pack_PathPaymentStrictSendOp(data.body.pathPaymentStrictSendOp)
        else:
            raise XDRError('bad switch=%s' % data.body.type)

    def pack_MemoType(self, data):
        if hasattr(self, 'filter_MemoType'):
            data = getattr(self, 'filter_MemoType')(data)
        if self.check_enum and data not in [const.MEMO_NONE, const.MEMO_TEXT, const.MEMO_ID, const.MEMO_HASH, const.MEMO_RETURN]:
            raise XDRError('value=%s not in enum MemoType' % data)
        self.pack_int(data)

    def pack_Memo(self, data):
        if hasattr(self, 'filter_Memo'):
            data = getattr(self, 'filter_Memo')(data)
        if data.type is None:
            raise TypeError('data.type == None')
        self.pack_MemoType(data.type)
        if data.type == const.MEMO_NONE:
            pass
        elif data.type == const.MEMO_TEXT:
            if data.text is None:
                raise TypeError('data.text == None')
            if len(data.text) > 28 and self.check_array:
                raise XDRError('array length too long for data.text')
            self.pack_string(data.text)
        elif data.type == const.MEMO_ID:
            if data.id is None:
                raise TypeError('data.id == None')
            self.pack_uint64(data.id)
        elif data.type == const.MEMO_HASH:
            if data.hash is None:
                raise TypeError('data.hash == None')
            self.pack_Hash(data.hash)
        elif data.type == const.MEMO_RETURN:
            if data.retHash is None:
                raise TypeError('data.retHash == None')
            self.pack_Hash(data.retHash)
        else:
            raise XDRError('bad switch=%s' % data.type)

    def pack_TimeBounds(self, data):
        if hasattr(self, 'filter_TimeBounds'):
            data = getattr(self, 'filter_TimeBounds')(data)
        if data.minTime is None:
            raise TypeError('data.minTime == None')
        self.pack_TimePoint(data.minTime)
        if data.maxTime is None:
            raise TypeError('data.maxTime == None')
        self.pack_TimePoint(data.maxTime)

    def pack_Transaction(self, data):
        if hasattr(self, 'filter_Transaction'):
            data = getattr(self, 'filter_Transaction')(data)
        if data.sourceAccount is None:
            raise TypeError('data.sourceAccount == None')
        self.pack_AccountID(data.sourceAccount)
        if data.fee is None:
            raise TypeError('data.fee == None')
        self.pack_uint32(data.fee)
        if data.seqNum is None:
            raise TypeError('data.seqNum == None')
        self.pack_SequenceNumber(data.seqNum)
        if data.timeBounds is None:
            raise TypeError('data.timeBounds == None')
        if len(data.timeBounds) > 1 and self.check_array:
            raise XDRError('array length too long for data.timeBounds')
        self.pack_array(data.timeBounds, self.pack_TimeBounds)
        if data.memo is None:
            raise TypeError('data.memo == None')
        self.pack_Memo(data.memo)
        if data.operations is None:
            raise TypeError('data.operations == None')
        if len(data.operations) > const.MAX_OPS_PER_TX and self.check_array:
            raise XDRError('array length too long for data.operations')
        self.pack_array(data.operations, self.pack_Operation)
        if data.ext is None:
            raise TypeError('data.ext == None')
        if data.ext.v is None:
            raise TypeError('data.ext.v == None')
        self.pack_int(data.ext.v)
        if data.ext.v == 0:
            pass
        else:
            raise XDRError('bad switch=%s' % data.ext.v)

    def pack_TransactionSignaturePayload(self, data):
        if hasattr(self, 'filter_TransactionSignaturePayload'):
            data = getattr(self, 'filter_TransactionSignaturePayload')(data)
        if data.networkId is None:
            raise TypeError('data.networkId == None')
        self.pack_Hash(data.networkId)
        if data.taggedTransaction is None:
            raise TypeError('data.taggedTransaction == None')
        if data.taggedTransaction.type is None:
            raise TypeError('data.taggedTransaction.type == None')
        self.pack_EnvelopeType(data.taggedTransaction.type)
        if data.taggedTransaction.type == const.ENVELOPE_TYPE_TX:
            if data.taggedTransaction.tx is None:
                raise TypeError('data.taggedTransaction.tx == None')
            self.pack_Transaction(data.taggedTransaction.tx)
        else:
            raise XDRError('bad switch=%s' % data.taggedTransaction.type)

    def pack_TransactionEnvelope(self, data):
        if hasattr(self, 'filter_TransactionEnvelope'):
            data = getattr(self, 'filter_TransactionEnvelope')(data)
        if data.tx is None:
            raise TypeError('data.tx == None')
        self.pack_Transaction(data.tx)
        if data.signatures is None:
            raise TypeError('data.signatures == None')
        if len(data.signatures) > 20 and self.check_array:
            raise XDRError('array length too long for data.signatures')
        self.pack_array(data.signatures, self.pack_DecoratedSignature)

    def pack_ClaimOfferAtom(self, data):
        if hasattr(self, 'filter_ClaimOfferAtom'):
            data = getattr(self, 'filter_ClaimOfferAtom')(data)
        if data.sellerID is None:
            raise TypeError('data.sellerID == None')
        self.pack_AccountID(data.sellerID)
        if data.offerID is None:
            raise TypeError('data.offerID == None')
        self.pack_int64(data.offerID)
        if data.assetSold is None:
            raise TypeError('data.assetSold == None')
        self.pack_Asset(data.assetSold)
        if data.amountSold is None:
            raise TypeError('data.amountSold == None')
        self.pack_int64(data.amountSold)
        if data.assetBought is None:
            raise TypeError('data.assetBought == None')
        self.pack_Asset(data.assetBought)
        if data.amountBought is None:
            raise TypeError('data.amountBought == None')
        self.pack_int64(data.amountBought)

    def pack_CreateAccountResultCode(self, data):
        if hasattr(self, 'filter_CreateAccountResultCode'):
            data = getattr(self, 'filter_CreateAccountResultCode')(data)
        if self.check_enum and data not in [const.CREATE_ACCOUNT_SUCCESS, const.CREATE_ACCOUNT_MALFORMED, const.CREATE_ACCOUNT_UNDERFUNDED, const.CREATE_ACCOUNT_LOW_RESERVE, const.CREATE_ACCOUNT_ALREADY_EXIST]:
            raise XDRError('value=%s not in enum CreateAccountResultCode' % data)
        self.pack_int(data)

    def pack_CreateAccountResult(self, data):
        if hasattr(self, 'filter_CreateAccountResult'):
            data = getattr(self, 'filter_CreateAccountResult')(data)
        if data.code is None:
            raise TypeError('data.code == None')
        self.pack_CreateAccountResultCode(data.code)
        if data.code == const.CREATE_ACCOUNT_SUCCESS:
            pass
        else:
            pass

    def pack_PaymentResultCode(self, data):
        if hasattr(self, 'filter_PaymentResultCode'):
            data = getattr(self, 'filter_PaymentResultCode')(data)
        if self.check_enum and data not in [const.PAYMENT_SUCCESS, const.PAYMENT_MALFORMED, const.PAYMENT_UNDERFUNDED, const.PAYMENT_SRC_NO_TRUST, const.PAYMENT_SRC_NOT_AUTHORIZED, const.PAYMENT_NO_DESTINATION, const.PAYMENT_NO_TRUST, const.PAYMENT_NOT_AUTHORIZED, const.PAYMENT_LINE_FULL, const.PAYMENT_NO_ISSUER]:
            raise XDRError('value=%s not in enum PaymentResultCode' % data)
        self.pack_int(data)

    def pack_PaymentResult(self, data):
        if hasattr(self, 'filter_PaymentResult'):
            data = getattr(self, 'filter_PaymentResult')(data)
        if data.code is None:
            raise TypeError('data.code == None')
        self.pack_PaymentResultCode(data.code)
        if data.code == const.PAYMENT_SUCCESS:
            pass
        else:
            pass

    def pack_PathPaymentStrictReceiveResultCode(self, data):
        if hasattr(self, 'filter_PathPaymentStrictReceiveResultCode'):
            data = getattr(self, 'filter_PathPaymentStrictReceiveResultCode')(data)
        if self.check_enum and data not in [const.PATH_PAYMENT_STRICT_RECEIVE_SUCCESS, const.PATH_PAYMENT_STRICT_RECEIVE_MALFORMED, const.PATH_PAYMENT_STRICT_RECEIVE_UNDERFUNDED, const.PATH_PAYMENT_STRICT_RECEIVE_SRC_NO_TRUST, const.PATH_PAYMENT_STRICT_RECEIVE_SRC_NOT_AUTHORIZED, const.PATH_PAYMENT_STRICT_RECEIVE_NO_DESTINATION, const.PATH_PAYMENT_STRICT_RECEIVE_NO_TRUST, const.PATH_PAYMENT_STRICT_RECEIVE_NOT_AUTHORIZED, const.PATH_PAYMENT_STRICT_RECEIVE_LINE_FULL, const.PATH_PAYMENT_STRICT_RECEIVE_NO_ISSUER, const.PATH_PAYMENT_STRICT_RECEIVE_TOO_FEW_OFFERS, const.PATH_PAYMENT_STRICT_RECEIVE_OFFER_CROSS_SELF, const.PATH_PAYMENT_STRICT_RECEIVE_OVER_SENDMAX]:
            raise XDRError('value=%s not in enum PathPaymentStrictReceiveResultCode' % data)
        self.pack_int(data)

    def pack_SimplePaymentResult(self, data):
        if hasattr(self, 'filter_SimplePaymentResult'):
            data = getattr(self, 'filter_SimplePaymentResult')(data)
        if data.destination is None:
            raise TypeError('data.destination == None')
        self.pack_AccountID(data.destination)
        if data.asset is None:
            raise TypeError('data.asset == None')
        self.pack_Asset(data.asset)
        if data.amount is None:
            raise TypeError('data.amount == None')
        self.pack_int64(data.amount)

    def pack_PathPaymentStrictReceiveResult(self, data):
        if hasattr(self, 'filter_PathPaymentStrictReceiveResult'):
            data = getattr(self, 'filter_PathPaymentStrictReceiveResult')(data)
        if data.code is None:
            raise TypeError('data.code == None')
        self.pack_PathPaymentStrictReceiveResultCode(data.code)
        if data.code == const.PATH_PAYMENT_STRICT_RECEIVE_SUCCESS:
            if data.success is None:
                raise TypeError('data.success == None')
            if data.success.offers is None:
                raise TypeError('data.success.offers == None')
            self.pack_array(data.success.offers, self.pack_ClaimOfferAtom)
            if data.success.last is None:
                raise TypeError('data.success.last == None')
            self.pack_SimplePaymentResult(data.success.last)
        elif data.code == const.PATH_PAYMENT_STRICT_RECEIVE_NO_ISSUER:
            if data.noIssuer is None:
                raise TypeError('data.noIssuer == None')
            self.pack_Asset(data.noIssuer)
        else:
            pass

    def pack_PathPaymentStrictSendResultCode(self, data):
        if hasattr(self, 'filter_PathPaymentStrictSendResultCode'):
            data = getattr(self, 'filter_PathPaymentStrictSendResultCode')(data)
        if self.check_enum and data not in [const.PATH_PAYMENT_STRICT_SEND_SUCCESS, const.PATH_PAYMENT_STRICT_SEND_MALFORMED, const.PATH_PAYMENT_STRICT_SEND_UNDERFUNDED, const.PATH_PAYMENT_STRICT_SEND_SRC_NO_TRUST, const.PATH_PAYMENT_STRICT_SEND_SRC_NOT_AUTHORIZED, const.PATH_PAYMENT_STRICT_SEND_NO_DESTINATION, const.PATH_PAYMENT_STRICT_SEND_NO_TRUST, const.PATH_PAYMENT_STRICT_SEND_NOT_AUTHORIZED, const.PATH_PAYMENT_STRICT_SEND_LINE_FULL, const.PATH_PAYMENT_STRICT_SEND_NO_ISSUER, const.PATH_PAYMENT_STRICT_SEND_TOO_FEW_OFFERS, const.PATH_PAYMENT_STRICT_SEND_OFFER_CROSS_SELF, const.PATH_PAYMENT_STRICT_SEND_UNDER_DESTMIN]:
            raise XDRError('value=%s not in enum PathPaymentStrictSendResultCode' % data)
        self.pack_int(data)

    def pack_PathPaymentStrictSendResult(self, data):
        if hasattr(self, 'filter_PathPaymentStrictSendResult'):
            data = getattr(self, 'filter_PathPaymentStrictSendResult')(data)
        if data.code is None:
            raise TypeError('data.code == None')
        self.pack_PathPaymentStrictSendResultCode(data.code)
        if data.code == const.PATH_PAYMENT_STRICT_SEND_SUCCESS:
            if data.success is None:
                raise TypeError('data.success == None')
            if data.success.offers is None:
                raise TypeError('data.success.offers == None')
            self.pack_array(data.success.offers, self.pack_ClaimOfferAtom)
            if data.success.last is None:
                raise TypeError('data.success.last == None')
            self.pack_SimplePaymentResult(data.success.last)
        elif data.code == const.PATH_PAYMENT_STRICT_SEND_NO_ISSUER:
            if data.noIssuer is None:
                raise TypeError('data.noIssuer == None')
            self.pack_Asset(data.noIssuer)
        else:
            pass

    def pack_ManageSellOfferResultCode(self, data):
        if hasattr(self, 'filter_ManageSellOfferResultCode'):
            data = getattr(self, 'filter_ManageSellOfferResultCode')(data)
        if self.check_enum and data not in [const.MANAGE_SELL_OFFER_SUCCESS, const.MANAGE_SELL_OFFER_MALFORMED, const.MANAGE_SELL_OFFER_SELL_NO_TRUST, const.MANAGE_SELL_OFFER_BUY_NO_TRUST, const.MANAGE_SELL_OFFER_SELL_NOT_AUTHORIZED, const.MANAGE_SELL_OFFER_BUY_NOT_AUTHORIZED, const.MANAGE_SELL_OFFER_LINE_FULL, const.MANAGE_SELL_OFFER_UNDERFUNDED, const.MANAGE_SELL_OFFER_CROSS_SELF, const.MANAGE_SELL_OFFER_SELL_NO_ISSUER, const.MANAGE_SELL_OFFER_BUY_NO_ISSUER, const.MANAGE_SELL_OFFER_NOT_FOUND, const.MANAGE_SELL_OFFER_LOW_RESERVE]:
            raise XDRError('value=%s not in enum ManageSellOfferResultCode' % data)
        self.pack_int(data)

    def pack_ManageOfferEffect(self, data):
        if hasattr(self, 'filter_ManageOfferEffect'):
            data = getattr(self, 'filter_ManageOfferEffect')(data)
        if self.check_enum and data not in [const.MANAGE_OFFER_CREATED, const.MANAGE_OFFER_UPDATED, const.MANAGE_OFFER_DELETED]:
            raise XDRError('value=%s not in enum ManageOfferEffect' % data)
        self.pack_int(data)

    def pack_ManageOfferSuccessResult(self, data):
        if hasattr(self, 'filter_ManageOfferSuccessResult'):
            data = getattr(self, 'filter_ManageOfferSuccessResult')(data)
        if data.offersClaimed is None:
            raise TypeError('data.offersClaimed == None')
        self.pack_array(data.offersClaimed, self.pack_ClaimOfferAtom)
        if data.offer is None:
            raise TypeError('data.offer == None')
        if data.offer.effect is None:
            raise TypeError('data.offer.effect == None')
        self.pack_ManageOfferEffect(data.offer.effect)
        if data.offer.effect == const.MANAGE_OFFER_CREATED or data.offer.effect == const.MANAGE_OFFER_UPDATED:
            if data.offer.offer is None:
                raise TypeError('data.offer.offer == None')
            self.pack_OfferEntry(data.offer.offer)
        else:
            pass

    def pack_ManageSellOfferResult(self, data):
        if hasattr(self, 'filter_ManageSellOfferResult'):
            data = getattr(self, 'filter_ManageSellOfferResult')(data)
        if data.code is None:
            raise TypeError('data.code == None')
        self.pack_ManageSellOfferResultCode(data.code)
        if data.code == const.MANAGE_SELL_OFFER_SUCCESS:
            if data.success is None:
                raise TypeError('data.success == None')
            self.pack_ManageOfferSuccessResult(data.success)
        else:
            pass

    def pack_ManageBuyOfferResultCode(self, data):
        if hasattr(self, 'filter_ManageBuyOfferResultCode'):
            data = getattr(self, 'filter_ManageBuyOfferResultCode')(data)
        if self.check_enum and data not in [const.MANAGE_BUY_OFFER_SUCCESS, const.MANAGE_BUY_OFFER_MALFORMED, const.MANAGE_BUY_OFFER_SELL_NO_TRUST, const.MANAGE_BUY_OFFER_BUY_NO_TRUST, const.MANAGE_BUY_OFFER_SELL_NOT_AUTHORIZED, const.MANAGE_BUY_OFFER_BUY_NOT_AUTHORIZED, const.MANAGE_BUY_OFFER_LINE_FULL, const.MANAGE_BUY_OFFER_UNDERFUNDED, const.MANAGE_BUY_OFFER_CROSS_SELF, const.MANAGE_BUY_OFFER_SELL_NO_ISSUER, const.MANAGE_BUY_OFFER_BUY_NO_ISSUER, const.MANAGE_BUY_OFFER_NOT_FOUND, const.MANAGE_BUY_OFFER_LOW_RESERVE]:
            raise XDRError('value=%s not in enum ManageBuyOfferResultCode' % data)
        self.pack_int(data)

    def pack_ManageBuyOfferResult(self, data):
        if hasattr(self, 'filter_ManageBuyOfferResult'):
            data = getattr(self, 'filter_ManageBuyOfferResult')(data)
        if data.code is None:
            raise TypeError('data.code == None')
        self.pack_ManageBuyOfferResultCode(data.code)
        if data.code == const.MANAGE_BUY_OFFER_SUCCESS:
            if data.success is None:
                raise TypeError('data.success == None')
            self.pack_ManageOfferSuccessResult(data.success)
        else:
            pass

    def pack_SetOptionsResultCode(self, data):
        if hasattr(self, 'filter_SetOptionsResultCode'):
            data = getattr(self, 'filter_SetOptionsResultCode')(data)
        if self.check_enum and data not in [const.SET_OPTIONS_SUCCESS, const.SET_OPTIONS_LOW_RESERVE, const.SET_OPTIONS_TOO_MANY_SIGNERS, const.SET_OPTIONS_BAD_FLAGS, const.SET_OPTIONS_INVALID_INFLATION, const.SET_OPTIONS_CANT_CHANGE, const.SET_OPTIONS_UNKNOWN_FLAG, const.SET_OPTIONS_THRESHOLD_OUT_OF_RANGE, const.SET_OPTIONS_BAD_SIGNER, const.SET_OPTIONS_INVALID_HOME_DOMAIN]:
            raise XDRError('value=%s not in enum SetOptionsResultCode' % data)
        self.pack_int(data)

    def pack_SetOptionsResult(self, data):
        if hasattr(self, 'filter_SetOptionsResult'):
            data = getattr(self, 'filter_SetOptionsResult')(data)
        if data.code is None:
            raise TypeError('data.code == None')
        self.pack_SetOptionsResultCode(data.code)
        if data.code == const.SET_OPTIONS_SUCCESS:
            pass
        else:
            pass

    def pack_ChangeTrustResultCode(self, data):
        if hasattr(self, 'filter_ChangeTrustResultCode'):
            data = getattr(self, 'filter_ChangeTrustResultCode')(data)
        if self.check_enum and data not in [const.CHANGE_TRUST_SUCCESS, const.CHANGE_TRUST_MALFORMED, const.CHANGE_TRUST_NO_ISSUER, const.CHANGE_TRUST_INVALID_LIMIT, const.CHANGE_TRUST_LOW_RESERVE, const.CHANGE_TRUST_SELF_NOT_ALLOWED]:
            raise XDRError('value=%s not in enum ChangeTrustResultCode' % data)
        self.pack_int(data)

    def pack_ChangeTrustResult(self, data):
        if hasattr(self, 'filter_ChangeTrustResult'):
            data = getattr(self, 'filter_ChangeTrustResult')(data)
        if data.code is None:
            raise TypeError('data.code == None')
        self.pack_ChangeTrustResultCode(data.code)
        if data.code == const.CHANGE_TRUST_SUCCESS:
            pass
        else:
            pass

    def pack_AllowTrustResultCode(self, data):
        if hasattr(self, 'filter_AllowTrustResultCode'):
            data = getattr(self, 'filter_AllowTrustResultCode')(data)
        if self.check_enum and data not in [const.ALLOW_TRUST_SUCCESS, const.ALLOW_TRUST_MALFORMED, const.ALLOW_TRUST_NO_TRUST_LINE, const.ALLOW_TRUST_TRUST_NOT_REQUIRED, const.ALLOW_TRUST_CANT_REVOKE, const.ALLOW_TRUST_SELF_NOT_ALLOWED]:
            raise XDRError('value=%s not in enum AllowTrustResultCode' % data)
        self.pack_int(data)

    def pack_AllowTrustResult(self, data):
        if hasattr(self, 'filter_AllowTrustResult'):
            data = getattr(self, 'filter_AllowTrustResult')(data)
        if data.code is None:
            raise TypeError('data.code == None')
        self.pack_AllowTrustResultCode(data.code)
        if data.code == const.ALLOW_TRUST_SUCCESS:
            pass
        else:
            pass

    def pack_AccountMergeResultCode(self, data):
        if hasattr(self, 'filter_AccountMergeResultCode'):
            data = getattr(self, 'filter_AccountMergeResultCode')(data)
        if self.check_enum and data not in [const.ACCOUNT_MERGE_SUCCESS, const.ACCOUNT_MERGE_MALFORMED, const.ACCOUNT_MERGE_NO_ACCOUNT, const.ACCOUNT_MERGE_IMMUTABLE_SET, const.ACCOUNT_MERGE_HAS_SUB_ENTRIES, const.ACCOUNT_MERGE_SEQNUM_TOO_FAR, const.ACCOUNT_MERGE_DEST_FULL]:
            raise XDRError('value=%s not in enum AccountMergeResultCode' % data)
        self.pack_int(data)

    def pack_AccountMergeResult(self, data):
        if hasattr(self, 'filter_AccountMergeResult'):
            data = getattr(self, 'filter_AccountMergeResult')(data)
        if data.code is None:
            raise TypeError('data.code == None')
        self.pack_AccountMergeResultCode(data.code)
        if data.code == const.ACCOUNT_MERGE_SUCCESS:
            if data.sourceAccountBalance is None:
                raise TypeError('data.sourceAccountBalance == None')
            self.pack_int64(data.sourceAccountBalance)
        else:
            pass

    def pack_InflationResultCode(self, data):
        if hasattr(self, 'filter_InflationResultCode'):
            data = getattr(self, 'filter_InflationResultCode')(data)
        if self.check_enum and data not in [const.INFLATION_SUCCESS, const.INFLATION_NOT_TIME]:
            raise XDRError('value=%s not in enum InflationResultCode' % data)
        self.pack_int(data)

    def pack_InflationPayout(self, data):
        if hasattr(self, 'filter_InflationPayout'):
            data = getattr(self, 'filter_InflationPayout')(data)
        if data.destination is None:
            raise TypeError('data.destination == None')
        self.pack_AccountID(data.destination)
        if data.amount is None:
            raise TypeError('data.amount == None')
        self.pack_int64(data.amount)

    def pack_InflationResult(self, data):
        if hasattr(self, 'filter_InflationResult'):
            data = getattr(self, 'filter_InflationResult')(data)
        if data.code is None:
            raise TypeError('data.code == None')
        self.pack_InflationResultCode(data.code)
        if data.code == const.INFLATION_SUCCESS:
            if data.payouts is None:
                raise TypeError('data.payouts == None')
            self.pack_array(data.payouts, self.pack_InflationPayout)
        else:
            pass

    def pack_ManageDataResultCode(self, data):
        if hasattr(self, 'filter_ManageDataResultCode'):
            data = getattr(self, 'filter_ManageDataResultCode')(data)
        if self.check_enum and data not in [const.MANAGE_DATA_SUCCESS, const.MANAGE_DATA_NOT_SUPPORTED_YET, const.MANAGE_DATA_NAME_NOT_FOUND, const.MANAGE_DATA_LOW_RESERVE, const.MANAGE_DATA_INVALID_NAME]:
            raise XDRError('value=%s not in enum ManageDataResultCode' % data)
        self.pack_int(data)

    def pack_ManageDataResult(self, data):
        if hasattr(self, 'filter_ManageDataResult'):
            data = getattr(self, 'filter_ManageDataResult')(data)
        if data.code is None:
            raise TypeError('data.code == None')
        self.pack_ManageDataResultCode(data.code)
        if data.code == const.MANAGE_DATA_SUCCESS:
            pass
        else:
            pass

    def pack_BumpSequenceResultCode(self, data):
        if hasattr(self, 'filter_BumpSequenceResultCode'):
            data = getattr(self, 'filter_BumpSequenceResultCode')(data)
        if self.check_enum and data not in [const.BUMP_SEQUENCE_SUCCESS, const.BUMP_SEQUENCE_BAD_SEQ]:
            raise XDRError('value=%s not in enum BumpSequenceResultCode' % data)
        self.pack_int(data)

    def pack_BumpSequenceResult(self, data):
        if hasattr(self, 'filter_BumpSequenceResult'):
            data = getattr(self, 'filter_BumpSequenceResult')(data)
        if data.code is None:
            raise TypeError('data.code == None')
        self.pack_BumpSequenceResultCode(data.code)
        if data.code == const.BUMP_SEQUENCE_SUCCESS:
            pass
        else:
            pass

    def pack_OperationResultCode(self, data):
        if hasattr(self, 'filter_OperationResultCode'):
            data = getattr(self, 'filter_OperationResultCode')(data)
        if self.check_enum and data not in [const.opINNER, const.opBAD_AUTH, const.opNO_ACCOUNT, const.opNOT_SUPPORTED, const.opTOO_MANY_SUBENTRIES, const.opEXCEEDED_WORK_LIMIT]:
            raise XDRError('value=%s not in enum OperationResultCode' % data)
        self.pack_int(data)

    def pack_OperationResult(self, data):
        if hasattr(self, 'filter_OperationResult'):
            data = getattr(self, 'filter_OperationResult')(data)
        if data.code is None:
            raise TypeError('data.code == None')
        self.pack_OperationResultCode(data.code)
        if data.code == const.opINNER:
            if data.tr is None:
                raise TypeError('data.tr == None')
            if data.tr.type is None:
                raise TypeError('data.tr.type == None')
            self.pack_OperationType(data.tr.type)
            if data.tr.type == const.CREATE_ACCOUNT:
                if data.tr.createAccountResult is None:
                    raise TypeError('data.tr.createAccountResult == None')
                self.pack_CreateAccountResult(data.tr.createAccountResult)
            elif data.tr.type == const.PAYMENT:
                if data.tr.paymentResult is None:
                    raise TypeError('data.tr.paymentResult == None')
                self.pack_PaymentResult(data.tr.paymentResult)
            elif data.tr.type == const.PATH_PAYMENT_STRICT_RECEIVE:
                if data.tr.pathPaymentStrictReceiveResult is None:
                    raise TypeError('data.tr.pathPaymentStrictReceiveResult == None')
                self.pack_PathPaymentStrictReceiveResult(data.tr.pathPaymentStrictReceiveResult)
            elif data.tr.type == const.MANAGE_SELL_OFFER:
                if data.tr.manageSellOfferResult is None:
                    raise TypeError('data.tr.manageSellOfferResult == None')
                self.pack_ManageSellOfferResult(data.tr.manageSellOfferResult)
            elif data.tr.type == const.CREATE_PASSIVE_SELL_OFFER:
                if data.tr.createPassiveSellOfferResult is None:
                    raise TypeError('data.tr.createPassiveSellOfferResult == None')
                self.pack_ManageSellOfferResult(data.tr.createPassiveSellOfferResult)
            elif data.tr.type == const.SET_OPTIONS:
                if data.tr.setOptionsResult is None:
                    raise TypeError('data.tr.setOptionsResult == None')
                self.pack_SetOptionsResult(data.tr.setOptionsResult)
            elif data.tr.type == const.CHANGE_TRUST:
                if data.tr.changeTrustResult is None:
                    raise TypeError('data.tr.changeTrustResult == None')
                self.pack_ChangeTrustResult(data.tr.changeTrustResult)
            elif data.tr.type == const.ALLOW_TRUST:
                if data.tr.allowTrustResult is None:
                    raise TypeError('data.tr.allowTrustResult == None')
                self.pack_AllowTrustResult(data.tr.allowTrustResult)
            elif data.tr.type == const.ACCOUNT_MERGE:
                if data.tr.accountMergeResult is None:
                    raise TypeError('data.tr.accountMergeResult == None')
                self.pack_AccountMergeResult(data.tr.accountMergeResult)
            elif data.tr.type == const.INFLATION:
                if data.tr.inflationResult is None:
                    raise TypeError('data.tr.inflationResult == None')
                self.pack_InflationResult(data.tr.inflationResult)
            elif data.tr.type == const.MANAGE_DATA:
                if data.tr.manageDataResult is None:
                    raise TypeError('data.tr.manageDataResult == None')
                self.pack_ManageDataResult(data.tr.manageDataResult)
            elif data.tr.type == const.BUMP_SEQUENCE:
                if data.tr.bumpSeqResult is None:
                    raise TypeError('data.tr.bumpSeqResult == None')
                self.pack_BumpSequenceResult(data.tr.bumpSeqResult)
            elif data.tr.type == const.MANAGE_BUY_OFFER:
                if data.tr.manageBuyOfferResult is None:
                    raise TypeError('data.tr.manageBuyOfferResult == None')
                self.pack_ManageBuyOfferResult(data.tr.manageBuyOfferResult)
            elif data.tr.type == const.PATH_PAYMENT_STRICT_SEND:
                if data.tr.pathPaymentStrictSendResult is None:
                    raise TypeError('data.tr.pathPaymentStrictSendResult == None')
                self.pack_PathPaymentStrictSendResult(data.tr.pathPaymentStrictSendResult)
            else:
                raise XDRError('bad switch=%s' % data.tr.type)
        else:
            pass

    def pack_TransactionResultCode(self, data):
        if hasattr(self, 'filter_TransactionResultCode'):
            data = getattr(self, 'filter_TransactionResultCode')(data)
        if self.check_enum and data not in [const.txSUCCESS, const.txFAILED, const.txTOO_EARLY, const.txTOO_LATE, const.txMISSING_OPERATION, const.txBAD_SEQ, const.txBAD_AUTH, const.txINSUFFICIENT_BALANCE, const.txNO_ACCOUNT, const.txINSUFFICIENT_FEE, const.txBAD_AUTH_EXTRA, const.txINTERNAL_ERROR]:
            raise XDRError('value=%s not in enum TransactionResultCode' % data)
        self.pack_int(data)

    def pack_TransactionResult(self, data):
        if hasattr(self, 'filter_TransactionResult'):
            data = getattr(self, 'filter_TransactionResult')(data)
        if data.feeCharged is None:
            raise TypeError('data.feeCharged == None')
        self.pack_int64(data.feeCharged)
        if data.result is None:
            raise TypeError('data.result == None')
        if data.result.code is None:
            raise TypeError('data.result.code == None')
        self.pack_TransactionResultCode(data.result.code)
        if data.result.code == const.txSUCCESS or data.result.code == const.txFAILED:
            if data.result.results is None:
                raise TypeError('data.result.results == None')
            self.pack_array(data.result.results, self.pack_OperationResult)
        else:
            pass
        if data.ext is None:
            raise TypeError('data.ext == None')
        if data.ext.v is None:
            raise TypeError('data.ext.v == None')
        self.pack_int(data.ext.v)
        if data.ext.v == 0:
            pass
        else:
            raise XDRError('bad switch=%s' % data.ext.v)

    def pack_ErrorCode(self, data):
        if hasattr(self, 'filter_ErrorCode'):
            data = getattr(self, 'filter_ErrorCode')(data)
        if self.check_enum and data not in [const.ERR_MISC, const.ERR_DATA, const.ERR_CONF, const.ERR_AUTH, const.ERR_LOAD]:
            raise XDRError('value=%s not in enum ErrorCode' % data)
        self.pack_int(data)

    def pack_Error(self, data):
        if hasattr(self, 'filter_Error'):
            data = getattr(self, 'filter_Error')(data)
        if data.code is None:
            raise TypeError('data.code == None')
        self.pack_ErrorCode(data.code)
        if data.msg is None:
            raise TypeError('data.msg == None')
        if len(data.msg) > 100 and self.check_array:
            raise XDRError('array length too long for data.msg')
        self.pack_string(data.msg)

    def pack_AuthCert(self, data):
        if hasattr(self, 'filter_AuthCert'):
            data = getattr(self, 'filter_AuthCert')(data)
        if data.pubkey is None:
            raise TypeError('data.pubkey == None')
        self.pack_Curve25519Public(data.pubkey)
        if data.expiration is None:
            raise TypeError('data.expiration == None')
        self.pack_uint64(data.expiration)
        if data.sig is None:
            raise TypeError('data.sig == None')
        self.pack_Signature(data.sig)

    def pack_Hello(self, data):
        if hasattr(self, 'filter_Hello'):
            data = getattr(self, 'filter_Hello')(data)
        if data.ledgerVersion is None:
            raise TypeError('data.ledgerVersion == None')
        self.pack_uint32(data.ledgerVersion)
        if data.overlayVersion is None:
            raise TypeError('data.overlayVersion == None')
        self.pack_uint32(data.overlayVersion)
        if data.overlayMinVersion is None:
            raise TypeError('data.overlayMinVersion == None')
        self.pack_uint32(data.overlayMinVersion)
        if data.networkID is None:
            raise TypeError('data.networkID == None')
        self.pack_Hash(data.networkID)
        if data.versionStr is None:
            raise TypeError('data.versionStr == None')
        if len(data.versionStr) > 100 and self.check_array:
            raise XDRError('array length too long for data.versionStr')
        self.pack_string(data.versionStr)
        if data.listeningPort is None:
            raise TypeError('data.listeningPort == None')
        self.pack_int(data.listeningPort)
        if data.peerID is None:
            raise TypeError('data.peerID == None')
        self.pack_NodeID(data.peerID)
        if data.cert is None:
            raise TypeError('data.cert == None')
        self.pack_AuthCert(data.cert)
        if data.nonce is None:
            raise TypeError('data.nonce == None')
        self.pack_uint256(data.nonce)

    def pack_Auth(self, data):
        if hasattr(self, 'filter_Auth'):
            data = getattr(self, 'filter_Auth')(data)
        if data.unused is None:
            raise TypeError('data.unused == None')
        self.pack_int(data.unused)

    def pack_IPAddrType(self, data):
        if hasattr(self, 'filter_IPAddrType'):
            data = getattr(self, 'filter_IPAddrType')(data)
        if self.check_enum and data not in [const.IPv4, const.IPv6]:
            raise XDRError('value=%s not in enum IPAddrType' % data)
        self.pack_int(data)

    def pack_PeerAddress(self, data):
        if hasattr(self, 'filter_PeerAddress'):
            data = getattr(self, 'filter_PeerAddress')(data)
        if data.ip is None:
            raise TypeError('data.ip == None')
        if data.ip.type is None:
            raise TypeError('data.ip.type == None')
        self.pack_IPAddrType(data.ip.type)
        if data.ip.type == const.IPv4:
            if data.ip.ipv4 is None:
                raise TypeError('data.ip.ipv4 == None')
            self.pack_fopaque(4, data.ip.ipv4)
        elif data.ip.type == const.IPv6:
            if data.ip.ipv6 is None:
                raise TypeError('data.ip.ipv6 == None')
            self.pack_fopaque(16, data.ip.ipv6)
        else:
            raise XDRError('bad switch=%s' % data.ip.type)
        if data.port is None:
            raise TypeError('data.port == None')
        self.pack_uint32(data.port)
        if data.numFailures is None:
            raise TypeError('data.numFailures == None')
        self.pack_uint32(data.numFailures)

    def pack_MessageType(self, data):
        if hasattr(self, 'filter_MessageType'):
            data = getattr(self, 'filter_MessageType')(data)
        if self.check_enum and data not in [const.ERROR_MSG, const.AUTH, const.DONT_HAVE, const.GET_PEERS, const.PEERS, const.GET_TX_SET, const.TX_SET, const.TRANSACTION, const.GET_SCP_QUORUMSET, const.SCP_QUORUMSET, const.SCP_MESSAGE, const.GET_SCP_STATE, const.HELLO, const.SURVEY_REQUEST, const.SURVEY_RESPONSE]:
            raise XDRError('value=%s not in enum MessageType' % data)
        self.pack_int(data)

    def pack_DontHave(self, data):
        if hasattr(self, 'filter_DontHave'):
            data = getattr(self, 'filter_DontHave')(data)
        if data.type is None:
            raise TypeError('data.type == None')
        self.pack_MessageType(data.type)
        if data.reqHash is None:
            raise TypeError('data.reqHash == None')
        self.pack_uint256(data.reqHash)

    def pack_SurveyMessageCommandType(self, data):
        if hasattr(self, 'filter_SurveyMessageCommandType'):
            data = getattr(self, 'filter_SurveyMessageCommandType')(data)
        if self.check_enum and data not in [const.SURVEY_TOPOLOGY]:
            raise XDRError('value=%s not in enum SurveyMessageCommandType' % data)
        self.pack_int(data)

    def pack_SurveyRequestMessage(self, data):
        if hasattr(self, 'filter_SurveyRequestMessage'):
            data = getattr(self, 'filter_SurveyRequestMessage')(data)
        if data.surveyorPeerID is None:
            raise TypeError('data.surveyorPeerID == None')
        self.pack_NodeID(data.surveyorPeerID)
        if data.surveyedPeerID is None:
            raise TypeError('data.surveyedPeerID == None')
        self.pack_NodeID(data.surveyedPeerID)
        if data.ledgerNum is None:
            raise TypeError('data.ledgerNum == None')
        self.pack_uint32(data.ledgerNum)
        if data.encryptionKey is None:
            raise TypeError('data.encryptionKey == None')
        self.pack_Curve25519Public(data.encryptionKey)
        if data.commandType is None:
            raise TypeError('data.commandType == None')
        self.pack_SurveyMessageCommandType(data.commandType)

    def pack_SignedSurveyRequestMessage(self, data):
        if hasattr(self, 'filter_SignedSurveyRequestMessage'):
            data = getattr(self, 'filter_SignedSurveyRequestMessage')(data)
        if data.requestSignature is None:
            raise TypeError('data.requestSignature == None')
        self.pack_Signature(data.requestSignature)
        if data.request is None:
            raise TypeError('data.request == None')
        self.pack_SurveyRequestMessage(data.request)

    def pack_EncryptedBody(self, data):
        if hasattr(self, 'filter_EncryptedBody'):
            data = getattr(self, 'filter_EncryptedBody')(data)
        if len(data) > 64000 and self.check_array:
            raise XDRError('array length too long for data')
        self.pack_opaque(data)

    def pack_SurveyResponseMessage(self, data):
        if hasattr(self, 'filter_SurveyResponseMessage'):
            data = getattr(self, 'filter_SurveyResponseMessage')(data)
        if data.surveyorPeerID is None:
            raise TypeError('data.surveyorPeerID == None')
        self.pack_NodeID(data.surveyorPeerID)
        if data.surveyedPeerID is None:
            raise TypeError('data.surveyedPeerID == None')
        self.pack_NodeID(data.surveyedPeerID)
        if data.ledgerNum is None:
            raise TypeError('data.ledgerNum == None')
        self.pack_uint32(data.ledgerNum)
        if data.commandType is None:
            raise TypeError('data.commandType == None')
        self.pack_SurveyMessageCommandType(data.commandType)
        if data.encryptedBody is None:
            raise TypeError('data.encryptedBody == None')
        self.pack_EncryptedBody(data.encryptedBody)

    def pack_SignedSurveyResponseMessage(self, data):
        if hasattr(self, 'filter_SignedSurveyResponseMessage'):
            data = getattr(self, 'filter_SignedSurveyResponseMessage')(data)
        if data.responseSignature is None:
            raise TypeError('data.responseSignature == None')
        self.pack_Signature(data.responseSignature)
        if data.response is None:
            raise TypeError('data.response == None')
        self.pack_SurveyResponseMessage(data.response)

    def pack_PeerStats(self, data):
        if hasattr(self, 'filter_PeerStats'):
            data = getattr(self, 'filter_PeerStats')(data)
        if data.id is None:
            raise TypeError('data.id == None')
        self.pack_NodeID(data.id)
        if data.versionStr is None:
            raise TypeError('data.versionStr == None')
        if len(data.versionStr) > 100 and self.check_array:
            raise XDRError('array length too long for data.versionStr')
        self.pack_string(data.versionStr)
        if data.messagesRead is None:
            raise TypeError('data.messagesRead == None')
        self.pack_uint64(data.messagesRead)
        if data.messagesWritten is None:
            raise TypeError('data.messagesWritten == None')
        self.pack_uint64(data.messagesWritten)
        if data.bytesRead is None:
            raise TypeError('data.bytesRead == None')
        self.pack_uint64(data.bytesRead)
        if data.bytesWritten is None:
            raise TypeError('data.bytesWritten == None')
        self.pack_uint64(data.bytesWritten)
        if data.secondsConnected is None:
            raise TypeError('data.secondsConnected == None')
        self.pack_uint64(data.secondsConnected)
        if data.uniqueFloodBytesRecv is None:
            raise TypeError('data.uniqueFloodBytesRecv == None')
        self.pack_uint64(data.uniqueFloodBytesRecv)
        if data.duplicateFloodBytesRecv is None:
            raise TypeError('data.duplicateFloodBytesRecv == None')
        self.pack_uint64(data.duplicateFloodBytesRecv)
        if data.uniqueFetchBytesRecv is None:
            raise TypeError('data.uniqueFetchBytesRecv == None')
        self.pack_uint64(data.uniqueFetchBytesRecv)
        if data.duplicateFetchBytesRecv is None:
            raise TypeError('data.duplicateFetchBytesRecv == None')
        self.pack_uint64(data.duplicateFetchBytesRecv)
        if data.uniqueFloodMessageRecv is None:
            raise TypeError('data.uniqueFloodMessageRecv == None')
        self.pack_uint64(data.uniqueFloodMessageRecv)
        if data.duplicateFloodMessageRecv is None:
            raise TypeError('data.duplicateFloodMessageRecv == None')
        self.pack_uint64(data.duplicateFloodMessageRecv)
        if data.uniqueFetchMessageRecv is None:
            raise TypeError('data.uniqueFetchMessageRecv == None')
        self.pack_uint64(data.uniqueFetchMessageRecv)
        if data.duplicateFetchMessageRecv is None:
            raise TypeError('data.duplicateFetchMessageRecv == None')
        self.pack_uint64(data.duplicateFetchMessageRecv)

    def pack_PeerStatList(self, data):
        if hasattr(self, 'filter_PeerStatList'):
            data = getattr(self, 'filter_PeerStatList')(data)
        if len(data) > 25 and self.check_array:
            raise XDRError('array length too long for data')
        self.pack_array(data, self.pack_PeerStats)

    def pack_TopologyResponseBody(self, data):
        if hasattr(self, 'filter_TopologyResponseBody'):
            data = getattr(self, 'filter_TopologyResponseBody')(data)
        if data.inboundPeers is None:
            raise TypeError('data.inboundPeers == None')
        self.pack_PeerStatList(data.inboundPeers)
        if data.outboundPeers is None:
            raise TypeError('data.outboundPeers == None')
        self.pack_PeerStatList(data.outboundPeers)
        if data.totalInboundPeerCount is None:
            raise TypeError('data.totalInboundPeerCount == None')
        self.pack_uint32(data.totalInboundPeerCount)
        if data.totalOutboundPeerCount is None:
            raise TypeError('data.totalOutboundPeerCount == None')
        self.pack_uint32(data.totalOutboundPeerCount)

    def pack_SurveyResponseBody(self, data):
        if hasattr(self, 'filter_SurveyResponseBody'):
            data = getattr(self, 'filter_SurveyResponseBody')(data)
        if data.type is None:
            raise TypeError('data.type == None')
        self.pack_SurveyMessageCommandType(data.type)
        if data.type == const.SURVEY_TOPOLOGY:
            if data.topologyResponseBody is None:
                raise TypeError('data.topologyResponseBody == None')
            self.pack_TopologyResponseBody(data.topologyResponseBody)
        else:
            raise XDRError('bad switch=%s' % data.type)

    def pack_PaydexMessage(self, data):
        if hasattr(self, 'filter_PaydexMessage'):
            data = getattr(self, 'filter_PaydexMessage')(data)
        if data.type is None:
            raise TypeError('data.type == None')
        self.pack_MessageType(data.type)
        if data.type == const.ERROR_MSG:
            if data.error is None:
                raise TypeError('data.error == None')
            self.pack_Error(data.error)
        elif data.type == const.HELLO:
            if data.hello is None:
                raise TypeError('data.hello == None')
            self.pack_Hello(data.hello)
        elif data.type == const.AUTH:
            if data.auth is None:
                raise TypeError('data.auth == None')
            self.pack_Auth(data.auth)
        elif data.type == const.DONT_HAVE:
            if data.dontHave is None:
                raise TypeError('data.dontHave == None')
            self.pack_DontHave(data.dontHave)
        elif data.type == const.GET_PEERS:
            pass
        elif data.type == const.PEERS:
            if data.peers is None:
                raise TypeError('data.peers == None')
            if len(data.peers) > 100 and self.check_array:
                raise XDRError('array length too long for data.peers')
            self.pack_array(data.peers, self.pack_PeerAddress)
        elif data.type == const.GET_TX_SET:
            if data.txSetHash is None:
                raise TypeError('data.txSetHash == None')
            self.pack_uint256(data.txSetHash)
        elif data.type == const.TX_SET:
            if data.txSet is None:
                raise TypeError('data.txSet == None')
            self.pack_TransactionSet(data.txSet)
        elif data.type == const.TRANSACTION:
            if data.transaction is None:
                raise TypeError('data.transaction == None')
            self.pack_TransactionEnvelope(data.transaction)
        elif data.type == const.SURVEY_REQUEST:
            if data.signedSurveyRequestMessage is None:
                raise TypeError('data.signedSurveyRequestMessage == None')
            self.pack_SignedSurveyRequestMessage(data.signedSurveyRequestMessage)
        elif data.type == const.SURVEY_RESPONSE:
            if data.signedSurveyResponseMessage is None:
                raise TypeError('data.signedSurveyResponseMessage == None')
            self.pack_SignedSurveyResponseMessage(data.signedSurveyResponseMessage)
        elif data.type == const.GET_SCP_QUORUMSET:
            if data.qSetHash is None:
                raise TypeError('data.qSetHash == None')
            self.pack_uint256(data.qSetHash)
        elif data.type == const.SCP_QUORUMSET:
            if data.qSet is None:
                raise TypeError('data.qSet == None')
            self.pack_SCPQuorumSet(data.qSet)
        elif data.type == const.SCP_MESSAGE:
            if data.envelope is None:
                raise TypeError('data.envelope == None')
            self.pack_SCPEnvelope(data.envelope)
        elif data.type == const.GET_SCP_STATE:
            if data.getSCPLedgerSeq is None:
                raise TypeError('data.getSCPLedgerSeq == None')
            self.pack_uint32(data.getSCPLedgerSeq)
        else:
            raise XDRError('bad switch=%s' % data.type)

    def pack_AuthenticatedMessage(self, data):
        if hasattr(self, 'filter_AuthenticatedMessage'):
            data = getattr(self, 'filter_AuthenticatedMessage')(data)
        if data.v is None:
            raise TypeError('data.v == None')
        self.pack_uint32(data.v)
        if data.v == 0:
            if data.v0 is None:
                raise TypeError('data.v0 == None')
            if data.v0.sequence is None:
                raise TypeError('data.v0.sequence == None')
            self.pack_uint64(data.v0.sequence)
            if data.v0.message is None:
                raise TypeError('data.v0.message == None')
            self.pack_PaydexMessage(data.v0.message)
            if data.v0.mac is None:
                raise TypeError('data.v0.mac == None')
            self.pack_HmacSha256Mac(data.v0.mac)
        else:
            raise XDRError('bad switch=%s' % data.v)

class PaydexXDRUnpacker(xdrlib.Unpacker):

    def __init__(self, data, check_enum=True, check_array=True):
        xdrlib.Unpacker.__init__(self, data)
        self.check_enum = check_enum
        self.check_array = check_array

    unpack_int = xdrlib.Unpacker.unpack_int
    unpack_uint = xdrlib.Unpacker.unpack_uint
    unpack_unsigned = xdrlib.Unpacker.unpack_uint
    unpack_hyper = xdrlib.Unpacker.unpack_hyper
    unpack_uhyper = xdrlib.Unpacker.unpack_uhyper
    unpack_float = xdrlib.Unpacker.unpack_float
    unpack_double = xdrlib.Unpacker.unpack_double
    unpack_quadruple = xdrlib.Unpacker.unpack_double
    unpack_bool = xdrlib.Unpacker.unpack_bool
    unpack_opaque = xdrlib.Unpacker.unpack_opaque
    unpack_string = xdrlib.Unpacker.unpack_string
    def unpack_Hash(self):
        data = self.unpack_fopaque(32)
        if hasattr(self, 'filter_Hash'):
            data = getattr(self, 'filter_Hash')(data)
        return data

    def unpack_uint256(self):
        data = self.unpack_fopaque(32)
        if hasattr(self, 'filter_uint256'):
            data = getattr(self, 'filter_uint256')(data)
        return data

    unpack_uint32 = unpack_uint

    unpack_int32 = unpack_int

    unpack_uint64 = unpack_uhyper

    unpack_int64 = unpack_hyper

    def unpack_CryptoKeyType(self):
        data = self.unpack_int()
        if self.check_enum and data not in [const.KEY_TYPE_ED25519, const.KEY_TYPE_PRE_AUTH_TX, const.KEY_TYPE_HASH_X]:
            raise XDRError('value=%s not in enum CryptoKeyType' % data)
        if hasattr(self, 'filter_CryptoKeyType'):
            data = getattr(self, 'filter_CryptoKeyType')(data)
        return data

    def unpack_PublicKeyType(self):
        data = self.unpack_int()
        if self.check_enum and data not in [const.PUBLIC_KEY_TYPE_ED25519]:
            raise XDRError('value=%s not in enum PublicKeyType' % data)
        if hasattr(self, 'filter_PublicKeyType'):
            data = getattr(self, 'filter_PublicKeyType')(data)
        return data

    def unpack_SignerKeyType(self):
        data = self.unpack_int()
        if self.check_enum and data not in [const.SIGNER_KEY_TYPE_ED25519, const.SIGNER_KEY_TYPE_PRE_AUTH_TX, const.SIGNER_KEY_TYPE_HASH_X]:
            raise XDRError('value=%s not in enum SignerKeyType' % data)
        if hasattr(self, 'filter_SignerKeyType'):
            data = getattr(self, 'filter_SignerKeyType')(data)
        return data

    def unpack_PublicKey(self):
        data = types.PublicKey()
        data.type = self.unpack_PublicKeyType()
        if data.type == const.PUBLIC_KEY_TYPE_ED25519:
            data.ed25519 = self.unpack_uint256()
        else:
            raise XDRError('bad switch=%s' % data.type)
        if hasattr(self, 'filter_PublicKey'):
            data = getattr(self, 'filter_PublicKey')(data)
        return data

    def unpack_SignerKey(self):
        data = types.SignerKey()
        data.type = self.unpack_SignerKeyType()
        if data.type == const.SIGNER_KEY_TYPE_ED25519:
            data.ed25519 = self.unpack_uint256()
        elif data.type == const.SIGNER_KEY_TYPE_PRE_AUTH_TX:
            data.preAuthTx = self.unpack_uint256()
        elif data.type == const.SIGNER_KEY_TYPE_HASH_X:
            data.hashX = self.unpack_uint256()
        else:
            raise XDRError('bad switch=%s' % data.type)
        if hasattr(self, 'filter_SignerKey'):
            data = getattr(self, 'filter_SignerKey')(data)
        return data

    def unpack_Signature(self):
        data = self.unpack_opaque()
        if len(data) > 64 and self.check_array:
            raise XDRError('array length too long for data')
        if hasattr(self, 'filter_Signature'):
            data = getattr(self, 'filter_Signature')(data)
        return data

    def unpack_SignatureHint(self):
        data = self.unpack_fopaque(4)
        if hasattr(self, 'filter_SignatureHint'):
            data = getattr(self, 'filter_SignatureHint')(data)
        return data

    unpack_NodeID = unpack_PublicKey

    def unpack_Curve25519Secret(self):
        data = types.Curve25519Secret()
        data.key = self.unpack_fopaque(32)
        if hasattr(self, 'filter_Curve25519Secret'):
            data = getattr(self, 'filter_Curve25519Secret')(data)
        return data

    def unpack_Curve25519Public(self):
        data = types.Curve25519Public()
        data.key = self.unpack_fopaque(32)
        if hasattr(self, 'filter_Curve25519Public'):
            data = getattr(self, 'filter_Curve25519Public')(data)
        return data

    def unpack_HmacSha256Key(self):
        data = types.HmacSha256Key()
        data.key = self.unpack_fopaque(32)
        if hasattr(self, 'filter_HmacSha256Key'):
            data = getattr(self, 'filter_HmacSha256Key')(data)
        return data

    def unpack_HmacSha256Mac(self):
        data = types.HmacSha256Mac()
        data.mac = self.unpack_fopaque(32)
        if hasattr(self, 'filter_HmacSha256Mac'):
            data = getattr(self, 'filter_HmacSha256Mac')(data)
        return data

    def unpack_Value(self):
        data = self.unpack_opaque()
        if hasattr(self, 'filter_Value'):
            data = getattr(self, 'filter_Value')(data)
        return data

    def unpack_SCPBallot(self):
        data = types.SCPBallot()
        data.counter = self.unpack_uint32()
        data.value = self.unpack_Value()
        if hasattr(self, 'filter_SCPBallot'):
            data = getattr(self, 'filter_SCPBallot')(data)
        return data

    def unpack_SCPStatementType(self):
        data = self.unpack_int()
        if self.check_enum and data not in [const.SCP_ST_PREPARE, const.SCP_ST_CONFIRM, const.SCP_ST_EXTERNALIZE, const.SCP_ST_NOMINATE]:
            raise XDRError('value=%s not in enum SCPStatementType' % data)
        if hasattr(self, 'filter_SCPStatementType'):
            data = getattr(self, 'filter_SCPStatementType')(data)
        return data

    def unpack_SCPNomination(self):
        data = types.SCPNomination()
        data.quorumSetHash = self.unpack_Hash()
        data.votes = self.unpack_array(self.unpack_Value)
        data.accepted = self.unpack_array(self.unpack_Value)
        if hasattr(self, 'filter_SCPNomination'):
            data = getattr(self, 'filter_SCPNomination')(data)
        return data

    def unpack_SCPStatement(self):
        data = types.SCPStatement()
        data.nodeID = self.unpack_NodeID()
        data.slotIndex = self.unpack_uint64()
        data.pledges = nullclass()
        data.pledges.type = self.unpack_SCPStatementType()
        if data.pledges.type == const.SCP_ST_PREPARE:
            data.pledges.prepare = nullclass()
            data.pledges.prepare.quorumSetHash = self.unpack_Hash()
            data.pledges.prepare.ballot = self.unpack_SCPBallot()
            data.pledges.prepare.prepared = self.unpack_array(self.unpack_SCPBallot)
            if len(data.pledges.prepare.prepared) > 1 and self.check_array:
                raise XDRError('array length too long for data.pledges.prepare.prepared')
            data.pledges.prepare.preparedPrime = self.unpack_array(self.unpack_SCPBallot)
            if len(data.pledges.prepare.preparedPrime) > 1 and self.check_array:
                raise XDRError('array length too long for data.pledges.prepare.preparedPrime')
            data.pledges.prepare.nC = self.unpack_uint32()
            data.pledges.prepare.nH = self.unpack_uint32()
        elif data.pledges.type == const.SCP_ST_CONFIRM:
            data.pledges.confirm = nullclass()
            data.pledges.confirm.ballot = self.unpack_SCPBallot()
            data.pledges.confirm.nPrepared = self.unpack_uint32()
            data.pledges.confirm.nCommit = self.unpack_uint32()
            data.pledges.confirm.nH = self.unpack_uint32()
            data.pledges.confirm.quorumSetHash = self.unpack_Hash()
        elif data.pledges.type == const.SCP_ST_EXTERNALIZE:
            data.pledges.externalize = nullclass()
            data.pledges.externalize.commit = self.unpack_SCPBallot()
            data.pledges.externalize.nH = self.unpack_uint32()
            data.pledges.externalize.commitQuorumSetHash = self.unpack_Hash()
        elif data.pledges.type == const.SCP_ST_NOMINATE:
            data.pledges.nominate = self.unpack_SCPNomination()
        else:
            raise XDRError('bad switch=%s' % data.pledges.type)
        if hasattr(self, 'filter_SCPStatement'):
            data = getattr(self, 'filter_SCPStatement')(data)
        return data

    def unpack_SCPEnvelope(self):
        data = types.SCPEnvelope()
        data.statement = self.unpack_SCPStatement()
        data.signature = self.unpack_Signature()
        if hasattr(self, 'filter_SCPEnvelope'):
            data = getattr(self, 'filter_SCPEnvelope')(data)
        return data

    def unpack_SCPQuorumSet(self):
        data = types.SCPQuorumSet()
        data.threshold = self.unpack_uint32()
        data.validators = self.unpack_array(self.unpack_PublicKey)
        data.innerSets = self.unpack_array(self.unpack_SCPQuorumSet)
        if hasattr(self, 'filter_SCPQuorumSet'):
            data = getattr(self, 'filter_SCPQuorumSet')(data)
        return data

    def unpack_UpgradeType(self):
        data = self.unpack_opaque()
        if len(data) > 128 and self.check_array:
            raise XDRError('array length too long for data')
        if hasattr(self, 'filter_UpgradeType'):
            data = getattr(self, 'filter_UpgradeType')(data)
        return data

    def unpack_PaydexValueType(self):
        data = self.unpack_int()
        if self.check_enum and data not in [const.PAYDEX_VALUE_BASIC, const.PAYDEX_VALUE_SIGNED]:
            raise XDRError('value=%s not in enum PaydexValueType' % data)
        if hasattr(self, 'filter_PaydexValueType'):
            data = getattr(self, 'filter_PaydexValueType')(data)
        return data

    def unpack_LedgerCloseValueSignature(self):
        data = types.LedgerCloseValueSignature()
        data.nodeID = self.unpack_NodeID()
        data.signature = self.unpack_Signature()
        if hasattr(self, 'filter_LedgerCloseValueSignature'):
            data = getattr(self, 'filter_LedgerCloseValueSignature')(data)
        return data

    def unpack_PaydexValue(self):
        data = types.PaydexValue()
        data.txSetHash = self.unpack_Hash()
        data.closeTime = self.unpack_TimePoint()
        data.upgrades = self.unpack_array(self.unpack_UpgradeType)
        if len(data.upgrades) > 6 and self.check_array:
            raise XDRError('array length too long for data.upgrades')
        data.ext = nullclass()
        data.ext.v = self.unpack_PaydexValueType()
        if data.ext.v == const.PAYDEX_VALUE_BASIC:
            pass
        elif data.ext.v == const.PAYDEX_VALUE_SIGNED:
            data.ext.lcValueSignature = self.unpack_LedgerCloseValueSignature()
        else:
            raise XDRError('bad switch=%s' % data.ext.v)
        if hasattr(self, 'filter_PaydexValue'):
            data = getattr(self, 'filter_PaydexValue')(data)
        return data

    def unpack_LedgerHeader(self):
        data = types.LedgerHeader()
        data.ledgerVersion = self.unpack_uint32()
        data.previousLedgerHash = self.unpack_Hash()
        data.scpValue = self.unpack_PaydexValue()
        data.txSetResultHash = self.unpack_Hash()
        data.bucketListHash = self.unpack_Hash()
        data.ledgerSeq = self.unpack_uint32()
        data.totalCoins = self.unpack_int64()
        data.feePool = self.unpack_int64()
        data.inflationSeq = self.unpack_uint32()
        data.idPool = self.unpack_uint64()
        data.baseFee = self.unpack_uint32()
        data.baseReserve = self.unpack_uint32()
        data.maxTxSetSize = self.unpack_uint32()
        data.skipList = self.unpack_farray(4, self.unpack_Hash)
        data.ext = nullclass()
        data.ext.v = self.unpack_int()
        if data.ext.v == 0:
            pass
        else:
            raise XDRError('bad switch=%s' % data.ext.v)
        if hasattr(self, 'filter_LedgerHeader'):
            data = getattr(self, 'filter_LedgerHeader')(data)
        return data

    def unpack_LedgerUpgradeType(self):
        data = self.unpack_int()
        if self.check_enum and data not in [const.LEDGER_UPGRADE_VERSION, const.LEDGER_UPGRADE_BASE_FEE, const.LEDGER_UPGRADE_MAX_TX_SET_SIZE, const.LEDGER_UPGRADE_BASE_RESERVE]:
            raise XDRError('value=%s not in enum LedgerUpgradeType' % data)
        if hasattr(self, 'filter_LedgerUpgradeType'):
            data = getattr(self, 'filter_LedgerUpgradeType')(data)
        return data

    def unpack_LedgerUpgrade(self):
        data = types.LedgerUpgrade()
        data.type = self.unpack_LedgerUpgradeType()
        if data.type == const.LEDGER_UPGRADE_VERSION:
            data.newLedgerVersion = self.unpack_uint32()
        elif data.type == const.LEDGER_UPGRADE_BASE_FEE:
            data.newBaseFee = self.unpack_uint32()
        elif data.type == const.LEDGER_UPGRADE_MAX_TX_SET_SIZE:
            data.newMaxTxSetSize = self.unpack_uint32()
        elif data.type == const.LEDGER_UPGRADE_BASE_RESERVE:
            data.newBaseReserve = self.unpack_uint32()
        else:
            raise XDRError('bad switch=%s' % data.type)
        if hasattr(self, 'filter_LedgerUpgrade'):
            data = getattr(self, 'filter_LedgerUpgrade')(data)
        return data

    def unpack_LedgerKey(self):
        data = types.LedgerKey()
        data.type = self.unpack_LedgerEntryType()
        if data.type == const.ACCOUNT:
            data.account = nullclass()
            data.account.accountID = self.unpack_AccountID()
        elif data.type == const.TRUSTLINE:
            data.trustLine = nullclass()
            data.trustLine.accountID = self.unpack_AccountID()
            data.trustLine.asset = self.unpack_Asset()
        elif data.type == const.OFFER:
            data.offer = nullclass()
            data.offer.sellerID = self.unpack_AccountID()
            data.offer.offerID = self.unpack_int64()
        elif data.type == const.DATA:
            data.data = nullclass()
            data.data.accountID = self.unpack_AccountID()
            data.data.dataName = self.unpack_string64()
        else:
            raise XDRError('bad switch=%s' % data.type)
        if hasattr(self, 'filter_LedgerKey'):
            data = getattr(self, 'filter_LedgerKey')(data)
        return data

    def unpack_BucketEntryType(self):
        data = self.unpack_int()
        if self.check_enum and data not in [const.METAENTRY, const.LIVEENTRY, const.DEADENTRY, const.INITENTRY]:
            raise XDRError('value=%s not in enum BucketEntryType' % data)
        if hasattr(self, 'filter_BucketEntryType'):
            data = getattr(self, 'filter_BucketEntryType')(data)
        return data

    def unpack_BucketMetadata(self):
        data = types.BucketMetadata()
        data.ledgerVersion = self.unpack_uint32()
        data.ext = nullclass()
        data.ext.v = self.unpack_int()
        if data.ext.v == 0:
            pass
        else:
            raise XDRError('bad switch=%s' % data.ext.v)
        if hasattr(self, 'filter_BucketMetadata'):
            data = getattr(self, 'filter_BucketMetadata')(data)
        return data

    def unpack_BucketEntry(self):
        data = types.BucketEntry()
        data.type = self.unpack_BucketEntryType()
        if data.type == const.LIVEENTRY or data.type == const.INITENTRY:
            data.liveEntry = self.unpack_LedgerEntry()
        elif data.type == const.DEADENTRY:
            data.deadEntry = self.unpack_LedgerKey()
        elif data.type == const.METAENTRY:
            data.metaEntry = self.unpack_BucketMetadata()
        else:
            raise XDRError('bad switch=%s' % data.type)
        if hasattr(self, 'filter_BucketEntry'):
            data = getattr(self, 'filter_BucketEntry')(data)
        return data

    def unpack_TransactionSet(self):
        data = types.TransactionSet()
        data.previousLedgerHash = self.unpack_Hash()
        data.txs = self.unpack_array(self.unpack_TransactionEnvelope)
        if hasattr(self, 'filter_TransactionSet'):
            data = getattr(self, 'filter_TransactionSet')(data)
        return data

    def unpack_TransactionResultPair(self):
        data = types.TransactionResultPair()
        data.transactionHash = self.unpack_Hash()
        data.result = self.unpack_TransactionResult()
        if hasattr(self, 'filter_TransactionResultPair'):
            data = getattr(self, 'filter_TransactionResultPair')(data)
        return data

    def unpack_TransactionResultSet(self):
        data = types.TransactionResultSet()
        data.results = self.unpack_array(self.unpack_TransactionResultPair)
        if hasattr(self, 'filter_TransactionResultSet'):
            data = getattr(self, 'filter_TransactionResultSet')(data)
        return data

    def unpack_TransactionHistoryEntry(self):
        data = types.TransactionHistoryEntry()
        data.ledgerSeq = self.unpack_uint32()
        data.txSet = self.unpack_TransactionSet()
        data.ext = nullclass()
        data.ext.v = self.unpack_int()
        if data.ext.v == 0:
            pass
        else:
            raise XDRError('bad switch=%s' % data.ext.v)
        if hasattr(self, 'filter_TransactionHistoryEntry'):
            data = getattr(self, 'filter_TransactionHistoryEntry')(data)
        return data

    def unpack_TransactionHistoryResultEntry(self):
        data = types.TransactionHistoryResultEntry()
        data.ledgerSeq = self.unpack_uint32()
        data.txResultSet = self.unpack_TransactionResultSet()
        data.ext = nullclass()
        data.ext.v = self.unpack_int()
        if data.ext.v == 0:
            pass
        else:
            raise XDRError('bad switch=%s' % data.ext.v)
        if hasattr(self, 'filter_TransactionHistoryResultEntry'):
            data = getattr(self, 'filter_TransactionHistoryResultEntry')(data)
        return data

    def unpack_LedgerHeaderHistoryEntry(self):
        data = types.LedgerHeaderHistoryEntry()
        data.hash = self.unpack_Hash()
        data.header = self.unpack_LedgerHeader()
        data.ext = nullclass()
        data.ext.v = self.unpack_int()
        if data.ext.v == 0:
            pass
        else:
            raise XDRError('bad switch=%s' % data.ext.v)
        if hasattr(self, 'filter_LedgerHeaderHistoryEntry'):
            data = getattr(self, 'filter_LedgerHeaderHistoryEntry')(data)
        return data

    def unpack_LedgerSCPMessages(self):
        data = types.LedgerSCPMessages()
        data.ledgerSeq = self.unpack_uint32()
        data.messages = self.unpack_array(self.unpack_SCPEnvelope)
        if hasattr(self, 'filter_LedgerSCPMessages'):
            data = getattr(self, 'filter_LedgerSCPMessages')(data)
        return data

    def unpack_SCPHistoryEntryV0(self):
        data = types.SCPHistoryEntryV0()
        data.quorumSets = self.unpack_array(self.unpack_SCPQuorumSet)
        data.ledgerMessages = self.unpack_LedgerSCPMessages()
        if hasattr(self, 'filter_SCPHistoryEntryV0'):
            data = getattr(self, 'filter_SCPHistoryEntryV0')(data)
        return data

    def unpack_SCPHistoryEntry(self):
        data = types.SCPHistoryEntry()
        data.v = self.unpack_int()
        if data.v == 0:
            data.v0 = self.unpack_SCPHistoryEntryV0()
        else:
            raise XDRError('bad switch=%s' % data.v)
        if hasattr(self, 'filter_SCPHistoryEntry'):
            data = getattr(self, 'filter_SCPHistoryEntry')(data)
        return data

    def unpack_LedgerEntryChangeType(self):
        data = self.unpack_int()
        if self.check_enum and data not in [const.LEDGER_ENTRY_CREATED, const.LEDGER_ENTRY_UPDATED, const.LEDGER_ENTRY_REMOVED, const.LEDGER_ENTRY_STATE]:
            raise XDRError('value=%s not in enum LedgerEntryChangeType' % data)
        if hasattr(self, 'filter_LedgerEntryChangeType'):
            data = getattr(self, 'filter_LedgerEntryChangeType')(data)
        return data

    def unpack_LedgerEntryChange(self):
        data = types.LedgerEntryChange()
        data.type = self.unpack_LedgerEntryChangeType()
        if data.type == const.LEDGER_ENTRY_CREATED:
            data.created = self.unpack_LedgerEntry()
        elif data.type == const.LEDGER_ENTRY_UPDATED:
            data.updated = self.unpack_LedgerEntry()
        elif data.type == const.LEDGER_ENTRY_REMOVED:
            data.removed = self.unpack_LedgerKey()
        elif data.type == const.LEDGER_ENTRY_STATE:
            data.state = self.unpack_LedgerEntry()
        else:
            raise XDRError('bad switch=%s' % data.type)
        if hasattr(self, 'filter_LedgerEntryChange'):
            data = getattr(self, 'filter_LedgerEntryChange')(data)
        return data

    def unpack_LedgerEntryChanges(self):
        data = self.unpack_array(self.unpack_LedgerEntryChange)
        if hasattr(self, 'filter_LedgerEntryChanges'):
            data = getattr(self, 'filter_LedgerEntryChanges')(data)
        return data

    def unpack_OperationMeta(self):
        data = types.OperationMeta()
        data.changes = self.unpack_LedgerEntryChanges()
        if hasattr(self, 'filter_OperationMeta'):
            data = getattr(self, 'filter_OperationMeta')(data)
        return data

    def unpack_TransactionMetaV1(self):
        data = types.TransactionMetaV1()
        data.txChanges = self.unpack_LedgerEntryChanges()
        data.operations = self.unpack_array(self.unpack_OperationMeta)
        if hasattr(self, 'filter_TransactionMetaV1'):
            data = getattr(self, 'filter_TransactionMetaV1')(data)
        return data

    def unpack_TransactionMetaV2(self):
        data = types.TransactionMetaV2()
        data.txChangesBefore = self.unpack_LedgerEntryChanges()
        data.operations = self.unpack_array(self.unpack_OperationMeta)
        data.txChangesAfter = self.unpack_LedgerEntryChanges()
        if hasattr(self, 'filter_TransactionMetaV2'):
            data = getattr(self, 'filter_TransactionMetaV2')(data)
        return data

    def unpack_TransactionMeta(self):
        data = types.TransactionMeta()
        data.v = self.unpack_int()
        if data.v == 0:
            data.operations = self.unpack_array(self.unpack_OperationMeta)
        elif data.v == 1:
            data.v1 = self.unpack_TransactionMetaV1()
        elif data.v == 2:
            data.v2 = self.unpack_TransactionMetaV2()
        else:
            raise XDRError('bad switch=%s' % data.v)
        if hasattr(self, 'filter_TransactionMeta'):
            data = getattr(self, 'filter_TransactionMeta')(data)
        return data

    def unpack_TransactionResultMeta(self):
        data = types.TransactionResultMeta()
        data.result = self.unpack_TransactionResultPair()
        data.feeProcessing = self.unpack_LedgerEntryChanges()
        data.txApplyProcessing = self.unpack_TransactionMeta()
        if hasattr(self, 'filter_TransactionResultMeta'):
            data = getattr(self, 'filter_TransactionResultMeta')(data)
        return data

    def unpack_UpgradeEntryMeta(self):
        data = types.UpgradeEntryMeta()
        data.upgrade = self.unpack_LedgerUpgrade()
        data.changes = self.unpack_LedgerEntryChanges()
        if hasattr(self, 'filter_UpgradeEntryMeta'):
            data = getattr(self, 'filter_UpgradeEntryMeta')(data)
        return data

    def unpack_LedgerCloseMetaV0(self):
        data = types.LedgerCloseMetaV0()
        data.ledgerHeader = self.unpack_LedgerHeaderHistoryEntry()
        data.txSet = self.unpack_TransactionSet()
        data.txProcessing = self.unpack_array(self.unpack_TransactionResultMeta)
        data.upgradesProcessing = self.unpack_array(self.unpack_UpgradeEntryMeta)
        data.scpInfo = self.unpack_array(self.unpack_SCPHistoryEntry)
        if hasattr(self, 'filter_LedgerCloseMetaV0'):
            data = getattr(self, 'filter_LedgerCloseMetaV0')(data)
        return data

    def unpack_LedgerCloseMeta(self):
        data = types.LedgerCloseMeta()
        data.v = self.unpack_int()
        if data.v == 0:
            data.v0 = self.unpack_LedgerCloseMetaV0()
        else:
            raise XDRError('bad switch=%s' % data.v)
        if hasattr(self, 'filter_LedgerCloseMeta'):
            data = getattr(self, 'filter_LedgerCloseMeta')(data)
        return data

    unpack_AccountID = unpack_PublicKey

    def unpack_Thresholds(self):
        data = self.unpack_fopaque(4)
        if hasattr(self, 'filter_Thresholds'):
            data = getattr(self, 'filter_Thresholds')(data)
        return data

    def unpack_string32(self):
        data = self.unpack_string()
        if len(data) > 32 and self.check_array:
            raise XDRError('array length too long for data')
        if hasattr(self, 'filter_string32'):
            data = getattr(self, 'filter_string32')(data)
        return data

    def unpack_string64(self):
        data = self.unpack_string()
        if len(data) > 64 and self.check_array:
            raise XDRError('array length too long for data')
        if hasattr(self, 'filter_string64'):
            data = getattr(self, 'filter_string64')(data)
        return data

    unpack_SequenceNumber = unpack_int64

    unpack_TimePoint = unpack_uint64

    def unpack_DataValue(self):
        data = self.unpack_opaque()
        if len(data) > 64 and self.check_array:
            raise XDRError('array length too long for data')
        if hasattr(self, 'filter_DataValue'):
            data = getattr(self, 'filter_DataValue')(data)
        return data

    def unpack_AssetCode4(self):
        data = self.unpack_fopaque(4)
        if hasattr(self, 'filter_AssetCode4'):
            data = getattr(self, 'filter_AssetCode4')(data)
        return data

    def unpack_AssetCode12(self):
        data = self.unpack_fopaque(12)
        if hasattr(self, 'filter_AssetCode12'):
            data = getattr(self, 'filter_AssetCode12')(data)
        return data

    def unpack_AssetType(self):
        data = self.unpack_int()
        if self.check_enum and data not in [const.ASSET_TYPE_NATIVE, const.ASSET_TYPE_CREDIT_ALPHANUM4, const.ASSET_TYPE_CREDIT_ALPHANUM12]:
            raise XDRError('value=%s not in enum AssetType' % data)
        if hasattr(self, 'filter_AssetType'):
            data = getattr(self, 'filter_AssetType')(data)
        return data

    def unpack_Asset(self):
        data = types.Asset()
        data.type = self.unpack_AssetType()
        if data.type == const.ASSET_TYPE_NATIVE:
            pass
        elif data.type == const.ASSET_TYPE_CREDIT_ALPHANUM4:
            data.alphaNum4 = nullclass()
            data.alphaNum4.assetCode = self.unpack_AssetCode4()
            data.alphaNum4.issuer = self.unpack_AccountID()
        elif data.type == const.ASSET_TYPE_CREDIT_ALPHANUM12:
            data.alphaNum12 = nullclass()
            data.alphaNum12.assetCode = self.unpack_AssetCode12()
            data.alphaNum12.issuer = self.unpack_AccountID()
        else:
            raise XDRError('bad switch=%s' % data.type)
        if hasattr(self, 'filter_Asset'):
            data = getattr(self, 'filter_Asset')(data)
        return data

    def unpack_Price(self):
        data = types.Price()
        data.n = self.unpack_int32()
        data.d = self.unpack_int32()
        if hasattr(self, 'filter_Price'):
            data = getattr(self, 'filter_Price')(data)
        return data

    def unpack_Liabilities(self):
        data = types.Liabilities()
        data.buying = self.unpack_int64()
        data.selling = self.unpack_int64()
        if hasattr(self, 'filter_Liabilities'):
            data = getattr(self, 'filter_Liabilities')(data)
        return data

    def unpack_ThresholdIndexes(self):
        data = self.unpack_int()
        if self.check_enum and data not in [const.THRESHOLD_MASTER_WEIGHT, const.THRESHOLD_LOW, const.THRESHOLD_MED, const.THRESHOLD_HIGH]:
            raise XDRError('value=%s not in enum ThresholdIndexes' % data)
        if hasattr(self, 'filter_ThresholdIndexes'):
            data = getattr(self, 'filter_ThresholdIndexes')(data)
        return data

    def unpack_LedgerEntryType(self):
        data = self.unpack_int()
        if self.check_enum and data not in [const.ACCOUNT, const.TRUSTLINE, const.OFFER, const.DATA]:
            raise XDRError('value=%s not in enum LedgerEntryType' % data)
        if hasattr(self, 'filter_LedgerEntryType'):
            data = getattr(self, 'filter_LedgerEntryType')(data)
        return data

    def unpack_Signer(self):
        data = types.Signer()
        data.key = self.unpack_SignerKey()
        data.weight = self.unpack_uint32()
        if hasattr(self, 'filter_Signer'):
            data = getattr(self, 'filter_Signer')(data)
        return data

    def unpack_AccountFlags(self):
        data = self.unpack_int()
        if self.check_enum and data not in [const.AUTH_REQUIRED_FLAG, const.AUTH_REVOCABLE_FLAG, const.AUTH_IMMUTABLE_FLAG]:
            raise XDRError('value=%s not in enum AccountFlags' % data)
        if hasattr(self, 'filter_AccountFlags'):
            data = getattr(self, 'filter_AccountFlags')(data)
        return data

    def unpack_AccountEntry(self):
        data = types.AccountEntry()
        data.accountID = self.unpack_AccountID()
        data.balance = self.unpack_int64()
        data.seqNum = self.unpack_SequenceNumber()
        data.numSubEntries = self.unpack_uint32()
        data.inflationDest = self.unpack_array(self.unpack_AccountID)
        if len(data.inflationDest) > 1 and self.check_array:
            raise XDRError('array length too long for data.inflationDest')
        data.flags = self.unpack_uint32()
        data.homeDomain = self.unpack_string32()
        data.thresholds = self.unpack_Thresholds()
        data.signers = self.unpack_array(self.unpack_Signer)
        if len(data.signers) > 20 and self.check_array:
            raise XDRError('array length too long for data.signers')
        data.ext = nullclass()
        data.ext.v = self.unpack_int()
        if data.ext.v == 0:
            pass
        elif data.ext.v == 1:
            data.ext.v1 = nullclass()
            data.ext.v1.liabilities = self.unpack_Liabilities()
            data.ext.v1.ext = nullclass()
            data.ext.v1.ext.v = self.unpack_int()
            if data.ext.v1.ext.v == 0:
                pass
            else:
                raise XDRError('bad switch=%s' % data.ext.v1.ext.v)
        else:
            raise XDRError('bad switch=%s' % data.ext.v)
        if hasattr(self, 'filter_AccountEntry'):
            data = getattr(self, 'filter_AccountEntry')(data)
        return data

    def unpack_TrustLineFlags(self):
        data = self.unpack_int()
        if self.check_enum and data not in [const.AUTHORIZED_FLAG]:
            raise XDRError('value=%s not in enum TrustLineFlags' % data)
        if hasattr(self, 'filter_TrustLineFlags'):
            data = getattr(self, 'filter_TrustLineFlags')(data)
        return data

    def unpack_TrustLineEntry(self):
        data = types.TrustLineEntry()
        data.accountID = self.unpack_AccountID()
        data.asset = self.unpack_Asset()
        data.balance = self.unpack_int64()
        data.limit = self.unpack_int64()
        data.flags = self.unpack_uint32()
        data.ext = nullclass()
        data.ext.v = self.unpack_int()
        if data.ext.v == 0:
            pass
        elif data.ext.v == 1:
            data.ext.v1 = nullclass()
            data.ext.v1.liabilities = self.unpack_Liabilities()
            data.ext.v1.ext = nullclass()
            data.ext.v1.ext.v = self.unpack_int()
            if data.ext.v1.ext.v == 0:
                pass
            else:
                raise XDRError('bad switch=%s' % data.ext.v1.ext.v)
        else:
            raise XDRError('bad switch=%s' % data.ext.v)
        if hasattr(self, 'filter_TrustLineEntry'):
            data = getattr(self, 'filter_TrustLineEntry')(data)
        return data

    def unpack_OfferEntryFlags(self):
        data = self.unpack_int()
        if self.check_enum and data not in [const.PASSIVE_FLAG]:
            raise XDRError('value=%s not in enum OfferEntryFlags' % data)
        if hasattr(self, 'filter_OfferEntryFlags'):
            data = getattr(self, 'filter_OfferEntryFlags')(data)
        return data

    def unpack_OfferEntry(self):
        data = types.OfferEntry()
        data.sellerID = self.unpack_AccountID()
        data.offerID = self.unpack_int64()
        data.selling = self.unpack_Asset()
        data.buying = self.unpack_Asset()
        data.amount = self.unpack_int64()
        data.price = self.unpack_Price()
        data.flags = self.unpack_uint32()
        data.ext = nullclass()
        data.ext.v = self.unpack_int()
        if data.ext.v == 0:
            pass
        else:
            raise XDRError('bad switch=%s' % data.ext.v)
        if hasattr(self, 'filter_OfferEntry'):
            data = getattr(self, 'filter_OfferEntry')(data)
        return data

    def unpack_DataEntry(self):
        data = types.DataEntry()
        data.accountID = self.unpack_AccountID()
        data.dataName = self.unpack_string64()
        data.dataValue = self.unpack_DataValue()
        data.ext = nullclass()
        data.ext.v = self.unpack_int()
        if data.ext.v == 0:
            pass
        else:
            raise XDRError('bad switch=%s' % data.ext.v)
        if hasattr(self, 'filter_DataEntry'):
            data = getattr(self, 'filter_DataEntry')(data)
        return data

    def unpack_LedgerEntry(self):
        data = types.LedgerEntry()
        data.lastModifiedLedgerSeq = self.unpack_uint32()
        data.data = nullclass()
        data.data.type = self.unpack_LedgerEntryType()
        if data.data.type == const.ACCOUNT:
            data.data.account = self.unpack_AccountEntry()
        elif data.data.type == const.TRUSTLINE:
            data.data.trustLine = self.unpack_TrustLineEntry()
        elif data.data.type == const.OFFER:
            data.data.offer = self.unpack_OfferEntry()
        elif data.data.type == const.DATA:
            data.data.data = self.unpack_DataEntry()
        else:
            raise XDRError('bad switch=%s' % data.data.type)
        data.ext = nullclass()
        data.ext.v = self.unpack_int()
        if data.ext.v == 0:
            pass
        else:
            raise XDRError('bad switch=%s' % data.ext.v)
        if hasattr(self, 'filter_LedgerEntry'):
            data = getattr(self, 'filter_LedgerEntry')(data)
        return data

    def unpack_EnvelopeType(self):
        data = self.unpack_int()
        if self.check_enum and data not in [const.ENVELOPE_TYPE_SCP, const.ENVELOPE_TYPE_TX, const.ENVELOPE_TYPE_AUTH, const.ENVELOPE_TYPE_SCPVALUE]:
            raise XDRError('value=%s not in enum EnvelopeType' % data)
        if hasattr(self, 'filter_EnvelopeType'):
            data = getattr(self, 'filter_EnvelopeType')(data)
        return data

    def unpack_DecoratedSignature(self):
        data = types.DecoratedSignature()
        data.hint = self.unpack_SignatureHint()
        data.signature = self.unpack_Signature()
        if hasattr(self, 'filter_DecoratedSignature'):
            data = getattr(self, 'filter_DecoratedSignature')(data)
        return data

    def unpack_OperationType(self):
        data = self.unpack_int()
        if self.check_enum and data not in [const.CREATE_ACCOUNT, const.PAYMENT, const.PATH_PAYMENT_STRICT_RECEIVE, const.MANAGE_SELL_OFFER, const.CREATE_PASSIVE_SELL_OFFER, const.SET_OPTIONS, const.CHANGE_TRUST, const.ALLOW_TRUST, const.ACCOUNT_MERGE, const.INFLATION, const.MANAGE_DATA, const.BUMP_SEQUENCE, const.MANAGE_BUY_OFFER, const.PATH_PAYMENT_STRICT_SEND]:
            raise XDRError('value=%s not in enum OperationType' % data)
        if hasattr(self, 'filter_OperationType'):
            data = getattr(self, 'filter_OperationType')(data)
        return data

    def unpack_CreateAccountOp(self):
        data = types.CreateAccountOp()
        data.destination = self.unpack_AccountID()
        data.startingBalance = self.unpack_int64()
        if hasattr(self, 'filter_CreateAccountOp'):
            data = getattr(self, 'filter_CreateAccountOp')(data)
        return data

    def unpack_PaymentOp(self):
        data = types.PaymentOp()
        data.destination = self.unpack_AccountID()
        data.asset = self.unpack_Asset()
        data.amount = self.unpack_int64()
        if hasattr(self, 'filter_PaymentOp'):
            data = getattr(self, 'filter_PaymentOp')(data)
        return data

    def unpack_PathPaymentStrictReceiveOp(self):
        data = types.PathPaymentStrictReceiveOp()
        data.sendAsset = self.unpack_Asset()
        data.sendMax = self.unpack_int64()
        data.destination = self.unpack_AccountID()
        data.destAsset = self.unpack_Asset()
        data.destAmount = self.unpack_int64()
        data.path = self.unpack_array(self.unpack_Asset)
        if len(data.path) > 5 and self.check_array:
            raise XDRError('array length too long for data.path')
        if hasattr(self, 'filter_PathPaymentStrictReceiveOp'):
            data = getattr(self, 'filter_PathPaymentStrictReceiveOp')(data)
        return data

    def unpack_PathPaymentStrictSendOp(self):
        data = types.PathPaymentStrictSendOp()
        data.sendAsset = self.unpack_Asset()
        data.sendAmount = self.unpack_int64()
        data.destination = self.unpack_AccountID()
        data.destAsset = self.unpack_Asset()
        data.destMin = self.unpack_int64()
        data.path = self.unpack_array(self.unpack_Asset)
        if len(data.path) > 5 and self.check_array:
            raise XDRError('array length too long for data.path')
        if hasattr(self, 'filter_PathPaymentStrictSendOp'):
            data = getattr(self, 'filter_PathPaymentStrictSendOp')(data)
        return data

    def unpack_ManageSellOfferOp(self):
        data = types.ManageSellOfferOp()
        data.selling = self.unpack_Asset()
        data.buying = self.unpack_Asset()
        data.amount = self.unpack_int64()
        data.price = self.unpack_Price()
        data.offerID = self.unpack_int64()
        if hasattr(self, 'filter_ManageSellOfferOp'):
            data = getattr(self, 'filter_ManageSellOfferOp')(data)
        return data

    def unpack_ManageBuyOfferOp(self):
        data = types.ManageBuyOfferOp()
        data.selling = self.unpack_Asset()
        data.buying = self.unpack_Asset()
        data.buyAmount = self.unpack_int64()
        data.price = self.unpack_Price()
        data.offerID = self.unpack_int64()
        if hasattr(self, 'filter_ManageBuyOfferOp'):
            data = getattr(self, 'filter_ManageBuyOfferOp')(data)
        return data

    def unpack_CreatePassiveSellOfferOp(self):
        data = types.CreatePassiveSellOfferOp()
        data.selling = self.unpack_Asset()
        data.buying = self.unpack_Asset()
        data.amount = self.unpack_int64()
        data.price = self.unpack_Price()
        if hasattr(self, 'filter_CreatePassiveSellOfferOp'):
            data = getattr(self, 'filter_CreatePassiveSellOfferOp')(data)
        return data

    def unpack_SetOptionsOp(self):
        data = types.SetOptionsOp()
        data.inflationDest = self.unpack_array(self.unpack_AccountID)
        if len(data.inflationDest) > 1 and self.check_array:
            raise XDRError('array length too long for data.inflationDest')
        data.clearFlags = self.unpack_array(self.unpack_uint32)
        if len(data.clearFlags) > 1 and self.check_array:
            raise XDRError('array length too long for data.clearFlags')
        data.setFlags = self.unpack_array(self.unpack_uint32)
        if len(data.setFlags) > 1 and self.check_array:
            raise XDRError('array length too long for data.setFlags')
        data.masterWeight = self.unpack_array(self.unpack_uint32)
        if len(data.masterWeight) > 1 and self.check_array:
            raise XDRError('array length too long for data.masterWeight')
        data.lowThreshold = self.unpack_array(self.unpack_uint32)
        if len(data.lowThreshold) > 1 and self.check_array:
            raise XDRError('array length too long for data.lowThreshold')
        data.medThreshold = self.unpack_array(self.unpack_uint32)
        if len(data.medThreshold) > 1 and self.check_array:
            raise XDRError('array length too long for data.medThreshold')
        data.highThreshold = self.unpack_array(self.unpack_uint32)
        if len(data.highThreshold) > 1 and self.check_array:
            raise XDRError('array length too long for data.highThreshold')
        data.homeDomain = self.unpack_array(self.unpack_string32)
        if len(data.homeDomain) > 1 and self.check_array:
            raise XDRError('array length too long for data.homeDomain')
        data.signer = self.unpack_array(self.unpack_Signer)
        if len(data.signer) > 1 and self.check_array:
            raise XDRError('array length too long for data.signer')
        if hasattr(self, 'filter_SetOptionsOp'):
            data = getattr(self, 'filter_SetOptionsOp')(data)
        return data

    def unpack_ChangeTrustOp(self):
        data = types.ChangeTrustOp()
        data.line = self.unpack_Asset()
        data.limit = self.unpack_int64()
        if hasattr(self, 'filter_ChangeTrustOp'):
            data = getattr(self, 'filter_ChangeTrustOp')(data)
        return data

    def unpack_AllowTrustOp(self):
        data = types.AllowTrustOp()
        data.trustor = self.unpack_AccountID()
        data.asset = nullclass()
        data.asset.type = self.unpack_AssetType()
        if data.asset.type == const.ASSET_TYPE_CREDIT_ALPHANUM4:
            data.asset.assetCode4 = self.unpack_AssetCode4()
        elif data.asset.type == const.ASSET_TYPE_CREDIT_ALPHANUM12:
            data.asset.assetCode12 = self.unpack_AssetCode12()
        else:
            raise XDRError('bad switch=%s' % data.asset.type)
        data.authorize = self.unpack_bool()
        if hasattr(self, 'filter_AllowTrustOp'):
            data = getattr(self, 'filter_AllowTrustOp')(data)
        return data

    def unpack_ManageDataOp(self):
        data = types.ManageDataOp()
        data.dataName = self.unpack_string64()
        data.dataValue = self.unpack_array(self.unpack_DataValue)
        if len(data.dataValue) > 1 and self.check_array:
            raise XDRError('array length too long for data.dataValue')
        if hasattr(self, 'filter_ManageDataOp'):
            data = getattr(self, 'filter_ManageDataOp')(data)
        return data

    def unpack_BumpSequenceOp(self):
        data = types.BumpSequenceOp()
        data.bumpTo = self.unpack_SequenceNumber()
        if hasattr(self, 'filter_BumpSequenceOp'):
            data = getattr(self, 'filter_BumpSequenceOp')(data)
        return data

    def unpack_Operation(self):
        data = types.Operation()
        data.sourceAccount = self.unpack_array(self.unpack_AccountID)
        if len(data.sourceAccount) > 1 and self.check_array:
            raise XDRError('array length too long for data.sourceAccount')
        data.body = nullclass()
        data.body.type = self.unpack_OperationType()
        if data.body.type == const.CREATE_ACCOUNT:
            data.body.createAccountOp = self.unpack_CreateAccountOp()
        elif data.body.type == const.PAYMENT:
            data.body.paymentOp = self.unpack_PaymentOp()
        elif data.body.type == const.PATH_PAYMENT_STRICT_RECEIVE:
            data.body.pathPaymentStrictReceiveOp = self.unpack_PathPaymentStrictReceiveOp()
        elif data.body.type == const.MANAGE_SELL_OFFER:
            data.body.manageSellOfferOp = self.unpack_ManageSellOfferOp()
        elif data.body.type == const.CREATE_PASSIVE_SELL_OFFER:
            data.body.createPassiveSellOfferOp = self.unpack_CreatePassiveSellOfferOp()
        elif data.body.type == const.SET_OPTIONS:
            data.body.setOptionsOp = self.unpack_SetOptionsOp()
        elif data.body.type == const.CHANGE_TRUST:
            data.body.changeTrustOp = self.unpack_ChangeTrustOp()
        elif data.body.type == const.ALLOW_TRUST:
            data.body.allowTrustOp = self.unpack_AllowTrustOp()
        elif data.body.type == const.ACCOUNT_MERGE:
            data.body.destination = self.unpack_AccountID()
        elif data.body.type == const.INFLATION:
            pass
        elif data.body.type == const.MANAGE_DATA:
            data.body.manageDataOp = self.unpack_ManageDataOp()
        elif data.body.type == const.BUMP_SEQUENCE:
            data.body.bumpSequenceOp = self.unpack_BumpSequenceOp()
        elif data.body.type == const.MANAGE_BUY_OFFER:
            data.body.manageBuyOfferOp = self.unpack_ManageBuyOfferOp()
        elif data.body.type == const.PATH_PAYMENT_STRICT_SEND:
            data.body.pathPaymentStrictSendOp = self.unpack_PathPaymentStrictSendOp()
        else:
            raise XDRError('bad switch=%s' % data.body.type)
        if hasattr(self, 'filter_Operation'):
            data = getattr(self, 'filter_Operation')(data)
        return data

    def unpack_MemoType(self):
        data = self.unpack_int()
        if self.check_enum and data not in [const.MEMO_NONE, const.MEMO_TEXT, const.MEMO_ID, const.MEMO_HASH, const.MEMO_RETURN]:
            raise XDRError('value=%s not in enum MemoType' % data)
        if hasattr(self, 'filter_MemoType'):
            data = getattr(self, 'filter_MemoType')(data)
        return data

    def unpack_Memo(self):
        data = types.Memo()
        data.type = self.unpack_MemoType()
        if data.type == const.MEMO_NONE:
            pass
        elif data.type == const.MEMO_TEXT:
            data.text = self.unpack_string()
            if len(data.text) > 28 and self.check_array:
                raise XDRError('array length too long for data.text')
        elif data.type == const.MEMO_ID:
            data.id = self.unpack_uint64()
        elif data.type == const.MEMO_HASH:
            data.hash = self.unpack_Hash()
        elif data.type == const.MEMO_RETURN:
            data.retHash = self.unpack_Hash()
        else:
            raise XDRError('bad switch=%s' % data.type)
        if hasattr(self, 'filter_Memo'):
            data = getattr(self, 'filter_Memo')(data)
        return data

    def unpack_TimeBounds(self):
        data = types.TimeBounds()
        data.minTime = self.unpack_TimePoint()
        data.maxTime = self.unpack_TimePoint()
        if hasattr(self, 'filter_TimeBounds'):
            data = getattr(self, 'filter_TimeBounds')(data)
        return data

    def unpack_Transaction(self):
        data = types.Transaction()
        data.sourceAccount = self.unpack_AccountID()
        data.fee = self.unpack_uint32()
        data.seqNum = self.unpack_SequenceNumber()
        data.timeBounds = self.unpack_array(self.unpack_TimeBounds)
        if len(data.timeBounds) > 1 and self.check_array:
            raise XDRError('array length too long for data.timeBounds')
        data.memo = self.unpack_Memo()
        data.operations = self.unpack_array(self.unpack_Operation)
        if len(data.operations) > const.MAX_OPS_PER_TX and self.check_array:
            raise XDRError('array length too long for data.operations')
        data.ext = nullclass()
        data.ext.v = self.unpack_int()
        if data.ext.v == 0:
            pass
        else:
            raise XDRError('bad switch=%s' % data.ext.v)
        if hasattr(self, 'filter_Transaction'):
            data = getattr(self, 'filter_Transaction')(data)
        return data

    def unpack_TransactionSignaturePayload(self):
        data = types.TransactionSignaturePayload()
        data.networkId = self.unpack_Hash()
        data.taggedTransaction = nullclass()
        data.taggedTransaction.type = self.unpack_EnvelopeType()
        if data.taggedTransaction.type == const.ENVELOPE_TYPE_TX:
            data.taggedTransaction.tx = self.unpack_Transaction()
        else:
            raise XDRError('bad switch=%s' % data.taggedTransaction.type)
        if hasattr(self, 'filter_TransactionSignaturePayload'):
            data = getattr(self, 'filter_TransactionSignaturePayload')(data)
        return data

    def unpack_TransactionEnvelope(self):
        data = types.TransactionEnvelope()
        data.tx = self.unpack_Transaction()
        data.signatures = self.unpack_array(self.unpack_DecoratedSignature)
        if len(data.signatures) > 20 and self.check_array:
            raise XDRError('array length too long for data.signatures')
        if hasattr(self, 'filter_TransactionEnvelope'):
            data = getattr(self, 'filter_TransactionEnvelope')(data)
        return data

    def unpack_ClaimOfferAtom(self):
        data = types.ClaimOfferAtom()
        data.sellerID = self.unpack_AccountID()
        data.offerID = self.unpack_int64()
        data.assetSold = self.unpack_Asset()
        data.amountSold = self.unpack_int64()
        data.assetBought = self.unpack_Asset()
        data.amountBought = self.unpack_int64()
        if hasattr(self, 'filter_ClaimOfferAtom'):
            data = getattr(self, 'filter_ClaimOfferAtom')(data)
        return data

    def unpack_CreateAccountResultCode(self):
        data = self.unpack_int()
        if self.check_enum and data not in [const.CREATE_ACCOUNT_SUCCESS, const.CREATE_ACCOUNT_MALFORMED, const.CREATE_ACCOUNT_UNDERFUNDED, const.CREATE_ACCOUNT_LOW_RESERVE, const.CREATE_ACCOUNT_ALREADY_EXIST]:
            raise XDRError('value=%s not in enum CreateAccountResultCode' % data)
        if hasattr(self, 'filter_CreateAccountResultCode'):
            data = getattr(self, 'filter_CreateAccountResultCode')(data)
        return data

    def unpack_CreateAccountResult(self):
        data = types.CreateAccountResult()
        data.code = self.unpack_CreateAccountResultCode()
        if data.code == const.CREATE_ACCOUNT_SUCCESS:
            pass
        else:
            pass
        if hasattr(self, 'filter_CreateAccountResult'):
            data = getattr(self, 'filter_CreateAccountResult')(data)
        return data

    def unpack_PaymentResultCode(self):
        data = self.unpack_int()
        if self.check_enum and data not in [const.PAYMENT_SUCCESS, const.PAYMENT_MALFORMED, const.PAYMENT_UNDERFUNDED, const.PAYMENT_SRC_NO_TRUST, const.PAYMENT_SRC_NOT_AUTHORIZED, const.PAYMENT_NO_DESTINATION, const.PAYMENT_NO_TRUST, const.PAYMENT_NOT_AUTHORIZED, const.PAYMENT_LINE_FULL, const.PAYMENT_NO_ISSUER]:
            raise XDRError('value=%s not in enum PaymentResultCode' % data)
        if hasattr(self, 'filter_PaymentResultCode'):
            data = getattr(self, 'filter_PaymentResultCode')(data)
        return data

    def unpack_PaymentResult(self):
        data = types.PaymentResult()
        data.code = self.unpack_PaymentResultCode()
        if data.code == const.PAYMENT_SUCCESS:
            pass
        else:
            pass
        if hasattr(self, 'filter_PaymentResult'):
            data = getattr(self, 'filter_PaymentResult')(data)
        return data

    def unpack_PathPaymentStrictReceiveResultCode(self):
        data = self.unpack_int()
        if self.check_enum and data not in [const.PATH_PAYMENT_STRICT_RECEIVE_SUCCESS, const.PATH_PAYMENT_STRICT_RECEIVE_MALFORMED, const.PATH_PAYMENT_STRICT_RECEIVE_UNDERFUNDED, const.PATH_PAYMENT_STRICT_RECEIVE_SRC_NO_TRUST, const.PATH_PAYMENT_STRICT_RECEIVE_SRC_NOT_AUTHORIZED, const.PATH_PAYMENT_STRICT_RECEIVE_NO_DESTINATION, const.PATH_PAYMENT_STRICT_RECEIVE_NO_TRUST, const.PATH_PAYMENT_STRICT_RECEIVE_NOT_AUTHORIZED, const.PATH_PAYMENT_STRICT_RECEIVE_LINE_FULL, const.PATH_PAYMENT_STRICT_RECEIVE_NO_ISSUER, const.PATH_PAYMENT_STRICT_RECEIVE_TOO_FEW_OFFERS, const.PATH_PAYMENT_STRICT_RECEIVE_OFFER_CROSS_SELF, const.PATH_PAYMENT_STRICT_RECEIVE_OVER_SENDMAX]:
            raise XDRError('value=%s not in enum PathPaymentStrictReceiveResultCode' % data)
        if hasattr(self, 'filter_PathPaymentStrictReceiveResultCode'):
            data = getattr(self, 'filter_PathPaymentStrictReceiveResultCode')(data)
        return data

    def unpack_SimplePaymentResult(self):
        data = types.SimplePaymentResult()
        data.destination = self.unpack_AccountID()
        data.asset = self.unpack_Asset()
        data.amount = self.unpack_int64()
        if hasattr(self, 'filter_SimplePaymentResult'):
            data = getattr(self, 'filter_SimplePaymentResult')(data)
        return data

    def unpack_PathPaymentStrictReceiveResult(self):
        data = types.PathPaymentStrictReceiveResult()
        data.code = self.unpack_PathPaymentStrictReceiveResultCode()
        if data.code == const.PATH_PAYMENT_STRICT_RECEIVE_SUCCESS:
            data.success = nullclass()
            data.success.offers = self.unpack_array(self.unpack_ClaimOfferAtom)
            data.success.last = self.unpack_SimplePaymentResult()
        elif data.code == const.PATH_PAYMENT_STRICT_RECEIVE_NO_ISSUER:
            data.noIssuer = self.unpack_Asset()
        else:
            pass
        if hasattr(self, 'filter_PathPaymentStrictReceiveResult'):
            data = getattr(self, 'filter_PathPaymentStrictReceiveResult')(data)
        return data

    def unpack_PathPaymentStrictSendResultCode(self):
        data = self.unpack_int()
        if self.check_enum and data not in [const.PATH_PAYMENT_STRICT_SEND_SUCCESS, const.PATH_PAYMENT_STRICT_SEND_MALFORMED, const.PATH_PAYMENT_STRICT_SEND_UNDERFUNDED, const.PATH_PAYMENT_STRICT_SEND_SRC_NO_TRUST, const.PATH_PAYMENT_STRICT_SEND_SRC_NOT_AUTHORIZED, const.PATH_PAYMENT_STRICT_SEND_NO_DESTINATION, const.PATH_PAYMENT_STRICT_SEND_NO_TRUST, const.PATH_PAYMENT_STRICT_SEND_NOT_AUTHORIZED, const.PATH_PAYMENT_STRICT_SEND_LINE_FULL, const.PATH_PAYMENT_STRICT_SEND_NO_ISSUER, const.PATH_PAYMENT_STRICT_SEND_TOO_FEW_OFFERS, const.PATH_PAYMENT_STRICT_SEND_OFFER_CROSS_SELF, const.PATH_PAYMENT_STRICT_SEND_UNDER_DESTMIN]:
            raise XDRError('value=%s not in enum PathPaymentStrictSendResultCode' % data)
        if hasattr(self, 'filter_PathPaymentStrictSendResultCode'):
            data = getattr(self, 'filter_PathPaymentStrictSendResultCode')(data)
        return data

    def unpack_PathPaymentStrictSendResult(self):
        data = types.PathPaymentStrictSendResult()
        data.code = self.unpack_PathPaymentStrictSendResultCode()
        if data.code == const.PATH_PAYMENT_STRICT_SEND_SUCCESS:
            data.success = nullclass()
            data.success.offers = self.unpack_array(self.unpack_ClaimOfferAtom)
            data.success.last = self.unpack_SimplePaymentResult()
        elif data.code == const.PATH_PAYMENT_STRICT_SEND_NO_ISSUER:
            data.noIssuer = self.unpack_Asset()
        else:
            pass
        if hasattr(self, 'filter_PathPaymentStrictSendResult'):
            data = getattr(self, 'filter_PathPaymentStrictSendResult')(data)
        return data

    def unpack_ManageSellOfferResultCode(self):
        data = self.unpack_int()
        if self.check_enum and data not in [const.MANAGE_SELL_OFFER_SUCCESS, const.MANAGE_SELL_OFFER_MALFORMED, const.MANAGE_SELL_OFFER_SELL_NO_TRUST, const.MANAGE_SELL_OFFER_BUY_NO_TRUST, const.MANAGE_SELL_OFFER_SELL_NOT_AUTHORIZED, const.MANAGE_SELL_OFFER_BUY_NOT_AUTHORIZED, const.MANAGE_SELL_OFFER_LINE_FULL, const.MANAGE_SELL_OFFER_UNDERFUNDED, const.MANAGE_SELL_OFFER_CROSS_SELF, const.MANAGE_SELL_OFFER_SELL_NO_ISSUER, const.MANAGE_SELL_OFFER_BUY_NO_ISSUER, const.MANAGE_SELL_OFFER_NOT_FOUND, const.MANAGE_SELL_OFFER_LOW_RESERVE]:
            raise XDRError('value=%s not in enum ManageSellOfferResultCode' % data)
        if hasattr(self, 'filter_ManageSellOfferResultCode'):
            data = getattr(self, 'filter_ManageSellOfferResultCode')(data)
        return data

    def unpack_ManageOfferEffect(self):
        data = self.unpack_int()
        if self.check_enum and data not in [const.MANAGE_OFFER_CREATED, const.MANAGE_OFFER_UPDATED, const.MANAGE_OFFER_DELETED]:
            raise XDRError('value=%s not in enum ManageOfferEffect' % data)
        if hasattr(self, 'filter_ManageOfferEffect'):
            data = getattr(self, 'filter_ManageOfferEffect')(data)
        return data

    def unpack_ManageOfferSuccessResult(self):
        data = types.ManageOfferSuccessResult()
        data.offersClaimed = self.unpack_array(self.unpack_ClaimOfferAtom)
        data.offer = nullclass()
        data.offer.effect = self.unpack_ManageOfferEffect()
        if data.offer.effect == const.MANAGE_OFFER_CREATED or data.offer.effect == const.MANAGE_OFFER_UPDATED:
            data.offer.offer = self.unpack_OfferEntry()
        else:
            pass
        if hasattr(self, 'filter_ManageOfferSuccessResult'):
            data = getattr(self, 'filter_ManageOfferSuccessResult')(data)
        return data

    def unpack_ManageSellOfferResult(self):
        data = types.ManageSellOfferResult()
        data.code = self.unpack_ManageSellOfferResultCode()
        if data.code == const.MANAGE_SELL_OFFER_SUCCESS:
            data.success = self.unpack_ManageOfferSuccessResult()
        else:
            pass
        if hasattr(self, 'filter_ManageSellOfferResult'):
            data = getattr(self, 'filter_ManageSellOfferResult')(data)
        return data

    def unpack_ManageBuyOfferResultCode(self):
        data = self.unpack_int()
        if self.check_enum and data not in [const.MANAGE_BUY_OFFER_SUCCESS, const.MANAGE_BUY_OFFER_MALFORMED, const.MANAGE_BUY_OFFER_SELL_NO_TRUST, const.MANAGE_BUY_OFFER_BUY_NO_TRUST, const.MANAGE_BUY_OFFER_SELL_NOT_AUTHORIZED, const.MANAGE_BUY_OFFER_BUY_NOT_AUTHORIZED, const.MANAGE_BUY_OFFER_LINE_FULL, const.MANAGE_BUY_OFFER_UNDERFUNDED, const.MANAGE_BUY_OFFER_CROSS_SELF, const.MANAGE_BUY_OFFER_SELL_NO_ISSUER, const.MANAGE_BUY_OFFER_BUY_NO_ISSUER, const.MANAGE_BUY_OFFER_NOT_FOUND, const.MANAGE_BUY_OFFER_LOW_RESERVE]:
            raise XDRError('value=%s not in enum ManageBuyOfferResultCode' % data)
        if hasattr(self, 'filter_ManageBuyOfferResultCode'):
            data = getattr(self, 'filter_ManageBuyOfferResultCode')(data)
        return data

    def unpack_ManageBuyOfferResult(self):
        data = types.ManageBuyOfferResult()
        data.code = self.unpack_ManageBuyOfferResultCode()
        if data.code == const.MANAGE_BUY_OFFER_SUCCESS:
            data.success = self.unpack_ManageOfferSuccessResult()
        else:
            pass
        if hasattr(self, 'filter_ManageBuyOfferResult'):
            data = getattr(self, 'filter_ManageBuyOfferResult')(data)
        return data

    def unpack_SetOptionsResultCode(self):
        data = self.unpack_int()
        if self.check_enum and data not in [const.SET_OPTIONS_SUCCESS, const.SET_OPTIONS_LOW_RESERVE, const.SET_OPTIONS_TOO_MANY_SIGNERS, const.SET_OPTIONS_BAD_FLAGS, const.SET_OPTIONS_INVALID_INFLATION, const.SET_OPTIONS_CANT_CHANGE, const.SET_OPTIONS_UNKNOWN_FLAG, const.SET_OPTIONS_THRESHOLD_OUT_OF_RANGE, const.SET_OPTIONS_BAD_SIGNER, const.SET_OPTIONS_INVALID_HOME_DOMAIN]:
            raise XDRError('value=%s not in enum SetOptionsResultCode' % data)
        if hasattr(self, 'filter_SetOptionsResultCode'):
            data = getattr(self, 'filter_SetOptionsResultCode')(data)
        return data

    def unpack_SetOptionsResult(self):
        data = types.SetOptionsResult()
        data.code = self.unpack_SetOptionsResultCode()
        if data.code == const.SET_OPTIONS_SUCCESS:
            pass
        else:
            pass
        if hasattr(self, 'filter_SetOptionsResult'):
            data = getattr(self, 'filter_SetOptionsResult')(data)
        return data

    def unpack_ChangeTrustResultCode(self):
        data = self.unpack_int()
        if self.check_enum and data not in [const.CHANGE_TRUST_SUCCESS, const.CHANGE_TRUST_MALFORMED, const.CHANGE_TRUST_NO_ISSUER, const.CHANGE_TRUST_INVALID_LIMIT, const.CHANGE_TRUST_LOW_RESERVE, const.CHANGE_TRUST_SELF_NOT_ALLOWED]:
            raise XDRError('value=%s not in enum ChangeTrustResultCode' % data)
        if hasattr(self, 'filter_ChangeTrustResultCode'):
            data = getattr(self, 'filter_ChangeTrustResultCode')(data)
        return data

    def unpack_ChangeTrustResult(self):
        data = types.ChangeTrustResult()
        data.code = self.unpack_ChangeTrustResultCode()
        if data.code == const.CHANGE_TRUST_SUCCESS:
            pass
        else:
            pass
        if hasattr(self, 'filter_ChangeTrustResult'):
            data = getattr(self, 'filter_ChangeTrustResult')(data)
        return data

    def unpack_AllowTrustResultCode(self):
        data = self.unpack_int()
        if self.check_enum and data not in [const.ALLOW_TRUST_SUCCESS, const.ALLOW_TRUST_MALFORMED, const.ALLOW_TRUST_NO_TRUST_LINE, const.ALLOW_TRUST_TRUST_NOT_REQUIRED, const.ALLOW_TRUST_CANT_REVOKE, const.ALLOW_TRUST_SELF_NOT_ALLOWED]:
            raise XDRError('value=%s not in enum AllowTrustResultCode' % data)
        if hasattr(self, 'filter_AllowTrustResultCode'):
            data = getattr(self, 'filter_AllowTrustResultCode')(data)
        return data

    def unpack_AllowTrustResult(self):
        data = types.AllowTrustResult()
        data.code = self.unpack_AllowTrustResultCode()
        if data.code == const.ALLOW_TRUST_SUCCESS:
            pass
        else:
            pass
        if hasattr(self, 'filter_AllowTrustResult'):
            data = getattr(self, 'filter_AllowTrustResult')(data)
        return data

    def unpack_AccountMergeResultCode(self):
        data = self.unpack_int()
        if self.check_enum and data not in [const.ACCOUNT_MERGE_SUCCESS, const.ACCOUNT_MERGE_MALFORMED, const.ACCOUNT_MERGE_NO_ACCOUNT, const.ACCOUNT_MERGE_IMMUTABLE_SET, const.ACCOUNT_MERGE_HAS_SUB_ENTRIES, const.ACCOUNT_MERGE_SEQNUM_TOO_FAR, const.ACCOUNT_MERGE_DEST_FULL]:
            raise XDRError('value=%s not in enum AccountMergeResultCode' % data)
        if hasattr(self, 'filter_AccountMergeResultCode'):
            data = getattr(self, 'filter_AccountMergeResultCode')(data)
        return data

    def unpack_AccountMergeResult(self):
        data = types.AccountMergeResult()
        data.code = self.unpack_AccountMergeResultCode()
        if data.code == const.ACCOUNT_MERGE_SUCCESS:
            data.sourceAccountBalance = self.unpack_int64()
        else:
            pass
        if hasattr(self, 'filter_AccountMergeResult'):
            data = getattr(self, 'filter_AccountMergeResult')(data)
        return data

    def unpack_InflationResultCode(self):
        data = self.unpack_int()
        if self.check_enum and data not in [const.INFLATION_SUCCESS, const.INFLATION_NOT_TIME]:
            raise XDRError('value=%s not in enum InflationResultCode' % data)
        if hasattr(self, 'filter_InflationResultCode'):
            data = getattr(self, 'filter_InflationResultCode')(data)
        return data

    def unpack_InflationPayout(self):
        data = types.InflationPayout()
        data.destination = self.unpack_AccountID()
        data.amount = self.unpack_int64()
        if hasattr(self, 'filter_InflationPayout'):
            data = getattr(self, 'filter_InflationPayout')(data)
        return data

    def unpack_InflationResult(self):
        data = types.InflationResult()
        data.code = self.unpack_InflationResultCode()
        if data.code == const.INFLATION_SUCCESS:
            data.payouts = self.unpack_array(self.unpack_InflationPayout)
        else:
            pass
        if hasattr(self, 'filter_InflationResult'):
            data = getattr(self, 'filter_InflationResult')(data)
        return data

    def unpack_ManageDataResultCode(self):
        data = self.unpack_int()
        if self.check_enum and data not in [const.MANAGE_DATA_SUCCESS, const.MANAGE_DATA_NOT_SUPPORTED_YET, const.MANAGE_DATA_NAME_NOT_FOUND, const.MANAGE_DATA_LOW_RESERVE, const.MANAGE_DATA_INVALID_NAME]:
            raise XDRError('value=%s not in enum ManageDataResultCode' % data)
        if hasattr(self, 'filter_ManageDataResultCode'):
            data = getattr(self, 'filter_ManageDataResultCode')(data)
        return data

    def unpack_ManageDataResult(self):
        data = types.ManageDataResult()
        data.code = self.unpack_ManageDataResultCode()
        if data.code == const.MANAGE_DATA_SUCCESS:
            pass
        else:
            pass
        if hasattr(self, 'filter_ManageDataResult'):
            data = getattr(self, 'filter_ManageDataResult')(data)
        return data

    def unpack_BumpSequenceResultCode(self):
        data = self.unpack_int()
        if self.check_enum and data not in [const.BUMP_SEQUENCE_SUCCESS, const.BUMP_SEQUENCE_BAD_SEQ]:
            raise XDRError('value=%s not in enum BumpSequenceResultCode' % data)
        if hasattr(self, 'filter_BumpSequenceResultCode'):
            data = getattr(self, 'filter_BumpSequenceResultCode')(data)
        return data

    def unpack_BumpSequenceResult(self):
        data = types.BumpSequenceResult()
        data.code = self.unpack_BumpSequenceResultCode()
        if data.code == const.BUMP_SEQUENCE_SUCCESS:
            pass
        else:
            pass
        if hasattr(self, 'filter_BumpSequenceResult'):
            data = getattr(self, 'filter_BumpSequenceResult')(data)
        return data

    def unpack_OperationResultCode(self):
        data = self.unpack_int()
        if self.check_enum and data not in [const.opINNER, const.opBAD_AUTH, const.opNO_ACCOUNT, const.opNOT_SUPPORTED, const.opTOO_MANY_SUBENTRIES, const.opEXCEEDED_WORK_LIMIT]:
            raise XDRError('value=%s not in enum OperationResultCode' % data)
        if hasattr(self, 'filter_OperationResultCode'):
            data = getattr(self, 'filter_OperationResultCode')(data)
        return data

    def unpack_OperationResult(self):
        data = types.OperationResult()
        data.code = self.unpack_OperationResultCode()
        if data.code == const.opINNER:
            data.tr = nullclass()
            data.tr.type = self.unpack_OperationType()
            if data.tr.type == const.CREATE_ACCOUNT:
                data.tr.createAccountResult = self.unpack_CreateAccountResult()
            elif data.tr.type == const.PAYMENT:
                data.tr.paymentResult = self.unpack_PaymentResult()
            elif data.tr.type == const.PATH_PAYMENT_STRICT_RECEIVE:
                data.tr.pathPaymentStrictReceiveResult = self.unpack_PathPaymentStrictReceiveResult()
            elif data.tr.type == const.MANAGE_SELL_OFFER:
                data.tr.manageSellOfferResult = self.unpack_ManageSellOfferResult()
            elif data.tr.type == const.CREATE_PASSIVE_SELL_OFFER:
                data.tr.createPassiveSellOfferResult = self.unpack_ManageSellOfferResult()
            elif data.tr.type == const.SET_OPTIONS:
                data.tr.setOptionsResult = self.unpack_SetOptionsResult()
            elif data.tr.type == const.CHANGE_TRUST:
                data.tr.changeTrustResult = self.unpack_ChangeTrustResult()
            elif data.tr.type == const.ALLOW_TRUST:
                data.tr.allowTrustResult = self.unpack_AllowTrustResult()
            elif data.tr.type == const.ACCOUNT_MERGE:
                data.tr.accountMergeResult = self.unpack_AccountMergeResult()
            elif data.tr.type == const.INFLATION:
                data.tr.inflationResult = self.unpack_InflationResult()
            elif data.tr.type == const.MANAGE_DATA:
                data.tr.manageDataResult = self.unpack_ManageDataResult()
            elif data.tr.type == const.BUMP_SEQUENCE:
                data.tr.bumpSeqResult = self.unpack_BumpSequenceResult()
            elif data.tr.type == const.MANAGE_BUY_OFFER:
                data.tr.manageBuyOfferResult = self.unpack_ManageBuyOfferResult()
            elif data.tr.type == const.PATH_PAYMENT_STRICT_SEND:
                data.tr.pathPaymentStrictSendResult = self.unpack_PathPaymentStrictSendResult()
            else:
                raise XDRError('bad switch=%s' % data.tr.type)
        else:
            pass
        if hasattr(self, 'filter_OperationResult'):
            data = getattr(self, 'filter_OperationResult')(data)
        return data

    def unpack_TransactionResultCode(self):
        data = self.unpack_int()
        if self.check_enum and data not in [const.txSUCCESS, const.txFAILED, const.txTOO_EARLY, const.txTOO_LATE, const.txMISSING_OPERATION, const.txBAD_SEQ, const.txBAD_AUTH, const.txINSUFFICIENT_BALANCE, const.txNO_ACCOUNT, const.txINSUFFICIENT_FEE, const.txBAD_AUTH_EXTRA, const.txINTERNAL_ERROR]:
            raise XDRError('value=%s not in enum TransactionResultCode' % data)
        if hasattr(self, 'filter_TransactionResultCode'):
            data = getattr(self, 'filter_TransactionResultCode')(data)
        return data

    def unpack_TransactionResult(self):
        data = types.TransactionResult()
        data.feeCharged = self.unpack_int64()
        data.result = nullclass()
        data.result.code = self.unpack_TransactionResultCode()
        if data.result.code == const.txSUCCESS or data.result.code == const.txFAILED:
            data.result.results = self.unpack_array(self.unpack_OperationResult)
        else:
            pass
        data.ext = nullclass()
        data.ext.v = self.unpack_int()
        if data.ext.v == 0:
            pass
        else:
            raise XDRError('bad switch=%s' % data.ext.v)
        if hasattr(self, 'filter_TransactionResult'):
            data = getattr(self, 'filter_TransactionResult')(data)
        return data

    def unpack_ErrorCode(self):
        data = self.unpack_int()
        if self.check_enum and data not in [const.ERR_MISC, const.ERR_DATA, const.ERR_CONF, const.ERR_AUTH, const.ERR_LOAD]:
            raise XDRError('value=%s not in enum ErrorCode' % data)
        if hasattr(self, 'filter_ErrorCode'):
            data = getattr(self, 'filter_ErrorCode')(data)
        return data

    def unpack_Error(self):
        data = types.Error()
        data.code = self.unpack_ErrorCode()
        data.msg = self.unpack_string()
        if len(data.msg) > 100 and self.check_array:
            raise XDRError('array length too long for data.msg')
        if hasattr(self, 'filter_Error'):
            data = getattr(self, 'filter_Error')(data)
        return data

    def unpack_AuthCert(self):
        data = types.AuthCert()
        data.pubkey = self.unpack_Curve25519Public()
        data.expiration = self.unpack_uint64()
        data.sig = self.unpack_Signature()
        if hasattr(self, 'filter_AuthCert'):
            data = getattr(self, 'filter_AuthCert')(data)
        return data

    def unpack_Hello(self):
        data = types.Hello()
        data.ledgerVersion = self.unpack_uint32()
        data.overlayVersion = self.unpack_uint32()
        data.overlayMinVersion = self.unpack_uint32()
        data.networkID = self.unpack_Hash()
        data.versionStr = self.unpack_string()
        if len(data.versionStr) > 100 and self.check_array:
            raise XDRError('array length too long for data.versionStr')
        data.listeningPort = self.unpack_int()
        data.peerID = self.unpack_NodeID()
        data.cert = self.unpack_AuthCert()
        data.nonce = self.unpack_uint256()
        if hasattr(self, 'filter_Hello'):
            data = getattr(self, 'filter_Hello')(data)
        return data

    def unpack_Auth(self):
        data = types.Auth()
        data.unused = self.unpack_int()
        if hasattr(self, 'filter_Auth'):
            data = getattr(self, 'filter_Auth')(data)
        return data

    def unpack_IPAddrType(self):
        data = self.unpack_int()
        if self.check_enum and data not in [const.IPv4, const.IPv6]:
            raise XDRError('value=%s not in enum IPAddrType' % data)
        if hasattr(self, 'filter_IPAddrType'):
            data = getattr(self, 'filter_IPAddrType')(data)
        return data

    def unpack_PeerAddress(self):
        data = types.PeerAddress()
        data.ip = nullclass()
        data.ip.type = self.unpack_IPAddrType()
        if data.ip.type == const.IPv4:
            data.ip.ipv4 = self.unpack_fopaque(4)
        elif data.ip.type == const.IPv6:
            data.ip.ipv6 = self.unpack_fopaque(16)
        else:
            raise XDRError('bad switch=%s' % data.ip.type)
        data.port = self.unpack_uint32()
        data.numFailures = self.unpack_uint32()
        if hasattr(self, 'filter_PeerAddress'):
            data = getattr(self, 'filter_PeerAddress')(data)
        return data

    def unpack_MessageType(self):
        data = self.unpack_int()
        if self.check_enum and data not in [const.ERROR_MSG, const.AUTH, const.DONT_HAVE, const.GET_PEERS, const.PEERS, const.GET_TX_SET, const.TX_SET, const.TRANSACTION, const.GET_SCP_QUORUMSET, const.SCP_QUORUMSET, const.SCP_MESSAGE, const.GET_SCP_STATE, const.HELLO, const.SURVEY_REQUEST, const.SURVEY_RESPONSE]:
            raise XDRError('value=%s not in enum MessageType' % data)
        if hasattr(self, 'filter_MessageType'):
            data = getattr(self, 'filter_MessageType')(data)
        return data

    def unpack_DontHave(self):
        data = types.DontHave()
        data.type = self.unpack_MessageType()
        data.reqHash = self.unpack_uint256()
        if hasattr(self, 'filter_DontHave'):
            data = getattr(self, 'filter_DontHave')(data)
        return data

    def unpack_SurveyMessageCommandType(self):
        data = self.unpack_int()
        if self.check_enum and data not in [const.SURVEY_TOPOLOGY]:
            raise XDRError('value=%s not in enum SurveyMessageCommandType' % data)
        if hasattr(self, 'filter_SurveyMessageCommandType'):
            data = getattr(self, 'filter_SurveyMessageCommandType')(data)
        return data

    def unpack_SurveyRequestMessage(self):
        data = types.SurveyRequestMessage()
        data.surveyorPeerID = self.unpack_NodeID()
        data.surveyedPeerID = self.unpack_NodeID()
        data.ledgerNum = self.unpack_uint32()
        data.encryptionKey = self.unpack_Curve25519Public()
        data.commandType = self.unpack_SurveyMessageCommandType()
        if hasattr(self, 'filter_SurveyRequestMessage'):
            data = getattr(self, 'filter_SurveyRequestMessage')(data)
        return data

    def unpack_SignedSurveyRequestMessage(self):
        data = types.SignedSurveyRequestMessage()
        data.requestSignature = self.unpack_Signature()
        data.request = self.unpack_SurveyRequestMessage()
        if hasattr(self, 'filter_SignedSurveyRequestMessage'):
            data = getattr(self, 'filter_SignedSurveyRequestMessage')(data)
        return data

    def unpack_EncryptedBody(self):
        data = self.unpack_opaque()
        if len(data) > 64000 and self.check_array:
            raise XDRError('array length too long for data')
        if hasattr(self, 'filter_EncryptedBody'):
            data = getattr(self, 'filter_EncryptedBody')(data)
        return data

    def unpack_SurveyResponseMessage(self):
        data = types.SurveyResponseMessage()
        data.surveyorPeerID = self.unpack_NodeID()
        data.surveyedPeerID = self.unpack_NodeID()
        data.ledgerNum = self.unpack_uint32()
        data.commandType = self.unpack_SurveyMessageCommandType()
        data.encryptedBody = self.unpack_EncryptedBody()
        if hasattr(self, 'filter_SurveyResponseMessage'):
            data = getattr(self, 'filter_SurveyResponseMessage')(data)
        return data

    def unpack_SignedSurveyResponseMessage(self):
        data = types.SignedSurveyResponseMessage()
        data.responseSignature = self.unpack_Signature()
        data.response = self.unpack_SurveyResponseMessage()
        if hasattr(self, 'filter_SignedSurveyResponseMessage'):
            data = getattr(self, 'filter_SignedSurveyResponseMessage')(data)
        return data

    def unpack_PeerStats(self):
        data = types.PeerStats()
        data.id = self.unpack_NodeID()
        data.versionStr = self.unpack_string()
        if len(data.versionStr) > 100 and self.check_array:
            raise XDRError('array length too long for data.versionStr')
        data.messagesRead = self.unpack_uint64()
        data.messagesWritten = self.unpack_uint64()
        data.bytesRead = self.unpack_uint64()
        data.bytesWritten = self.unpack_uint64()
        data.secondsConnected = self.unpack_uint64()
        data.uniqueFloodBytesRecv = self.unpack_uint64()
        data.duplicateFloodBytesRecv = self.unpack_uint64()
        data.uniqueFetchBytesRecv = self.unpack_uint64()
        data.duplicateFetchBytesRecv = self.unpack_uint64()
        data.uniqueFloodMessageRecv = self.unpack_uint64()
        data.duplicateFloodMessageRecv = self.unpack_uint64()
        data.uniqueFetchMessageRecv = self.unpack_uint64()
        data.duplicateFetchMessageRecv = self.unpack_uint64()
        if hasattr(self, 'filter_PeerStats'):
            data = getattr(self, 'filter_PeerStats')(data)
        return data

    def unpack_PeerStatList(self):
        data = self.unpack_array(self.unpack_PeerStats)
        if len(data) > 25 and self.check_array:
            raise XDRError('array length too long for data')
        if hasattr(self, 'filter_PeerStatList'):
            data = getattr(self, 'filter_PeerStatList')(data)
        return data

    def unpack_TopologyResponseBody(self):
        data = types.TopologyResponseBody()
        data.inboundPeers = self.unpack_PeerStatList()
        data.outboundPeers = self.unpack_PeerStatList()
        data.totalInboundPeerCount = self.unpack_uint32()
        data.totalOutboundPeerCount = self.unpack_uint32()
        if hasattr(self, 'filter_TopologyResponseBody'):
            data = getattr(self, 'filter_TopologyResponseBody')(data)
        return data

    def unpack_SurveyResponseBody(self):
        data = types.SurveyResponseBody()
        data.type = self.unpack_SurveyMessageCommandType()
        if data.type == const.SURVEY_TOPOLOGY:
            data.topologyResponseBody = self.unpack_TopologyResponseBody()
        else:
            raise XDRError('bad switch=%s' % data.type)
        if hasattr(self, 'filter_SurveyResponseBody'):
            data = getattr(self, 'filter_SurveyResponseBody')(data)
        return data

    def unpack_PaydexMessage(self):
        data = types.PaydexMessage()
        data.type = self.unpack_MessageType()
        if data.type == const.ERROR_MSG:
            data.error = self.unpack_Error()
        elif data.type == const.HELLO:
            data.hello = self.unpack_Hello()
        elif data.type == const.AUTH:
            data.auth = self.unpack_Auth()
        elif data.type == const.DONT_HAVE:
            data.dontHave = self.unpack_DontHave()
        elif data.type == const.GET_PEERS:
            pass
        elif data.type == const.PEERS:
            data.peers = self.unpack_array(self.unpack_PeerAddress)
            if len(data.peers) > 100 and self.check_array:
                raise XDRError('array length too long for data.peers')
        elif data.type == const.GET_TX_SET:
            data.txSetHash = self.unpack_uint256()
        elif data.type == const.TX_SET:
            data.txSet = self.unpack_TransactionSet()
        elif data.type == const.TRANSACTION:
            data.transaction = self.unpack_TransactionEnvelope()
        elif data.type == const.SURVEY_REQUEST:
            data.signedSurveyRequestMessage = self.unpack_SignedSurveyRequestMessage()
        elif data.type == const.SURVEY_RESPONSE:
            data.signedSurveyResponseMessage = self.unpack_SignedSurveyResponseMessage()
        elif data.type == const.GET_SCP_QUORUMSET:
            data.qSetHash = self.unpack_uint256()
        elif data.type == const.SCP_QUORUMSET:
            data.qSet = self.unpack_SCPQuorumSet()
        elif data.type == const.SCP_MESSAGE:
            data.envelope = self.unpack_SCPEnvelope()
        elif data.type == const.GET_SCP_STATE:
            data.getSCPLedgerSeq = self.unpack_uint32()
        else:
            raise XDRError('bad switch=%s' % data.type)
        if hasattr(self, 'filter_PaydexMessage'):
            data = getattr(self, 'filter_PaydexMessage')(data)
        return data

    def unpack_AuthenticatedMessage(self):
        data = types.AuthenticatedMessage()
        data.v = self.unpack_uint32()
        if data.v == 0:
            data.v0 = nullclass()
            data.v0.sequence = self.unpack_uint64()
            data.v0.message = self.unpack_PaydexMessage()
            data.v0.mac = self.unpack_HmacSha256Mac()
        else:
            raise XDRError('bad switch=%s' % data.v)
        if hasattr(self, 'filter_AuthenticatedMessage'):
            data = getattr(self, 'filter_AuthenticatedMessage')(data)
        return data

