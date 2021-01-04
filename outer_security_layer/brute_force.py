import hashlib
import itertools
import sys

numbers = '0123456789'
adigit = list(numbers)

six_digits = itertools.product(adigit, repeat=6)

known_snippets = [('3','0','0'), ('7', '2', '6')]

expected_hash = '351635d71448baca'

def brute_force_hash(d):
  d = ''.join(d)
  print('the digits: {}'.format(d))
  result = hashlib.md5(d.encode())
  the_hash = result.hexdigest()
  print('1st 7 chars of the hash from {}: {}'.format(d, the_hash[0:10]))
  if the_hash[:7] == expected_hash[:7]:
    print('found it! digits: {}, hash: {}'.format(d, the_hash))
    sys.exit(0)

for d in six_digits:
  first_3digit_block = d[0:3]
  second_3digit_block = d[3:6]
  third_3digit_block = known_snippets[1]
  fourth_3digit_block = known_snippets[0]

  twelve_digits_blocks = [
    first_3digit_block,
    second_3digit_block,
    third_3digit_block,
    fourth_3digit_block
  ]

  for twelve_digits in itertools.permutations(twelve_digits_blocks):
    twelve_digits = twelve_digits[0] + twelve_digits[1] + twelve_digits[2] + twelve_digits[3]
    print('trying set of 12 digits: {}'.format(twelve_digits))
    brute_force_hash(twelve_digits)
