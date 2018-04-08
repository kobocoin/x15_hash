import x15_hash

from binascii import unhexlify, hexlify
from collections import namedtuple

import unittest

HashSpec = namedtuple("HashSpec", "data hash")

class TestHashes(unittest.TestCase):

    def assert_hash(self, hash_fn, spec):
        for s in spec:
            hash = hexlify(hash_fn(s.data))
            self.assertEqual(hash, s.hash)

    def test_kobocoin1(self):
        header4004 = bytes.fromhex('06000000c7830827d6073a9d2b2768bb1f738a63553f7fe901f225d90f1524b9ba866c9b5633e849c755daf198e499303902ff842dabf1ffecc3e9ae8f8facd0fcc49a92e889d954ddde0e1e00000000')
        hash4004 = hexlify(bytes(reversed(bytes.fromhex('bc1e040f92aa5cc22b0b0d6a8ada6f051760edd42e8c278339bd7a60f95a8550'))))

        header4005 = bytes.fromhex('0600000050855af9607abd3983278c2ed4ed6017056fda8a6a0d0b2bc25caa920f041ebc64e1d750e408dfff287209ef9057df2af97d90c1516dc628785dd3375e71dd6bb989d95424d20d1e00000000')
        hash4005 = hexlify(bytes(reversed(bytes.fromhex('f1620f7cdfcd12d4f47729b0546f57a1a598f23c45315d760b9e6d551f7dfd4a'))))

        spec = [

            HashSpec(header4004,hash4004),
            HashSpec(header4005,hash4005),

        ]
        self.assert_hash(x15_hash.getPoWHash, spec)

if __name__ == '__main__':
    unittest.main()
