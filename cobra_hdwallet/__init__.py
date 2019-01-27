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

















