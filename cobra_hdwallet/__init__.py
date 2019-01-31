#!/usr/bin/env python3
"""
Author: Meheret Tesfaye
Email: meherett@zoho.com
Github: https://github.com/meherett
"""

import sha3
import hmac
import ecdsa
import struct
import codecs
import hashlib
import binascii

from hashlib import sha256
from ecdsa.curves import SECP256k1
from mnemonic.mnemonic import Mnemonic
from two1.bitcoin.utils import rand_bytes
from ecdsa.ecdsa import int_to_string, string_to_int

__base58_alphabet = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
__base58_alphabet_bytes = b'123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
__base58_radix = len(__base58_alphabet)

MIN_ENTROPY_LEN = 128
BIP32_HARDEN = 0x80000000
CURVE_GEN = ecdsa.ecdsa.generator_secp256k1
CURVE_ORDER = CURVE_GEN.order()
FIELD_ORDER = SECP256k1.curve.p()
INFINITY = ecdsa.ellipticcurve.INFINITY
EX_MAIN_PRIVATE = [codecs.decode('0488ade4', 'hex')]
EX_MAIN_PUBLIC = [codecs.decode('0488b21e', 'hex'), codecs.decode('049d7cb2', 'hex')]


def checksum_encode(address):
    keccak = sha3.keccak_256()
    out = ''
    addr = address.lower().replace('0x', '')
    keccak.update(addr.encode('ascii'))
    hash_addr = keccak.hexdigest()
    for i, c in enumerate(addr):
        if int(hash_addr[i], 16) >= 8:
            out += c.upper()
        else:
            out += c
    return '0x' + out


def get_bytes(string):
    if isinstance(string, bytes):
        byte = string
    elif isinstance(string, str):
        byte = bytes.fromhex(string)
    else:
        raise TypeError("Agreement must be either 'bytes' or 'string'!")
    return byte


def __string_to_int(data):
    val = 0

    if type(data) == str:
        data = bytearray(data)

    for (i, c) in enumerate(data[::-1]):
        val += (256 ** i) * c
    return val


def encode(data):
    enc = ''
    val = __string_to_int(data)
    while val >= __base58_radix:
        val, mod = divmod(val, __base58_radix)
        enc = __base58_alphabet[mod] + enc
    if val:
        enc = __base58_alphabet[val] + enc

    n = len(data) - len(data.lstrip(b'\0'))
    return __base58_alphabet[0] * n + enc


def check_encode(raw):
    chk = sha256(sha256(raw).digest()).digest()[:4]
    return encode(raw + chk)


def decode(data):
    if bytes != str:
        data = bytes(data, 'ascii')

    val = 0
    for (i, c) in enumerate(data[::-1]):
        val += __base58_alphabet_bytes.find(c) * (__base58_radix ** i)

    dec = bytearray()
    while val >= 256:
        val, mod = divmod(val, 256)
        dec.append(mod)
    if val:
        dec.append(val)

    return bytes(dec[::-1])


def check_decode(enc):
    dec = decode(enc)
    raw, chk = dec[:-4], dec[-4:]
    if chk != sha256(sha256(raw).digest()).digest()[:4]:
        raise ValueError("base58 decoding checksum error")
    else:
        return raw


class CobraHDWallet:

    def __init__(self, secret, chain, depth, index, fingerprint):

        self.key = ecdsa.SigningKey.from_string(secret, curve=SECP256k1)
        self.verifiedKey = self.key.get_verifying_key()

        self.chain = chain
        self.depth = depth
        self.index = index
        self.parent_fingerprint = fingerprint

    def __call__(self, private):
        self.key = ecdsa.SigningKey.from_string(private, curve=SECP256k1)
        self.verifiedKey = self.key.get_verifying_key()

    @staticmethod
    def master_key_from_mnemonic(mnemonic, passphrase=''):

        return CobraHDWallet.master_key_from_seed(
            Mnemonic.to_seed(mnemonic, passphrase))

    @staticmethod
    def check_master_key_from_mnemonic(mnemonic, language='english'):
        try:
            Mnemonic(language=language).check(mnemonic)
            return True
        except:
            return False

    @staticmethod
    def master_key_from_entropy(passphrase='', language='english', strength=128):

        if strength % 32 != 0:
            raise ValueError("strength must be a multiple of 32")
        if strength < 128 or strength > 256:
            raise ValueError("strength should be >= 128 and <= 256")

        entropy = rand_bytes(strength // 8)
        mnemonic = Mnemonic(language=language)\
            .to_mnemonic(entropy)

        return CobraHDWallet.master_key_from_seed(
            Mnemonic.to_seed(mnemonic, passphrase)), mnemonic

    @staticmethod
    def master_key_from_seed(seed):

        I = hmac.new(b"Bitcoin seed", get_bytes(seed), hashlib.sha512).digest()
        Il, Ir = I[:32], I[32:]

        parse_Il = int.from_bytes(Il, 'big')
        if parse_Il == 0 or parse_Il >= SECP256k1.order:
            raise ValueError("Bad seed, resulting in invalid key!")

        return CobraHDWallet(
            secret=Il, chain=Ir, depth=0, index=0, fingerprint=b'\0\0\0\0')

    def hmac(self, data):
        I = hmac.new(self.chain, data, hashlib.sha512).digest()
        return I[:32], I[32:]

    def DerivePrivateKey(self, index):

        i_str = struct.pack(">L", index)
        if index & BIP32_HARDEN:
            data = b'\0' + self.key.to_string() + i_str
        else:
            data = self.PublicKey() + i_str
        Il, Ir = self.hmac(data)

        Il_int = string_to_int(Il)
        if Il_int > CURVE_ORDER:
            return None
        pvt_int = string_to_int(self.key.to_string())
        k_int = (Il_int + pvt_int) % CURVE_ORDER
        if k_int == 0:
            return None
        secret = (b'\0' * 32 + int_to_string(k_int))[-32:]

        return CobraHDWallet(
            secret=secret, chain=Ir,
            depth=self.depth + 1, index=index,
            fingerprint=self.Fingerprint())

    def fromPath(self, path):
        derivePrivateKey = self
        if str(path)[0:2] != 'm/':
            raise ValueError("Bad path, please insert like this type of path \"m/0'/0\"! ")

        for index in path.lstrip('m/').split('/'):
            if "'" in index:
                derivePrivateKey = derivePrivateKey.DerivePrivateKey(int(index[:-1]) + BIP32_HARDEN)
            else:
                derivePrivateKey = derivePrivateKey.DerivePrivateKey(int(index))
        return derivePrivateKey

    def fromIndex(self, index):
        if not str(index)[0:2] != 'm/':
            raise ValueError("Bad path, please insert only index int!")
        return self.DerivePrivateKey(int(index))

    def PrivateKey(self):
        return self.key.to_string()

    def PublicKey(self, private=None):
        if private:
            private = binascii.unhexlify(private)
            key = ecdsa.SigningKey.from_string(bytes(private), curve=SECP256k1)
            verifiedKey = key.get_verifying_key()
            padx = (b'\0' * 32 + int_to_string(verifiedKey.pubkey.point.x()))[-32:]
            if self.verifiedKey.pubkey.point.y() & 1:
                ck = b'\3' + padx
            else:
                ck = b'\2' + padx
            return ck
        padx = (b'\0' * 32 + int_to_string(self.verifiedKey.pubkey.point.x()))[-32:]
        if self.verifiedKey.pubkey.point.y() & 1:
            ck = b'\3' + padx
        else:
            ck = b'\2' + padx
        return ck

    def UncompressedPublicKey(self, private=None):
        if private:
            private = binascii.unhexlify(private)
            key = ecdsa.SigningKey.from_string(bytes(private), curve=SECP256k1)
            verifiedKey = key.get_verifying_key()
            return verifiedKey.to_string()
        return self.verifiedKey.to_string()

    def ChainCode(self):
        return self.chain

    def Identifier(self, private=None):
        cK = self.PublicKey(private)
        return hashlib.new('ripemd160', sha256(cK).digest()).digest()

    def Fingerprint(self, private=None):
        return self.Identifier(private)[:4]

    def Address(self, private=None):
        keccak_256 = sha3.keccak_256()
        if private:
            private = binascii.unhexlify(private)
            key = ecdsa.SigningKey.from_string(private, curve=SECP256k1)
            verifiedKey = key.get_verifying_key()
            keccak_256.update(verifiedKey.to_string())
            address = keccak_256.hexdigest()[24:]
            return checksum_encode(address)
        keccak_256.update(self.verifiedKey.to_string())
        address = keccak_256.hexdigest()[24:]
        return checksum_encode(address)

    def WalletImportFormat(self, private=None):
        if private:
            private = binascii.unhexlify(private)
            key = ecdsa.SigningKey.from_string(private, curve=SECP256k1)
            raw = b'\x80' + key.to_string() + b'\x01'
            return check_encode(raw)
        raw = b'\x80' + self.key.to_string() + b'\x01'
        return check_encode(raw)

    def ExtendedKey(self, private=True, encoded=True):
        version = EX_MAIN_PRIVATE[0] if private else EX_MAIN_PUBLIC[0]
        depth = bytes(bytearray([self.depth]))
        fingerprint = self.parent_fingerprint
        child = struct.pack('>L', self.index)
        chain = self.chain

        data = b'\x00' + self.PrivateKey()
        raw = version + depth + fingerprint + child + chain + data
        if not encoded:
            return raw
        else:
            return check_encode(raw)


class HDWallet:

    def __init__(self):
        self.hdwallet = {
            "coin": "ETH",
            "name": "Ethereum",
            "address": "",
            "mnemonic": "",
            "wif": "",
            "finger_print": "",
            "chain_code": "",
            "private_key": "",
            "public_key": "",
            "uncompressed_public_key": "",
            "serialized": {
                "private_key_hex": "",
                "public_key_hex": "",
                "xprivate_key_base58": "",
                "xpublic_key_base58": "",
            }
        }

        self.hdwallet_private = {
            "coin": "ETH",
            "name": "Ethereum",
            "address": "",
            "wif": "",
            "finger_print": "",
            "private_key": "",
            "public_key": "",
            "uncompressed_public_key": ""
        }










