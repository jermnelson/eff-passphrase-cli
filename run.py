"""Run EFF Password Generator from the command-line"""

__author__ = "Jeremy Nelson"
import argparse
import pathlib
import random
import string

large_wordlist_path = pathlib.Path("eff_large_wordlist.txt")

if not large_wordlist_path.exists():
    raise ValueError("Missing eff_large_wordlist")
 
eff_lookup = dict()

raw_wordlist = large_wordlist_path.read_text()
for line in raw_wordlist.splitlines():
    key, value = line.split("\t")
    eff_lookup[key] = value

number_lookup = {
  'o': '0',
  'l': '1',
  'e': '3',
  's': '5',
  'b': '6',
  'g': '9'
}

def _number_subsitution(passphrase: str, count: int) -> str:
    """Substitutes character for a number
 
    args:
      - passphrase: incoming passphrase
      - count: number of characters to substitute
    returns:
      - modified passphrase
    """
    mod_passphrase = ''
    total = 0
    for i,char in enumerate(passphrase):
        if total >= count:
           mod_passphrase += passphrase[i:]
           break
        if char.lower() in number_lookup: # and total >= count:
            mod_passphrase += number_lookup[char.lower()]
            total += 1
        else:
            mod_passphrase += char
    return mod_passphrase


def _symbol_subsitution(passphrase: str, count: int) -> str:
    """Substitutes character for symbols

    args:
      - passpharse: incoming passphrase
      - count: number of characters to substitute
   
    returns:
      - modified passphrase
    """ 
    mod_passphrase = [char for char in passphrase]
    for _ in range(count):
        symbol_idx = random.randint(0, len(string.punctuation))
        symbol = string.punctuation[symbol_idx]
        char_idx = random.randint(0, len(passphrase))
        mod_passphrase[char_idx] = symbol
    return ''.join(mod_passphrase)
        

def generate(total_terms: int, mixed_chars: bool) -> str:
    """Generates a random passphrase based EFF Large Wordlist

    args:
      - total_terms: Total terms in passphrase, default is 2
      - mixed_chars: Bool for replaces random characters in passpharse with numerals and
                     symbols

    returns:
      - passphrase string
    """
    for count in range(total_terms):
        key = ''
        for event in range(1,6):
            roll = random.randint(1,6)
            key = f"{key}{roll}"
        word = eff_lookup[key]
        if count < 1:
            passphrase = word
        else:
            passphrase = f"{passphrase}-{word}"
    if mixed_chars:
        original_passphrase = passphrase
        # Replace characters with numbers
        num_count = input("How many chars to replace with numbers? (default is 1)")
        if len(num_count) < 1:
            num_count=1
        passphrase = _number_subsitution(passphrase, int(num_count))
        symbol_count = input("How many chars to replace with symbols? (default is 1)")
        if len(symbol_count) < 1:
            symbol_count = 1
        passphrase = _symbol_subsitution(passphrase, int(symbol_count))
    return passphrase

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                        prog="PasswordGenerator",
                        description="EFF Password Generator")
    parser.add_argument("--terms", default=2)
    parser.add_argument('-m', '--mixed', default=False)
    args = parser.parse_args()
    print(generate(int(args.terms), args.mixed))                 

