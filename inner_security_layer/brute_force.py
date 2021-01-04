import hashlib
import itertools
import sys

alphabet = 'abcdefghijklmnopqrstuvwxyz'
numbers = '0123456789'

alowerc = alphabet
anupperc = alphabet.upper()
adigit = numbers

chars = alowerc + anupperc + adigit
four_chars_permutations = itertools.product(chars, repeat=4)

parts_we_already_know = [('3','w'), ('s', 'Q')]

firt_16_chars_expected_hash = '002a8a8b23d03e70'

def brute_force_hash(the_text):
  result = hashlib.md5(''.join(the_text).encode())
  the_hash = result.hexdigest()
  print('1st 10 chars of the hash from {}: {}'.format(the_text, the_hash[0:10]))
  if the_hash[:10] == firt_16_chars_expected_hash[:10]:
    print('found it! text: {}, hash: {}'.format(the_text, the_hash))
    sys.exit(0)

for i in four_chars_permutations:
  eight_chars_sections = [
    i,
    parts_we_already_know[0],
    parts_we_already_know[1]
  ]

  for eight_chars in itertools.permutations(eight_chars_sections):
    eight_chars = eight_chars[0] + eight_chars[1] + eight_chars[2]
    print('trying set of 8 chars: {}'.format(eight_chars))
    brute_force_hash(eight_chars)
