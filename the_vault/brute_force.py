import hashlib
import itertools
import sys
import re

alphabet = 'abcdefghijklmnopqrstuvwxyz'
numbers = '0123456789'

alowerc = alphabet
anupperc = alphabet.upper()
adigit = numbers

chars = alowerc + anupperc + adigit
four_chars_permutations = itertools.product(chars, repeat=4)

parts_we_already_know = [('O', 'b'), ('q', 'g')]

firt_16_chars_expected_hash = 'a84ba651fd122ef5'

def brute_force_hash(chars):
  print('trying with {}'.format(chars))
  possible_permutations = list(itertools.product(*chars))
  for the_text in possible_permutations:
    the_text = ''.join(the_text)

    # try b or 6 and 0 or O
    # Trying permutations within this silly loop due to bad hand writing
        # i == 0 -> Ob
        # i == 1 -> O6
        # i == 2 -> 0b
        # i == 3 -> 06
    for i in range(4):
      if i == 1:
        the_text = re.sub("b", "6", the_text)
      elif i == 2:
        the_text = re.sub("O", "0", the_text)
      elif i == 3:
        the_text = re.sub("b", "6", the_text)
        the_text = re.sub("O", "0", the_text)

      # print('the text: {}'.format(the_text))
      result = hashlib.md5(the_text.encode())
      the_hash = result.hexdigest()
      print('1st 12 chars of the hash from {}: {}'.format(the_text, the_hash[0:10]))
      if the_hash[:12] == firt_16_chars_expected_hash[:12]:
        print('found it! text: {}, hash: {}'.format(the_text, the_hash))
        sys.exit(0)


for i in four_chars_permutations:
  #li = ''.join(i)
  #print('four_chars_permutation: {}'.format(li))
  eight_chars_sections = [
    i,
    parts_we_already_know[0],
    parts_we_already_know[1],
  ]

  for eight_chars in itertools.permutations(eight_chars_sections):
    eight_chars = eight_chars[0] + eight_chars[1] + eight_chars[2]
    print('trying set of 8 chars: {}'.format(eight_chars))
    brute_force_hash(eight_chars)
