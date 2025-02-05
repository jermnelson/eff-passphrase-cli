__author__ = "Jeremy Nelson"

import string
import unittest

from run import (
    generate,
    _number_subsitution,
    _symbol_subsitution
)

class TestEFFPassPhraseGeneration(unittest.TestCase):
    
    def test_baseline(self):
        passphrase = generate(2, False)
        self.assertEqual(len(passphrase.split("-")), 2)


    def test_number_subsitution(self):
        modified_passphrase = _number_subsitution("devoutly-spring", 1)
        self.assertEqual(modified_passphrase, "d3voutly-spring")

    def test_multiple_number_subsitution(self):
        modified_passphrase = _number_subsitution("reflex-emptier", 2)
        self.assertEqual(modified_passphrase, "r3f1ex-emptier") 

    def test_symbol_subsitution(self):
        modified_passphrase = _symbol_subsitution("ecard-decorated", 1)
        self.assertTrue(any([char in string.punctuation for char in modified_passphrase]))        

if __name__ == "__main__":
    unittest.main()
