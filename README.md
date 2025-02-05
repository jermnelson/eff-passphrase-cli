# EFF Dice CLI
A command-line utility for generating passphrases based on the 
Electronic Frontier Foundation [Dice-Generated Passphrases](https://www.eff.org/dice)
method.

## Using
1. Download or clone the repository.
1. Run `python run.py` to use the defaults (two terms with no character substitutions)
1. To increase the number of terms to generate add `--terms` flag with a number, i.e.
   `python run.py --terms 5` to generate a five term passphrase.
1. To generate a passphrase with symbol and numeral substitution, add `-m True` or 
   `--mixed True` which will the prompt you to specify the number of characters to 
   substitute numbers and symbols.
1. New passphrase will be printed to the command-line.

## Tests
To run tests, `python3 tests.py`.
