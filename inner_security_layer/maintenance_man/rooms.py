import re
from collections import Counter

room_count = 1
num_of_valid_rooms = 0

while True:
  #print('room_count: {}'.format(room_count))
  c=Counter(re.findall(r'\d',str(room_count)))
  twos_count = c['2']
  zeros_count = c['0']
  # print('removing other digits and leaving just 2\'s and 0\'s: {}'.format(re.sub("[^2|^0]", " ", str(room_count))))
  twos_and_zeros = re.sub("[^2|^0]", "", str(room_count)).lstrip('0')

  if twos_count >= 2 and zeros_count >= 2:
    print('iterating through twos_and_zeros for {}: {}'.format(room_count, twos_and_zeros))
    pattern_to_find = ['2', '0', '2', '0']
    for d in twos_and_zeros:
      print('what is left to find: {}'.format(pattern_to_find))

      if len(pattern_to_find) > 0 and d == pattern_to_find[0]:
        pattern_to_find.pop(0)

    if len(pattern_to_find) == 0:
      print('pattern found!')
      print('invalid room: {}'.format(room_count))
    else:
      print('The pattern was not found. This is a valid room number.')
      num_of_valid_rooms += 1

  else:
    num_of_valid_rooms += 1
    # print('num_of_valid_rooms: {}'.format(num_of_valid_rooms))

  if num_of_valid_rooms == 1000000:
    break
  room_count += 1

print('final room: {}'.format(room_count))
